---
name: track
description: Insight Engine investigation workspace — the living-analysis layer. Triggers when the user asks to start, continue, update, or check on an ongoing investigation that accumulates over days or weeks, re-verify an analysis as new facts or documents arrive, or maintain a living dossier across sessions. Runs an OPEN / UPDATE / STATUS elicitation contract over a persisted dossier, carrying the grade-locked spine and re-verifying on update.
---

# Insight Engine — track  (the living workspace layer)

Maintain a living investigation dossier for a long-running inquiry across sessions. Keep it THIN: one structured document the operator owns, not a state engine. The operator drives it through three modes — **OPEN**, **UPDATE**, **STATUS** — and each begins by *asking*, never by guessing. If it starts to need complex mechanisms, stop and re-scope.

## The dossier (one markdown file in the operator's folder, persisted across sessions)
One file per investigation, named `track-<slug>-<date>.md`, kept in the operator's folder so it survives sessions. Sections:
- **Question** — what conclusion is being kept live, in one line.
- **Spine** — every claim with its `[V]`/`[N]` grade and source tier (`[V1]`/`[V2]`/`[V3]`), plus two currency fields: `last-verified: <date>` and a volatility class — **FIXED** (a settled historical fact), **SLOW** (changes on the scale of years), or **VOLATILE** (current status that can change week to week) — set at OPEN and itself revisable with a dated log line (it is metadata, not a grade — do not grade-lock it by accident); and, where a claim underpins another claim or the call, a one-line `supports: [the call | claim X]` tag, so that a later grade change makes its dependents explicit. Each `[N]` claim also carries a `situation:` field recording which of the five `[N]` situations it is in — a claim a real search left uncorroborated, or found contradicted; a claim resting only on an interested or self-reporting party; a claim awaiting a named document that would settle it; a claim inheriting the cap from an unverified thing it depends on; or a judgement or prediction this method never grades higher (which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips) — UPDATE behaviour depends on it: it determines which `[N]`s can move at all, and what would move them.
- **Dominant unknown** — the one fact that would most change the conclusion now.
- **Open (deep core)** — the framing / legitimacy / opportunity-cost / value questions, with the operator's recorded positions (carried from the `analyse` gate) or marked unresolved.
- **Pending (party-held)** — each item with the exact document or evidence that would settle it.
- **Watch-list (update triggers)** — the facts, documents, or events that would change the call; this is what an update is checked against.
- **The call** — the current decision-brief call + confidence basis, re-derived whenever any grade in the spine changes.
- **Sources.**
- **Update log** — dated entries. Each records either a grade change (before -> after, with the evidence that moved it) or a **checked-and-held** result: **HELD-FIRM** (the check found nothing to change the grade) or **HELD-ERODED** (a *cited* new observation was found that is insufficient to change the grade — e.g. a corroborating source retracted while the primary holds; a bare "less sure" with no citable observation is not allowed, and two HELD-ERODED entries on one claim force a full re-grade review). Every entry — change or held — names in one line what was searched and what would have counted as disconfirmation: a "held" without a named falsifier is not a check.

## Mode 1 — OPEN (start a tracked investigation): ASK FIRST
Before creating the dossier, put these to the operator with AskUserQuestion (skippable; proceed on stated assumptions if declined):
1. **What are we tracking?** — the investigation question / the conclusion to keep live.
2. **Starting spine** — carry the grade-locked spine from an existing `analyse` run (point at the file or synthesis), or start fresh from a problem statement.
3. **Watch-list** — what new facts, documents, or events would change the call? These become the update triggers. Test each candidate for diagnosticity: would it actually discriminate between the call holding and the call flipping? Drop any trigger that would fire either way — a trigger consistent with every outcome is noise, not a usable trigger. Accept any party-held items the operator already holds.
4. **Cadence** — re-check on demand only, or on a schedule? If a schedule, offer to set a recurring re-verification of the web-verifiable claims (the `schedule` capability) and state plainly what it will check and when.
Then write the dossier file, seeded from the answers, and confirm its location.

## Mode 2 — UPDATE (a new fact, document, or event): ASK WHAT CHANGED
Begin by asking the operator **what has arrived** — a new document, a web development, a settled party-held item, an event — and accept uploads. Then:
1. Identify which claims the new information bears on.
2. Re-verify those claims (run the `verify` skill — router, source-tiering, and a disconfirmation pass on the load-bearing few): web-verifiable items against current sources; a newly-arrived party-held document against the pending list.
3. Update grades EXPLICITLY — never silently: record before -> after in the log and state what evidence changed it. Where re-verification does NOT change a grade, still record a **checked-and-held** entry (HELD-FIRM, or HELD-ERODED with its cited observation), naming what was searched and what would have counted as disconfirmation — so the log distinguishes "re-checked and survived" from "never revisited", and update the claim's `last-verified` date.
4. Re-surface the dominant unknown (it may have moved) and clear any pending item the new evidence settles.
5. **Re-derive the call** — if any grade changed, recompute the decision brief (call · confidence basis · dominant unknown · what-to-verify-first · what-flips-it) and say whether the call flipped.
6. Append a dated log entry: what arrived, what changed, what is still open.

## Mode 3 — STATUS (where does it stand?): READ, don't re-verify
Report the current state from the dossier without new verification (unless asked): the question, the spine with grades and — for each claim — its `last-verified` date and volatility class (flag any VOLATILE claim whose `last-verified` date is stale), the current dominant unknown, what is still pending (party-held), the open deep-core with the operator's positions, the current call, and what changed since the last update. Offer to run an UPDATE if the operator has new material.

## Hard invariants
- **Grade-lock carries — changing versus challenging.** A finding's grade changes only on new evidence, recorded in the log — never by re-expression. *Challenging* a grade (re-verifying it, searching for disconfirmation) needs no new evidence and may happen at any time — it is a search, not a write, and is recorded as a checked-and-held entry. Grade-lock constrains the write path; a challenge that turns up cited new evidence flows through the normal change path. (Because a flip still requires a cited new source, repeated challenging cannot by itself move a grade — grade-lock is also the multiplicity safeguard.)
- **The permanent set never moves.** Which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips are never graded above `[N]`, on any evidence. Log new evidence bearing on them against the routed open question — or as an ordinary finding about a link or a loop's existence — never as a grade change on the capped item.
- **Every change is dated and explicit.** No silent edits to the spine; the log is the audit trail.
- **The dominant unknown is always current.** Re-point it on every update.
- **Stay THIN.** One operator-owned file; if it needs complex mechanisms, re-scope.

## Status (state honestly)
The re-verification discipline here is sound, and `track` now has a real elicitation contract (OPEN / UPDATE / STATUS) — it no longer fails to ask the operator anything. It remains newer than `analyse`: its at-scale accumulation has not yet passed a controlled test, so rely on it as a disciplined living dossier and treat large accumulated re-gradings as worth a spot-check.
