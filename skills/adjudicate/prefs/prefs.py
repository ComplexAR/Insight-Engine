#!/usr/bin/env python3
"""
User-level preferences for the Insight Engine adjudication layer (Step 10).

Schema v3: a 17-key switchable settings block (adjudication.settings) plus a
DERIVED standing_opt_out mirror so older plugins still honour an opt-out. v3 adds
the multi-provider cross-lab keys (crosslab_provider / crosslab_base_url /
crosslab_other_key_env / crosslab_other_lineage) and defaults crosslab_model to
'auto' (= the resolved provider's own default model).
Everything is operator-switchable, standing and per-run; nothing is centrally
locked (personal-use philosophy). Defaults are the cautious behaviour; a change
that removes a per-run ask or widens egress is a deliberate, confirmed act.

Location (default): ~/.insight-engine/preferences.json
  - Overridable with INSIGHT_ENGINE_PREFS (used by tests).
  - Deliberately OUTSIDE the plugin dir so it survives upgrades and is never
    version-controlled. Schema (documentation, not runtime-enforced):
    preferences.schema.json (this folder). Migration lives in _coerce().

Backward compatibility:
  - A v1 file (only standing_opt_out.{scope}) is migrated on load:
      scope all      -> offer=off      (whole offer suppressed)
      scope crosslab -> crosslab=off   (rung A suppressed; B/C still offered)
      scope none     -> defaults
  - A v2 file is still readable by old v1 code: the derived standing_opt_out
    mirror sits at exactly adjudication.standing_opt_out with a valid scope.
  - opt-out / re-enable / should-offer are kept as aliases onto offer/crosslab.

Fail-safe: a missing or corrupt file defaults to OFFER (all keys default) with a
stderr note. On doubt we offer; no rung ever runs without an explicit yes.

Stdlib only. Pure ASCII.
"""
import json, os, re, sys, argparse, datetime, tempfile

SCHEMA_VERSION = 3
SCOPES = ["none", "crosslab", "all"]  # legacy opt-out scopes (mirror + aliases)
ONOFF = ["on", "off"]

# ---- the 17 switchable settings: type, allowed values / range, default ----
KEYS = {
    "offer":                 {"type": "enum", "values": ONOFF,                       "default": "on"},
    "crosslab":              {"type": "enum", "values": ONOFF,                       "default": "on"},
    "default_rung":          {"type": "enum", "values": ["ask", "A", "B", "C", "D"], "default": "ask"},
    "privilege_ask":         {"type": "enum", "values": ONOFF,                       "default": "on"},
    "egress_mode":           {"type": "enum", "values": ["redacted", "full", "ask"], "default": "redacted"},
    "show_outbound_package": {"type": "enum", "values": ONOFF,                       "default": "on"},
    "block_override":        {"type": "enum", "values": ["allowed", "disabled"],     "default": "allowed"},
    "rung_consent":          {"type": "enum", "values": ONOFF,                       "default": "on"},
    "crosslab_model":        {"type": "str",                                         "default": "auto"},
    "crosslab_provider":     {"type": "enum", "values": ["auto", "openai", "google", "xai", "other"], "default": "auto"},
    "crosslab_base_url":     {"type": "url",                                         "default": ""},
    "crosslab_other_key_env":{"type": "envname",                                     "default": "CROSSLAB_OTHER_API_KEY"},
    "crosslab_other_lineage":{"type": "str0",                                        "default": ""},
    "log_overrides":         {"type": "enum", "values": ONOFF,                       "default": "on"},
    "panel_size":            {"type": "int",  "min": 2, "max": 5,                    "default": 2},
    "crosslab_breadth":      {"type": "int",  "min": 1, "max": 3,                    "default": 1},
    "runs_per_model":        {"type": "enum", "values": ["auto", "1", "2", "3"],     "default": "auto"},
}
KEY_ORDER = list(KEYS.keys())
META_FIELDS = ("set_on", "confirmed", "consequence", "note")


def _default():
    return {
        "schema_version": SCHEMA_VERSION,
        "adjudication": {
            "settings": {k: KEYS[k]["default"] for k in KEY_ORDER},
            "meta": {},
            "standing_opt_out": {"scope": "none", "set_on": None, "note": None},
        },
    }


def prefs_path():
    env = os.environ.get("INSIGHT_ENGINE_PREFS")
    if env:
        return env
    return os.path.join(os.path.expanduser("~"), ".insight-engine", "preferences.json")


def parse_value(key, raw):
    """Return (value, warn_or_None). Raise ValueError on genuinely invalid input.
    Out-of-range ints are CLAMPED (with a warn), not rejected."""
    spec = KEYS[key]
    t = spec["type"]
    if t == "enum":
        s = str(raw)
        if s in spec["values"]:
            return s, None
        raise ValueError("value for %s must be one of %s (got %r)" % (key, "/".join(spec["values"]), raw))
    if t == "int":
        try:
            n = int(raw)
        except (ValueError, TypeError):
            raise ValueError("value for %s must be an integer in %d..%d (got %r)" % (key, spec["min"], spec["max"], raw))
        warn = None
        if n < spec["min"]:
            warn = "clamped %d up to %d" % (n, spec["min"]); n = spec["min"]
        elif n > spec["max"]:
            warn = "clamped %d down to %d" % (n, spec["max"]); n = spec["max"]
        return n, warn
    if t == "url":
        s = str(raw).strip()
        if s == "":
            return "", None
        if not s.startswith("https://"):
            raise ValueError("value for %s must be an https:// URL or empty (got %r)" % (key, raw))
        return s, None
    if t == "envname":
        s = str(raw).strip()
        if not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", s):
            raise ValueError("value for %s must be a valid environment-variable name (got %r)" % (key, raw))
        return s, None
    if t == "str0":
        return (str(raw) if raw is not None else ""), None
    if isinstance(raw, str) and raw.strip():
        return raw, None
    raise ValueError("value for %s must be a non-empty string" % key)


def _derive_mirror(settings, prev=None):
    """Derive the legacy standing_opt_out scope from offer/crosslab (offer dominates).
    Preserve the prior set_on/note when the derived scope is unchanged (avoids date
    churn and keeps the true opt-out date that old v1 code displays)."""
    if settings.get("offer") == "off":
        scope = "all"
    elif settings.get("crosslab") == "off":
        scope = "crosslab"
    else:
        scope = "none"
    if scope == "none":
        return {"scope": "none", "set_on": None, "note": None}
    if isinstance(prev, dict) and prev.get("scope") == scope and prev.get("set_on"):
        return {"scope": scope, "set_on": prev.get("set_on"), "note": prev.get("note")}
    return {"scope": scope, "set_on": datetime.date.today().isoformat(), "note": None}


def _coerce(raw):
    """Return a valid v3 prefs dict from possibly-partial/older/corrupt data."""
    out = _default()
    if not isinstance(raw, dict):
        return out
    adj = raw.get("adjudication")
    if not isinstance(adj, dict):
        return out
    settings = adj.get("settings")
    if isinstance(settings, dict):
        for k in KEY_ORDER:
            if k in settings:
                try:
                    v, _ = parse_value(k, settings[k])
                    out["adjudication"]["settings"][k] = v
                except ValueError as e:
                    sys.stderr.write("insight-engine prefs: %s; using default.\n" % e)
        meta = adj.get("meta")
        if isinstance(meta, dict):
            for k in KEY_ORDER:
                m = meta.get(k)
                if isinstance(m, dict):
                    out["adjudication"]["meta"][k] = {f: m.get(f) for f in META_FIELDS}
    else:
        soo = adj.get("standing_opt_out")
        if isinstance(soo, dict) and soo.get("scope") in SCOPES:
            scope = soo["scope"]
            if scope == "all":
                out["adjudication"]["settings"]["offer"] = "off"
            elif scope == "crosslab":
                out["adjudication"]["settings"]["crosslab"] = "off"
    out["adjudication"]["standing_opt_out"] = _derive_mirror(out["adjudication"]["settings"], adj.get("standing_opt_out"))
    return out


def load(path=None):
    path = path or prefs_path()
    if not os.path.exists(path):
        return _default()
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read().strip()
        if not text:
            return _default()
        return _coerce(json.loads(text))
    except Exception as e:
        sys.stderr.write("insight-engine prefs: could not read %s (%s); defaulting to 'offer'.\n" % (path, e))
        return _default()


def save(prefs, path=None):
    path = path or prefs_path()
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d or ".", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(prefs, f, indent=2)
            f.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise
    return path


def get_settings(path=None):
    return load(path)["adjudication"]["settings"]


def get_value(key, path=None):
    if key not in KEYS:
        raise KeyError(key)
    return get_settings(path)[key]


def transition(key, old, new):
    """Is a change consequential? -> {needs_confirm, consequence}.
    Ask-removing / egress-widening / block-reopening changes need --confirm.
    Spend-widening (sizing) changes get a cost line but no confirm; crosslab_breadth
    is the exception (a raise adds a new counterparty) and IS confirmed."""
    c, needs = None, False
    if key == "privilege_ask" and new == "off":
        needs = True; c = "Standing pre-consent: cross-lab runs treated as NOT privileged unless flagged in-run; the privilege question will not be asked."
    elif key == "egress_mode" and new == "full":
        needs = True; c = "Cross-lab packages may carry the full brief and claim text, not the redacted spine. Raw source documents are still never sent."
    elif key == "show_outbound_package" and new == "off":
        needs = True; c = "The exact outbound package will no longer be shown before sending."
    elif key == "rung_consent" and new == "off":
        needs = True; c = "Each rung's consent recap will no longer be shown before dispatch."
    elif key == "default_rung" and new != "ask":
        needs = True; c = "The rung menu will be skipped; rung %s runs by default with a one-line saved-setting notice." % new
    elif key == "log_overrides" and new == "off":
        needs = True; c = "Future governance overrides will leave no record anywhere."
    elif key == "block_override" and old == "disabled" and new == "allowed":
        needs = True; c = "Governance blocks become overridable again."
    elif key == "crosslab_breadth" and isinstance(new, int) and isinstance(old, int) and new > old:
        needs = True; c = "Each added lab is a new organisation that will hold your redacted package under its own retention terms."
    elif key == "panel_size" and isinstance(new, int) and new > 3:
        c = "Above 3 Opus instances is mostly cost, not signal - same-lineage runs are correlated."
    elif key == "runs_per_model" and str(new) in ("2", "3"):
        c = "Each extra run is a full paid call. Repeat runs de-noise a single verdict; they do not add new coverage."
    elif key == "crosslab_provider" and new == "other":
        needs = True; c = "Provider 'other' sends your redacted package to an operator-supplied endpoint (CROSSLAB_BASE_URL). It runs only after you also set its key env + CROSSLAB_OTHER_LINEAGE and confirm the destination per run."
    elif key == "crosslab_provider" and new in ("openai", "google", "xai") and old != new:
        c = "Rung A will now target %s - a different organisation that holds your redacted package under its own retention terms." % new
    elif key == "crosslab_base_url" and new:
        needs = True; c = "This is the cross-lab egress destination for provider 'other'. Confirm you trust this endpoint with your redacted package."
    return {"needs_confirm": needs, "consequence": c}


def set_value(key, raw, confirm=False, note=None, path=None):
    """Return {status: ok|invalid|confirm-required, ...}. CLI maps status to exit code."""
    if key not in KEYS:
        return {"status": "invalid", "msg": "unknown key %r (see 'settings')" % key}
    try:
        value, warn = parse_value(key, raw)
    except ValueError as e:
        return {"status": "invalid", "msg": str(e)}
    prefs = load(path)
    old = prefs["adjudication"]["settings"][key]
    tr = transition(key, old, value)
    if tr["needs_confirm"] and not confirm:
        return {"status": "confirm-required", "consequence": tr["consequence"], "warn": warn}
    prefs["adjudication"]["settings"][key] = value
    prefs["adjudication"]["meta"][key] = {
        "set_on": datetime.date.today().isoformat(),
        "confirmed": bool(confirm) if tr["needs_confirm"] else None,
        "consequence": tr["consequence"],
        "note": note,
    }
    prefs["adjudication"]["standing_opt_out"] = _derive_mirror(prefs["adjudication"]["settings"], prefs["adjudication"].get("standing_opt_out"))
    save(prefs, path)
    return {"status": "ok", "value": value, "warn": warn, "consequence": tr["consequence"]}


def reset_key(key, path=None):
    if key not in KEYS:
        raise KeyError(key)
    prefs = load(path)
    prefs["adjudication"]["settings"][key] = KEYS[key]["default"]
    prefs["adjudication"]["meta"].pop(key, None)
    prefs["adjudication"]["standing_opt_out"] = _derive_mirror(prefs["adjudication"]["settings"], prefs["adjudication"].get("standing_opt_out"))
    save(prefs, path)
    return prefs


def reset_all(path=None):
    return save(_default(), path)


def set_opt_out(scope, note=None, path=None):
    if scope not in ("crosslab", "all"):
        raise ValueError("opt-out scope must be 'crosslab' or 'all' (got %r)" % scope)
    key = "offer" if scope == "all" else "crosslab"
    return set_value(key, "off", confirm=True, note=note, path=path)


def re_enable(path=None):
    """Clear any standing opt-out; offers resume (offer=on, crosslab=on)."""
    prefs = load(path)
    prefs["adjudication"]["settings"]["offer"] = "on"
    prefs["adjudication"]["settings"]["crosslab"] = "on"
    prefs["adjudication"]["meta"].pop("offer", None)
    prefs["adjudication"]["meta"].pop("crosslab", None)
    prefs["adjudication"]["standing_opt_out"] = _derive_mirror(prefs["adjudication"]["settings"], prefs["adjudication"].get("standing_opt_out"))
    save(prefs, path)
    return prefs


def _is_crosslab(rung):
    r = str(rung).strip().lower()
    return r.startswith("a") or "crosslab" in r or "cross-lab" in r


# ---- gates (uniform exit contract): exit 0 = ask/offer; exit 1 = fixed value applies ----

def should_offer(rung, path=None):
    try:
        s = get_settings(path)
    except Exception as e:
        sys.stderr.write("insight-engine prefs: %s; defaulting to 'offer'.\n" % e)
        return True
    if s["offer"] == "off":
        return False
    if s["crosslab"] == "off" and _is_crosslab(rung):
        return False
    return True


def gate_default_rung(path=None):
    v = get_settings(path)["default_rung"]
    return (True, None) if v == "ask" else (False, v)


def gate_should_ask(what, path=None):
    s = get_settings(path)
    if what == "privilege":
        return (True, None) if s["privilege_ask"] == "on" else (False, "pre-consented")
    if what == "egress":
        return (True, None) if s["egress_mode"] == "ask" else (False, s["egress_mode"])
    if what == "package":
        return (True, None) if s["show_outbound_package"] == "on" else (False, "skip")
    if what == "consent":
        return (True, None) if s["rung_consent"] == "on" else (False, "skip")
    raise ValueError("should-ask takes one of: privilege, egress, package, consent")


def gate_can_override(path=None):
    return get_settings(path)["block_override"] == "allowed"


def panel_plan(rung, path=None):
    s = get_settings(path)
    r = str(rung).upper()
    if r.startswith("C"):
        n = s["panel_size"]
        return {"rung": "C", "instances": n, "runs_per_model_applied": 1, "total_calls": n,
                "on_divergence": "offer one more Opus instance for the 2-vs-1 read (cap 5); never auto-run",
                "note": "N is the depth axis; runs_per_model is NOT multiplied on top"}
    m = s["crosslab_breadth"]
    rpm = s["runs_per_model"]
    r_eff = (2 if m == 1 else 1) if rpm == "auto" else int(rpm)
    div = ("two runs disagreeing => the flag is likely sampling noise; say so" if m == 1
           else "offer one targeted re-run of only the divergent model")
    esc = ("offer escalation to M=%d on decision-relevant disagreement (max 3)" % (m + 1)) if m < 3 else "at max labs (3)"
    return {"rung": "A", "models": m, "runs_per_model": r_eff, "total_calls": m * r_eff,
            "on_divergence": div, "escalation": esc}


def _print_settings(path=None):
    prefs = load(path)
    s = prefs["adjudication"]["settings"]
    meta = prefs["adjudication"]["meta"]
    p = path or prefs_path()
    print("Insight Engine - adjudication settings")
    print("  file: %s%s" % (p, "" if os.path.exists(p) else "  (not yet created; defaults in effect)"))
    for k in KEY_ORDER:
        star = " *" if s[k] != KEYS[k]["default"] else "  "
        print("  %s %-22s = %-12s (default %s)" % (star, k, s[k], KEYS[k]["default"]))
        c = (meta.get(k) or {}).get("consequence")
        if c:
            print("      note: %s" % c)
    print("  derived opt-out scope (for older plugins): %s" % prefs["adjudication"]["standing_opt_out"]["scope"])


def _print_status(path=None):
    s = get_settings(path)
    print("adjudication offer: %s | cross-lab rung A: %s | default rung: %s"
          % (s["offer"], s["crosslab"], s["default_rung"]))
    if s["offer"] == "off":
        print("  => the whole adjudication offer is SUPPRESSED until re-enabled.")
    elif s["crosslab"] == "off":
        print("  => cross-lab rung A is NOT offered; in-boundary rungs (Fable / Opus panel) still offered.")
    else:
        print("  => adjudication is OFFERED on qualifying high-stakes/wicked runs (still opt-in; nothing auto-runs).")


def _selftest():
    tf = tempfile.mkdtemp()
    p = os.path.join(tf, "preferences.json")
    v1 = os.path.join(tf, "v1.json")
    ok = True

    def check(cond, msg):
        nonlocal ok
        if not cond:
            ok = False
        print("  [%s] %s" % ("ok  " if cond else "FAIL", msg))

    s = get_settings(p)
    check(all(s[k] == KEYS[k]["default"] for k in KEY_ORDER), "missing file -> all 17 defaults")
    check(should_offer("A", p) and should_offer("B", p), "defaults -> offer all rungs")

    for scope, exp in (("all", ("off", "on")), ("crosslab", ("on", "off")), ("none", ("on", "on"))):
        with open(v1, "w", encoding="utf-8") as f:
            json.dump({"schema_version": 1, "adjudication": {"standing_opt_out": {"scope": scope}}}, f)
        sv = get_settings(v1)
        check((sv["offer"], sv["crosslab"]) == exp, "v1 scope %s -> offer/crosslab %s" % (scope, exp))
        check(sv["default_rung"] == "ask" and sv["panel_size"] == 2, "v1 %s -> other keys default" % scope)

    reset_all(p)
    set_value("crosslab", "off", path=p)
    raw = json.load(open(p, encoding="utf-8"))
    check(raw["adjudication"]["standing_opt_out"]["scope"] == "crosslab", "v2 save -> mirror scope crosslab (old code reads this)")
    set_value("offer", "off", path=p)
    raw = json.load(open(p, encoding="utf-8"))
    check(raw["adjudication"]["standing_opt_out"]["scope"] == "all", "offer=off -> mirror scope all (offer dominates)")

    reset_all(p)
    set_opt_out("crosslab", path=p)
    check(get_value("crosslab", p) == "off" and get_value("offer", p) == "on", "opt-out crosslab -> crosslab off, offer on")
    set_opt_out("all", path=p)
    check(get_value("offer", p) == "off", "opt-out all -> offer off")
    re_enable(p)
    check(get_value("offer", p) == "on" and get_value("crosslab", p) == "on", "re-enable -> both on")
    check(should_offer("A", p) and should_offer("B", p), "re-enable -> offers resume")

    reset_all(p)
    r = set_value("privilege_ask", "off", path=p)
    check(r["status"] == "confirm-required" and get_value("privilege_ask", p) == "on", "privilege_ask off without --confirm -> blocked, unchanged")
    r = set_value("privilege_ask", "off", confirm=True, path=p)
    check(r["status"] == "ok" and get_value("privilege_ask", p) == "off", "privilege_ask off with --confirm -> applied")
    r = set_value("egress_mode", "full", path=p)
    check(r["status"] == "confirm-required", "egress_mode full needs --confirm")
    r = set_value("runs_per_model", "2", path=p)
    check(r["status"] == "ok" and r["consequence"], "runs_per_model 2 -> writes with a cost line, no confirm")
    r = set_value("panel_size", "5", path=p)
    check(r["status"] == "ok" and get_value("panel_size", p) == 5 and r["consequence"], "panel_size 5 -> writes with cost line")
    r = set_value("crosslab_breadth", "2", path=p)
    check(r["status"] == "confirm-required", "crosslab_breadth raise needs --confirm (new counterparty)")
    r = set_value("nope", "x", path=p)
    check(r["status"] == "invalid", "unknown key -> invalid")
    r = set_value("egress_mode", "sideways", path=p)
    check(r["status"] == "invalid", "bad enum value -> invalid")
    v, w = parse_value("panel_size", "9")
    check(v == 5 and w, "panel_size 9 -> clamped to 5 with warn")

    # v3 multi-provider keys + confirm rules + migration
    reset_all(p)
    check(get_value("crosslab_provider", p) == "auto" and get_value("crosslab_model", p) == "auto"
          and get_value("crosslab_base_url", p) == "" and get_value("crosslab_other_key_env", p) == "CROSSLAB_OTHER_API_KEY"
          and get_value("crosslab_other_lineage", p) == "", "v3 -> new provider keys default")
    r = set_value("crosslab_provider", "google", path=p)
    check(r["status"] == "ok" and r["consequence"], "provider google -> ok with retention consequence, no confirm")
    r = set_value("crosslab_provider", "other", path=p)
    check(r["status"] == "confirm-required", "provider other -> needs --confirm")
    r = set_value("crosslab_base_url", "https://api.example.com/v1", path=p)
    check(r["status"] == "confirm-required", "crosslab_base_url -> needs --confirm (egress destination)")
    r = set_value("crosslab_base_url", "http://x", confirm=True, path=p)
    check(r["status"] == "invalid", "non-https base_url -> invalid")
    r = set_value("crosslab_other_key_env", "MY KEY", path=p)
    check(r["status"] == "invalid", "bad env-var name -> invalid")
    r = set_value("crosslab_other_key_env", "MY_KEY", path=p)
    check(r["status"] == "ok", "valid env-var name -> ok, no confirm")
    r = set_value("crosslab_other_lineage", "mistral", path=p)
    check(r["status"] == "ok", "crosslab_other_lineage -> ok, no confirm")
    v2 = os.path.join(tf, "v2.json")
    v2keys = ("offer", "crosslab", "default_rung", "privilege_ask", "egress_mode", "show_outbound_package",
              "block_override", "rung_consent", "log_overrides", "panel_size", "crosslab_breadth", "runs_per_model")
    v2set = {k: KEYS[k]["default"] for k in v2keys}
    v2set["crosslab"] = "off"; v2set["crosslab_model"] = "gpt-5.6-sol"
    v2doc = {"schema_version": 2, "adjudication": {"settings": v2set, "meta": {},
             "standing_opt_out": {"scope": "crosslab", "set_on": "2026-01-01", "note": None}}}
    with open(v2, "w", encoding="utf-8") as f:
        json.dump(v2doc, f)
    sv = get_settings(v2)
    check(sv["crosslab"] == "off" and sv["crosslab_model"] == "gpt-5.6-sol" and sv["crosslab_provider"] == "auto",
          "v2->v3: values preserved (incl. explicit crosslab_model), new keys default")
    mg = _coerce(v2doc)
    check(mg["schema_version"] == 3 and mg["adjudication"]["standing_opt_out"]["scope"] == "crosslab"
          and mg["adjudication"]["standing_opt_out"]["set_on"] == "2026-01-01",
          "v2->v3: schema bumped to 3, standing_opt_out mirror preserved")
    v2set2 = {k: KEYS[k]["default"] for k in v2keys}  # a v2 file with NO crosslab_model
    mg2 = _coerce({"schema_version": 2, "adjudication": {"settings": v2set2, "meta": {}, "standing_opt_out": {"scope": "none"}}})
    check(mg2["adjudication"]["settings"]["crosslab_model"] == "auto", "v2->v3: absent crosslab_model -> auto")

    reset_all(p)
    check(gate_default_rung(p) == (True, None), "default_rung ask -> interactive")
    set_value("default_rung", "B", confirm=True, path=p)
    check(gate_default_rung(p) == (False, "B"), "default_rung B -> fixed B")
    check(gate_should_ask("privilege", p)[0] is True, "privilege_ask on -> ask")
    set_value("show_outbound_package", "off", confirm=True, path=p)
    check(gate_should_ask("package", p)[0] is False, "package off -> skip")
    check(gate_can_override(p) is True, "block_override allowed -> can-override")
    set_value("block_override", "disabled", path=p)
    check(gate_can_override(p) is False, "block_override disabled -> cannot override")

    reset_all(p)
    pc = panel_plan("C", p)
    check(pc["instances"] == 2 and pc["total_calls"] == 2, "panel-plan C defaults -> 2 calls (no R mult)")
    pa = panel_plan("A", p)
    check(pa["models"] == 1 and pa["runs_per_model"] == 2 and pa["total_calls"] == 2, "panel-plan A defaults -> M1 R2")
    set_value("crosslab_breadth", "2", confirm=True, path=p)
    pa2 = panel_plan("A", p)
    check(pa2["models"] == 2 and pa2["runs_per_model"] == 1 and pa2["total_calls"] == 2, "panel-plan A M2 -> R1 each")

    with open(p, "w", encoding="utf-8") as f:
        f.write("{ this is not json")
    check(get_value("offer", p) == "on", "corrupt file -> defaults (fail-safe offer)")
    check(should_offer("A", p), "corrupt file -> still offers")

    print("SELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Insight Engine adjudication preferences (v3 switchable settings).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="one-line offer/cross-lab/default-rung state")
    sub.add_parser("settings", help="full switch table with defaults and consequence notes")

    st = sub.add_parser("set", help="set a setting (ask-removing/egress-widening/breadth-raise need --confirm)")
    st.add_argument("key"); st.add_argument("value")
    st.add_argument("--confirm", action="store_true"); st.add_argument("--note", default=None)

    g = sub.add_parser("get", help="print one setting's value")
    g.add_argument("key")

    rs = sub.add_parser("reset", help="restore default(s)")
    rs.add_argument("key", nargs="?", default=None); rs.add_argument("--all", action="store_true")

    so = sub.add_parser("should-offer", help="exit 0 offer / 1 suppressed")
    so.add_argument("--rung", required=True, help="A/A-crosslab, or B/C/D")

    sa = sub.add_parser("should-ask", help="exit 0 ask / 1 fixed(stdout)")
    sa.add_argument("what", choices=["privilege", "egress", "package", "consent"])

    sub.add_parser("default-rung", help="exit 0 ask / 1 fixed rung(stdout)")
    sub.add_parser("can-override", help="exit 0 allowed / 1 disabled")

    pp = sub.add_parser("panel-plan", help="print the N/M/R dispatch plan for a rung")
    pp.add_argument("--rung", default=None, choices=["A", "C", "a", "c"], help="A or C (default: both)")

    oo = sub.add_parser("opt-out", help="alias: set a standing opt-out")
    oo.add_argument("--scope", required=True, choices=["crosslab", "all"]); oo.add_argument("--note", default=None)
    sub.add_parser("re-enable", help="alias: clear any standing opt-out")

    sub.add_parser("selftest", help="offline self-tests (temp file)")

    a = ap.parse_args(argv)

    if a.cmd == "status":
        _print_status()
    elif a.cmd == "settings":
        _print_settings()
    elif a.cmd == "set":
        r = set_value(a.key, a.value, confirm=a.confirm, note=a.note)
        if r.get("warn"):
            sys.stderr.write("insight-engine prefs: %s\n" % r["warn"])
        if r["status"] == "invalid":
            print(r["msg"]); return 2
        if r["status"] == "confirm-required":
            print("change not applied - it removes an ask or widens exposure:")
            print("  %s" % r["consequence"])
            print("re-run with --confirm to apply.")
            return 3
        print("set %s = %s" % (a.key, r["value"]))
        if r.get("consequence"):
            print("  note: %s" % r["consequence"])
    elif a.cmd == "get":
        if a.key not in KEYS:
            print("unknown key %r" % a.key); return 2
        print(get_value(a.key))
    elif a.cmd == "reset":
        if a.all or a.key is None:
            reset_all(); print("all settings reset to defaults.")
        elif a.key not in KEYS:
            print("unknown key %r" % a.key); return 2
        else:
            reset_key(a.key); print("%s reset to default (%s)." % (a.key, KEYS[a.key]["default"]))
    elif a.cmd == "should-offer":
        offer = should_offer(a.rung)
        print("offer" if offer else "suppressed")
        return 0 if offer else 1
    elif a.cmd == "should-ask":
        ask, val = gate_should_ask(a.what)
        if ask:
            print("ask"); return 0
        print(val); return 1
    elif a.cmd == "default-rung":
        ask, val = gate_default_rung()
        if ask:
            print("ask"); return 0
        print(val); return 1
    elif a.cmd == "can-override":
        allowed = gate_can_override()
        print("allowed" if allowed else "disabled")
        return 0 if allowed else 1
    elif a.cmd == "panel-plan":
        rungs = [a.rung.upper()] if a.rung else ["A", "C"]
        for rg in rungs:
            print(json.dumps(panel_plan(rg), indent=2))
    elif a.cmd == "opt-out":
        set_opt_out(a.scope, note=a.note); print("standing opt-out set:"); _print_status()
    elif a.cmd == "re-enable":
        re_enable(); print("standing opt-out cleared:"); _print_status()
    elif a.cmd == "selftest":
        return _selftest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
