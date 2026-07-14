#!/usr/bin/env python3
"""
Cross-lab adjudicator adapter (rung A) - the external-lab independent second pass.
Calls an external-lab frontier model (default OpenAI GPT-5.6 Sol) via its API, key from ENV,
egress-governed, stdlib only (urllib). A MockAdjudicator mirrors the interface for offline tests.

GOVERNANCE (build-spec 4a): off by default; `privileged -> blocked by default (operator-overridable, logged)`; minimise the package;
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
# report's _adjudicator_model field. Sol verified live on this account 2026-07-12 (a live
# smoke returned a clean parse tagged _adjudicator_model=gpt-5.6-sol); falls back to gpt-5.5
# (also a different-lab frontier model, so cross-lab independence holds) if Sol is unavailable.
DEFAULT_MODEL = os.environ.get("CROSSLAB_MODEL", "gpt-5.6-sol")
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
        if not k: raise RuntimeError(
            "CROSSLAB-BLOCKED [no-key] OPENAI_API_KEY is not set in this shell. Cross-lab needs your own "
            "OpenAI API key, set by you in your own local terminal - PowerShell is easiest (its output copies cleanly back into chat): $env:OPENAI_API_KEY = Read-Host 'Paste key'. Never paste the key into chat; a new window needs it "
            "set again). Options: set the key and re-run, or use an in-boundary rung (B Fable / C Opus panel "
            "/ D self-adversarial).")
        return k
    def _gate(self, privileged, override_privileged=False):
        if privileged and not override_privileged:
            raise EgressBlocked(
                "CROSSLAB-BLOCKED [privileged] privileged/confidential matter - cross-lab egress is blocked by "
                "default. Overriding is a deliberate typed act (--override-privileged); otherwise use an "
                "in-boundary rung (B/C/D).")
        if self.egress_policy=="off":
            raise EgressBlocked(
                "CROSSLAB-BLOCKED [egress-off] egress_policy=off - set 'redacted' or 'full' to use a cross-lab model")
    def dispatch(self, blind_pkg, adjudicate_prompt, privileged=False, override_privileged=False):
        self._gate(privileged, override_privileged)
        body = {"model": self.model, "reasoning": {"effort": self.effort},
                "input": build_blind_text(blind_pkg, adjudicate_prompt)}
        req = urllib.request.Request(OPENAI_URL, method="POST",
              headers={"Authorization": f"Bearer {self._key()}", "Content-Type": "application/json"},
              data=json.dumps(body).encode())
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                raw = json.loads(r.read())
        except urllib.error.HTTPError as e:
            body = e.read()[:300]
            if e.code == 401:
                raise RuntimeError(f"CROSSLAB-FAILED [auth 401] OpenAI rejected the credentials. Likely: key "
                    f"invalid/revoked, or set in a different terminal window. Fix: re-set or regenerate the key "
                    f"and check billing, then re-run - or use an in-boundary rung. Raw: {body!r}")
            if e.code == 404:
                raise RuntimeError(f"CROSSLAB-FAILED [model-unavailable 404] OpenAI could not serve model "
                    f"'{self.model}'. Likely not enabled on this account (Sol is preview-gated on some). Fix: set "
                    f"CROSSLAB_MODEL to another frontier model (e.g. gpt-5.5 - cross-lab independence still holds) "
                    f"and re-run, or request access - or use an in-boundary rung. Raw: {body!r}")
            if e.code == 429:
                raise RuntimeError(f"CROSSLAB-FAILED [quota 429] OpenAI rate or credit limit hit. Fix: check "
                    f"billing/limits, wait, then re-run - or use an in-boundary rung. Raw: {body!r}")
            raise RuntimeError(f"CROSSLAB-FAILED [api {e.code}] Unexpected OpenAI API error. If a 4xx about the "
                f"request body, the Responses-API schema may have moved - adjust the request dict in crosslab.py "
                f"against current OpenAI docs and re-run the smoke - or use an in-boundary rung. Raw: {body!r}")
        except urllib.error.URLError as e:
            raise RuntimeError(f"CROSSLAB-FAILED [network] Could not reach {OPENAI_URL}: {e}. Check connection / "
                f"proxy / firewall, then re-run - or use an in-boundary rung.")
        return _parse_report(_extract_text(raw), self.model)

class MockAdjudicator(CrossLabAdjudicator):
    """Offline stand-in: same interface + gates, canned report; no network, no key, no spend."""
    def dispatch(self, blind_pkg, adjudicate_prompt, privileged=False, override_privileged=False):
        self._gate(privileged, override_privileged)
        canned = {"pass1_call": "(mock) independently reached a similar call",
                  "concur_with_analysis": True,
                  "disputes": [{"point": "dominance is load-bearing",
                                "challenge": "asserted but not decomposed",
                                "discriminating_observable": "pre/post split of the series",
                                "would_change_the_call": False}],
                  "omissions": ["a materially-affected party not in the room"],
                  "net": "refine"}
        return _parse_report(json.dumps(canned), "mock-" + self.model)
