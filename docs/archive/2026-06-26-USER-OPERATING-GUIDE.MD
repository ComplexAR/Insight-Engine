# Insight Engine — User Operating Guide

**`v0.1.7`** · A tool for analysing high-stakes, complex, or wicked problems — the kind where the danger is that the important things hide, the evidence is mixed or interested, and the deciding questions are value judgements. **The model provides the insight; the engine makes it verified, defensible, and audience-ready.**

> This is the Markdown edition, for reading on GitHub. The original styled version (with the rich diagrams) is in [`originals/`](originals/) and on the [project site](https://complexar.github.io/Insight-Engine/).

## 1. What it's for (and when not)

Reach for the Insight Engine when a decision matters and the surface is not the whole story — a strategy call, a post-incident review, a contract or regulatory question, an investment, a contested situation where you need to know what is really going on and how strongly you actually know it.

It is not a search box or a chatbot. It is a discipline: **verify what can be verified, grade how strongly each claim is established, separate fact from value, and make you own the value calls.** What you get back is a graded, defensible analysis and a decision brief — and, on request, the same analysis re-voiced for a particular reader, or kept live as an investigation.

> You don't need it for genuinely trivial things. It will notice triviality and right-size itself to a short answer — but you get the most from it on problems that actually have hidden depth.

## 2. Quick start

The engine is the `insight-engine` plugin. To update, re-install the latest `.plugin` from **Customize → Skills**. You drive it with four chat commands:

- **`/analyse`** — The main one. Hand it a problem in your own words, or attach a document and say "analyse this."
- **`/verify`** — Fact-check a set of claims or a premise before you rely on it.
- **`/render`** — Re-voice a finished analysis for a specific reader.
- **`/track`** — Keep an investigation live across sessions as new facts arrive.

**Simplest use:** type `/analyse` followed by your problem, answer the gate when it asks, and read the brief.

## 3. The components

The engine is a stack of layers (L0–L6) held together by an invariant **grade-lock spine** and owned, at one critical point, by you. A fail-safe **proportionality triage** sits in front of it and decides whether the full machinery should run at all.

```mermaid
flowchart TD
    TR["fail-safe PROPORTIONALITY TRIAGE<br/>unambiguously trivial? a short answer · under any doubt, full depth"]
    TR --> L1["L1 · Provocation page<br/>displacement &amp; 2nd-order · provenance V/N · seven probes · omission sweep"]
    L1 --> L2["L2 · Verification<br/>three-bucket router · source tiers V1/V2/V3 · disconfirmation · coverage-retention"]
    L2 --> L25["L2.5 · Systems pass — conditional<br/>feedback-driven problems only · graded causal map:<br/>loops · tipping conditions · leverage · investigate, don't predict"]
    L25 --> L3["L3 · Deep-core routing<br/>framing · legitimacy · opportunity-cost · value → the un-verifiable OPEN list"]
    L3 --> GATE["★ Forced judgement gate — YOU<br/>you record a one-line position on each deep-core question, or defer"]
    GATE --> L4["L4 · Assembly — the decision brief<br/>call · calibration · dominant unknown · what-to-verify-first · what-would-flip-it"]
    L4 --> L5["L5 · Rendering<br/>audience re-voicing: adversarial · advocate · board · counsel · regulator · family · any"]
    L5 --> L6["L6 · Workspace<br/>living dossier across sessions: OPEN · UPDATE · STATUS"]
    L0["L0 · Strong model — the substrate that provides the insight"] -.->|substrate| L1
    SPINE["GRADE-LOCK SPINE — the invariant through every layer<br/>V1 primary · V2 secondary · V3 weak/contested · N interested party<br/>the single dominant unknown · the non-droppable caveat core<br/>grades are locked: set once, never changed downstream — only re-expressed"]
    SPINE -.->|runs through every layer| L2
    classDef gate fill:#fdf1df,stroke:#e8a33d,stroke-width:2px;
    classDef cond fill:#fff7ec,stroke:#eac489,stroke-width:2px;
    classDef green fill:#e9f5ee,stroke:#a9d4bd;
    class GATE gate;
    class L25 cond;
    class L2 green;
```

**The four skills (the interface):** `/analyse` orchestrates the whole pipeline (triage → L1–L6 with the gate); `/verify` is L2 standalone; `/render` is L5 standalone; `/track` is L6 standalone.

In short: **L0** the model is the substrate; **L1–L6** are the processing layers; the **spine** is the epistemic backbone that never bends; the **gate** is where you act; the **triage** decides how much machinery to run.

## 4. How it works

Here is what actually happens when you hand it a problem. Most of the pipeline runs silently — the one place it stops for you is the gate.

```mermaid
flowchart TD
    U["You · /analyse your problem"] --> T{"⚑ Proportionality triage<br/>trivial, self-contained, reversible,<br/>no third parties or legal exposure?"}
    T -->|"YES — rare"| SH["A short, proportionate answer<br/>+ an offer to run the full pass"]
    T -->|"NO / any doubt → full depth (the default)"| S0["STEP 0 · Optional scoping<br/>a few skippable questions"]
    S0 --> S1["STEP 1 · Provocation pass<br/>surface what's material but sits where attention doesn't go; mark each claim V or N"]
    S1 --> S2["STEP 2 · Verification<br/>route each claim · tier it V1/V2/V3 · search the negation of the load-bearing few · re-scan"]
    S2 --> S25["STEP 2.5 · Systems-investigation pass — conditional<br/>only if genuinely systemic (feedback · stocks · delays · tipping):<br/>a graded causal map of loops, tipping conditions, leverage · investigate, don't predict"]
    S25 --> S3["STEP 3 · Deep-core routing<br/>set aside the questions no evidence can settle: framing · legitimacy · opportunity-cost · value"]
    S3 --> S4["STEP 4 · Grade-lock + resilience check<br/>fix every grade; stress-test whether the call survives its assumptions moving together"]
    S4 --> G["★ STEP 5 · THE FORCED GATE — YOU<br/>take a one-line position on each deep-core question, or explicitly defer.<br/>The brief does not finalise until you do."]
    G --> S6["STEP 6 · Assemble → the decision brief<br/>your positions · graded findings · call · calibration · dominant unknown · verify-first · flip-it · sources"]
    S6 --> S7["STEP 7 · Offer follow-ons — /render · /track"]
    classDef gate fill:#fdf1df,stroke:#e8a33d,stroke-width:2px;
    classDef cond fill:#fff7ec,stroke:#eac489,stroke-width:2px;
    classDef green fill:#e9f5ee,stroke:#a9d4bd;
    class G gate;
    class T cond;
    class S25 cond;
    class S2 green;
    class S4 green;
```

From Step 4 onward the **grade-lock spine** holds: grades never change — they are only re-expressed.

**Step 2.5 is new in v0.1.7 and conditional.** When a problem is genuinely *systemic* — driven by feedback loops, accumulating pressures, delays, or a possible tipping point — the engine adds a **systems-investigation pass**: a graded causal map of the loops, the *conditions* under which the system could tip (never a date or a probability), and the highest-leverage places to intervene. It investigates the structure and routes the "will it / when" judgement to you; it never forecasts. On a static, one-shot problem it skips this step and says so.

## 5. Using `/analyse`

**What to type:** `/analyse` and your problem in plain words, the specific questions you want answered, or a document to analyse — it will answer your questions inside the graded analysis. The more raw the problem (rather than a pre-digested summary), the more the engine can surface what you might have framed out.

**What it does:** runs the pipeline above. You may see it search the web — that is verification, grading each load-bearing claim and searching for evidence that would *disprove* the ones the conclusion rests on.

**What you get:** a written analysis led by your gate positions, the graded findings (each marked and tiered), and a five-part decision brief.

## 6. Clearing the gate — the one moment that's yours

Part-way through, the engine stops and puts two to four **deep-core questions** to you — about the framing, the legitimacy, the opportunity cost, or the values at stake. These have no verifiable answer; they are judgements only you can make. You can:

- **Take a position** — a single line on each is enough.
- **Override the engine's framing** — encouraged. If you disagree with how it has framed the problem, say so; it will reshape the brief around your judgement.
- **Defer** — logged, not ignored; the brief notes it as open.

> **Why it's forced.** The engine learned, by test, that if these questions are merely *shown* to you they get read and then ignored — attention slides to the verifiable. Being made to take a position is what gets the value questions actually addressed. In real use, an operator's override at the gate materially reshaped the final brief. This is the engine's most valuable interaction; treat it as the decision, not a form to clear.

## 7. Reading the output

### The grade markers

Every load-bearing claim is marked. `[V]` = independently corroborated; `[N]` = rests on an interested or self-reporting party. A `[V]` always carries a strength tier: `[V1]` primary (the regulation, the official statistic, the study), `[V2]` secondary (reputable reporting on top of primaries), `[V3]` weak or contested. The `[V3]` and `[N]` items are where the analysis is exposed — that is where to push.

### The decision brief (always five parts)

- **The call** — the actual recommendation.
- **Calibration** — how sure, and the conditions under which it changes (it will name the weakest grade the call leans on).
- **The dominant unknown** — the one fact that would most change the conclusion. Chase this first.
- **What to verify first** — the cheapest next step that most reduces risk.
- **What would flip the call** — including any assumptions that, moved together, the call could not survive.

### Two things that always travel with it

A one-line **reliability caveat** naming what the analysis rests on; and, for a wicked problem with no verifiable solution, the "call" arrives as a **provisional stance** — the value it trades and what would re-open it — rather than a false-confident verdict. That is deliberate.

## 8. The other three skills

- **`/verify`** — Hand it a set of claims or a premise. It routes each (web-checkable / your-document / value-judgement), grades and tiers them, searches for counter-evidence, and tells you which are exposed. Use it to check something before you rely on it.
- **`/render`** — Takes a finished analysis and re-voices it for a reader. It will ask who — or you name them: a board, counsel, a regulator, a journalist, the family, an adversary. The grades never change; only the register does.
- **`/track`** — For inquiries that evolve. **OPEN** starts a dossier; **UPDATE** folds in new facts and re-verifies; **STATUS** reads back where it stands. (Newest skill — sound, but the least battle-tested.)
- **Chaining them** — A natural flow: `/analyse` a problem → `/render` it for each stakeholder → `/track` it as the situation develops. `/verify` can be used at any point to re-check a claim.

## 9. Tips for good results

- **Give it the raw problem**, not a tidy summary — it verifies, and it surfaces what a tidy summary has already framed out.
- **Upload the documents you hold** (contracts, figures). It will not pretend to verify what it cannot see, but it will use what you give it and name what would settle the rest.
- **Answer the gate honestly, and override it when you disagree.** That is the point of the gate.
- **Don't rewrite for a different reader** — use `/render`; the grades stay intact.
- **For something that will change, use `/track`** rather than re-running from scratch.
- **Trust the tiers.** A `[V1]` is solid; a `[V3]` or `[N]` the call leans on is the soft spot — push there.

## 10. What it won't do

- It won't over-analyse a genuinely trivial decision — it right-sizes, so don't be surprised by a short answer (you can always ask for the full pass).
- It won't pseudo-verify a private document — it names what would settle it.
- It won't resolve your value questions — it forces *you* to.
- It won't change a grade to suit an audience.

## 11. Glossary

| Term | Meaning |
|---|---|
| `[V]` / `[N]` | A claim is **[V]** (independently corroborated) or **[N]** (rests on an interested or self-reporting party). |
| `[V1]` / `[V2]` / `[V3]` | Source-strength tiers on a [V]: primary / reputable-secondary / weak-or-contested. |
| Dominant unknown | The single fact that, if known, would most change the conclusion. |
| Deep core | The questions no evidence can settle — framing, legitimacy, opportunity cost, value. Yours to judge. |
| The gate | The forced step where you take a position on each deep-core question before the brief finalises. |
| Grade-lock | Once set, a claim's grade never changes downstream — only its wording does. What makes the output defensible. |
| Disconfirmation | For load-bearing claims, a second search aimed at *disproving* them — the counter to confirmation bias. |
| Coverage-retention | A re-scan for material issues that focusing on the load-bearing few may have dropped. |
| Systems-investigation pass | A conditional step (v0.1.7) for genuinely systemic problems: a graded causal map of feedback loops, tipping *conditions*, and leverage points — investigating structure, never predicting whether or when the system tips. |
| Proportionality triage | The fail-safe pre-flight that right-sizes the analysis — short answer for the unambiguously trivial, full depth otherwise. |
| Provocation page | The fixed one-page method applied verbatim every run — the engine's analytical L1. |
| Wicked problem | One with no verifiable solution, where the deep core dominates. The call comes as a provisional stance, not a verdict. |

---

**Insight Engine v0.1.7** — User Operating Guide. The model provides the insight; the engine makes it verified, defensible, and audience-ready. For the full design specification, layer-by-layer detail, and the controlled-testing record behind each feature, see the companion [Architecture](Architecture.md) document.
