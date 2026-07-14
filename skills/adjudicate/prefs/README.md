# Adjudication preferences — code-backed switchable settings (v3)

This folder makes the Step 10 adjudication settings **mechanical rather than model-remembered**.
The operator's choices are persisted to a small JSON file and read back on every future run.
v3 extends the switchable settings block to **17 keys** (v2 introduced the block; v3 adds the
multi-provider cross-lab keys) — every setting is operator-changeable, standing and per-run;
nothing is centrally locked (personal-use philosophy). The old opt-out survives as two of the
keys plus a derived mirror.

## Where it lives

Default: `~/.insight-engine/preferences.json`
(Windows: `%USERPROFILE%\.insight-engine\preferences.json`.)

Override with the `INSIGHT_ENGINE_PREFS` environment variable (used by the self-tests).
Deliberately **outside** the plugin directory so it survives upgrades, and **never**
version-controlled.

## The 17 settings

Defaults are the cautious behaviour. A change that **removes a per-run ask, widens egress,
re-opens a governance block, raises cross-lab breadth, switches the provider to `other`, or
sets a cross-lab base URL** requires a deliberate `--confirm`
(it prints the consequence and writes nothing otherwise). Spend-widening sizing changes
(`panel_size`, `runs_per_model`) write with a cost note but need no confirm.

| key | values | default | controls |
|---|---|---|---|
| `offer` | on/off | on | whether the Step 10 offer appears at all (off = old opt-out scope `all`) |
| `crosslab` | on/off | on | whether cross-lab rung A appears (off = old scope `crosslab`; B/C still offered) |
| `default_rung` | ask/A/B/C/D | ask | ask = show the rung menu; a fixed value skips it with a saved-setting notice |
| `privilege_ask` | on/off | on | every cross-lab run asks "privileged?" first; off = standing pre-consent |
| `egress_mode` | redacted/full/ask | redacted | outbound content; raw source documents are never sent at any value |
| `show_outbound_package` | on/off | on | show the exact package for confirm/edit/cancel before any send |
| `block_override` | allowed/disabled | allowed | whether a fired governance block can be overridden by the typed act; re-enabling needs `--confirm` |
| `rung_consent` | on/off | on | each rung's consent recap before dispatch |
| `crosslab_model` | string | auto | which model rung A targets (exported as `CROSSLAB_MODEL`); `auto` = the resolved provider's default model; verified on next preflight |
| `crosslab_provider` | auto/openai/google/xai/other | auto | which lab rung A targets; auto = infer from the model name; `other` needs `--confirm`, predefined switches write a retention note |
| `crosslab_base_url` | https URL or empty | (empty) | for provider `other`: the https API root (harness appends `/chat/completions`); setting it needs `--confirm` |
| `crosslab_other_key_env` | env-var name | CROSSLAB_OTHER_API_KEY | for `other`: the NAME of the env var holding the key (never the key value) |
| `crosslab_other_lineage` | string | (empty) | for `other`: the lab behind the endpoint, so the same-lineage guard can confirm it is not Anthropic; required before an `other` run |
| `log_overrides` | on/off | on | record governance-block overrides in the monitor; never in the deliverable |
| `panel_size` | int 2..5 | 2 | rung-C Opus instances (N); N is the depth axis (runs_per_model not multiplied on top) |
| `crosslab_breadth` | int 1..3 | 1 | distinct cross-lab models on rung A (M); each added lab is a new counterparty |
| `runs_per_model` | auto/1/2/3 | auto | repeat runs per model (R); auto = M==1 -> R=2, M>=2 -> R=1 each |

The **panel-sizing defaults are theory-grounded priors, to be revised on test evidence**
(see the monitor's per-class retirement rule and the panel-sizing recommendation).

## How the skill uses it (the exact commands)

`prefs.py` is stdlib-only. Run it from this folder. Gate commands follow a uniform contract:
**exit 0 = ask/offer (the safe interactive branch); exit 1 = a fixed value applies (printed)**.

```
python prefs.py settings                       # full switch table with consequence notes
python prefs.py status                         # one-line offer/cross-lab/default-rung state
python prefs.py get <key>
python prefs.py set <key> <value> [--confirm] [--note "..."]
python prefs.py reset [<key> | --all]

python prefs.py should-offer --rung A|B|C|D    # 0 offer / 1 suppressed
python prefs.py should-ask privilege|egress|package|consent   # 0 ask / 1 fixed(stdout)
python prefs.py default-rung                   # 0 ask / 1 fixed rung(stdout)
python prefs.py can-override                   # 0 allowed / 1 disabled
python prefs.py panel-plan [--rung A|C]        # N/M/R dispatch plan for a rung

python prefs.py opt-out --scope crosslab|all [--note "..."]   # alias -> offer/crosslab off
python prefs.py re-enable                       # alias -> offer=on, crosslab=on
python prefs.py selftest                        # offline self-tests (temp file)
```

## Backward compatibility

- A **v1 file** (only `adjudication.standing_opt_out.scope`) is migrated on load:
  `all` -> `offer=off`, `crosslab` -> `crosslab=off`, `none` -> defaults.
- A **v2 file is still readable by old v1 code**: a derived `standing_opt_out` mirror is
  recomputed on every save (offer=off -> scope all; else crosslab=off -> scope crosslab; else
  none), so an older plugin still honours the opt-out. The mirror is non-authoritative —
  `settings.offer`/`settings.crosslab` are the source of truth.
- A **v2 file** (13-key settings, no provider keys) migrates to v3 on load: every v2 value is
  preserved, the four new provider keys default, and an absent `crosslab_model` becomes `auto`
  (an explicit `gpt-5.6-sol` is kept verbatim). The `standing_opt_out` mirror is preserved.
- Rollback note: reverting to v1 code is safe-direction but **lossy on first v1 write** — an
  `opt-out`/`re-enable` under reverted code rebuilds the file from v1 defaults, discarding the
  v2 `settings`/`meta`. The opt-out state itself survives via the mirror.

## Enterprise-deferred seam

`meta` records per-key provenance. A future enterprise edition would add a `locked_by` field and
a read-only policy overlay over the centrally-lockable keys (`crosslab`, `egress_mode`,
`privilege_ask`, `show_outbound_package`, `block_override`, `log_overrides`, `crosslab_model`,
`crosslab_breadth`). Nothing central is built now.

## Fail-safe

A missing or corrupt file defaults to **offer** (all keys default) with a warning on stderr.
Showing an offer is low-cost and one-word-declinable; silently suppressing a choice removes the
operator's agency, so on any doubt the layer offers. No rung ever runs without an explicit yes.
