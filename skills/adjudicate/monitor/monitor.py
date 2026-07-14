#!/usr/bin/env python3
"""
Real-Use Monitor (RUM) for independent adjudication.
Answers observationally what constructed cases cannot (per the seed-batch decision):
in genuine high-stakes use, does an independent second pass ever catch a
decision-RELEVANT error the disciplined first pass missed — and does it ever FLIP the call?

Append-only ledger + PRE-REGISTERED rollup + read-out rule. Deterministic; testable offline.
The data accrues from your real use; this is the instrument, not the dataset.
"""
import json, os, sys, argparse, datetime

HERE=os.path.dirname(os.path.abspath(__file__))
LEDGER=os.environ.get("INSIGHT_ENGINE_LEDGER") or os.path.join(HERE,"ledger.jsonl")

# ---- FROZEN coding (do not change without a dated amendment; that is the point) ----
VERDICTS = ["real-catch-flipped",         # a genuine catch that WOULD have changed the call
            "real-catch-refined",         # a genuine, decision-relevant sharpening (did not flip)
            "useful-not-decision-relevant",# valid but would not change the decision
            "false-alarm",                # a confident objection that was wrong / would have corrupted
            "nothing"]                    # adjudicator raised nothing material
RUNGS = ["A-crosslab","B-fable","C-panel","D-self"]
K_MIN = 20            # minimum real high-stakes runs before the rule reads out
FLIP_THRESHOLD = 1    # >=1 operator-agreed, observable-backed flip on a real call => adjudication earned its place
# A "flip" counts ONLY if: operator agrees, it names a discriminating observable, and it would have reversed
# or materially changed a real high-stakes decision. A hunch without an observable does NOT count.

# ---- AMENDMENT-1 (dated 2026-07-09; pre-registered before any cross-lab run) ----
# Clean "cross-lab (rung A) SPECIFICALLY earned its place" read-out, isolated from the blended rate.
CROSSLAB_K_MIN = 12          # min rung-A runs before a "negligible" cross-lab conclusion may be drawn
CROSSLAB_FLIP_THRESHOLD = 1  # >=1 operator-agreed, observable-backed flip on a rung-A run => cross-lab earned its place

# ---- AMENDMENT-2 (dated 2026-07-13; pre-registered) ----
# Per-class, per-rung retirement rule: does adjudication become redundant for a class of
# problem as analyser models strengthen? Decided from the ledger, reversibly, never wholesale.
# Optional ledger fields: class, panel_n, labs, runs_per_model, blind_divergence, provider, record_type.
RETIRE_N = 20  # adjudications in a (class, rung) window before condition (a) may read out

# ---- AMENDMENT-3 (dated 2026-07-14; pre-registered) ----
# Per-provider cross-lab yield: with multi-provider rung A, split the rung-A read-out by lab
# (openai / google / xai / other:<name>) so the ledger shows which provider's runs earn the value.
# Optional ledger field: provider. Read-out only; no threshold, no auto-action; records without it
# count under 'unspecified'. Changes no pre-registered count or verdict.

def append(rec, path=None):
    rec["ts"]=datetime.datetime.now().isoformat(timespec="seconds")
    if rec.get("record_type")=="override":
        # AMENDMENT-2: a governance-block override record. No verdict/rung asserts, and it is
        # EXCLUDED from every rollup count so it cannot dilute the pre-registered read-outs.
        with open(path or LEDGER,"a",encoding="utf-8") as f: f.write(json.dumps(rec)+"\n")
        return rec
    assert rec.get("operator_verdict") in VERDICTS, f"verdict must be one of {VERDICTS}"
    assert rec.get("adjudicator_rung") in RUNGS, f"rung must be one of {RUNGS}"
    if rec.get("would_have_flipped_call"):
        assert rec.get("operator_agreed") and rec.get("discriminating_observable"), \
            "a flip requires operator_agreed=true AND a discriminating_observable"
    with open(path or LEDGER,"a",encoding="utf-8") as f: f.write(json.dumps(rec)+"\n")
    return rec

def load(path=LEDGER):
    return [json.loads(l) for l in open(path,encoding="utf-8")] if os.path.exists(path) else []

def rollup(recs):
    recs=[r for r in recs if r.get("record_type")!="override"]  # AMENDMENT-2: overrides never counted
    n=len(recs)
    flips=[r for r in recs if r.get("would_have_flipped_call") and r.get("operator_agreed") and r.get("discriminating_observable")]
    catches=[r for r in recs if r.get("operator_verdict") in ("real-catch-flipped","real-catch-refined")]
    fa=[r for r in recs if r.get("operator_verdict")=="false-alarm"]
    by_rung={}
    for r in recs: by_rung[r.get("adjudicator_rung","?")]=by_rung.get(r.get("adjudicator_rung","?"),0)+1
    rung_stats={}
    for rg in by_rung:
        rr=[r for r in recs if r.get("adjudicator_rung")==rg]
        rf=[r for r in rr if r.get("would_have_flipped_call") and r.get("operator_agreed") and r.get("discriminating_observable")]
        rc=[r for r in rr if r.get("operator_verdict") in ("real-catch-flipped","real-catch-refined")]
        rung_stats[rg]={"n":len(rr),"flips":len(rf),"catches":len(rc)}
    return dict(n=n, flips=len(flips), catch=len(catches), false_alarm=len(fa),
                flip_rate=(len(flips)/n if n else 0), catch_rate=(len(catches)/n if n else 0),
                fa_rate=(len(fa)/n if n else 0), by_rung=by_rung, rung_stats=rung_stats, flip_records=flips)

def readout(ro):
    if ro["n"] < K_MIN:
        return f"ACCRUING ({ro['n']}/{K_MIN} real high-stakes runs) — no read-out yet."
    if ro["flips"] >= FLIP_THRESHOLD:
        return (f"ADJUDICATION EARNED ITS PLACE — {ro['flips']} real, operator-agreed, observable-backed "
                f"call-flip(s) in {ro['n']} runs. Prioritise building it properly (and note the false-alarm rate {ro['fa_rate']:.0%}).")
    return (f"DECISION-FLIP BENEFIT NEGLIGIBLE IN PRACTICE — 0 flips in {ro['n']} runs. Keep adjudication only as an "
            f"OPTIONAL refinement check (decision-relevant catch-rate {ro['catch_rate']:.0%}, false-alarm {ro['fa_rate']:.0%}).")

def crosslab_readout(ro):
    st=ro["rung_stats"].get("A-crosslab")
    if not st or st["n"]==0: return "no cross-lab (rung A) runs logged yet."
    if st["flips"]>=CROSSLAB_FLIP_THRESHOLD:
        return f"CROSS-LAB EARNED ITS PLACE — {st['flips']} operator-agreed, observable-backed flip(s) in {st['n']} rung-A run(s)."
    if st["n"]>=CROSSLAB_K_MIN:
        return f"CROSS-LAB decision-flip benefit NEGLIGIBLE in practice — 0 flips in {st['n']} rung-A runs (>= K_MIN {CROSSLAB_K_MIN})."
    return f"cross-lab ACCRUING ({st['n']}/{CROSSLAB_K_MIN} rung-A runs)."

def crosslab_provider_readout(recs):
    """AMENDMENT-3 (2026-07-14): split the rung-A yield by lab, so the ledger shows which provider's
    runs earn the cross-lab value. Records without a provider count under 'unspecified'. Read-out
    only; no threshold, no auto-action; changes no pre-registered count."""
    a=[r for r in recs if r.get("record_type")!="override" and r.get("adjudicator_rung")=="A-crosslab"]
    if not a: return "  (no cross-lab rung-A runs logged yet)"
    groups={}
    for r in a: groups.setdefault(r.get("provider") or "unspecified",[]).append(r)
    L=[]
    for pv,rr in sorted(groups.items()):
        rf=[r for r in rr if r.get("would_have_flipped_call") and r.get("operator_agreed") and r.get("discriminating_observable")]
        rc=[r for r in rr if r.get("operator_verdict") in ("real-catch-flipped","real-catch-refined")]
        L.append(f"  - {pv}: {len(rr)} run(s) · {len(rf)} flip(s) · {len(rc)} decision-relevant catch(es)")
    return "\n".join(L)

def retirement_readout(recs):
    """AMENDMENT-2 per-(class,rung) read-out. Condition (a) is mechanical; (b)/(c) are rendered as
    operator-confirm lines (no ledger field captures them). Never auto-demotes."""
    adj=[r for r in recs if r.get("record_type")!="override"]
    groups={}
    for r in adj:
        groups.setdefault((r.get("class") or "unclassified", r.get("adjudicator_rung","?")),[]).append(r)
    L=[]
    for (cls,rung),rr in sorted(groups.items()):
        if cls=="unclassified":
            L.append(f"  - unclassified/{rung}: {len(rr)} run(s) - not eligible for retirement (tag runs with --class)")
            continue
        window=rr[-RETIRE_N:]
        if len(window)<RETIRE_N:
            L.append(f"  - {cls}/{rung}: accruing ({len(rr)}/{RETIRE_N})")
            continue
        real=[r for r in window if r.get("operator_verdict") in ("real-catch-flipped","real-catch-refined")]
        if real:
            L.append(f"  - {cls}/{rung}: KEEP - {len(real)} real catch(es) in last {RETIRE_N}")
        else:
            L.append(f"  - {cls}/{rung}: RETIRE-CANDIDATE - condition (a) met (0 real catches in last {RETIRE_N}). "
                     f"Confirm (b) under ~10% of useful items changed a caveat/grade AND (c) they duplicate the "
                     f"analyse first pass, then demote to on-request + keep a 1-in-10 audit. "
                     f"Economic redundancy, not tail safety.")
    a=[r for r in adj if r.get("adjudicator_rung")=="A-crosslab" and r.get("blind_divergence") is not None]
    if a:
        div=[r for r in a if r.get("blind_divergence")]
        L.append(f"  - monoculture watch (rung A): blind-pass divergence {len(div)}/{len(a)} ({len(div)/len(a):.0%}). "
                 f"If this trends to ~0 while errors still surface elsewhere, read rung-A silence as loss of signal, not safety.")
    return "\n".join(L) if L else "  (no adjudication records yet)"


def report(recs):
    ro=rollup(recs)
    L=[f"# Real-use monitor — rollup ({ro['n']} runs)",""]
    L.append(f"- **Call-flips (operator-agreed + observable-backed): {ro['flips']}  → flip-rate {ro['flip_rate']:.0%}**   ← the decisive metric")
    L.append(f"- Decision-relevant catches: {ro['catch']}  ({ro['catch_rate']:.0%})")
    L.append(f"- False alarms: {ro['false_alarm']}  ({ro['fa_rate']:.0%})")
    L.append(f"- By rung: {ro['by_rung']}")
    if len(ro["rung_stats"])>1:
        L.append("\n**Per rung (isolates cross-lab's marginal value — nothing to rebuild when rung A is added):**")
        for rg,st in ro["rung_stats"].items():
            L.append(f"  - {rg}: {st['n']} runs · {st['flips']} flip(s) · {st['catches']} decision-relevant catch(es)")
    L.append(f"\n**Read-out (pre-registered, K_MIN={K_MIN}, flip-threshold={FLIP_THRESHOLD}):** {readout(ro)}")
    L.append(f"**Cross-lab-specific read-out (AMENDMENT-1, 2026-07-09; K_MIN_A={CROSSLAB_K_MIN}, threshold={CROSSLAB_FLIP_THRESHOLD}):** {crosslab_readout(ro)}")
    L.append(f"\n**Per-provider cross-lab split (AMENDMENT-3, 2026-07-14):**")
    L.append(crosslab_provider_readout(recs))
    L.append(f"\n**Per-class retirement read-out (AMENDMENT-2, 2026-07-13; RETIRE_N={RETIRE_N}):**")
    L.append(retirement_readout(recs))
    if ro["flip_records"]:
        L.append("\n**Flip records — the ones that matter; audit each:**")
        for r in ro["flip_records"]:
            L.append(f"- {r.get('problem_slug','?')} [{r.get('adjudicator_rung')}]: {r.get('notes','')[:140]}")
    L.append("\n_Observational, not controlled: high-stakes runs only; operator self-codes (hence the observable requirement); N accrues slowly; no counterfactual for self-catch-on-reflection. It gives a practical base rate, not a proof._")
    return "\n".join(L)

def _selftest():
    import tempfile
    tf=tempfile.mkdtemp(); p=os.path.join(tf,"ledger.jsonl"); ok=True
    def check(c,m):
        nonlocal ok
        ok=ok and bool(c); print("  [%s] %s"%("ok  " if c else "FAIL",m))
    def rec(verdict="nothing",rung="A-crosslab",cls="legal-exposure",**kw):
        d=dict(problem_slug="t",stakes_tier="high",adjudicator_rung=rung,items_raised=0,
               items_decision_relevant_after_rank=0,operator_verdict=verdict,
               would_have_flipped_call=False,operator_agreed=False,discriminating_observable="",notes="")
        if cls is not None: d["class"]=cls
        d.update(kw); return d
    append(rec(cls=None),path=p)
    check(len(load(p))==1, "legacy-style record loads")
    check("unclassified" in retirement_readout(load(p)), "no class -> unclassified, not retired")
    for _ in range(19): append(rec(),path=p)
    check("accruing" in retirement_readout(load(p)), "19 in class -> accruing (<20)")
    append(rec(),path=p)
    ro_txt=retirement_readout(load(p))
    check("RETIRE-CANDIDATE" in ro_txt, "20 nothing in class -> retire-candidate")
    check("economic redundancy" in ro_txt.lower(), "retire text carries honesty bound")
    append(rec(verdict="real-catch-refined"),path=p)
    check("KEEP" in retirement_readout(load(p)), "real catch in window -> KEEP")
    for _ in range(RETIRE_N): append(rec(),path=p)
    t=retirement_readout(load(p))
    check("RETIRE-CANDIDATE" in t and "KEEP" not in t, "catch scrolled out of last-RETIRE_N window -> retire-candidate again")
    n_before=rollup(load(p))["n"]
    append(dict(record_type="override",problem_slug="t",override_kind="privileged",reason="op override"),path=p)
    n_after=rollup(load(p))["n"]
    check(n_before==n_after, "override record does not change rollup n")
    ro=rollup(load(p))
    check(isinstance(readout(ro),str) and isinstance(crosslab_readout(ro),str), "AMENDMENT-1 read-outs still compute")
    append(rec(blind_divergence=True),path=p)
    check("monoculture watch" in retirement_readout(load(p)), "blind_divergence -> monoculture line")
    n0=rollup(load(p))["n"]
    append(rec(provider="openai",verdict="real-catch-refined"),path=p)
    check(rollup(load(p))["n"]==n0+1, "a record with a provider counts normally in the rollup")
    append(rec(provider="google"),path=p)
    pr=crosslab_provider_readout(load(p))
    check("openai" in pr and "google" in pr, "AMENDMENT-3 per-provider split lists each lab")
    import subprocess
    env=dict(os.environ); env["INSIGHT_ENGINE_LEDGER"]=os.path.join(tf,"cli.jsonl")
    r=subprocess.run([sys.executable,os.path.abspath(__file__),"add","--slug","c","--rung","A-crosslab",
                      "--verdict","nothing","--class","cls","--panel-n","2","--labs","1",
                      "--runs-per-model","auto","--blind-divergence","no","--provider","openai"],capture_output=True,text=True,env=env)
    check(r.returncode==0 and os.path.exists(env["INSIGHT_ENGINE_LEDGER"]), "CLI add accepts new flags (argparse dests resolve)")
    ov=subprocess.run([sys.executable,os.path.abspath(__file__),"override","--slug","c","--kind","privileged"],
                      capture_output=True,text=True,env=env)
    check(ov.returncode==0, "CLI override subcommand runs")
    print("SELFTEST","OK" if ok else "FAILED")
    return 0 if ok else 1


if __name__=="__main__":
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd",required=True)
    lg=sub.add_parser("log"); lg.add_argument("--json",required=True,help="one ledger record as JSON")
    ad=sub.add_parser("add")
    ad.add_argument("--slug",required=True); ad.add_argument("--rung",required=True); ad.add_argument("--verdict",required=True)
    ad.add_argument("--tier",default="high"); ad.add_argument("--items",type=int,default=0); ad.add_argument("--relevant",type=int,default=0)
    ad.add_argument("--flip",action="store_true"); ad.add_argument("--agreed",action="store_true")
    ad.add_argument("--observable",default=""); ad.add_argument("--notes",default="")
    ad.add_argument("--class",dest="cls",default=None,help="AMENDMENT-2 problem-class tag (absent -> unclassified)")
    ad.add_argument("--panel-n",type=int,default=None); ad.add_argument("--labs",type=int,default=None)
    ad.add_argument("--runs-per-model",dest="rpm",default=None)
    ad.add_argument("--blind-divergence",dest="bdiv",choices=["yes","no"],default=None,help="did the rung-A blind pass reach a different call?")
    ad.add_argument("--provider",default=None,help="AMENDMENT-3: the rung-A lab (openai/google/xai/other:<name>)")
    ov=sub.add_parser("override"); ov.add_argument("--slug",required=True)
    ov.add_argument("--kind",required=True,help="e.g. privileged, egress-off"); ov.add_argument("--reason",default="")
    sub.add_parser("report")
    sub.add_parser("selftest")
    a=ap.parse_args()
    if a.cmd=="add":
        rec=dict(problem_slug=a.slug,stakes_tier=a.tier,adjudicator_rung=a.rung,items_raised=a.items,
              items_decision_relevant_after_rank=a.relevant,operator_verdict=a.verdict,would_have_flipped_call=a.flip,
              operator_agreed=a.agreed,discriminating_observable=a.observable,notes=a.notes)
        if a.cls is not None: rec["class"]=a.cls
        if a.panel_n is not None: rec["panel_n"]=a.panel_n
        if a.labs is not None: rec["labs"]=a.labs
        if a.rpm is not None: rec["runs_per_model"]=a.rpm
        if a.bdiv is not None: rec["blind_divergence"]=(a.bdiv=="yes")
        if a.provider is not None: rec["provider"]=a.provider
        print("logged:", append(rec))
    elif a.cmd=="override":
        print("logged:", append(dict(record_type="override",problem_slug=a.slug,override_kind=a.kind,reason=a.reason)))
    elif a.cmd=="log": print("logged:", append(json.loads(a.json)))
    elif a.cmd=="selftest": sys.exit(_selftest())
    else: print(report(load()))
