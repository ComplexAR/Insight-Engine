#!/usr/bin/env python3
"""Dry-run / live-run the cross-lab adjudicator.
  MOCK (default, offline, no key):   python run_crosslab.py
  LIVE (your env, your key, paid):   set the resolved provider's API key, then: python run_crosslab.py --live
  If the matter is privileged/confidential, add --privileged (cross-lab is then blocked by
  default); overriding that block is a deliberate act: --privileged --override-privileged.

TWO DISPATCHES, NOT ONE. Pass 1 is blind by CONSTRUCTION: the outbound package carries the case
facts and the grade-locked spine, and the analysis's call is not in it. Only after pass 1 returns is
the draft brief revealed, in a second call, for the adversarial pass.

  Why: a single call that carries the brief and asks the model not to look at it until pass 2 makes
  the blindness a matter of the model's compliance. The adjudicator cannot use what it was not sent.

  Cost: this is two paid calls per rung-A run, not one. That is the price of the guarantee.

The `adjudicate` skill replaces CASE and DRAFT_BRIEF with the finished analysis's material.
Model resolves as: CROSSLAB_MODEL env (per-run override) -> the standing crosslab_model preference -> the built-in default.
"""
import sys, json, os, argparse

# Resolve adjudication prefs -> CROSSLAB_* env (provider / model / base-url / key-env / lineage),
# BEFORE importing crosslab so it reads them at import (keeps crosslab.py pure). A shell env var
# always wins; else the standing preference; else the adapter's built-in default.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import crosslab_env
    crosslab_env.resolve()
except Exception:
    pass

from crosslab import CrossLabAdjudicator, MockAdjudicator, EgressBlocked

_P = lambda name: open(os.path.join(os.path.dirname(__file__), "prompts", name), encoding="utf-8").read()
PROMPT_BLIND = _P("adjudicate.txt")
PROMPT_ADVERSARIAL = _P("adversarial.txt")

# TEMPLATE - replace CASE and DRAFT_BRIEF with the finished analysis's material.
# CASE is everything pass 1 may see. DRAFT_BRIEF is withheld until pass 2.
CASE = {
  "facts": "<one paragraph: the situation and the load-bearing facts>",
  "spine": {"claims": [{"claim": "<a load-bearing claim>", "grade": "[V1|V2|V3|N]"}],
            "dominant_unknown": "<the single fact that would most move the call>"}}

DRAFT_BRIEF = {"call": "<the recommendation>",
               "what_would_flip_it": "<the condition under which the call reverses>"}

ap = argparse.ArgumentParser(description="Dry-run / live-run the cross-lab adjudicator (rung A).")
ap.add_argument("--live", action="store_true", help="make the real paid calls (needs the resolved provider's API key); note this is TWO calls")
ap.add_argument("--privileged", action="store_true",
                help="flag this matter privileged/confidential (blocks cross-lab by default)")
ap.add_argument("--override-privileged", dest="override_privileged", action="store_true",
                help="deliberately override a privileged block (no effect without --privileged)")
ap.add_argument("--blind-only", action="store_true",
                help="run pass 1 and stop, without revealing the draft brief")
a = ap.parse_args()

if a.override_privileged and not a.privileged:
    print("note: --override-privileged has no effect without --privileged; there is nothing to override.")

adj = CrossLabAdjudicator(egress_policy="redacted") if a.live else MockAdjudicator(egress_policy="redacted")
print(f"[{('LIVE ' if a.live else 'MOCK ') + adj.provider + '/' + adj.model}]  egress={adj.egress_policy}  privileged={a.privileged}  override={a.override_privileged}")

# Guard: the call must not be reachable from the pass-1 package by any route.
assert "draft_brief" not in CASE and "call" not in CASE, \
    "the blind package must not carry the draft brief or the call"

try:
    print("\n--- PASS 1 (blind: facts + spine; the call is not sent) ---")
    pass1 = adj.dispatch(CASE, PROMPT_BLIND,
                         privileged=a.privileged, override_privileged=a.override_privileged)
    print(json.dumps(pass1, indent=2))

    if a.blind_only:
        print("\n--blind-only: stopping before the draft brief is revealed.")
        sys.exit(0)

    # crosslab.py substitutes exactly one token, {{blind_package}}; the pass-2 prompt reuses it for
    # the pass-2 package so the transport needs no change.
    print("\n--- PASS 2 (adversarial: the draft brief is revealed now) ---")
    pass2 = adj.dispatch({"your_pass1_verdict": pass1, "draft_brief": DRAFT_BRIEF},
                         PROMPT_ADVERSARIAL,
                         privileged=a.privileged, override_privileged=a.override_privileged)
    print(json.dumps(pass2, indent=2))

except (EgressBlocked, RuntimeError) as e:
    # A pass-1 failure stops the run: there is no adversarial pass without a blind verdict to attack.
    print("dispatch error:", e)
