#!/usr/bin/env python3
"""Render the narrated Insight Engine explainer video, with phase-synced highlights,
committed pronunciation fixes, and a fail-loud render-QA layer.

Reproducible pipeline (previously an ephemeral scratchpad -- which is why the red
highlight, the pronunciation fixes, and correct pacing were lost on every version
bump). Everything now lives in the repo:
  card_geometry.json      - card rectangles (emitted by the BUILD script)
  highlight_map.py         - which card is outlined red during each sentence
  pronunciation_lexicon.py - spoken-only respellings + the hard-word ratchet
  vocab_approved.txt       - approved narration vocabulary (novelty gate)

Stages:
  images   : pptx -> pdf (LibreOffice) -> 1920x1080 PNG per slide + red-outline variants
  tts      : one en-GB-RyanNeural mp3 per PHASE (rate +40%), lexicon applied, hash-cached
  assemble : per-phase image+audio segment -> concat -> post-checks -> atomic rename
  verify   : run every guard (and post-checks if a render exists); changes nothing

Pre-flight guards run UNCONDITIONALLY before any stage; there is deliberately no
skip flag. A finished-named output mp4 only ever exists if the post-checks passed.

Usage: python3 render_video.py [images|tts|assemble|verify|all] [--from N --to M]
Requires: libreoffice/soffice, pdftoppm (poppler), ffmpeg, Pillow, edge-tts, mutagen.
"""
import os, sys, re, json, subprocess, tempfile, asyncio, glob, hashlib
from PIL import Image, ImageDraw

HERE   = os.path.dirname(os.path.abspath(__file__))
PPTX   = os.path.join(HERE, "Insight-Engine-Explainer.pptx")
NARR   = os.path.join(HERE, "Insight-Engine-Explainer-Narration.md")
GEO    = os.path.join(HERE, "card_geometry.json")
VOCAB  = os.path.join(HERE, "vocab_approved.txt")
WORK   = os.environ.get("IE_WORK", os.path.join(tempfile.gettempdir(), "ie_render_work"))
VOICE  = "en-GB-RyanNeural"
RATE   = "+40%"
W, H, FPS = 1920, 1080, 2
PXIN   = W / 13.333
RED    = (222, 22, 22)
EXPECTED_SLIDES = 27
SENTINEL = "# ::IE-RENDER-EOF::"
DATE   = os.environ.get("IE_DATE", "2026-07-14")
OUT    = os.path.join(HERE, f"Insight-Engine-Explainer-Narrated-Ryan-1.4x-27slide-synced-{DATE}.mp4")
os.makedirs(WORK, exist_ok=True)

import importlib.util as _ilu
def _load(name, fname):
    spec = _ilu.spec_from_file_location(name, os.path.join(HERE, fname))
    m = _ilu.module_from_spec(spec); spec.loader.exec_module(m); return m
_lex = _load("pronunciation_lexicon", "pronunciation_lexicon.py")
_LEX = [(re.compile(p), r) for p, r in _lex.LEXICON]

def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + "\n" + r.stderr + "\n")
        raise SystemExit(f"FAILED: {' '.join(cmd)}")
    return r

def spoken(t):
    for rx, rep in _LEX: t = rx.sub(rep, t)
    return t

def text_sig(text):
    return hashlib.sha256(f"{VOICE}|{RATE}|{spoken(text)}".encode()).hexdigest()[:16]

def file_sig(path):
    with open(path, "rb") as f: return hashlib.sha256(f.read()).hexdigest()[:16]

def slide_narration():
    txt = open(NARR, encoding="utf-8").read()
    parts = re.split(r'(?m)^##\s+Slide\s+(\d+)\s*[—-].*$', txt)
    return {int(parts[i]): re.sub(r'\s+', ' ', parts[i+1]).strip() for i in range(1, len(parts), 2)}

def split_sentences(t):
    t = re.sub(r'\s+', ' ', t).strip(); P = '\x00'
    t2 = re.sub(r'(\d)\.(\d)', r'\1'+P+r'\2', t)
    t2 = re.sub(r'\b(e\.g|i\.e|etc|vs|Mr|Mrs|Dr|St|No|Inc|Ltd)\.', lambda m: m.group(1)+P, t2)
    pieces = re.split(r'(?<=[.!?])\s+(?=[“"\'A-Z])', t2)
    return [p.replace(P, '.').strip() for p in pieces if p.strip()]

def load_map():
    return _load("highlight_map", "highlight_map.py").HIGHLIGHT

def geo_by_slide():
    by = {}
    for c in json.load(open(GEO)): by.setdefault(c["slide"], []).append(c)
    return by

def phases_for(sl, narr, hmap):
    sents = split_sentences(narr[sl])
    if sl not in hmap: return [(-1, " ".join(sents))]
    cards = hmap[sl]
    if len(cards) != len(sents):
        raise SystemExit(f"HIGHLIGHT[{sl}] has {len(cards)} entries but slide has {len(sents)} sentences.")
    out, i = [], 0
    while i < len(sents):
        c = cards[i]; j = i
        while j < len(sents) and cards[j] == c: j += 1
        out.append((c, " ".join(sents[i:j]))); i = j
    return out

def dur(path):
    r = sh(["ffprobe","-v","error","-show_entries","format=duration",
            "-of","default=noprint_wrappers=1:nokey=1", path])
    return float(r.stdout.strip())

def audlen(path):
    try:
        from mutagen.mp3 import MP3
        return MP3(path).info.length
    except Exception:
        return dur(path)

# ---------------- pre-flight guards (unconditional) ----------------
def _tail_ok(p):
    return open(p, encoding="utf-8").read().rstrip().endswith(SENTINEL)

def preflight():
    narr, hmap, geo = slide_narration(), load_map(), geo_by_slide()
    e = []
    if len(narr) != EXPECTED_SLIDES:
        e.append(f"G1 narration has {len(narr)} slides, expected {EXPECTED_SLIDES}")
    for sl in narr:                                                # G7 narration completeness (anti-truncation)
        tail = narr[sl].rstrip()
        if not tail or tail[-1] not in '.!?"\u201d\u2019':
            e.append(f"G7 slide {sl} narration not terminated -- truncated? ...{tail[-45:]!r}")
    for sl, cards in hmap.items():                                  # G2 highlight sync
        ss = split_sentences(narr[sl]); nc = len(geo.get(sl, []))
        if len(cards) != len(ss): e.append(f"G2 slide {sl}: map {len(cards)} != {len(ss)} sentences")
        oor = [c for c in cards if c >= nc]
        if oor: e.append(f"G2 slide {sl}: card index {oor} >= {nc} cards")
    alltext = " ".join(narr.values())
    for tok in _lex.HARD_TOKENS:                                    # G3 pronunciation coverage
        m = re.search(rf"\b{re.escape(tok)}\b", alltext, re.I)
        if m and spoken(m.group(0)) == m.group(0):
            e.append(f"G3 hard word '{m.group(0)}' present but not covered by LEXICON")
    if (VOICE, RATE) != tuple(_lex.TUNED_FOR):                      # G3b voice coupling
        e.append(f"G3b voice/rate {(VOICE, RATE)} != lexicon TUNED_FOR {tuple(_lex.TUNED_FOR)}")
    approved = set(open(VOCAB, encoding="utf-8").read().split())    # G4 vocabulary novelty gate
    body = " ".join(narr.values())
    seen = {w.lower().strip("'-") for w in re.findall(r"[A-Za-z][A-Za-z'\-]*", body)}
    new = sorted(w for w in seen if len(w) >= 4 and w not in approved)
    if new:
        e.append("G4 new vocabulary not in vocab_approved.txt (listen, then append): " +
                 ", ".join(new[:25]) + (" ..." if len(new) > 25 else ""))
    for f in ("render_video.py", "highlight_map.py", "pronunciation_lexicon.py"):  # G6 truncation
        p = os.path.join(HERE, f)
        if os.path.exists(p) and not _tail_ok(p):
            e.append(f"G6 {f} does not end with the EOF sentinel (possible mount truncation)")
    if e:
        raise SystemExit("PRE-FLIGHT FAILED:\n  - " + "\n  - ".join(e))
    print("pre-flight OK  [G1 slides · G2 highlight-sync · G3 pronunciation · G3b voice · G4 vocab · G6 sentinels · G7 narration-complete]")

# ---------------- stage 1: images ----------------
def _variant(base_png, sl, card, geo):
    dst = os.path.join(WORK, f"slide-{sl:02d}-c{card}.png")
    if os.path.exists(dst) and os.path.getsize(dst) > 0: return dst
    im = Image.open(base_png).convert("RGB")
    sx, sy = im.width / W, im.height / H
    r = geo[sl][card]; pad = 6
    box = [r["x"]*PXIN*sx - pad, r["y"]*PXIN*sy - pad,
           (r["x"]+r["w"])*PXIN*sx + pad, (r["y"]+r["h"])*PXIN*sy + pad]
    ImageDraw.Draw(im).rounded_rectangle(box, radius=22, outline=RED, width=8)
    im.save(dst); return dst

def stage_images():
    sh(["soffice","--headless","--convert-to","pdf","--outdir",WORK,PPTX])
    pdf = os.path.join(WORK, "Insight-Engine-Explainer.pdf")
    pages = int(sh(["pdfinfo", pdf]).stdout.split("Pages:")[1].split()[0])
    if pages != EXPECTED_SLIDES:                                    # G1 triad: deck page count
        raise SystemExit(f"G1 rendered deck has {pages} pages, expected {EXPECTED_SLIDES} (truncated BUILD?)")
    sh(["pdftoppm","-png","-scale-to-x",str(W),"-scale-to-y",str(H), pdf, os.path.join(WORK,"slide")])
    narr, hmap, geo = slide_narration(), load_map(), geo_by_slide(); nv = 0
    for sl in sorted(narr):
        base = os.path.join(WORK, f"slide-{sl:02d}.png")
        if not os.path.exists(base):
            alt = os.path.join(WORK, f"slide-{sl}.png")
            if os.path.exists(alt): os.rename(alt, base)
        for card, _ in phases_for(sl, narr, hmap):
            if card >= 0: _variant(base, sl, card, geo); nv += 1
    print("images ready; red-outline variants:", nv)

def img_for(sl, card):
    return os.path.join(WORK, f"slide-{sl:02d}-c{card}.png") if card >= 0 \
           else os.path.join(WORK, f"slide-{sl:02d}.png")

# ---------------- stage 2: tts (lexicon + hash cache) ----------------
def stage_tts(lo, hi):
    import edge_tts
    narr, hmap = slide_narration(), load_map()
    async def one(pid, text):
        final = os.path.join(WORK, f"audio-{pid}.mp3"); sig = final + ".sig"; want = text_sig(text)
        if os.path.exists(final) and os.path.getsize(final) > 0 and \
           os.path.exists(sig) and open(sig).read().strip() == want:
            print(pid, "cached"); return
        tmp = final + ".tmp"
        c = edge_tts.Communicate(spoken(text), VOICE, rate=RATE)   # <-- lexicon applied to audio only
        with open(tmp, "wb") as f:
            async for ch in c.stream():
                if ch["type"] == "audio": f.write(ch["data"])
        os.replace(tmp, final); open(sig, "w").write(want); print(pid, os.path.getsize(final), "bytes")
    async def run():
        for sl in range(lo, hi+1):
            if sl not in narr: continue
            for k, (_c, text) in enumerate(phases_for(sl, narr, hmap)):
                await one(f"{sl:02d}-{k:02d}", text)
    asyncio.run(run())

# ---------------- stage 3: assemble (+ post-checks + atomic rename) ----------------
def _order():
    narr, hmap = slide_narration(), load_map()
    return [(sl, k, card) for sl in sorted(narr)
            for k, (card, _t) in enumerate(phases_for(sl, narr, hmap))]

def stage_assemble():
    order = _order()
    for sl, k, card in order:
        seg = os.path.join(WORK, f"seg-{sl:02d}-{k:02d}.mp4"); sigf = seg + ".sig"
        aud = os.path.join(WORK, f"audio-{sl:02d}-{k:02d}.mp3")
        want = hashlib.sha256((file_sig(aud) + "|" + file_sig(img_for(sl, card))).encode()).hexdigest()[:16]
        if os.path.exists(seg) and os.path.exists(sigf) and open(sigf).read().strip() == want:
            continue
        tmp = seg + ".tmp.mp4"
        sh(["ffmpeg","-y","-loop","1","-framerate",str(FPS),"-i",img_for(sl,card),
            "-i",aud,"-t",f"{audlen(aud):.3f}",
            "-c:v","libx264","-preset","ultrafast","-tune","stillimage","-pix_fmt","yuv420p","-r",str(FPS),
            "-c:a","aac","-b:a","96k","-ar","24000","-ac","1",tmp])
        os.replace(tmp, seg); open(sigf, "w").write(want); print("seg", sl, k, "ok")
    segs = [os.path.join(WORK, f"seg-{sl:02d}-{k:02d}.mp4") for sl,k,_ in order]
    miss = [order[i] for i,x in enumerate(segs) if not (os.path.exists(x) and os.path.getsize(x) > 0)]
    if miss:
        print("segments still missing:", miss[:8], "..." if len(miss) > 8 else ""); return
    listf = os.path.join(WORK, "concat.txt")
    with open(listf, "w") as lf:
        for x in segs: lf.write(f"file '{x}'\n")
    tmp_out = OUT + ".tmp.mp4"
    sh(["ffmpeg","-y","-f","concat","-safe","0","-i",listf,"-c","copy",tmp_out])
    _postcheck(tmp_out, order)                                     # raises on failure, keeps tmp
    os.replace(tmp_out, OUT)
    print("SAVED", OUT, f"{os.path.getsize(OUT)/1e6:.1f} MB", f"{dur(OUT):.0f}s")

def _postcheck(path, order):
    e = []
    sum_aud = sum(audlen(os.path.join(WORK, f"audio-{sl:02d}-{k:02d}.mp3")) for sl,k,_ in order)
    tot = dur(path); tol = max(5.0, 0.15 * len(order))             # P2 total duration vs sum-of-audio
    if abs(tot - sum_aud) > tol:
        e.append(f"P2 duration {tot:.0f}s vs sum-of-audio {sum_aud:.0f}s (>|{tol:.0f}|s) -- dead air or drops?")
    v = sh(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height",
            "-of","default=noprint_wrappers=1:nokey=1", path]).stdout.split()
    if v != ["1920","1080"]: e.append(f"P3 video stream {v} != 1920x1080")
    a = sh(["ffprobe","-v","error","-select_streams","a:0","-show_entries","stream=codec_name",
            "-of","default=noprint_wrappers=1:nokey=1", path]).stdout.strip()
    if a != "aac": e.append(f"P3 audio stream '{a}' != aac")
    if e:
        raise SystemExit("POST-CHECK FAILED (kept " + os.path.basename(path) + "):\n  - " + "\n  - ".join(e))
    print(f"post-check OK  [P2 duration {tot:.0f}s ~ audio {sum_aud:.0f}s · P3 streams 1920x1080/aac]")

def stage_verify():
    preflight()
    if os.path.exists(OUT):
        _postcheck(OUT, _order()); print("existing render passes post-checks")
    else:
        print("no render present; guards only")

if __name__ == "__main__":
    stage = sys.argv[1] if len(sys.argv) > 1 else "all"
    lo, hi = 1, 27
    if "--from" in sys.argv: lo = int(sys.argv[sys.argv.index("--from")+1])
    if "--to"   in sys.argv: hi = int(sys.argv[sys.argv.index("--to")+1])
    preflight()                                                    # UNCONDITIONAL, no skip flag
    if stage == "verify":                 stage_verify()
    if stage in ("images","all"):         stage_images()
    if stage in ("tts","all"):            stage_tts(lo, hi)
    if stage in ("assemble","all"):       stage_assemble()

# ::IE-RENDER-EOF::
