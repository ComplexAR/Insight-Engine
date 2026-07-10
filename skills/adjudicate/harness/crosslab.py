#!/usr/bin/env python3
"""
Cross-lab adjudicator adapter (rung A) - the external-lab independent second pass.
Calls an external-lab frontier model (default OpenAI GPT-5.6 Sol) via its API, key from ENV,
egress-governed, stdlib only (urllib). A MockAdjudicator mirrors the interface for offline tests.

GOVERNANCE (build-spec 4a): off by default; `privileged -> never`; minimise the package;
zero-retention terms must be arranged with the provider out of band. The key is read from the
environment and NEVER logged.

CAVEAT: the request/response shape below targets the OpenAI Responses API as understood at build
time. VERIFY it against current OpenAI docs before the live run; the body is a single dict, easy to adjust.
"""
import os, json, urllib.request, urllib.error

# Rung-A external-lab model. Pre-registered target = gpt-5.6-sol, but it is in limited
# preview and not yet enabled on this account (OpenAI's own error says: use gpt-5.5 for now).
# gpt-5.5 is still a different-lab frontier model, so cross-lab independence holds. Override
# anytime with the CROSSLAB_MODEL env var; the model actually used is recorded in each
# report's _adjudicator_model field. Set CROSSLAB_MODEL=gpt-5.6-sol once Sol is enabled.
DEFAULT_MODEL = os.environ.get("CROSSLAB_MODEL", "gpt-5.5")
OPENAI_URL    = "https://api.openai.com/v1/responses"

class EgressBlocked(Exception): pass

def build_blind_text(blind_pkg, adjudicate_prompt):
    pj = json.dumps(blind_pkg, indent=2)
    if "{{blind_package}}" in adjudicate_prompt:
        return adjudicate_prompt.replace("{{blind_package}}", pj)
    return adjudicate_prompt.rstrip() + "\n\n=== BLIND PACKAGE ===\n" + pj

def _extract_text(raw):
    try:
        for item in raw.get("output", []):
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text") and c.get("text"):
                    return c["text"]
    except Exception:
        pass
    return raw.get("output_text") or json.dumps(raw)

def _parse_report(text, model):
    s = text.strip()
    i, j = s.find("{"), s.rfind("}")          # tolerate ```json fences / prose
    rep = json.loads(s[i:j+1]) if (i >= 0 and j > i) else {"raw": text}
    rep["_adjudicator_model"] = model
    rep["_rung"] = "A-crosslab"
    return rep

class CrossLabAdjudicator:
    rung = "A-crosslab"
    def __init__(self, model=DEFAULT_MODEL, egress_policy="off", effort="high", timeout=120):
        self.model, self.egress_policy, self.effort, self.timeout = model, egress_policy, effort, timeout
    def _key(self):
        k = os.environ.get("OPENAI_API_KEY")
        if not k: raise RuntimeError("OPENAI_API_KEY is not set in the environment")
        return k
    def _gate(self, privileged):
        if privileged:               raise EgressBlocked("privileged/confidential matter - cross-lab egress is NEVER permitted")
        if self.egress_policy=="off": raise EgressBlocked("egress_policy=off - set 'redacted' or 'full' to use a cross-lab model")
    def dispatch(self, blind_pkg, adjudicate_prompt, privileged=False):
        self._gate(privileged)
        body = {"model": self.model, "reasoning": {"effort": self.effort},
                "input": build_blind_text(blind_pkg, adjudicate_prompt)}
        req = urllib.request.Request(OPENAI_URL, method="POST",
              headers={"Authorization": f"Bearer {self._key()}", "Content-Type": "application/json"},
              data=json.dumps(body).encode())
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                raw = json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"OpenAI API HTTP {e.code}: {e.read()[:300]!r}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"network error reaching {OPENAI_URL}: {e}")
        return _parse_report(_extract_text(raw), self.model)

class MockAdjudicator(CrossLabAdjudicator):
    """Offline stand-in: same interface + gates, canned report; no network, no key, no spend."""
    def dispatch(self, blind_pkg, adjudicate_prompt, privileged=False):
        self._gate(privileged)
        canned = {"pass1_call": "(mock) independently reached a similar call",
                  "concur_with_analysis": True,
                  "disputes": [{"point": "dominance is load-bearing",
                                "challenge": "asserted but not decomposed",
                                "discriminating_observable": "pre/post split of the series",
                                "would_change_the_call": False}],
                  "omissions": ["a materially-affected party not in the room"],
                  "net": "refine"}
        return _parse_report(json.dumps(canned), "mock-" + self.model)
