#!/usr/bin/env python3
"""Resolve adjudication prefs -> CROSSLAB_* env vars, BEFORE importing crosslab (keeps crosslab pure).

Shared by run_crosslab.py and preflight.py. Resolution order for every value: an explicit shell
environment variable always wins (per-run override); else the standing preference; else the
adapter's built-in default. Provider is inferred from the model name when it is 'auto'; an explicit
provider always wins. Best-effort: if prefs are unavailable, crosslab's built-in defaults apply.

Stdlib only. Does NOT import crosslab (it runs before crosslab is imported).
"""
import os, sys

# model-name prefix -> provider (kept in sync with crosslab.PROVIDERS model_prefixes)
_PREFIX = (("gpt-", "openai"), ("o1", "openai"), ("o3", "openai"), ("o4", "openai"),
           ("gemini-", "google"), ("grok-", "xai"))


def infer_provider(model):
    """Which predefined provider a model name looks like, or None."""
    m = (model or "").lower()
    for pref, prov in _PREFIX:
        if m.startswith(pref):
            return prov
    return None


def resolve():
    """Read prefs and export the CROSSLAB_* env vars (only where the shell has not set them)."""
    try:
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "prefs"))
        import prefs as _prefs
        s = _prefs.get_settings()
    except Exception:
        return  # prefs unavailable -> crosslab uses its built-in defaults

    def setenv(name, val):
        if val and not os.environ.get(name):
            os.environ[name] = val

    provider = os.environ.get("CROSSLAB_PROVIDER") or s.get("crosslab_provider") or "auto"
    model_pref = s.get("crosslab_model") or "auto"
    if provider == "auto":
        basis = os.environ.get("CROSSLAB_MODEL") or (model_pref if model_pref != "auto" else "")
        provider = infer_provider(basis) or "openai"   # nothing to infer from -> default openai
    setenv("CROSSLAB_PROVIDER", provider)

    # Export a concrete model only; 'auto'/empty -> the adapter's own default_model applies.
    # For provider 'other' there is NO adapter default: do NOT inherit a predefined-lab standing
    # model (it would be sent to the foreign endpoint). The operator supplies CROSSLAB_MODEL per
    # run for 'other', else [no-model] fires. So export the standing model only for a predefined lab.
    if model_pref and model_pref != "auto" and provider != "other":
        setenv("CROSSLAB_MODEL", model_pref)

    setenv("CROSSLAB_BASE_URL", s.get("crosslab_base_url"))
    setenv("CROSSLAB_OTHER_KEY_ENV", s.get("crosslab_other_key_env"))
    setenv("CROSSLAB_OTHER_LINEAGE", s.get("crosslab_other_lineage"))
    setenv("CROSSLAB_ADAPTER_FILES", s.get("crosslab_adapter_files"))
    setenv("CROSSLAB_OTHER_ADAPTER", s.get("crosslab_other_adapter"))
    try:
        _sha = _prefs.get_adapter_sha()
        if _sha:
            setenv("CROSSLAB_ADAPTER_SHA", _sha)
    except Exception:
        pass
