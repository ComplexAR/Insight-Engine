#!/usr/bin/env python3
"""
Cross-lab adjudicator adapter (rung A) - the external-lab independent second pass.
Calls an external-lab frontier model (default OpenAI GPT-5.6 Sol) via its API, key from ENV,
egress-governed, stdlib only (urllib). A MockAdjudicator mirrors the interface for offline tests.

GOVERNANCE (build-spec 4a): off by default; `privileged -> blocked by default (operator-overridable, logged)`; minimise the package;
zero-retention terms must be arranged with the provider out of band. The key is read from the
environment and NEVER logged.

PROVIDERS: rung A is provider-agnostic via the PROVIDERS registry below - each entry supplies its
lab's endpoint, auth header, request body, response extraction, and error classification. crosslab.py
stays pure (reads only CROSSLAB_MODEL / CROSSLAB_PROVIDER from the environment; the runners resolve
prefs -> env before importing this module). Adapters target each lab's frontier REASONING surface.

CAVEAT: each adapter's request/response shape targets that lab's API as understood at build time.
VERIFY against current provider docs before the live run; each body is a single dict, easy to adjust.
"""
import os, re, json, urllib.request, urllib.error, urllib.parse

# --- resolution (env only; keeps crosslab.py pure - it never imports prefs) ---
DEFAULT_PROVIDER = os.environ.get("CROSSLAB_PROVIDER", "openai")
DEFAULT_MODEL    = os.environ.get("CROSSLAB_MODEL", "")   # "" -> resolved to the provider's default_model

OPENAI_URL = "https://api.openai.com/v1/responses"

class EgressBlocked(Exception): pass

# --- same-lineage guard (3A): rung A must be a DIFFERENT lab from the Anthropic analyser ---
ANTHROPIC_HOSTS = ("anthropic.com", "claude.ai")
_LINEAGE_TOKENS = re.compile(r"(?<![a-z0-9])(claude|opus|sonnet|haiku|fable)(?![a-z0-9])")

def _host(url):
    try:
        h = urllib.parse.urlsplit(url).hostname
        if not h and url: h = urllib.parse.urlsplit("//" + url.lstrip("/")).hostname   # scheme-less
        return (h or "").lower()
    except Exception:
        return ""

def _same_lineage_reason(provider_lineage, model, base_url=None, declared_lineage=None):
    """Return a short reason if the rung-A target is the analyser's (Anthropic) lineage, else ''.
    Provider / host / declared-lineage are the firm signals; model-name tokens are matched with
    word boundaries so an innocent name from a genuinely different lab is not falsely trapped."""
    if (provider_lineage or "").lower() == "anthropic": return f"provider lineage '{provider_lineage}'"
    dl = (declared_lineage or "").lower()
    if "anthropic" in dl or "claude" in dl: return f"declared lineage '{declared_lineage}'"
    h = _host(base_url or "")
    if h and any(h == a or h.endswith("." + a) for a in ANTHROPIC_HOSTS): return f"endpoint host '{h}'"
    if "anthropic" in (base_url or "").lower(): return "endpoint URL contains 'anthropic'"
    m = (model or "").lower()
    if "anthropic" in m or _LINEAGE_TOKENS.search(m): return f"model name '{model}'"
    return ""

def _lineage_guard(provider_lineage, model, base_url=None, declared_lineage=None):
    reason = _same_lineage_reason(provider_lineage, model, base_url, declared_lineage)
    if reason:
        raise EgressBlocked(
            f"CROSSLAB-BLOCKED [same-lineage] the configured rung-A target ({reason}) is the same lineage as the "
            "analyser (Anthropic) - this is NOT cross-lab, so the decorrelation rung A exists for collapses. There "
            "is no override. Use a different lab for rung A, or use rung B (Fable) / C (Opus panel), which are "
            "honestly declared as same-lineage checks.")

def build_blind_text(blind_pkg, adjudicate_prompt):
    pj = json.dumps(blind_pkg, indent=2)
    if "{{blind_package}}" in adjudicate_prompt:
        return adjudicate_prompt.replace("{{blind_package}}", pj)
    return adjudicate_prompt.rstrip() + "\n\n=== BLIND PACKAGE ===\n" + pj

# ---------------------------------------------------------------------------
# Provider adapters. Each entry is metadata + pure functions; CrossLabAdjudicator
# is provider-agnostic and simply drives the resolved adapter. (A1 ships openai;
# google/xai/other arrive in later commits.)
#   endpoint(model, base_url) -> url
#   headers(key)              -> dict
#   body(model, text, effort) -> dict
#   extract_text(raw)         -> str
#   classify(http_error, model, url) -> full CROSSLAB-FAILED message
# ---------------------------------------------------------------------------

def _openai_extract_text(raw):
    try:
        for item in raw.get("output", []):
            for c in item.get("content", []):
                if c.get("type") in ("output_text", "text") and c.get("text"):
                    return c["text"]
    except Exception:
        pass
    return raw.get("output_text") or json.dumps(raw)

def _openai_classify(e, model, url):
    body = e.read()[:300]
    if e.code == 401:
        return (f"CROSSLAB-FAILED [auth 401] OpenAI rejected the credentials. Likely: key "
                f"invalid/revoked, or set in a different terminal window. Fix: re-set or regenerate the key "
                f"and check billing, then re-run - or use an in-boundary rung. Raw: {body!r}")
    if e.code == 404:
        return (f"CROSSLAB-FAILED [model-unavailable 404] OpenAI could not serve model "
                f"'{model}'. Likely not enabled on this account (Sol is preview-gated on some). Fix: set "
                f"CROSSLAB_MODEL to another frontier model (e.g. gpt-5.5 - cross-lab independence still holds) "
                f"and re-run, or request access - or use an in-boundary rung. Raw: {body!r}")
    if e.code == 429:
        return (f"CROSSLAB-FAILED [quota 429] OpenAI rate or credit limit hit. Fix: check "
                f"billing/limits, wait, then re-run - or use an in-boundary rung. Raw: {body!r}")
    return (f"CROSSLAB-FAILED [api {e.code}] Unexpected OpenAI API error. If a 4xx about the "
            f"request body, the Responses-API schema may have moved - adjust the request dict in crosslab.py "
            f"against current OpenAI docs and re-run the smoke - or use an in-boundary rung. Raw: {body!r}")

def _gemini_extract_text(raw):
    try:
        parts = raw["candidates"][0]["content"]["parts"]
        t = "".join(p.get("text", "") for p in parts if isinstance(p, dict))
        if t: return t
    except Exception:
        pass
    return json.dumps(raw)

def _gemini_classify(e, model, url):
    body = e.read()[:300]
    if e.code in (401, 403):
        return (f"CROSSLAB-FAILED [auth {e.code}] Google rejected the credentials (check GEMINI_API_KEY, key "
                f"permissions, billing). Fix: re-set or regenerate the key, then re-run - or use an in-boundary "
                f"rung. Raw: {body!r}")
    if e.code == 400 and b"API_KEY" in body:
        return (f"CROSSLAB-FAILED [auth 400] Google reports an invalid API key (GEMINI_API_KEY). Fix: re-set or "
                f"regenerate the key, then re-run - or use an in-boundary rung. Raw: {body!r}")
    if e.code == 404:
        return (f"CROSSLAB-FAILED [model-unavailable 404] Google could not serve model '{model}'. Fix: set "
                f"CROSSLAB_MODEL to a current Gemini model (e.g. gemini-3.5-flash) and re-run - or use an "
                f"in-boundary rung. Raw: {body!r}")
    if e.code == 429:
        return (f"CROSSLAB-FAILED [quota 429] Google rate or quota limit hit. Fix: check quota/billing, wait, "
                f"then re-run - or use an in-boundary rung. Raw: {body!r}")
    return (f"CROSSLAB-FAILED [api {e.code}] Unexpected Google Gemini API error. If a 4xx about the request "
            f"body, the generateContent schema may have moved - adjust the google adapter in crosslab.py against "
            f"current Gemini docs and re-run the smoke - or use an in-boundary rung. Raw: {body!r}")

def _xai_extract_text(raw):
    try:
        return raw["choices"][0]["message"]["content"]
    except Exception:
        return json.dumps(raw)

def _xai_classify(e, model, url):
    body = e.read()[:300]
    if e.code == 401:
        return (f"CROSSLAB-FAILED [auth 401] xAI rejected the credentials (check XAI_API_KEY). Fix: re-set or "
                f"regenerate the key and check billing, then re-run - or use an in-boundary rung. Raw: {body!r}")
    if e.code == 404:
        return (f"CROSSLAB-FAILED [model-unavailable 404] xAI could not serve model '{model}'. Fix: set "
                f"CROSSLAB_MODEL to a current Grok model (e.g. grok-4.5) and re-run - or use an in-boundary "
                f"rung. Raw: {body!r}")
    if e.code == 429:
        return (f"CROSSLAB-FAILED [quota 429] xAI rate or credit limit hit. Fix: check billing/limits, wait, "
                f"then re-run - or use an in-boundary rung. Raw: {body!r}")
    return (f"CROSSLAB-FAILED [api {e.code}] Unexpected xAI API error. If a 4xx about the request body, the "
            f"chat-completions schema may have moved - adjust the xai adapter in crosslab.py against current "
            f"xAI docs and re-run the smoke - or use an in-boundary rung. Raw: {body!r}")

def _other_classify(e, model, url):
    body = e.read()[:300]
    if e.code == 401:
        return (f"CROSSLAB-FAILED [auth 401] the configured endpoint rejected the credentials (check the key env "
                f"named by CROSSLAB_OTHER_KEY_ENV). Fix: re-set the key, then re-run - or use a predefined provider "
                f"/ an in-boundary rung. Raw: {body!r}")
    if e.code == 404:
        return (f"CROSSLAB-FAILED [model-unavailable 404] the endpoint could not serve model '{model}' at {url}. "
                f"Your CROSSLAB_BASE_URL may need or must drop a path segment (e.g. '/v1'), or the endpoint is not "
                f"OpenAI-chat-completions compatible, or the model name is wrong. Raw: {body!r}")
    if e.code == 429:
        return (f"CROSSLAB-FAILED [quota 429] the endpoint hit a rate or credit limit. Fix: check billing/limits, "
                f"wait, then re-run - or use an in-boundary rung. Raw: {body!r}")
    return (f"CROSSLAB-FAILED [api {e.code}] unexpected error from the configured endpoint {url}. If a 4xx about "
            f"the request body, this endpoint may not be OpenAI-chat-completions compatible; use a predefined "
            f"provider or the pluggable-adapter mode - or an in-boundary rung. Raw: {body!r}")

PROVIDERS = {
    "openai": {
        "key_env":        "OPENAI_API_KEY",
        "label":          "OpenAI",
        "default_model":  "gpt-5.6-sol",
        "lineage":        "openai",
        "model_prefixes": ("gpt-", "o1", "o3", "o4"),
        "endpoint":       lambda model, base_url: OPENAI_URL,
        "headers":        lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        "body":           lambda model, text, effort: {"model": model, "reasoning": {"effort": effort}, "input": text},
        "extract_text":   _openai_extract_text,
        "classify":       _openai_classify,
    },
    "google": {
        "key_env":        "GEMINI_API_KEY",
        "label":          "Google Gemini",
        "default_model":  "gemini-3.5-flash",
        "lineage":        "google",
        "model_prefixes": ("gemini-",),
        "endpoint":       lambda model, base_url: f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
        "headers":        lambda key: {"x-goog-api-key": key, "Content-Type": "application/json"},
        "body":           lambda model, text, effort: {"contents": [{"parts": [{"text": text}]}]},
        "extract_text":   _gemini_extract_text,
        "classify":       _gemini_classify,
    },
    "xai": {
        "key_env":        "XAI_API_KEY",
        "label":          "xAI Grok",
        "default_model":  "grok-4.5",
        "lineage":        "xai",
        "model_prefixes": ("grok-",),
        "endpoint":       lambda model, base_url: "https://api.x.ai/v1/chat/completions",
        "headers":        lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        "body":           lambda model, text, effort: {"model": model, "messages": [{"role": "user", "content": text}], "reasoning_effort": effort},
        "extract_text":   _xai_extract_text,
        "classify":       _xai_classify,
    },
    "other": {
        "key_env":        "CROSSLAB_OTHER_API_KEY",
        "label":          "cross-lab endpoint",
        "default_model":  "",
        "lineage":        "",
        "model_prefixes": (),
        "endpoint":       lambda model, base_url: (base_url or "").rstrip("/") + "/chat/completions",
        "headers":        lambda key: {"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        "body":           lambda model, text, effort: {"model": model, "messages": [{"role": "user", "content": text}]},
        "extract_text":   _xai_extract_text,
        "classify":       _other_classify,
    },
}

def _parse_report(text, model, provider):
    s = text.strip()
    i, j = s.find("{"), s.rfind("}")          # tolerate ```json fences / prose
    rep = json.loads(s[i:j+1]) if (i >= 0 and j > i) else {"raw": text}
    rep["_adjudicator_model"] = model
    rep["_adjudicator_provider"] = provider
    rep["_rung"] = "A-crosslab"
    return rep

class CrossLabAdjudicator:
    rung = "A-crosslab"
    def __init__(self, model=None, provider=None, base_url=None, egress_policy="off", effort="high", timeout=120):
        self.provider = provider or DEFAULT_PROVIDER
        if self.provider not in PROVIDERS:
            raise RuntimeError(
                f"CROSSLAB-BLOCKED [provider-unknown] no adapter for provider '{self.provider}'. "
                f"Known: {', '.join(sorted(PROVIDERS))}. Set CROSSLAB_PROVIDER to one of these.")
        self._adapter = PROVIDERS[self.provider]
        self.key_env = self._adapter["key_env"]
        self.label   = self._adapter["label"]
        m = model if model is not None else DEFAULT_MODEL
        self.model = m or self._adapter["default_model"]
        if self.provider == "other":
            self.key_env = os.environ.get("CROSSLAB_OTHER_KEY_ENV") or "CROSSLAB_OTHER_API_KEY"
            self.label   = "cross-lab endpoint"
            if base_url is None: base_url = os.environ.get("CROSSLAB_BASE_URL")
        self.base_url, self.egress_policy, self.effort, self.timeout = base_url, egress_policy, effort, timeout
    def _key(self):
        ke = self.key_env; label = self.label
        k = os.environ.get(ke)
        if not k: raise RuntimeError(
            f"CROSSLAB-BLOCKED [no-key] {ke} is not set in this shell. Cross-lab needs your own "
            f"{label} API key, set by you in your own local terminal - PowerShell is easiest (its output copies cleanly back into chat): $env:{ke} = Read-Host 'Paste key'. Never paste the key into chat; a new window needs it "
            "set again. Options: set the key and re-run, or use an in-boundary rung (B Fable / C Opus panel "
            "/ D self-adversarial).")
        return k
    def _gate(self, privileged, override_privileged=False):
        if self.provider == "other":
            if not (self.base_url or "").startswith("https://"):
                raise EgressBlocked("CROSSLAB-BLOCKED [no-base-url] provider 'other' needs CROSSLAB_BASE_URL as an https:// API root (e.g. https://api.example.com/v1). Set it, or use a predefined provider / an in-boundary rung.")
            if not self.model:
                raise EgressBlocked("CROSSLAB-BLOCKED [no-model] provider 'other' has no default model - set CROSSLAB_MODEL to the model the endpoint serves.")
            if not os.environ.get("CROSSLAB_OTHER_LINEAGE"):
                raise EgressBlocked("CROSSLAB-BLOCKED [lineage-undeclared] provider 'other' needs CROSSLAB_OTHER_LINEAGE set to the lab behind the endpoint, so the same-lineage guard can confirm it is NOT the analyser's (Anthropic) lineage. Set it (e.g. 'openai', 'mistral', 'deepseek'), or use a predefined provider.")
        _lineage_guard(self._adapter["lineage"], self.model, self.base_url, os.environ.get("CROSSLAB_OTHER_LINEAGE"))
        if privileged and not override_privileged:
            raise EgressBlocked(
                "CROSSLAB-BLOCKED [privileged] privileged/confidential matter - cross-lab egress is blocked by "
                "default. Overriding is a deliberate typed act (--override-privileged); otherwise use an "
                "in-boundary rung (B/C/D).")
        if self.egress_policy=="off":
            raise EgressBlocked(
                "CROSSLAB-BLOCKED [egress-off] egress_policy=off - set 'redacted' or 'full' to use a cross-lab model")
    def _build_request(self, blind_pkg, adjudicate_prompt):
        a = self._adapter
        url  = a["endpoint"](self.model, self.base_url)
        body = a["body"](self.model, build_blind_text(blind_pkg, adjudicate_prompt), self.effort)
        return url, body
    def dispatch(self, blind_pkg, adjudicate_prompt, privileged=False, override_privileged=False):
        self._gate(privileged, override_privileged)
        a = self._adapter
        url, body = self._build_request(blind_pkg, adjudicate_prompt)
        req = urllib.request.Request(url, method="POST",
              headers=a["headers"](self._key()), data=json.dumps(body).encode())
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                raw = json.loads(r.read())
        except urllib.error.HTTPError as e:
            raise RuntimeError(a["classify"](e, self.model, url))
        except urllib.error.URLError as e:
            raise RuntimeError(f"CROSSLAB-FAILED [network] Could not reach {url}: {e}. Check connection / "
                f"proxy / firewall, then re-run - or use an in-boundary rung.")
        return _parse_report(a["extract_text"](raw), self.model, self.provider)

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
        return _parse_report(json.dumps(canned), "mock-" + self.model, "mock-" + self.provider)
