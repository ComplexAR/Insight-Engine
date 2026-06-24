---
name: track
description: Insight Engine investigation workspace — the living-analysis layer. Triggers when the user asks to start, continue, update, or check on an ongoing investigation that accumulates over days or weeks, re-verify an analysis as new facts or documents arrive, or maintain a living dossier across sessions. Runs an OPEN / UPDATE / STATUS elicitation contract over a persisted dossier, carrying the grade-locked spine and re-verifying on update.
---

# Insight Engine — track  (the living workspace layer)

Maintain a living investigation dossier for a long-running inquiry across sessions. Keep it THIN: one structured document the operator owns, not a state engine. The operator drives it through three modes — **OPEN**, **UPDATE**, **STATUS** — and each begins by *asking*, never by guessing. If it starts to grow heavy machinery, stop and re-scope.

## The dossier (one markdown file in the operator's folder, persisted across sessions)
One file per investigation, named `track-<slug>-<date>.md`, kept in the operator's folder so it survives sessions. Sections:
- **Question** — what conclusion is being kept live, in one line.
- **Spine** — every claim with its `[V]`/`[N]` grade and source tier (`[V1]`/`[V2]`/`[V3]`).
- **Dominant unknown** — the one fact that would most change the conclusion now.
- **Open (deep core)** — the framing / legitimacy / opportunity-cost / value questions, with the operator's recorded positions (carried from the `analyse` gate) or marked unresolved.
- **Pending (party-held)** — each item with the exact document or evidence that would settle it.
- **Watch-list (update triggers)** — the facts, documents, or events that would change the call; this is what an update is checked against.
- **The call** — the current decision-brief call + calibration, re-derived whenever the spine moves.
- **Sources.**
- **Update log** — dated entries.

## Mode 1 — OPEN (start a tracked investigation): ASK FIRST
Before creating the dossier, put these to the operator with AskUserQuestion (skippable; proceed on stated assumptions if declined):
1. **What are we tracking?** — the investigation question / the conclusion to keep live.
2. **Starting spine** — carry the grade-locked spine from an existing `analyse` run (point at the file or synthesis), or start fresh from a problem statement.
3. **Watch-list** — what new facts, documents, or events would change the call? These become the update triggers. Accept any party-held items the operator already holds.
4. **Cadence** — re-check on demand only, or on a schedule? If a schedule, offer to set a recurring re-verification of the web-verifiable claims (the `schedule` capability) and state plainly what it will check and when.
Then write the dossier file, seeded from the answers, and confirm its location.

## Mode 2 — UPDATE (a new fact, document, or event): ASK WHAT CHANGED
Begin by asking the operator **what has arrived** — a new document, a web development, a settled party-held item, an event — and accept uploads. Then:
1. Identify which claims the new information bears on.
2. Re-verify those claims (run the `verify` skill — router, source-tiering, and a disconfirmation pass on the load-bearing few): web-verifiable items against current sources; a newly-arrived party-held document against the pending list.
3. Update grades EXPLICITLY — never silently. Record before -> after in the log and state what evidence changed it.
4. Re-surface the dominant unknown (it may have moved) and clear any pending item the new evidence settles.
5. **Re-derive the call** — if the spine moved, recompute the decision brief (call · calibration · dominant unknown · what-to-verify-first · what-flips-it) and say whether the call flipped.
6. Append a dated log entry: what arrived, what changed, what is still open.

## Mode 3 — STATUS (where does it stand?): READ, don't re-verify
Report the current state from the dossier without new verification (unless asked): the question, the spine with grades, the current dominant unknown, what is still pending (party-held), the open deep-core with the operator's positions, the current call, and what changed since the last update. Offer to run an UPDATE if the operator has new material.

## Hard invariants
- **Grade-lock carries.** A finding's grade changes only on new evidence, recorded in the log — never by re-expression.
- **Every change is dated and explicit.** No silent edits to the spine; the log is the audit trail.
- **The dominant unknown is always current.** Re-point it on every update.
- **Stay THIN.** One operator-owned file; if it needs heavy machinery, re-scope.

## Status (state honestly)
The re-verification discipline here is sound, and `track` now has a real elicitation contract (OPEN / UPDATE / STATUS) — it no longer fails to ask the operator anything. It remains newer than `analyse`: its at-scale accumulation has not yet passed a controlled test, so rely on it as a disciplined living dossier and treat large accumulated re-gradings as worth a spot-check.
