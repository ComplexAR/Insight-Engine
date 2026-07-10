#!/usr/bin/env python3
"""Dry-run / live-run the cross-lab adjudicator.
  MOCK (default, offline, no key):   python run_crosslab.py
  LIVE (your env, your key, paid):   OPENAI_API_KEY=sk-... python run_crosslab.py --live
The `adjudicate` skill replaces SAMPLE with the finished analysis's blind package
(facts + grade-locked spine + draft brief; NO reasoning; redacted).
"""
import sys, json, os
from crosslab import CrossLabAdjudicator, MockAdjudicator, EgressBlocked

PROMPT = open(os.path.join(os.path.dirname(__file__), "prompts", "adjudicate.txt"), encoding="utf-8").read()
SAMPLE = {  # TEMPLATE - replace with the finished analysis's blind package
  "facts": "<one paragraph: the situation and the load-bearing facts>",
  "spine": {"claims": [{"claim": "<a load-bearing claim>", "grade": "[V1|V2|V3|N]"}],
            "dominant_unknown": "<the single fact that would most move the call>"},
  "draft_brief": {"call": "<the recommendation>",
                  "what_would_flip_it": "<the condition under which the call reverses>"},
  "supports_pass1": True}

live = "--live" in sys.argv
adj = CrossLabAdjudicator(egress_policy="redacted") if live else MockAdjudicator(egress_policy="redacted")
print(f"[{'LIVE ' + adj.model if live else 'MOCK'}]  egress={adj.egress_policy}")
try:
    rep = adj.dispatch(SAMPLE, PROMPT, privileged=False)
    print(json.dumps(rep, indent=2))
except (EgressBlocked, RuntimeError) as e:
    print("dispatch error:", e)
