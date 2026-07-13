---
name: adjudicate
description: Insight Engine independent-adjudication layer (Step 10) — an OPT-IN, off-by-default second pass on a finished high-stakes analysis. Triggers only when the operator asks for an independent check, adjudication, red-team, or second opinion on a completed Insight Engine analysis, or accepts the offer that `analyse` surfaces on a high-stakes or wicked problem. Runs a blind-then-adversarial adjudicator down an independence ladder — A a different-lab model (cross-lab, e.g. GPT-5.6 Sol / interim GPT-5.5), B a different in-house model (Fable 5), C a panel of blind Opus instances, D a self-adversarial reset — declares which rung it reached, folds discrepancies back under grade-lock without ever flipping the call itself, and logs the run to the real-use monitor. Every rung is opt-in and costs credits/setup; nothing runs automatically.
---

# Insight Engine - adjudicate (Step 10)

An independent second pass on a **finished** analysis. It re-derives the call blind, then tries to break it, and hands back discrepancies that fold in under grade-lock - **you always own the final call; the adjudicator never changes it.**

> **Honest claim - hold this line.** This is a *conditional, high-stakes-gated, off-by-default rigour-and-defensibility check*. Its **decision-flip** benefit - catching an error the disciplined first pass missed - is **unproven** (constructed-case testing was null; one real cross-lab run to date flipped nothing). What it does, safely and demonstrably, is **sharpen a sound analysis**: it flags where a load-bearing claim is asserted-but-not-established, without corrupting a correct call. Present it as that. It is **not** a safety net, and it is never run automatically. More decorrelation (a different lab) sharpens the *check*; it does not make the flip benefit proven, and no panel of any size ever flips the call.

## 0 - Nothing runs without an explicit opt-in

Every rung - cross-lab (A), Fable (B), Opus panel (C), self-adversarial (D) - is **opt-in** and has a cost/setup: A needs an OpenAI key + egress; B and C spend the operator's own Claude credits. Offer, then wait for a clear yes. Every escalation below (a 3rd Opus instance, a 2nd cross-lab lab, a targeted re-run) is likewise an **on-divergence offer**, never automatic.

## 1 - The necessity gate (offer only when warranted)

Before offering, run the gate and **declare the result either way** ("adjudication considered - not warranted because ..." / "warranted because ..."). Offer **only if all pass**:

- **G0 Layer** - a *completed* analysis exists (assembled brief + grade-locked spine). Never mid-pipeline.
- **G1 Stakes** - high-stakes or wicked (irreversible, binds people not in the room, legal exposure, contested blame, material money). Routine/reversible -> do not raise it.
- **G2 Confidentiality** - if the matter is privileged or confidential, cross-lab (A) is **blocked by default** (external egress). It is **operator-overridable** by a deliberate typed act when `block_override=allowed` (see 6), logged to the monitor and never written into the deliverable. In-boundary rungs (B/C/D) are unaffected. (This supersedes the old "never waivable" rule.)
- **G3 Residual judgment** - a live, decision-relevant, contestable judgment still remains. If the disciplined pass settled everything, adjudication is redundant.
- **G4 In-boundary sufficiency (A vs B/C)** - cross-lab's only marginal value over the cheaper in-house rungs is lineage decorrelation (Opus and Fable share Anthropic training). Reach for A only when the residual point is where shared blind spots bite.

**Consult the code-backed settings before offering** (do not rely on session memory):
- `python prefs/prefs.py should-offer --rung A` and `--rung B` (exit 0 = offer, 1 = suppressed). `offer=off` suppresses the whole offer; `crosslab=off` removes rung A only. Showing the offer is not running it.
- If `privilege_ask=on` (`should-ask privilege` -> exit 0), ask the operator once, pre-menu: "Is this matter privileged or confidential?" You flag and prompt; the **operator determines** (there is no reliable auto-detector). Their answer is the canonical privilege signal for the run.

## 2 - Settings (all switchable; standing + per-run)

Personal-use tool: **every setting is operator-switchable, standing and per-run; nothing is centrally locked.** Safe defaults; a change that removes a per-run ask, widens egress, re-opens a governance block, or raises cross-lab breadth is a deliberate, confirmed act.

- View/flip: `python prefs/prefs.py settings` | `get <key>` | `set <key> <value> [--confirm] [--note "..."]` | `reset [<key>|--all]`.
- The 13 keys: `offer`, `crosslab`, `default_rung`, `privilege_ask`, `egress_mode`, `show_outbound_package`, `block_override`, `rung_consent`, `crosslab_model`, `log_overrides`, `panel_size`, `crosslab_breadth`, `runs_per_model` (defaults + meaning in `prefs/README.md`).
- `set` returns exit 3 and writes nothing when a change needs `--confirm` (ask-removing / egress-widening / block-reopen / breadth-raise / log-disabling), printing the exact consequence line. Sizing raises (`panel_size`, `runs_per_model`) write with a cost note, no confirm.
- **Per-run vs standing:** a gate reading `ask` -> show the menu this run; a fixed value -> proceed with a one-line "using your saved setting: X - say 'change' to pick differently" notice. **Per-run choices never write the file**; only `set` (or an explicit "change my standing setting - confirm?") persists. Ambiguous -> ask "just this run, or standing?".

## 3 - Opt-out (always refusable, code-backed)

- **Per-run decline** - one word skips it; no reason; do not re-ask within the same analysis. Offer "skip this run only" vs "stop offering (standing - reversible)".
- **Standing** - `python prefs/prefs.py opt-out --scope <crosslab|all> [--note "..."]` (aliases onto `crosslab`/`offer`); restore with `re-enable`. Honoured mechanically by the gate.
- **No dark patterns** - a decline is never written into the deliverable as a caveat, footnote, or "reduced defensibility" note; do not nudge. Re-offering at a later, separate analysis is a fresh decision, itself governed by the standing setting.

## 4 - How the pass runs (any rung)

Run the adjudicator as a **subagent** - its own isolated context, handed **facts + grade-locked spine + draft brief, NOT the first model's reasoning** (so it cannot anchor). Two passes: **blind** (re-derive: does it reach the same call?) then **adversarial** (break the load-bearing claims and the call). **Fold under grade-lock:** a factual challenge -> re-verify (logged); a value challenge -> re-open one gate item for the human; an irreducible one -> caveat. **Never auto-flip.** Then **rank by decision-relevance and surface only the top ~3**. **Declare the rung reached**; same-lineage agreement is stability, not proof.

## 5 - The independence ladder (strongest first; each opt-in)

Tag each rung by **independence**, not an invented quality ranking. Render rung A's model from `crosslab_model` (never a hard-coded "Sol").

- **A - cross-lab** (strongest - different lab, most decorrelated lineage). Target = `crosslab_model` (e.g. OpenAI GPT-5.6 Sol / GPT-5.5, Google Gemini, xAI Grok 4.5). Needs setup + egress; blocked-by-default for privileged (G2, overridable). May be a **panel** of M labs (`crosslab_breadth`, default 1); on decision-relevant disagreement, **offer** a 2nd lab (max 3). Each added lab is a new counterparty -> its own consent recap + package preview. (Harness note: the bundled adapter speaks only the OpenAI endpoint; a non-OpenAI `crosslab_model` or an M>=2 second lab needs an adapter added to `harness/crosslab.py` first.)
- **B - Fable 5** (strong - different in-house model, nothing leaves the boundary). Spends Claude credits; plan-included now, moving to a credits basis - point the operator to their account page and assert no dates.
- **C - Opus panel** (same lineage - divergence is the signal, convergence is stability not proof). Dispatch `panel_size` instances (default 2); on decision-relevant divergence, **offer** a 3rd for the 2-vs-1 read.
- **D - self-adversarial** (weakest - same session, shared blind spots).

**Panel sizing.** Get the dispatch plan from `python prefs/prefs.py panel-plan --rung <A|C>`: rung C = `panel_size` instances (N is the depth axis; `runs_per_model` is NOT multiplied on top); rung A = `crosslab_breadth` models at `runs_per_model` each (`auto` = 2 runs for a lone lab, 1 each in a multi-lab panel; on divergence, offer one targeted re-run of only the divergent model). Present repeat runs as a **noise filter** (does this verdict reproduce?), never a truth amplifier.

## 6 - Cross-lab (rung A) setup, governance, and the tagged-error branch

The operator runs the paid call; **you never handle the key.** Walk it **one step at a time**, waiting after each.

1. **Privilege** (canonical, from 1). If privileged and `block_override=allowed`: rung A is blocked by default; say overriding is a deliberate typed act, and offer B/C/D. To override, the operator runs `python run_crosslab.py --live --privileged --override-privileged` themselves and states a one-line reason; if `log_overrides=on`, record it (below). If `block_override=disabled`, there is no override path until they switch it back (which itself needs `--confirm`).
2. **Consent recap** (if `rung_consent=on`; `should-ask consent`): privilege status, egress **content** per `egress_mode`, retention terms for this lab, spend.
3. **Egress** (`should-ask egress`): redacted (default, spine + contested claims) / full brief / ask-per-run. Raw source documents are never sent at any value.
4. **Outbound-package preview** (if `show_outbound_package=on`; `should-ask package`): show the EXACT package (grade-locked spine + contested claims + draft brief; never raw source docs) for **confirm / edit / cancel** before anything leaves. Repeat per counterparty when M>1.
5. **Setup + smoke:** `cd harness/`; the operator sets the key in their own shell (never in chat; Windows PowerShell `$env:OPENAI_API_KEY = Read-Host "Paste key"`); `python preflight.py` (expect READY), then `python preflight.py --live` (cheap smoke). To target a model, set the `CROSSLAB_MODEL` env var - the harness reads only this, so when a standing `crosslab_model` is saved, set `CROSSLAB_MODEL` to that value before the run.
6. **Run:** `python run_crosslab.py --live` on the finished analysis's blind package -> 7.

**Branch on the harness's stable tag** (the tag begins the message; match by *line contains*, never by provider wording). Never auto-retry a paid `--live`; never auto-descend a rung - each is a fresh yes.
- `CROSSLAB-BLOCKED [no-key]` -> guide key setup (platform.openai.com/api-keys; set in their own terminal), or drop to B/C/D.
- `CROSSLAB-BLOCKED [privileged]` -> governance block; offer the typed override (if `block_override=allowed`) or B/C/D.
- `CROSSLAB-BLOCKED [egress-off]` -> harness fail-safe; set `egress_mode` to redacted/full.
- `CROSSLAB-FAILED [auth 401]` -> re-set/regenerate the key, check billing; retry.
- `CROSSLAB-FAILED [model-unavailable 404]` -> set `CROSSLAB_MODEL` to another frontier model (e.g. gpt-5.5 - cross-lab independence still holds) this run only, or request access. A standing `set crosslab_model ...` (on explicit confirm) records the preference, but the harness reads `CROSSLAB_MODEL`, so set that env var for the actual run.
- `CROSSLAB-FAILED [quota 429]` -> check billing/limits, wait; retry.
- `CROSSLAB-FAILED [network]` -> check connection/proxy/firewall; retry.
- `CROSSLAB-FAILED [api NNN]` -> a 4xx about the body likely means the Responses-API schema moved; adjust the request dict in `harness/crosslab.py` and re-smoke.
- untagged/unexpected -> generic: show it verbatim; offer fix / B/C/D / skip.

**In-boundary rungs (B/C)** need only a light consent: "this spawns a Fable / Opus adjudicator subagent and spends your Claude credits - proceed?" If a B/C subagent dispatch fails, show the error verbatim (do not parse the wording) and offer retry / another rung / skip; a panel returning fewer than `panel_size` instances is a degraded panel - say so.

## 7 - After the run: rank, fold, log

- **Rank & surface** the top ~3 decision-relevant, observable-backed items; log the rest.
- **Fold under grade-lock** (4); never auto-flip.
- **Log to the monitor** (`monitor/`): `python monitor.py add --slug "<case>" --rung <A-crosslab|B-fable|C-panel|D-self> --verdict <real-catch-flipped|real-catch-refined|useful-not-decision-relevant|false-alarm|nothing> --items N --relevant M [--class "<problem-class>"] [--panel-n N] [--labs M] [--runs-per-model R] [--blind-divergence yes|no] [--agreed] [--flip --observable "<checkable fact>"] --notes "..."`. A **flip** counts only if the operator agrees, names a discriminating observable, and it would have changed a real decision. Tag `--class` to feed the per-class retirement read-out.
- **Log an override** (if a governance block was overridden and `log_overrides=on`): `python monitor.py override --slug "<case>" --kind <privileged|egress-off> --reason "<one line>"` - to the monitor only, never the deliverable.
- `python monitor.py report` for the accruing read-outs (blended, cross-lab AMENDMENT-1, and the per-class AMENDMENT-2 retirement recommendation).

## 8 - Boundaries (non-negotiable)

- **Never handle, echo, log, or request-in-chat the API key.** The operator sets it in their own environment; the adapter reads it from env and never logs it.
- **The paid call is operator-initiated** - hand over the command; do not run the spend yourself.
- **Privileged -> blocked by default, operator-overridable by a deliberate typed act, logged** (never silently, never in the deliverable). Redacted package by default; raw source docs never sent; zero-retention reminder.
- **Never auto-flip a call**; the human decides.
- **Always refusable** - no friction, no defensibility penalty for opting out.
- **Declare the rung and model actually used.** Keep the monitor `ledger.jsonl` and the `~/.insight-engine/` preferences out of version control. Every escalation is an on-divergence offer, never automatic.
