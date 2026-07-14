# Render QA — narrated explainer video

**The only supported way to render the video is `render_video.py`. Never render from a
scratchpad script.** Every recurring defect (lost red-border highlight, "cow-ork",
per-segment dead air) came from a throwaway render whose fix was never committed. The
pipeline and all its fixes now live in this folder and are reproduced on every render.

## Committed pieces
- `render_video.py` — the pipeline (images → tts → assemble → verify) + all guards.
- `highlight_map.py` — per-slide, one highlighted card-index per narration sentence.
- `pronunciation_lexicon.py` — spoken-only respellings + `HARD_TOKENS` ratchet.
- `vocab_approved.txt` — approved narration vocabulary (novelty gate baseline).
- `card_geometry.json` — card rectangles (emitted by the BUILD script; input to the renderer).

## Automatic, fail-loud (run before any stage; there is no skip flag)
- **G1** narration + rendered deck are both 27 slides.
- **G2** highlight map length == sentence count, card indices in range, every slide.
- **G3** every `HARD_TOKENS` word in the narration is covered by the lexicon (so a
  re-introduced hard word stops the render instead of reverting to a mispronunciation).
- **G3b** voice/rate == the lexicon's `TUNED_FOR` (respellings are only known-good there).
- **G4** every narration word is in `vocab_approved.txt`; a new word halts the render.
- **G6** the pipeline source files end with the EOF sentinel (catches mount truncation).
- **P2/P3** (post-assemble) final duration ≈ sum of phase audio (catches dead air/drops);
  streams are 1920×1080 / aac. The final mp4 is only named on pass (atomic rename).

## Human checkpoints (machine can't decide these)
- **E1 — ear:** after a render, listen to any phase whose audio changed (the tts stage
  reports them; usually 1–3 clips). Pronunciation of *approved* words and prosody are ear-only.
- **E3 — eye/ear:** play the first 15 s, a midpoint, and the last 15 s of the final video.

## How to fix a new mispronunciation (permanent)
1. Add `(r"\bWord\b", "res-pelling")` to `LEXICON` and the lowercased word to `HARD_TOKENS`
   in `pronunciation_lexicon.py`. 2. Re-render (only affected phases re-synthesize).
3. Listen (E1). The fix is now permanent — G3 will fail any future render that drops it.

## How to approve genuinely new vocabulary
Run a render; G4 lists new words. Listen to each; if fine, append it to `vocab_approved.txt`.
