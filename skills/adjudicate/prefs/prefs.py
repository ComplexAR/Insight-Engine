#!/usr/bin/env python3
"""
User-level preferences for the Insight Engine adjudication layer (L4.5).

Makes the STANDING OPT-OUT code-backed instead of model-remembered: the skill
persists the operator's choice here and reads it back on every future run, so
"recorded and honoured on every future run" is mechanical, not discretionary.

Location (default): ~/.insight-engine/preferences.json
  - Overridable with the INSIGHT_ENGINE_PREFS environment variable (used by tests).
  - Deliberately OUTSIDE the plugin directory so it survives plugin upgrades and
    is never version-controlled. Schema: preferences.schema.json (this folder).

Scopes (adjudication.standing_opt_out.scope):
  none     offer normally (default)
  crosslab suppress ONLY the cross-lab rung A offer; still offer in-boundary B/C
  all      suppress the entire adjudication offer

Fail-safe: a missing or corrupt file defaults to scope "none" (offer, one-word
declinable) with a stderr warning. An offer is low-cost and refusable; silently
suppressing a choice the operator may want removes their agency, so on doubt we
offer. No rung ever runs without an explicit yes regardless.

Stdlib only. Pure ASCII.
"""
import json, os, sys, argparse, datetime, copy, tempfile

SCHEMA_VERSION = 1
SCOPES = ["none", "crosslab", "all"]

DEFAULT = {
    "schema_version": SCHEMA_VERSION,
    "adjudication": {
        "standing_opt_out": {"scope": "none", "set_on": None, "note": None}
    },
}


def prefs_path():
    env = os.environ.get("INSIGHT_ENGINE_PREFS")
    if env:
        return env
    return os.path.join(os.path.expanduser("~"), ".insight-engine", "preferences.json")


def _default():
    return copy.deepcopy(DEFAULT)


def _coerce(raw):
    """Return a valid prefs dict from possibly-partial/older data, filling defaults."""
    out = _default()
    if isinstance(raw, dict):
        adj = raw.get("adjudication")
        if isinstance(adj, dict):
            soo = adj.get("standing_opt_out")
            if isinstance(soo, dict):
                scope = soo.get("scope")
                if scope in SCOPES:
                    out["adjudication"]["standing_opt_out"]["scope"] = scope
                    out["adjudication"]["standing_opt_out"]["set_on"] = soo.get("set_on")
                    out["adjudication"]["standing_opt_out"]["note"] = soo.get("note")
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
    except Exception as e:  # fail-safe: corrupt file -> offer, but say so
        sys.stderr.write("insight-engine prefs: could not read %s (%s); defaulting to 'offer'.\n" % (path, e))
        return _default()


def save(prefs, path=None):
    path = path or prefs_path()
    d = os.path.dirname(path)
    if d and not os.path.isdir(d):
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(prefs, f, indent=2)
        f.write("\n")
    return path


def get_scope(path=None):
    return load(path)["adjudication"]["standing_opt_out"]["scope"]


def set_opt_out(scope, note=None, path=None):
    if scope not in ("crosslab", "all"):
        raise ValueError("opt-out scope must be 'crosslab' or 'all' (got %r)" % scope)
    prefs = load(path)
    prefs["adjudication"]["standing_opt_out"] = {
        "scope": scope,
        "set_on": datetime.date.today().isoformat(),
        "note": note,
    }
    save(prefs, path)
    return prefs


def re_enable(path=None):
    """Clear any standing opt-out; offers resume at every scope."""
    prefs = load(path)
    prefs["adjudication"]["standing_opt_out"] = {"scope": "none", "set_on": None, "note": None}
    save(prefs, path)
    return prefs


def _is_crosslab(rung):
    r = str(rung).strip().lower()
    return r.startswith("a") or "crosslab" in r or "cross-lab" in r


def should_offer(rung, path=None):
    """True if the offer for this rung should be shown. Robust: any error -> offer."""
    try:
        scope = get_scope(path)
    except Exception as e:
        sys.stderr.write("insight-engine prefs: %s; defaulting to 'offer'.\n" % e)
        return True
    if scope == "all":
        return False
    if scope == "crosslab":
        return not _is_crosslab(rung)
    return True  # none


# ------------------------------- CLI -------------------------------

def _print_status(path=None):
    p = path or prefs_path()
    soo = load(path)["adjudication"]["standing_opt_out"]
    exists = os.path.exists(p)
    print("Insight Engine preferences")
    print("  file:   %s%s" % (p, "" if exists else "  (not yet created; defaults in effect)"))
    print("  adjudication standing opt-out:")
    print("    scope:  %s" % soo["scope"])
    print("    set_on: %s" % soo["set_on"])
    print("    note:   %s" % soo["note"])
    if soo["scope"] == "none":
        print("  => adjudication is OFFERED on every qualifying high-stakes/wicked run (still opt-in; nothing auto-runs).")
    elif soo["scope"] == "crosslab":
        print("  => cross-lab rung A is NOT offered; in-boundary rungs (Fable / Opus panel) still offered.")
    else:
        print("  => the whole adjudication offer is SUPPRESSED until re-enabled.")


def _selftest():
    tf = tempfile.mkdtemp()
    p = os.path.join(tf, "preferences.json")
    ok = True

    def check(cond, msg):
        nonlocal ok
        status = "ok  " if cond else "FAIL"
        if not cond:
            ok = False
        print("  [%s] %s" % (status, msg))

    # default (no file)
    check(get_scope(p) == "none", "missing file -> scope none")
    check(should_offer("A", p) and should_offer("B", p), "none -> offer all rungs")

    # crosslab opt-out
    set_opt_out("crosslab", note="testing", path=p)
    check(get_scope(p) == "crosslab", "set crosslab -> scope crosslab")
    check(not should_offer("A", p), "crosslab -> rung A suppressed")
    check(not should_offer("A-crosslab", p), "crosslab -> 'A-crosslab' suppressed")
    check(should_offer("B", p) and should_offer("C", p), "crosslab -> B/C still offered")

    # all opt-out
    set_opt_out("all", path=p)
    check(get_scope(p) == "all", "set all -> scope all")
    check(not should_offer("A", p) and not should_offer("B", p), "all -> every rung suppressed")

    # re-enable
    re_enable(p)
    check(get_scope(p) == "none", "re-enable -> scope none")
    check(should_offer("A", p) and should_offer("B", p), "re-enable -> offers resume")

    # invalid scope rejected
    try:
        set_opt_out("none", path=p)
        check(False, "set_opt_out('none') should raise")
    except ValueError:
        check(True, "set_opt_out('none') rejected (use re-enable)")

    # corrupt file fails safe to offer
    with open(p, "w", encoding="utf-8") as f:
        f.write("{ this is not json")
    check(get_scope(p) == "none", "corrupt file -> scope none (fail-safe)")
    check(should_offer("A", p), "corrupt file -> still offers")

    print("SELFTEST", "OK" if ok else "FAILED")
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Insight Engine user preferences (adjudication opt-out).")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="show the current opt-out state")

    oo = sub.add_parser("opt-out", help="set a standing opt-out")
    oo.add_argument("--scope", required=True, choices=["crosslab", "all"])
    oo.add_argument("--note", default=None)

    sub.add_parser("re-enable", help="clear any standing opt-out; offers resume")

    so = sub.add_parser("should-offer", help="exit 0 if the rung should be offered, 1 if suppressed")
    so.add_argument("--rung", required=True, help="A/A-crosslab, or B/C/D")

    sub.add_parser("selftest", help="run offline self-tests (uses a temp file)")

    a = ap.parse_args(argv)

    if a.cmd == "status":
        _print_status()
    elif a.cmd == "opt-out":
        set_opt_out(a.scope, note=a.note)
        print("standing opt-out set:")
        _print_status()
    elif a.cmd == "re-enable":
        re_enable()
        print("standing opt-out cleared:")
        _print_status()
    elif a.cmd == "should-offer":
        offer = should_offer(a.rung)
        print("offer" if offer else "suppressed")
        return 0 if offer else 1
    elif a.cmd == "selftest":
        return _selftest()
    return 0


if __name__ == "__main__":
    sys.exit(main())
