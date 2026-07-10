# Adjudication preferences — code-backed standing opt-out

This folder makes the L4.5 **standing opt-out** mechanical rather than something the
model has to remember. The operator's choice is persisted to a small JSON file and
read back on every future run, so "recorded and honoured on every future run" is
guaranteed by code.

## Where it lives

Default: `~/.insight-engine/preferences.json`
(Windows: `%USERPROFILE%\.insight-engine\preferences.json`.)

Override with the `INSIGHT_ENGINE_PREFS` environment variable (used by the self-tests).

It is deliberately **outside** the plugin directory so it survives plugin upgrades,
and it is **never** version-controlled (it is in the user's home, not the repo).

## Schema

Defined in `preferences.schema.json` (JSON Schema draft-07). Shape:

```json
{
  "schema_version": 1,
  "adjudication": {
    "standing_opt_out": { "scope": "none", "set_on": null, "note": null }
  }
}
```

`scope` values:

| scope | effect |
|---|---|
| `none` | offer normally (default) — adjudication is offered on every qualifying high-stakes/wicked run; still opt-in, nothing auto-runs |
| `crosslab` | suppress **only** the cross-lab rung A offer; still offer the in-boundary rungs (B Fable / C Opus panel) |
| `all` | suppress the **entire** adjudication offer until re-enabled |

`note` is optional operator free-text and is **never** surfaced in any deliverable.

## How the skill uses it (the exact commands)

`prefs.py` is stdlib-only. Run it from this folder.

Check whether to show an offer for a rung (this is the gate the skill consults —
exit code 0 = offer, 1 = suppressed):

```
python prefs.py should-offer --rung A     # cross-lab rung
python prefs.py should-offer --rung B     # in-boundary rung
```

Record a standing opt-out when the operator asks not to be offered again:

```
python prefs.py opt-out --scope crosslab            # stop offering cross-lab only
python prefs.py opt-out --scope all --note "reason"  # stop offering adjudication entirely
```

Restore offers (matching re-enable):

```
python prefs.py re-enable
```

Inspect the current state, and run the self-tests:

```
python prefs.py status
python prefs.py selftest
```

## Fail-safe

A missing or corrupt file defaults to `none` (offer) with a warning on stderr.
Showing an offer is low-cost and one-word-declinable; silently suppressing a choice
the operator might want removes their agency, so on any doubt the layer offers.
No rung ever runs without an explicit yes regardless of this file.
