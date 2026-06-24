---
name: analyse
description: Primary Insight Engine orchestrator for high-stakes, complex, or wicked problems. Triggers when the user asks to analyse a scenario or document, surface hidden or non-obvious issues, produce a defensible analysis or a decision brief, investigate what is really going on beneath a situation, or assess a high-stakes decision. Runs a fail-safe proportionality triage, an optional scoping step, a fixed provocation-page pass, web verification of load-bearing claims with source-tiering and a disconfirmation pass, a conditional systems-investigation pass (a graded causal map for feedback-driven problems; investigate, don't predict), deep-core routing, a forced deep-core judgement gate, an assumption-resilience check, and grade-locked assembly with a decision brief.
---

# Insight Engine — analyse

Run the Insight Engine on the problem. The model provides the insight; your job is to frame it, verify it, grade it, route what cannot be verified to the human, force a judgement on it, and deliver a defensible analysis plus a decision brief. Work the steps in order. Do not skip verification, and never change a grade once set.

## Proportionality triage (run this FIRST — fail-safe; default to depth)
Before running the steps below, judge whether the problem is UNAMBIGUOUSLY low-stakes — routine, self-contained, reversible, with no third parties bound, no material money or dependency, no legal or regulatory exposure, and no contested values. Apply strong skepticism to the framing: ask "am I being invited to treat this as routine?" Treat ANY of the following as disqualifying — run the full method: irreversibility; anyone bound who is not in the room; material money or dependency; legal or regulatory exposure; contested values; a party who benefits from light scrutiny; anything not easily reversed. ONLY if the problem is unambiguously trivial on every count: give a proportionate short answer, skip the heavy machinery, say you have done so, and invite the operator to request the full pass. Under ANY doubt, run the full method — depth is the default and down-scoping is the rare exception. (Fail-safe by design, and validated this way: a mild over-analysis is cheap; wrongly down-scoping a problem that only looks routine is not.)

## Step 0 — Optional scoping (offer, never block)
Offer the operator up to five optional, skippable clarifying questions with AskUserQuestion. Ask only what is not already clear. If they skip any or all, proceed on explicit stated assumptions and mark them as assumptions.
1. The decision at stake — what is being decided or acted on?
2. The intended audience(s) for the output.
3. The stakes / value frame — whose costs matter most, and what counts as a serious outcome. (You articulate the value structure; the operator owns the value judgement.)
4. Scope boundaries — what is explicitly in and out of scope. (Scope is where the largest hiddens hide.)
5. Any party-held material the operator holds that cannot be verified online — accept uploaded documents or figures.

## Step 1 — The provocation pass (L0 + L1)
Load `references/provocation-page.md` and apply it verbatim. Treat your fluent first reading as the baseline a competent reader already has — not the finding. Run the two always-on moves (displacement / second-order; provenance `[V]`/`[N]` plus the single dominant unknown) and the candidate probes (absent voice; cui bono from the framing; base rate & measurement; normalised-as-natural; spuriously-present; conspicuously-absent / omission sweep; reflexive). Then steelman your strongest findings and name every materially affected party, including those not in the room.

## Step 2 — Verification (L2): verify before asserting
For every load-bearing claim, apply the three-bucket router:
- **Web-verifiable** (a public fact, pattern, or rule): search; grade `[V]` with a cited current source, or `[N]` if uncorroborated or contradicted. Correct your own confidently-wrong facts — a strong model will assert some, and this is where they get caught. Verify before relying; if the premise of the question is itself checkable, check it.
- **Party-held** (a private document or internal figure): do NOT pseudo-verify; record what document would settle it.
- **Irreducibly open** (a value, a framing, or a forecast): route to the human in Step 3.
Two disciplines make `[V]` mean something:
- **Tier every `[V]`** by source strength — `[V1]` primary (the regulation/statute, official statistic, peer-reviewed study, court ruling, primary dataset), `[V2]` secondary (reputable reporting/interpretation resting on primaries), `[V3]` contested/weak (only weaker or interested sources, or credible sources disagree). The tier is part of the grade.
- **Disconfirm the load-bearing few** — for each claim the call materially rests on, run a second search at its NEGATION; if credible counter-evidence of comparable strength exists, downgrade to `[V3]`/`[N]` and record the dispute; if a real negation search finds nothing, mark it *survived disconfirmation*.
Weight a self-damaging admission above a self-serving claim. Revise the dominant unknown against what you find. (The `verify` skill runs this step — router, tiering, and disconfirmation — standalone.)

## Step 2.5 — Systems-investigation pass (conditional; investigate, do not predict)
Run this only when the problem is genuinely systemic — when it shows **two or more** of: feedback / circular causation; accumulation (stocks that build up or drain); material delays between cause and effect; multiple interacting actors; a possible regime shift / tipping; self-fulfilling expectations. Otherwise skip it with one line — *"no material feedback structure — systems pass not warranted"* — and go to Step 3. (Proportionate by design: do not force a causal map onto a static or one-shot problem; importance, emotion, or difficulty is not systemic structure, and a spurious map is a failure, not thoroughness.)

If it runs, build a **causal map as a graded hypothesis — not a simulation and not a forecast.** Keep it to the load-bearing few: ≤8 variables, ≤5 loops, ≤4 tipping points, ≤5 leverage points (a sprawling map is itself false precision).
- **Variables & links.** Name the key variables (mark accumulators as stocks). Write each causal link `A --(+/−[, delay])--> B` with a grade and a one-line mechanism. Grade links `[V1]` established mechanism / `[V2]` reputable consensus / `[V3]` disputed or weak / `[N]` your structural inference. Flag material delays — a lag is where the system feels fine until it isn't. Do not assert magnitudes beyond what is `[V1]`-grounded.
- **Feedback loops.** Identify reinforcing (R) and balancing (B) loops. Grade each **twice** — *exists* (the chain is real) and *dominates-now* (it currently drives behaviour). Existence may be `[V]`; **dominance is usually `[N]` — never assert which loop wins as fact; route it to the human.**
- **Tipping points.** Name candidate regime-shift thresholds **as conditions, never dates or probabilities**, each with reversibility (reversible / hard / irreversible) and a grade (`[N]` unless a specific threshold is evidenced). Name them to *watch*, not to predict.
- **Emergence.** Name any behaviour that arises from the interaction and is in no single part — especially self-fulfilling expectations, where the shared narrative is itself a causal variable.
- **Leverage points (ranked).** Where would a small intervention move the system most — the dominant loop's entry node, a delay, or the driving expectations? Rank them; grade each **twice** — *mechanism* (why structurally high-leverage) and *effectiveness* (whether acting there will actually work — usually `[N]`).

**The hard ceiling (the spine of this pass):** structure may be graded up to `[V]`; **whether or when the system tips has a ceiling of `[N]` and routes to the human.** State the conditions under which it could shift; never that it will, or when, or with what probability. The map is a hypothesis to be falsified, not a model to be trusted. This pass investigates structure; it does NOT simulate dynamics or compute outcomes — if genuine quantitative modelling is needed, say so and route to specialists and data.

Feed forward: loop *dominance*, *regime*, and *timing* join the deep-core OPEN list (Step 3 → the gate); the ranked **leverage points** inform the call (Step 6, brief item a); the **tipping conditions** inform what-to-verify-first / monitor (6d) and what-would-flip-the-call (6e); and the Step 4 resilience check stress-tests the call against the map's load-bearing links and loops.

## Step 3 — Deep-core routing
Separate the material issues that are NOT externally verifiable — the framing of the decision itself; legitimacy and who is bound without a say; opportunity cost and unmodelled alternatives; value trade-offs — into an explicit OPEN list. Do not resolve them, do not drop them, and do not assert them as verified. These are the questions the operator must judge in Step 5.

## Step 4 — Grade-lock, then resilience-check (the invariants)
Fix every claim's `[V]`/`[N]` grade with its source tier (`[V1]`/`[V2]`/`[V3]`), the single dominant residual unknown, and the non-droppable caveat core (all grades + the dominant unknown + a one-line reliability caveat naming what the analysis rests on, e.g. a single interested source or a `[V3]` the call leans on). Nothing downstream may change a grade — only re-express it.
Then **stress-test the conclusion, not just the claims.** Name the two to four assumptions the call most rests on, vary them *together*, and record whether the conclusion survives. This is an **assumption-fragility** check: it exposes where jointly-moved assumptions would break the call. It is NOT system modelling — it does not simulate feedback loops, cascades, or tipping points, and must not claim to (the conditional Step 2.5 systems-investigation pass is where graded structure is mapped). Feed the result into calibration and what-would-flip-it in Step 6.

## Step 5 — The deep-core judgement GATE (forced; the operator clears it)
Before you write the final brief, **stop and put the deep-core open questions to the operator as a gate.** Present the framing / legitimacy / opportunity-cost / value questions from Step 3 plainly, and ask the operator to record a one-line position on each — or to explicitly defer (a deferral is logged, not ignored). **Do not finalise the brief until the operator has taken a position on each or chosen to defer.**

Why this is a gate, not a heading: controlled testing showed that merely leading the brief with these questions — even calling them mandatory — does NOT get a decision-maker to act on them; they read them, then prioritise the verifiable. The deep core is a **judgement the human takes**, not a priority that competes with "commission a study." Forcing an explicit position is what actually gets it addressed. Keep it light — a handful of questions, one position each, deferral always available. You articulate the questions and the value structure; the operator owns the judgement.

## Step 6 — Assemble, with the operator's judgements and the decision brief (L4)
First, a **coverage-retention check**: having concentrated on the load-bearing few (Step 2) and on the dominant unknown and deep core (Steps 4-5), re-scan once for material issues that this focus deprioritised, and fold any that resurface back into the findings. Sharpening the spotlight darkens its edges; this is the counter-sweep.

Then produce the deliverable in this order:
1. **The deep-core questions with the operator's recorded positions** (or noted deferrals) — leading the document. This is the gate, cleared and on the record.
2. **The verified findings** — each hidden with its `[V]`/`[N]` grade, source tier, and any disconfirmation result, plus its source. Separate documented patterns from any interest- or grief-driven over-claims, and say which you are setting aside and why.
3. **The decision brief — always include this block:** (a) **the call** — the actual recommendation. *If the problem is wicked* (the deep core dominates and there is no verifiable solution), the call is a **provisional stance, not a verdict**: state which value it trades against which ("this prioritises X at the expense of Y"), mark it explicitly re-openable, name what would re-open it, and offer to hand off to `track`. A crisp verdict on a wicked problem re-imports the false closure the analysis exists to avoid. (b) **calibration** — your confidence and the conditions under which it changes, naming the weakest load-bearing grade (any `[V3]` or `[N]` the call leans on). (c) **the dominant unknown** — the one fact that would most move it. (d) **what to verify first** — the cheapest next step that most reduces risk. (e) **what would flip the call** — including any jointly-moved assumptions the Step-4 resilience check found the call could not survive, and any tipping conditions from the Step 2.5 systems pass. Where the operator's deep-core positions bear on the call, reflect them.
4. **Sources.**
Do not over-claim causation; an over-claim costs more than a miss. Hold the reliability caveat to the end.

## Step 7 — Offer follow-ons
Offer to render the analysis for specific audiences (the `render` skill), and — for a long-running inquiry — to open or update a living workspace (the `track` skill).
