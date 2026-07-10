---
name: adjudicate
description: Insight Engine independent-adjudication layer (L4.5) — an OPT-IN, off-by-default second pass on a finished high-stakes analysis. Triggers only when the operator asks for an independent check, adjudication, red-team, or second opinion on a completed Insight Engine analysis, or accepts the offer that `analyse` surfaces on a high-stakes or wicked problem. Runs a blind-then-adversarial adjudicator down an independence ladder — A a different-lab model (cross-lab, e.g. GPT-5.6 Sol / interim GPT-5.5), B a different in-house model (Fable 5), C a panel of blind Opus instances, D a self-adversarial reset — declares which rung it reached, folds discrepancies back under grade-lock without ever flipping the call itself, and logs the run to the real-use monitor. Every rung is opt-in and costs credits/setup; nothing runs automatically.
---

# Insight Engine — adjudicate (L4.5)

An independent second pass on a **finished** analysis. It re-derives the call blind, then tries to break it, and hands back discrepancies that fold in under grade-lock — **you always own the final call; the adjudicator never changes it.**

> **Honest claim — hold this line.** This is a *conditional, high-stakes-gated, off-by-default rigour-and-defensibility check*. Its **decision-flip** benefit — catching an error the disciplined first pass missed — is **unproven** (constructed-case testing was null; one real cross-lab run to date flipped nothing). What it does, safely and demonstrably, is **sharpen a sound analysis**: it flags where a load-bearing claim is asserted-but-not-established, without corrupting a correct call. Present it as that. It is **not** a safety net, and it is never run automatically.

## 0 — Nothing runs without an explicit opt-in

Every rung — cross-lab (A), Fable (B), Opus panel (C), self-adversarial (D) — is **opt-in** and has a cost/setup: A needs an OpenAI key + egress; B and C spend the operator's own Claude credits and need Fable/model access. So there is no silent default. Offer, then wait for a clear yes.

## 1 — The necessity gate (offer only when warranted)

Before offering anything, run the gate and **declare the result either way** ("adjudication considered — not warranted because …" / "warranted because …"). Offer **only if all pass**:

- **G0 Layer** — a *completed* analysis exists (assembled brief + grade-locked spine). Never mid-pipeline.
- **G1 Stakes** — the proportionality triage rated this **high-stakes or wicked** (irreversible, binds people not in the room, legal exposure, contested blame, material money). Routine/reversible → do not raise it.
- **G2 Confidentiality (HARD, overrides all)** — if the matter is privileged or confidential, **cross-lab (A) is never offered** (external egress is forbidden for privileged material). In-boundary rungs may still be offered. This gate cannot be waived.
- **G3 Residual judgment** — a live, decision-relevant, *contestable* judgment still remains (contested attribution, which loop dominates, a value/framing call, a weakly-graded load-bearing claim). If the disciplined pass already settled everything, adjudication is redundant.
- **G4 In-boundary sufficiency (for choosing A vs B/C)** — cross-lab's only marginal value over the cheaper in-house rungs is **lineage decorrelation** (Opus and Fable share Anthropic training → partially correlated blind spots). Reach for A only when the residual point is where shared blind spots bite, or when an in-boundary pass converged without resolving it.

**Offer default:** when the gate passes, offer the check on a first-time high-stakes user **and on every subsequent high-stakes/wicked run** — *unless* a standing opt-out is set (see §2). Showing the offer is not running it; the layer stays off-by-default.

## 2 — Opt-out (always refusable)

- **Per-run decline** — one word skips it; no reason needed, and **do not re-ask within the same analysis**.
- **Scope** — the operator may decline cross-lab (A) only (keeping B/C available to opt into), or the whole adjudication layer.
- **Standing opt-out** — "don't offer this again" is recorded in the user-level Insight Engine preferences file and honoured on every future run (never offered again, at the chosen scope); a matching **re-enable** restores it.
- **No dark patterns** — a decline is respected and is **not** written into the deliverable as a caveat, footnote, or "reduced defensibility" note; do not escalate or nudge. Re-offering at a *later, separate* high-stakes analysis is a fresh decision, not nagging, and is itself governed by the standing opt-out.

## 3 — How the pass runs (any rung)

Run the adjudicator as a **subagent** — its own isolated context, handed the **facts + the grade-locked spine + the draft brief, NOT the first model's reasoning** (so it cannot anchor). Two passes:
1. **Blind** — re-derive: does it reach the same call?
2. **Adversarial** — try to break the load-bearing claims and the call.

It returns a discrepancy report. **Fold under grade-lock:** a factual challenge → re-verify (logged); a value challenge → re-open one gate item for the human; an irreducible one → caveat. **Never auto-flip the call.** Then **rank the discrepancies by decision-relevance and surface only the top ~3** — the report is verbose, and most items are not decision-relevant. **Declare the rung reached** (below); same-model agreement is stability, not proof.

## 4 — The independence ladder (strongest first; each opt-in)

- **A · cross-lab** — a different-*lab* frontier model (target **GPT-5.6 Sol**; interim **GPT-5.5** while Sol is preview-gated). Strongest independence (decorrelated lineage). **Needs setup + egress** — run §5. **Off for privileged/confidential (G2).**
- **B · Fable 5** — a different in-house model: model + context independence, no external egress. Spends Claude credits; needs Fable access.
- **C · Opus panel** — 2+ blind Opus instances; read the **divergence** (convergence = stability, not proof; divergence localises the fragile point). A same-model cross-check, not independent adjudication. Spends Claude credits.
- **D · self-adversarial** — a reset in the same session (weakest; shared context and blind spots).

Whichever rung runs, **say so** in the output.

## 5 — Cross-lab (rung A) setup walkthrough — operator runs it, you guide

The bundled harness is under `harness/` (see `harness/PREFLIGHT.md` and `harness/CROSSLAB.md`). **You never handle the key**; the operator sets it in their own terminal and runs the paid call. First detect state (OS/shell, Python present, key set) and branch:

**Fast path (already configured):** confirm not-privileged + redacted egress → `cd` to `harness/` → ensure the key is set for this shell → `python preflight.py --live` (cheap smoke) → build the blind package → `python run_crosslab.py --live` → §6.

**First-time path (one step at a time, wait after each):**
1. Governance: confirm not privileged (hard stop if it is); redacted egress; remind them to arrange zero-retention terms with the provider.
2. Python check (`python --version`); if missing, guide install (python.org, tick *Add to PATH*; if the Store stub appears, turn off the `python.exe` App-execution alias).
3. `cd` to the bundled `harness/` folder (full path; a fresh window loses cwd).
4. Set the key **without exposing it**: `$env:OPENAI_API_KEY = Read-Host "Paste key"` (PowerShell) / `read -s OPENAI_API_KEY; export OPENAI_API_KEY` (bash). Never paste it into the chat; single `sk-` prefix; each new window re-sets.
5. `python preflight.py` → expect `READY for --live`.
6. `python preflight.py --live` → expect `{"ok": true, ...}`.

**Branch table (from real runs):** `python not found` → install / Store-alias-off · PowerShell `VAR=value command` rejected → two lines / `Read-Host` · fresh window (no cwd/key) → re-`cd` + re-set key · HTTP 401 → regenerate key / check billing · HTTP 404 `gpt-5.6-sol` gated → `CROSSLAB_MODEL=gpt-5.5` · other HTTP 4xx on the body → patch the request dict in `harness/crosslab.py` to current OpenAI Responses-API docs, re-smoke.

**In-boundary rungs (B/C)** need only a lighter consent: "this spawns a Fable / Opus adjudicator subagent and spends your Claude credits — proceed?"

## 6 — After the run: rank, fold, log

- **Rank & surface** the top ~3 decision-relevant, observable-backed items; log the rest.
- **Fold under grade-lock** (§3); never auto-flip.
- **Log to the monitor** from `harness/../monitor` (or `harness/monitor` if bundled together): `python monitor.py add --slug "<case>" --rung <A-crosslab|B-fable|C-panel|D-self> --verdict <real-catch-flipped|real-catch-refined|useful-not-decision-relevant|false-alarm|nothing> --items N --relevant M [--agreed] [--flip --observable "<checkable fact>"] --notes "..."`. A **flip** counts only if the operator agrees, it names a discriminating observable, and it would have changed a real decision. Then `python monitor.py report` for the accruing read-out (cross-lab-specific at rung A).

## 7 — Boundaries (non-negotiable)

- **Never handle, echo, log, or request-in-chat the API key.** The operator sets it in their own environment; the adapter reads it from `env` and never logs it.
- **The paid call is operator-initiated** — hand over the command; do not run the spend yourself.
- **`privileged → never`** cross-lab egress; off by default; redacted package; zero-retention reminder.
- **Never auto-flip a call**; the human decides.
- **Always refusable** (§2) — no friction, no defensibility penalty for opting out.
- Record the model actually used; keep the monitor `ledger.jsonl` out of version control.
