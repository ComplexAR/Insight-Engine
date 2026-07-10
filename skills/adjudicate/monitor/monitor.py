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
LEDGER=os.path.join(HERE,"ledger.jsonl")

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

def append(rec):
    rec["ts"]=datetime.datetime.now().isoformat(timespec="seconds")
    assert rec.get("operator_verdict") in VERDICTS, f"verdict must be one of {VERDICTS}"
    assert rec.get("adjudicator_rung") in RUNGS, f"rung must be one of {RUNGS}"
    if rec.get("would_have_flipped_call"):
        assert rec.get("operator_agreed") and rec.get("discriminating_observable"), \
            "a flip requires operator_agreed=true AND a discriminating_observable"
    with open(LEDGER,"a",encoding="utf-8") as f: f.write(json.dumps(rec)+"\n")
    return rec

def load(path=LEDGER):
    return [json.loads(l) for l in open(path,encoding="utf-8")] if os.path.exists(path) else []

def rollup(recs):
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
    if ro["flip_records"]:
        L.append("\n**Flip records — the ones that matter; audit each:**")
        for r in ro["flip_records"]:
            L.append(f"- {r.get('problem_slug','?')} [{r.get('adjudicator_rung')}]: {r.get('notes','')[:140]}")
    L.append("\n_Observational, not controlled: high-stakes runs only; operator self-codes (hence the observable requirement); N accrues slowly; no counterfactual for self-catch-on-reflection. It gives a practical base rate, not a proof._")
    return "\n".join(L)

if __name__=="__main__":
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd",required=True)
    lg=sub.add_parser("log"); lg.add_argument("--json",required=True,help="one ledger record as JSON")
    ad=sub.add_parser("add")
    ad.add_argument("--slug",required=True); ad.add_argument("--rung",required=True); ad.add_argument("--verdict",required=True)
    ad.add_argument("--tier",default="high"); ad.add_argument("--items",type=int,default=0); ad.add_argument("--relevant",type=int,default=0)
    ad.add_argument("--flip",action="store_true"); ad.add_argument("--agreed",action="store_true")
    ad.add_argument("--observable",default=""); ad.add_argument("--notes",default="")
    sub.add_parser("report")
    a=ap.parse_args()
    if a.cmd=="add":
        print("logged:", append(dict(problem_slug=a.slug,stakes_tier=a.tier,adjudicator_rung=a.rung,items_raised=a.items,
              items_decision_relevant_after_rank=a.relevant,operator_verdict=a.verdict,would_have_flipped_call=a.flip,
              operator_agreed=a.agreed,discriminating_observable=a.observable,notes=a.notes)))
    elif a.cmd=="log": print("logged:", append(json.loads(a.json)))
    else: print(report(load()))
