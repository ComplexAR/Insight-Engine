#!/usr/bin/env python3
"""Dry-run / live-run the cross-lab adjudicator.
  MOCK (default, offline, no key):   python run_crosslab.py
  LIVE (your env, your key, paid):   OPENAI_API_KEY=sk-... python run_crosslab.py --live
  If the matter is privileged/confidential, add --privileged (cross-lab is then blocked by
  default); overriding that block is a deliberate act: --privileged --override-privileged.
The `adjudicate` skill replaces SAMPLE with the finished analysis's blind package
(facts + grade-locked spine + draft brief; NO reasoning; redacted).
Model resolves as: CROSSLAB_MODEL env (per-run override) -> the standing crosslab_model preference -> the built-in default.
"""
import sys, json, os, argparse

# Resolve the cross-lab model: an explicit CROSSLAB_MODEL env wins (per-run override); else fall
# back to the standing crosslab_model preference; else crosslab.py's built-in default. Set the env
# BEFORE importing crosslab so its DEFAULT_MODEL (read at import) picks it up - keeps crosslab.py
# pure (it never imports prefs).
if not os.environ.get("CROSSLAB_MODEL"):
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "prefs"))
        import prefs as _prefs
        _m = _prefs.get_value("crosslab_model")
        if _m:
            os.environ["CROSSLAB_MODEL"] = _m
    except Exception:
        pass

from crosslab import CrossLabAdjudicator, MockAdjudicator, EgressBlocked

PROMPT = open(os.path.join(os.path.dirname(__file__), "prompts", "adjudicate.txt"), encoding="utf-8").read()
SAMPLE = {  # TEMPLATE - replace with the finished analysis's blind package
  "facts": "<one paragraph: the situation and the load-bearing facts>",
  "spine": {"claims": [{"claim": "<a load-bearing claim>", "grade": "[V1|V2|V3|N]"}],
            "dominant_unknown": "<the single fact that would most move the call>"},
  "draft_brief": {"call": "<the recommendation>",
                  "what_would_flip_it": "<the condition under which the call reverses>"},
  "supports_pass1": True}

ap = argparse.ArgumentParser(description="Dry-run / live-run the cross-lab adjudicator (rung A).")
ap.add_argument("--live", action="store_true", help="make the real paid call (needs OPENAI_API_KEY)")
ap.add_argument("--privileged", action="store_true",
                help="flag this matter privileged/confidential (blocks cross-lab by default)")
ap.add_argument("--override-privileged", dest="override_privileged", action="store_true",
                help="deliberately override a privileged block (no effect without --privileged)")
a = ap.parse_args()

if a.override_privileged and not a.privileged:
    print("note: --override-privileged has no effect without --privileged; there is nothing to override.")

adj = CrossLabAdjudicator(egress_policy="redacted") if a.live else MockAdjudicator(egress_policy="redacted")
print(f"[{('LIVE ' if a.live else 'MOCK ') + adj.model}]  egress={adj.egress_policy}  privileged={a.privileged}  override={a.override_privileged}")
try:
    rep = adj.dispatch(SAMPLE, PROMPT, privileged=a.privileged, override_privileged=a.override_privileged)
    print(json.dumps(rep, indent=2))
except (EgressBlocked, RuntimeError) as e:
    print("dispatch error:", e)
