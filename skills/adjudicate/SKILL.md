---
name: adjudicate
description: Insight Engine independent-adjudication layer (Step 10) — an OPT-IN, off-by-default second pass on a finished high-stakes analysis. Triggers only when the operator asks for an independent check, adjudication, red-team, or second opinion on a completed Insight Engine analysis, or accepts the offer that `analyse` surfaces on a high-stakes or wicked problem. Runs a blind-then-adversarial adjudicator down an independence ladder — A a different-lab model (cross-lab, e.g. GPT-5.6 Sol / interim GPT-5.5), B a different in-house model (Fable 5), C a panel of blind Opus instances, D a self-adversarial reset — declares which rung it reached, folds discrepancies back under grade-lock without ever flipping the call itself, and logs the run to the real-use monitor. Every rung is opt-in and costs credits/setup; nothing runs automatically.
---

# Insight Engine - adjudicate (Step 10)

An independent second pass on a **finished** analysis. It re-derives the call blind, then tries to break it, and hands back discrepancies that fold in under grade-lock - **you always own the final call; the adjudicator never changes it.**

> **Honest claim - state it exactly as follows.** This is a *conditional, high-stakes-gated, off-by-default rigour-and-defensibility check*. Its **decision-flip** benefit - catching an error the disciplined first pass missed - is **unproven** (constructed-case testing was null; one real cross-lab run to date flipped nothing). What it does, safely and demonstrably, is **sharpen a sound analysis**: it flags where a load-bearing claim is asserted-but-not-established, without corrupting a correct call. Present it as that. Do not present it as reliably catching errors the first pass missed; it is never run automatically. More decorrelation (a different lab) sharpens the *check*; it does not make the flip benefit proven, and no panel of any size ever flips the call.

## 0 - Nothing runs without an explicit opt-in

Every rung - cross-lab (A), Fable (B), Opus panel (C), self-adversarial (D) - is **opt-in** and has a cost/setup: A needs the chosen lab's API key + egress; B and C spend the operator's own Claude credits. Offer, then wait for a clear yes. Every escalation below (a 3rd Opus instance, a 2nd cross-lab lab, a targeted re-run) is likewise an **on-divergence offer**, never automatic.

## 1 - The necessity gate (offer only when warranted)

Before offering, run the gate and **declare the result either way** ("adjudication considered - not warranted because ..." / "warranted because ..."). Offer **only if all pass**:

- **G0 Layer** - a *completed* analysis exists (assembled brief + grade-locked spine). Never mid-pipeline.
- **G1 Stakes** - high-stakes or wicked (irreversible, binds people not in the room, legal exposure, contested blame, material money). Routine/reversible -> do not raise it.
- **G2 Confidentiality** - if the matter is privileged or confidential, cross-lab (A) is **blocked by default** (external egress). It is **operator-overridable** by a deliberate typed act when `block_override=allowed` (see 6), logged to the monitor and never written into the deliverable. In-boundary rungs (B/C/D) are unaffected. (This supersedes the old "never waivable" rule.)
- **G3 Residual judgment** - a live, decision-relevant, contestable judgment still remains. If the disciplined pass settled everything, adjudication is redundant.
- **G4 In-boundary sufficiency (A vs B/C)** - cross-lab's only marginal value over the cheaper in-house rungs is lineage decorrelation (Opus and Fable share Anthropic training). Use A only when the residual point is where shared blind spots are most likely to matter.

**Consult the code-backed settings before offering** (do not rely on session memory):
- `python prefs/prefs.py should-offer --rung A` and `--rung B` (exit 0 = offer, 1 = suppressed). `offer=off` suppresses the whole offer; `crosslab=off` removes rung A only. Showing the offer is not running it.
- If `privilege_ask=on` (`should-ask privilege` -> exit 0), ask the operator once, pre-menu: "Is this matter privileged or confidential?" You flag and prompt; the **operator determines** (there is no reliable auto-detector). Their answer is the canonical privilege signal for the run.

## 2 - Settings (all switchable; standing + per-run)

Personal-use tool: **every setting is operator-switchable, standing and per-run; nothing is centrally locked.** Safe defaults; a change that removes a per-run ask, widens egress, re-opens a governance block, or raises cross-lab breadth is a deliberate, confirmed act.

- View/flip: `python prefs/prefs.py settings` | `get <key>` | `set <key> <value> [--confirm] [--note "..."]` | `reset [<key>|--all]`.
- The 19 keys: `offer`, `crosslab`, `default_rung`, `privilege_ask`, `egress_mode`, `show_outbound_package`, `block_override`, `rung_consent`, `crosslab_model`, `crosslab_provider`, `crosslab_base_url`, `crosslab_other_key_env`, `crosslab_other_lineage`, `crosslab_adapter_files`, `crosslab_other_adapter`, `log_overrides`, `panel_size`, `crosslab_breadth`, `runs_per_model` (defaults + meaning in `prefs/README.md`).
- `set` returns exit 3 and writes nothing when a change needs `--confirm` (ask-removing / egress-widening / block-reopen / breadth-raise / log-disabling / provider-to-`other` / base-url / adapter-files-on / adapter-approve), printing the exact consequence line. Sizing raises (`panel_size`, `runs_per_model`) write with a cost note, no confirm.
- **Per-run vs standing:** a gate reading `ask` -> show the menu this run; a fixed value -> proceed with a one-line "using your saved setting: X - say 'change' to pick differently" notice. **Per-run choices never write the file**; only `set` (or an explicit "change my standing setting - confirm?") persists. Ambiguous -> ask "just this run, or standing?".

## 3 - Opt-out (always refusable, code-backed)

- **Per-run decline** - one word skips it; no reason; do not re-ask within the same analysis. Offer "skip this run only" vs "stop offering (standing - reversible)".
- **Standing** - `python prefs/prefs.py opt-out --scope <crosslab|all> [--note "..."]` (aliases onto `crosslab`/`offer`); restore with `re-enable`. Honoured mechanically by the gate.
- **No dark patterns** - a decline is never written into the deliverable as a caveat, footnote, or "reduced defensibility" note; do not nudge. Re-offering at a later, separate analysis is a fresh decision, itself governed by the standing setting.

## 4 - How the pass runs (any rung)

Run the adjudicator as a **subagent** - its own isolated context - in **two dispatches, not one**. Pass 1 is **blind by construction**: it is handed **facts + grade-locked spine ONLY**, with the call, the first model's reasoning and the operator's gate positions withheld, so it cannot anchor on what it was never sent. Only when pass 1 has returned is the draft brief revealed, in a second dispatch, for the **adversarial** pass (break the load-bearing claims and the call). Asking one call to ignore the brief until pass 2 makes blindness a matter of the model's compliance; withholding it makes blindness a property of the package. **Fold under grade-lock:** a factual challenge -> re-verify (logged); a value challenge -> re-open one deep-core item at the Step-8 judgement gate; an irreducible one -> caveat. **Never auto-flip.** Then **rank by decision-relevance and surface only the top ~3**. **Declare the rung reached**; same-lineage agreement is stability, not proof.

## 5 - The independence ladder (strongest first; each opt-in)

Tag each rung by **independence**, not an invented quality ranking. Render rung A's model from `crosslab_model` (never a hard-coded "Sol").

- **A - cross-lab** (strongest - different lab, most decorrelated lineage). Choose the lab with `crosslab_provider`: **openai** (default `gpt-5.6-sol`; on a 404, retarget to `gpt-5.5`), **google** (`gemini-3.5-flash`), **xai** (`grok-4.5`), or **other** (any OpenAI-compatible endpoint via `crosslab_base_url`, or a pluggable adapter file). `auto` infers the lab from `crosslab_model`. Each lab uses its own key env (`OPENAI_API_KEY` / `GEMINI_API_KEY` / `XAI_API_KEY` / the one `crosslab_other_key_env` names). Needs setup + egress; blocked-by-default for privileged (G2, overridable). May be a **panel** of M labs (`crosslab_breadth`, default 1); on decision-relevant disagreement, **offer** a 2nd lab (max 3). Each added lab is a new counterparty -> its own consent recap + package preview. **Honesty:** OpenAI is live-verified; the Google/xAI adapters are built to each lab's current published API and are live-verified only once you run the smoke with that lab's key. A Claude/Anthropic-lineage target on rung A is refused (`[same-lineage]`) - use B/C for a same-lineage check.
- **B - Fable 5** (strong - different in-house model, nothing leaves the boundary). Spends Claude credits; point the operator to their own account page for what it costs and **assert no dates** - do not state billing arrangements or pricing changes you cannot know.
- **C - Opus panel** (same lineage - divergence is the signal, convergence is stability not proof). Dispatch `panel_size` instances (default 2); on decision-relevant divergence, **offer** a 3rd for the 2-vs-1 read.
- **D - self-adversarial** (weakest - same session, shared blind spots).

**Panel sizing.** Get the dispatch plan from `python prefs/prefs.py panel-plan --rung <A|C>`: rung C = `panel_size` instances (N is the depth axis; `runs_per_model` is NOT multiplied on top); rung A = `crosslab_breadth` models at `runs_per_model` each (`auto` = 2 runs for a lone lab, 1 each in a multi-lab panel; on divergence, offer one targeted re-run of only the divergent model). Present repeat runs as a **noise filter** (does this verdict reproduce?), never as evidence that the verdict is more likely correct.

**"Other" labs and adapters.** For a lab with no built-in adapter: set `crosslab_provider other` + `crosslab_base_url` (its https API root) + `crosslab_other_lineage` + a key in the env var `crosslab_other_key_env` names - the harness uses the OpenAI-compatible `chat/completions` shape. For a non-compatible API, an operator-written adapter file (`~/.insight-engine/adapters/<name>.py`) can be enabled with `set crosslab_adapter_files on --confirm` and approved with `set crosslab_other_adapter <name> --confirm`. An adapter runs the operator's own code in the egress path (opt-in and default-off, hash-pinned, shape- and lineage-checked, with every gate enforced around it), so only enable one they wrote or have read in full - the engine validates its shape and hash, not its behaviour.

## 6 - Cross-lab (rung A) setup, governance, and the tagged-error branch

The operator runs the paid call; **you never handle the key.** Walk it **one step at a time**, waiting after each.

1. **Privilege** (canonical, from 1). If privileged and `block_override=allowed`: rung A is blocked by default; say overriding is a deliberate typed act, and offer B/C/D. To override, the operator runs `python run_crosslab.py --live --privileged --override-privileged` themselves and states a one-line reason; if `log_overrides=on`, record it (below). If `block_override=disabled`, there is no override path until they switch it back (which itself needs `--confirm`).
2. **Consent recap** (if `rung_consent=on`; `should-ask consent`): privilege status, egress **content** per `egress_mode`, retention terms for this lab, spend.
3. **Egress** (`should-ask egress`): redacted (default, spine + contested claims) / full brief / ask-per-run. Raw source documents are never sent at any value.
4. **Outbound-package preview** (if `show_outbound_package=on`; `should-ask package`): show the EXACT package for **confirm / edit / cancel** before anything leaves - **both packages**, since there are two: pass 1 carries the grade-locked spine and contested claims and NOT the call; pass 2 carries the pass-1 verdict and the draft brief. Raw source docs are never sent in either. Repeat per counterparty when M>1.
5. **Setup + smoke:** this all runs in the operator's OWN local terminal, never in chat - tell them to use **PowerShell** (its output copies cleanly back here; Command Prompt's `set VAR=` key syntax also differs). `cd harness/`. Pick the lab if not OpenAI: `python ../prefs/prefs.py set crosslab_provider <openai|google|xai|other>` (or the `CROSSLAB_PROVIDER` env for one run). Set THAT lab's key in their own shell (never in chat; PowerShell e.g. `$env:GEMINI_API_KEY = Read-Host 'Paste key'`) - the key env is OpenAI `OPENAI_API_KEY` / Google `GEMINI_API_KEY` / xAI `XAI_API_KEY` / the name `crosslab_other_key_env` gives. `python preflight.py` shows the resolved provider/model and whether that key is set (expect READY); `python preflight.py --live` runs the cheap smoke against that lab. Model: the provider's default is used unless you set `crosslab_model` (standing) or `CROSSLAB_MODEL` (this run; env wins). For provider `other` the standing `crosslab_model` is intentionally NOT inherited (so a predefined-lab model can't be sent to a foreign endpoint) - set `CROSSLAB_MODEL` per run, or rely on the adapter's own `default_model`.
6. **Run:** `python run_crosslab.py --live` on the finished analysis. This makes **two paid calls** - the blind pass, then the adversarial pass - which is the cost of blinding by construction. `--blind-only` runs pass 1 and stops. -> 7.

**Branch on the harness's stable tag** (the tag begins the message; match by *line contains*, never by provider wording). Never auto-retry a paid `--live`; never auto-descend a rung - each is a fresh yes.
- `CROSSLAB-BLOCKED [no-key]` -> guide key setup in their own local PowerShell terminal (the resolved lab's key console, e.g. platform.openai.com/api-keys for OpenAI; never in chat), or drop to B/C/D.
- `CROSSLAB-BLOCKED [provider-unknown]` -> `CROSSLAB_PROVIDER` is not a known lab; set it to openai/google/xai/other.
- `CROSSLAB-BLOCKED [privileged]` -> governance block; offer the typed override (if `block_override=allowed`) or B/C/D.
- `CROSSLAB-BLOCKED [egress-off]` -> harness fail-safe; set `egress_mode` to redacted/full.
- `CROSSLAB-BLOCKED [same-lineage]` -> the target is a Claude/Anthropic-lineage model; rung A must be a different lab. Use B (Fable) / C (Opus panel), or set a genuinely different lab.
- `CROSSLAB-BLOCKED [provider-model-mismatch]` -> `crosslab_provider` and `crosslab_model` disagree; set the model to match the provider, or the provider to match the model.
- `CROSSLAB-BLOCKED [no-base-url] / [no-model] / [lineage-undeclared]` -> provider `other` needs `crosslab_base_url` (https), `crosslab_other_lineage`, and a **per-run `CROSSLAB_MODEL`** set first (for `other` the standing `crosslab_model` is intentionally not inherited; the adapter's own `default_model` also satisfies `[no-model]`).
- `CROSSLAB-BLOCKED [adapter-off]` -> pluggable adapter files are disabled; enable deliberately with `set crosslab_adapter_files on --confirm` (it runs your own code), or use a predefined lab / the `other` base_url.
- `CROSSLAB-BLOCKED [adapter-path | adapter-missing | adapter-shape | adapter-changed]` -> the named adapter file is outside the adapters dir, absent, malformed, or changed since approval; fix it or re-approve with `set crosslab_other_adapter <name> --confirm`.
- `CROSSLAB-FAILED [auth 401/403/400]` -> the lab rejected the key (Google may use 400/403 for a bad `GEMINI_API_KEY`); re-set/regenerate the key, check billing; retry.
- `CROSSLAB-FAILED [model-unavailable 404]` -> set `CROSSLAB_MODEL` to another frontier model (e.g. gpt-5.5 - cross-lab independence still holds) this run only, or request access. Retarget with a standing `set crosslab_model ...` (on explicit confirm; the harness reads it as a fallback) or with `CROSSLAB_MODEL` for just this run (env wins).
- `CROSSLAB-FAILED [quota 429]` -> check billing/limits, wait; retry.
- `CROSSLAB-FAILED [network]` -> check connection/proxy/firewall; retry.
- `CROSSLAB-FAILED [api NNN]` -> a 4xx about the body likely means that provider's API schema moved; adjust that provider's adapter in `harness/crosslab.py` and re-smoke.
- untagged/unexpected -> generic: show it verbatim; offer fix / B/C/D / skip.

**In-boundary rungs (B/C)** need only a brief consent: "this spawns a Fable / Opus adjudicator subagent and spends your Claude credits - proceed?" If a B/C subagent dispatch fails, show the error verbatim (do not parse the wording) and offer retry / another rung / skip; a panel returning fewer than `panel_size` instances is a degraded panel - say so.

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
