---
title: "The Insight Engine — Glossary"
subtitle: "Every term, symbol, identifier series and abbreviation in use across the Insight Engine corpus, with the multiple-meaning audit and a governing section"
date: "27 August 2026"
---

# The Insight Engine — Glossary

*Companion to the [User Operating Guide](User-Operating-Guide.md) and the [Architecture](Architecture.md) document.*

**Corpus version described:** insight-engine **v1.0.0** (shipped); the identifier scheme is unchanged since v0.1.22. The identifier scheme in Section 4 is the shipped scheme, fixed by the specification in `skills/analyse/SKILL.md`.

**Provenance:** compiled 24 August 2026 by Fable 5 (`claude-fable-5`) against v0.1.21, when the identifier scheme was designed and unshipped; revised on first publication, 27 August 2026, to describe the scheme as shipped. The stems were fixed on 25 August 2026, five of them differing from those first proposed.

**Status:** reference document for vocabulary. It defines terms and does not set method. Where this document and a skill differ, the skill governs.

---

## How to read this glossary

- Entries are grouped in eight sections and **alphabetical within each section or subsection** (grade symbols lead Section 1 in symbol order, because their order is part of their meaning).
- Each entry gives: the term; a one-or-two-sentence literal definition in plain modern English; where it is defined authoritatively in the corpus; and a note where usage currently varies.
- **Two audiences.** Reader-tier entries serve a non-specialist reading a decision brief; engine-and-record entries serve someone working on the engine or its test record. A reader-tier entry serves both audiences. No entry carries an audience marker; the tier is carried by structure: the whole of Section 1 is reader tier, Sections 2 and 3 are each divided into a reader-tier subsection and an engine-and-record subsection, and Sections 4 to 8 serve the engine and record audience. The Guide's §11 glossary should be a subset of the reader tier: all of Section 1, plus the reader-tier subsections of Sections 2 and 3.
- This glossary is consistent with ADJ-006 §5.1 (protected technical vocabulary) and §5.2 (banned constructions) and does not re-open either. Where a §5.1 term is protected because it reads as figurative, its entry here is the place its literal meaning is written down.
- **Fixed corpus-wide, flagged and not resolved here:** the grade symbols `[V]`, `[V1]`, `[V2]`, `[V3]`, `[U]`; the canonical five-situation `[U]` definition (quoted verbatim in Section 1); and the wording of the fixed plain-language legend, which is versioned behaviour. Nothing in this glossary proposes changing any of them. **Superseded as to one symbol, and only one:** the unverified grade was `[U]` until 30 August 2026, when the operator renamed it `[U]` by a corpus-level decision recorded at `Grade-Symbol-Decision-2026-08-30.md`. This glossary did not propose that change and does not propose any other.

---

## Section 1 — Grade and evidence vocabulary

### The symbols

**`[V]`** — Independently corroborated: the claim is supported by at least one cited current source independent of any party with a stake in it. A `[V]` is never bare; it always carries a source-strength tier. Authority: `analyse` Step 4 and the fixed legend (`skills/analyse/SKILL.md`); `verify`; Architecture §4.

**`[V1]` — primary** — The claim is confirmed against the authoritative source itself: the statute or regulation text, the court ruling, the official statistic, the peer-reviewed study, the primary dataset. *Primary* means the source is proximate — produced at first hand — not that its content is trustworthy: an interested party's own primary material does not on that basis earn `[V1]` on a claim it has a stake in. Authority: `verify`; Architecture §4; Guide §11.

**`[V2]` — secondary** — Confirmed against reputable reporting or interpretation resting on primaries: an established news organisation, a professional body, a textbook, a well-regarded analyst. Where it can, the analysis names the primary source that would lift the claim to `[V1]`. Authority: `verify`; Architecture §4.

**`[N]` — the former symbol for the unverified grade (historical).** Used from the first release to `insight-engine` v0.1.23 and Portable Edition 1.1.8, renamed `[U]` on 30 August 2026 by the corpus decision at `Grade-Symbol-Decision-2026-08-30.md`. **`[N]` in a document dated before that day and `[U]` in one dated after are the same grade under different symbols** — the five situations, the tier definitions and the permanent set did not change. Documents delivered before the rename are never retrospectively rewritten, so `[N]` remains correct in every test record, run artefact, archived document and retained example output. This entry exists because that record is permanent and a reader meeting `[N]` needs somewhere to look. Authority: the corpus decision; Architecture version table.

**`[V3]` — weak or contested** — The weakest `[V]`: only weak but *independent* corroboration exists, or credible sources disagree, or (on a map link) the mechanism is carried by analogy with no in-case support. A claim resting only on an interested party's own materials is `[U]`, not `[V3]`. The specific weakness is named and travels with the claim. Authority: `verify`; `analyse` Steps 4–5; Architecture §4.

**`[U]`** — Unverified: not independently verified. `U` stands for *unverified*; the definition is the full phrase, and the word *independently* is load-bearing, because a claim resting only on an interested party has been attested but not independently. The canonical definition, quoted verbatim from the shipped legend (wording fixed at v0.1.21, untouched at v0.1.22, symbol renamed and letter expansions added at the convergence release of 2026-08-30) (local paraphrase of this block is the recorded cause of the v0.1.20 legend defect, so this glossary quotes and does not restate):

> [V] = verified, independently corroborated; [U] = unverified, meaning not independently verified. That one mark covers five situations: a claim a real search left uncorroborated, or found contradicted; a claim resting only on an interested or self-reporting party; a claim awaiting a named document that would settle it; a claim inheriting the cap from an unverified thing it depends on; and a judgement or prediction this method never grades higher, however strong the evidence — which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips. The first three can move if someone looks harder. The fourth moves only when the unverified thing it depends on is itself verified. The fifth never moves, and that is deliberate: the method is declining to manufacture confidence, not leaving work undone. The claim's own line says which of the five it is, and records any contradiction found. Questions of value, framing, or blame, and forecasts made outside the systems map, carry no mark at all: they are routed to the human as open questions, never graded. Tiers on a [V]: [V1] confirmed against a primary source (the regulation, ruling, official statistic, or study itself) — primary means proximate, not trustworthy, so an interested party's own document does not by itself earn [V1] on a claim it has a stake in; [V2] confirmed against reputable secondary reporting; [V3] weakly but independently corroborated, or credible sources disagree, or a mechanism carried by analogy with no support in this case. Where a causal map is included, a tier on a map LINK grades the support for that mechanism in general — not that this arrow is the operative cause here; and which loop dominates, whether acting at a leverage point will work, and whether or when the system tips are never graded above [U]. "Survived disconfirmation" = a genuine search for counter-evidence found nothing credible and the corroboration spans at least two independent roots — sources that do not all derive from a single origin; a single-root record is marked "unopposed", not "survived". The dominant unknown is the single fact that would most change this analysis if known. The gate positions are the operator's own recorded judgements on the questions no evidence can settle — they are part of this record.

Authority: the fixed legend in `skills/analyse/SKILL.md` (Step 9 item 5); ADJ-006 §1 (the reconciliation that fixed this wording); Architecture §4. One boundary note from ADJ-006 §1, part of the adjudicated doctrine: credible disagreement between comparable sources is `[V3]` (contested), not `[U]`; `[U]`-by-contradiction is for counter-evidence strong enough that the claim fails verification.

**The five situations of `[U]`** — The five distinct states the single `[U]` symbol covers, listed in the quotation above and referred to ordinally ("the first three", "the fourth", "the fifth"). They are never numbered with identifiers; they are carried in words, and each `[U]` claim's own line states which situation applies (`analyse` Step 7; `track` records it in a `situation:` field). Authority: the legend; `track` spine definition; Architecture §4.

### The terms

**Attribution ceiling** — The rule that an official account's finding that a named person or group erred, failed, or ignored something is an attribution — a recorded judgement by an interested party. That the body made the finding may grade up to `[V1]`; the blame itself is never graded as established fact and routes to the human. Authority: `verify` Rules; `analyse` Step 4; Architecture §5.3 (shipped v0.1.9). Note: one of three distinct "ceiling" terms — see Section 7.

**Dominant unknown** — The single fact that, if known, would most change the conclusion. Named explicitly in every full pass, re-pointed whenever the evidence moves, and part of the non-droppable caveat core. Authority: provocation page; `analyse` Steps 4 and 9; Architecture §4.

**Grade** — The provenance mark on a claim: `[V]` with its tier, or `[U]`. A grade attests how strongly a claim is independently established, not whether it is true. Authority: Architecture §4.

**Grade-lock** — The invariant that once a grade is set (at the Step 7 grade-lock), nothing downstream may change it — only re-express it. A grade moves only on new evidence, recorded in a log. Grade-lock is what lets a finished analysis be re-voiced for any audience without its claim set changing. Authority: `analyse` Step 7; Architecture §4; carried in `render` and `track` as hard invariants.

**Grade transport** — The requirement that Step 4's routing marks travel downstream: any later claim, map link, or brief element whose mechanism depends on a party-held or irreducibly-open item caps at `[U]`, however well established the general mechanism is. The v0.1.19 release repaired observed leaks in this invariant. Authority: `analyse` Steps 4–5; `verify`; Architecture version table (v0.1.19).

**Inheriting the cap** — Situation 4 of `[U]`: a claim is `[U]` because an unverified thing it depends on caps it, not because it was itself checked and failed. It moves only when the dependency is verified. The word "cap" here is the grade sense, fixed by the legend wording — see Section 7, "cap". Authority: the legend; Architecture §4.

**Irreducibly open** — The third router bucket: a value, a framing, or a forecast outside the systems map — something no evidence can settle now. It is routed to the human unmarked, never graded, and the mark of having been routed travels: a downstream step may use it as an open question, never as a graded premise. Authority: `analyse` Step 4; `verify` (wording since v0.1.21, unchanged in the shipped `verify`: "routed, not marked `[V]` or `[U]`").

**Non-droppable caveat core** — The minimum content that appears in every output and every render: all grades, the dominant unknown, and the one-line reliability caveat. Authority: `analyse` Step 7; `render` hard invariant 2; Architecture §4.

**Party-held** — The second router bucket: a private document or internal figure the operator holds that cannot be verified online. It is never pseudo-verified; the analysis names the exact document that would settle it, and everything depending on it caps at `[U]` until that document arrives (situation 3, and situation 4 for dependents). Authority: `analyse` Steps 2 and 4; `verify`; `track` Pending section.

**Permanent set** — The three judgements graded `[U]` by design on any evidence: which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips (situation 5). New evidence bearing on them is logged against the routed open question, or as an ordinary finding about a link or a loop's existence — never as a grade change on the capped item. Authority: `analyse` Step 5 (the hard ceiling); `verify` and `track` ("The permanent set never moves", identical wording, shipped v0.1.21); Architecture §4.

**Provenance** — Where a claim's support comes from and how directly. The `[V]`/`[U]` grade is a provenance mark; the tier states the provenance strength. Authority: provocation page (move 2); Architecture §4.

**Reliability caveat** — A one-line statement naming what the analysis rests on — for example a single interested source, or a `[V3]` the call leans on. Held to the end of the deliverable and part of the caveat core. Authority: `analyse` Steps 7 and 9.

**Routed** — Sent to the human as an open question instead of being graded. Value, framing, blame, and forecasts outside the systems map are routed unmarked; the permanent set is the one class that is both graded (`[U]`) and routed, because a structured map slot exists for it. Authority: `analyse` Steps 4 and 6; ADJ-006 §3 (the dual-marking ruling).

**Single-root record — see "Unopposed"**

**Survived disconfirmation** — The status of a load-bearing claim for which a genuine search at its negation found nothing credible, where the corroboration spans at least two independent roots — sources that do not all derive from a single origin. Authority: `analyse` Step 4; `verify`; the legend.

**Tier** — The source-strength suffix on a `[V]`: `[V1]` primary, `[V2]` secondary, `[V3]` weak or contested. The tier is part of the grade, travels with the claim, is never dropped, and its definitions are fixed by the specification and never re-based for a case. On a causal-map link the same tier symbols carry a weaker promise — see Section 3, "Weaker promise". Authority: `verify`; `analyse` Step 4; Architecture §4. Note: in one workspace record "tier" also names a browser access level ("read tier"); that is tooling vocabulary, not grade vocabulary.

**Unopposed — single-root record** — The status of a claim whose negation search found nothing but whose corroborating material traces to a single origin (one report, one leak, one party's account repeated by others). An empty negation search then shows only that one root exists, so the claim is marked unopposed, not survived. Authority: `analyse` Step 4; `verify`; the legend.

---

## Section 2 — Method vocabulary

### Reader-tier entries

**Action contingency** — The part of the confidence basis stating what must hold true *after* acting for the call to succeed. An intervention can fail even when every premise is `[V1]`; this is distinct from what would flip the evidence. Authority: `analyse` Step 9 item 3(b); shipped v0.1.12.

**Addressee rendering** — Re-expressing a finished, graded analysis for a specific reader — a register transform over the grade-locked spine, never a re-analysis. No claim or grade changes; the caveat core appears in every render. The `render` skill is this layer (L5) standalone. Authority: `render`; Architecture §5.10.

**Assumption-resilience check** — After grade-lock, the step that names the two to four assumptions the call most rests on, varies them *together*, and records whether the conclusion survives. It is an assumption-fragility check on the conclusion, deliberately not system modelling, and it states which load-bearing assumptions it did not vary. Authority: `analyse` Step 7; Architecture §5.5.

**The call** — Decision-brief item (a): the actual recommendation. On a wicked problem it is a provisional stance, not a verdict. "Call" also appears in the adjudication layer meaning an API call — see Section 7. Authority: `analyse` Step 9 item 3(a).

**Confidence basis** — Decision-brief item (b): confidence in the fact-chain and the conditions under which it changes, naming the weakest load-bearing grade, plus the action contingency. It is evidence-quality transparency, not a track-record calibration — no scored probability is implied. Authority: `analyse` Step 9 item 3(b); renamed from "calibration" at v0.1.12–13.

**Coverage-retention re-scan** — A single re-scan, before assembly and before `verify` returns, for material issues that concentrating on the load-bearing few withdrew attention from; anything that resurfaces is folded back into the findings. Authority: `analyse` Step 9; `verify`; Architecture §5.3.

**Decision brief** — The fixed five-part closing block of every full pass: (a) the call; (b) confidence basis, plus the action contingency; (c) the dominant unknown; (d) what to verify first — the cheapest next step that most reduces risk; (e) what would flip the call, phrased as first-person conditionals. It is kept a short decision surface: a new consideration merges into an existing element. Authority: `analyse` Step 9 item 3; Architecture §5.7.

**Deep core** — The material questions no evidence can settle: the framing of the decision, legitimacy and who is bound without a say, opportunity cost and unmodelled alternatives, value trade-offs. Separated into an explicit OPEN list at Step 6 and put to the operator at the gate. Authority: `analyse` Step 6; Architecture §5.4.

**Deferral** — An operator's explicit choice not to take a position on a gate question. It is logged, not ignored, and the brief notes the question as open. Authority: `analyse` Step 8; Guide §6.

**Disconfirmation pass** — For every claim the conclusion materially rests on, a second search aimed at the claim's negation. Credible counter-evidence of comparable strength downgrades the claim to `[V3]` or `[U]` and the dispute is recorded; an empty genuine search marks the claim survived (two or more independent roots) or unopposed (single root). Authority: `analyse` Step 4; `verify`; Architecture §5.3.

**Forced judgement gate** — Step 8: before the brief is finalised, the engine stops and puts the deep-core questions to the operator one at a time, each with a plain wording, an example answer, an "I don't know — explain this" route, and a defer option. The brief does not finalise until the operator has taken a one-line position on each or explicitly deferred. It is forced because controlled testing showed that merely displaying the questions does not get them acted on. Bare "the gate" in engine prose means this gate — see Section 7. Authority: `analyse` Step 8; Architecture §5.6.

**Grade-locked assembly** — Step 9: producing the deliverable in fixed order — the operator's recorded gate positions first, then the graded findings with checkable references, then the decision brief, sources, and the fixed plain-language legend — with every grade already locked. Authority: `analyse` Step 9; Architecture §5.7.

**Hard / soft / messy tags** — Optional finding tags naming what kind of component a finding is and the honest aim of a response: hard (bounded and optimisable — solve), soft (behavioural or political — resolve by satisficing), messy (rooted in conflicting values — dissolve by reframing). Reporting vocabulary only; they change no grade. Authority: Guide §7 (Madhavan, 2024).

**Independence ladder** — The order of adjudicators, strongest first, ranked by how decorrelated the adjudicator's blind spots are from the analysing model: rung A a different-lab model (cross-lab); rung B a different in-house model (Fable 5); rung C a panel of blind Opus instances (same lineage — divergence is the signal, convergence is stability, not proof); rung D a self-adversarial reset. The engine declares which rung it reached. Authority: `adjudicate` §5; Architecture §5.12; Guide §11.

**Living dossier** — `track`'s single operator-owned markdown file per investigation (`track-<slug>-<date>.md`), persisted across sessions: question, spine, dominant unknown, open deep core, pending party-held items, watch-list, the call, sources, update log. Kept thin by rule. Authority: `track`.

**Omission sweep** — The "conspicuously absent" provocation probe: generate freshly, from the model's own domain knowledge and never from a fixed checklist, what a thorough expert treatment of this kind of problem would include, then flag what is missing from what was given. Distinct from the counter-sweep (below). Authority: provocation page; Architecture §5.2.

**Power-problem line** — The rule that where verified evidence shows the outcome is being determined by power rather than merits, the deliverable says so plainly ("this is a power problem, not an analysis problem") and downgrades options premised on accommodation the powerful party has no need to grant. Authority: `analyse` Step 9 item 2; README.

**Proportionality triage** — The fail-safe pre-flight check (Step 1): run the full method unless the problem is unambiguously trivial on every listed count; only then give a short, proportionate answer, say so, and invite the full pass. Depth is the default; down-scoping is the rare exception, because wrongly down-scoping a problem that only looks routine costs more than mild over-analysis. Authority: `analyse` Step 1; Architecture §5.9.

**Provisional stance** — The form the call takes on a wicked problem: it states which value it trades against which, marks itself re-openable, names what would re-open it, and offers a hand-off to `track`. A firm verdict on a wicked problem reintroduces false closure. Authority: `analyse` Step 9 item 3(a); Architecture §5.8 (the wicked-call guard).

**Provocation page** — The fixed one-page analytical method (currently v1.1) applied verbatim on every run: two always-on moves (displacement / second-order; provenance / verification) plus the candidate probes and a closing discipline (steelman, name every affected party, prefer the material set over length). It is the 234-framework SAF corpus distilled to one page, revised only under the page-revision governance rule. Authority: `skills/analyse/references/provocation-page.md`; Architecture §5.2.

**Rung** — A position on the independence ladder (A–D). One meaning corpus-wide; "declare the rung" means state which adjudicator was actually used. Authority: `adjudicate` §5; Guide §11.

**Scoping** — Step 2: up to five optional, skippable questions in the TOSCA problem-framing shape — the trouble and why now; the owner and audience; success criteria and stakes; constraints and scope; party-held material. If skipped, the engine writes its own one-line problem statement (trouble, owner, core question) marked as an assumption. Authority: `analyse` Step 2; Foundations §2.

**Systems-investigation pass** — Step 5, conditional: for genuinely systemic problems only (two or more of: feedback, accumulation, material delays, multiple interacting actors, possible regime shift, self-fulfilling expectations), a graded causal map — variables, signed links, loops graded exists versus dominates-now, tipping conditions, ranked leverage points — built as a hypothesis to be falsified. It investigates structure; it never simulates, forecasts, or computes outcomes. Section 3 carries its vocabulary. Authority: `analyse` Step 5; Architecture §5.3.1.

**Three-bucket evidence router** — The Step 4 sort applied to every load-bearing claim: web-verifiable (search, then grade and tier); party-held (name the settling document; cap dependents); irreducibly open (route to the human unmarked). Authority: `analyse` Step 4; `verify`; Architecture §5.3.

**Verification** — The L2 layer: the router, source-strength tiering, the disconfirmation pass, and the coverage-retention re-scan, turning "the model believes X" into "X is corroborated by a cited source of stated strength, has survived a search for its own counter-evidence, or it is not". The `verify` skill is this layer standalone. Authority: `verify`; Architecture §5.3.

**Watch-list** — In a dossier, the facts, documents, or events that would change the call; updates are checked against it. Each trigger must be diagnostic — it must discriminate between the call holding and flipping; a trigger consistent with every outcome is noise and is dropped. Authority: `track` Mode 1.

**What to verify first** — Decision-brief item (d): the cheapest next step that most reduces risk. Meaningful for `[U]` situations one to four; empty for the fifth. Authority: `analyse` Step 9; Architecture §4.

**What would flip the call** — Decision-brief item (e): the named conditions under which the call reverses, including jointly-moved assumptions the resilience check found fatal and any tipping conditions from the systems pass, each phrased as a first-person conditional. Authority: `analyse` Step 9 item 3(e).

**Wicked problem** — A problem with no definitive formulation, no stopping rule, and no true-or-false answers (Rittel and Webber, 1973), where the deep core dominates and there is no verifiable solution. Wicked problems are navigated, not solved; the call on one is a provisional stance. Authority: Foundations §2; Architecture §1; Guide §11.

### Engine-and-record entries

**Adversarial pass** — The second adjudication pass: the adjudicator tries to break the load-bearing claims and the call, after the blind pass. Authority: `adjudicate` §4.

**Blind pass** — The first adjudication pass: a separate model, handed the facts and the grade-locked spine but not the call, the first model's reasoning or the operator's gate positions, re-derives the analysis to see whether it reaches the same call. Blind **by construction** — the withheld material is absent from the package sent, so blindness does not rest on the model's compliance. Authority: `adjudicate` §4; Architecture §5.12.

**Checked-and-held** — A `track` update-log result recording that a claim was re-verified and its grade did not change: **HELD-FIRM** (nothing found bearing on the grade) or **HELD-ERODED** (a cited new observation was found that is insufficient to change the grade; two HELD-ERODED entries on one claim force a full re-grade review). Every entry names what was searched and what would have counted as disconfirmation. Authority: `track` Update log and Mode 2.

**Counter-sweep** — The name for the coverage-retention re-scan (above). It is **not** the omission sweep, which is a Step 3 provocation probe: the omission sweep finds what the given material never contained; the counter-sweep recovers what the analysis itself deprioritised while concentrating on the load-bearing few. Authority: `analyse` Step 9; `verify`; Architecture §5.3.

**Decision surface** — The property that the brief presents only what a decision needs, with each element present only where needed. Protected §5.1 term; literal content: a deliberately small set of decision-relevant statements. Authority: `analyse` Step 9 item 3.

**Deep-core routing** — Step 6: separating those questions into the OPEN list without resolving, dropping, or asserting them. Items routed there that are empirical rather than evaluative (a forecast, which loop dominates, regime, timing) are labelled as revisable judgements the evidence cannot settle *yet* — the judgement is revisable; the permanent-set `[U]` grade is not. Authority: `analyse` Step 6.

**Displacement / second-order** — The first always-on provocation move: for every apparent gain, ask where the cost went — onto an unmeasured node, an absent party, or the future. Authority: provocation page. Reader-tier readers meet its results as findings, not the move name.

**Divergence Ledger** — In `render`'s comparative mode, the per-spine-node table recording each audience panel's frame and the divergence type, which must be register, scope, or framing only — never a changed fact or grade. Authority: `render` Modes. See Section 7, "ledger".

**Dossier — see "Living dossier"**

**Elicitation contract** — The defined set of points where the engine stops and asks the operator: the triage's short-answer offer, Step 2 scoping, the Step 8 gate, the Step 10 adjudication offer, the render audience prompt, and `track`'s OPEN / UPDATE / STATUS modes. Everything else is generated without asking. Authority: Architecture §7.

**Fidelity self-check** — `render`'s hard closing check that each render's claim and grade set is identical to the spine and the caveat core is present; on drift it re-renders once, then stops and reports. Authority: `render`.

**Fold under grade-lock** — What happens to adjudication discrepancies: a factual challenge triggers a logged re-verification; a value challenge re-opens one deep-core item at the gate; an irreducible one becomes a caveat. The adjudicator never flips the call. Authority: `adjudicate` §4; Architecture §5.12.

**Hedge discipline** — The rule that every hedge in the brief must bind to a named grade, flip condition, gate position, or re-opener, and stacked hedges must reference the same named conditions; a hedge that names nothing is banned. Authority: `analyse` Step 9 item 3(e).

**Living workspace** — The L6 layer: the investigation that accumulates across sessions through `track`'s three modes — OPEN (start, ask what to track), UPDATE (ask what arrived, re-verify, re-grade explicitly), STATUS (read back without re-verifying). Authority: `track`; Architecture §5.11.

**Necessity gate** — `adjudicate`'s pre-offer check G0–G4: G0 a completed analysis exists; G1 high-stakes or wicked; G2 confidentiality (cross-lab blocked by default for privileged matters, operator-overridable and logged); G3 a live contestable judgment remains; G4 in-boundary sufficiency. The result is declared either way. Authority: `adjudicate` §1. See Section 7, "gate".

**Page-revision governance** — The rule that the provocation page is fixed per version, not fixed forever: it changes only on evidence from real runs, through an A/B gate, with a version bump, and is verbatim within a version. Authority: Architecture §5.2 (P3, 2026-07-02).

**Probes (candidate)** — The provocation page's per-problem probe set, each kept where it fires: absent voice; cui bono from the framing; base rate and measurement; normalised-as-natural; spuriously present; conspicuously absent (the omission sweep); reflexive. Authority: provocation page v1.1.

**Provocation pass** — Step 3: applying the provocation page, treating the fluent first reading as the baseline a competent reader already has, not the finding. Authority: `analyse` Step 3.

**Robustness Map** — In `render`'s comparative mode, the tag table marking each spine node hardened, contested, or narrator-only. It is not a causal map. Authority: `render` Modes.

**Steelman** — To state the strongest version of the opposing reading and keep only findings that survive it. Cited-literature term, protected. Authority: provocation page; `render` (the adversarial render steelmans the opposing interest).

**Streetlight effect** — The tested finding that decision-makers attend to the verifiable items and leave the value questions untouched even when those are displayed and called mandatory; the reason the gate is forced. Cited-literature term. Authority: Architecture §§5.6, 8 (T-L2-005/006).

**Wicked-call guard** — The rule implementing the provisional stance (above). Authority: `analyse` Step 9 item 3(a); Architecture §5.8.

### Section 2 supplement — adjudication operations (alphabetical)

Every entry in this supplement serves the engine and record tier; the one reader-tier adjudication term, **rung**, is listed under the reader-tier entries above.

**Cross-lab** — Rung A: adjudication by a frontier model from a different lab (different training lineage), chosen by the `crosslab_provider` setting; the strongest rung because a different lineage gives the most decorrelated blind spots. A Claude/Anthropic-lineage target on rung A is refused by the same-lineage guard. Authority: `adjudicate` §§5–6; Architecture §5.12.

**Decorrelation** — The degree to which the adjudicator's systematic blind spots differ from the analysing model's. The ladder is ordered by decorrelation, not capability. Authority: `adjudicate`; Architecture §5.12.

**Egress / egress mode** — Whether and what analysis content leaves the local boundary for a cross-lab call: redacted (default — spine plus contested claims), full brief, or ask-per-run. Raw source documents are never sent at any value. Authority: `adjudicate` §6.

**Noise filter** — The framing rule for repeat adjudication runs: they answer "does this verdict reproduce?", never "is this verdict more likely correct?". Protected §5.1 term. Authority: `adjudicate` §5 (panel sizing).

**Outbound-package preview** — The confirm / edit / cancel display of the exact package before anything leaves for a cross-lab counterparty. There are two, because adjudication is two dispatches: the pass-1 package (grade-locked spine and contested claims, and not the call) and the pass-2 package (the adjudicator's own pass-1 verdict and the draft brief). Raw source documents are sent in neither. Authority: `adjudicate` §6.

**Real-use monitor (RUM)** — The accruing observational log of adjudication runs (`monitor/ledger.jsonl` plus `monitor.py`), answering whether a second pass ever catches a decision-relevant error or flips a call in real use, with a frozen coding rule and per-class retirement recommendations. Authority: `skills/adjudicate/monitor/README.md`; `adjudicate` §7.

**Same-lineage guard** — The hard refusal (`[same-lineage]`) of any Anthropic-lineage model as a rung-A target: a same-lineage check is not cross-lab; rungs B and C are the honest same-lineage path. Authority: `adjudicate` §§5–6; Architecture v0.1.18 row.

**Standing versus per-run** — The two scopes of every adjudication setting: a per-run choice applies once and never writes the preferences file; a standing change persists via `prefs.py set` and, where it removes an ask or widens egress, requires an explicit confirm. Authority: `adjudicate` §2.

---

## Section 3 — Systems-map vocabulary

### Reader-tier entries

**Archetype** — A named recurring feedback structure from the systems literature (Shifting the Burden, Limits to Growth, Escalation, Fixes that Fail, and the rest of the standard catalogue). The shipped engine — at v0.1.21, and unchanged at v0.1.22 — has no archetype vocabulary and named none in 7 of 7 runs across two cases; T-ARCH-001 showed a two-sentence slot moves naming from 0 of 5 to 5 of 5. A designed rule, not shipped in any release to date: an archetype name in a deliverable is a claim, asserted only in the reserved form `Archetype: <name>` and graded; element names never use archetype-catalogue names descriptively; mechanism prose (for example "escalation of commitment" as an organisational-behaviour citation) is not covered. Authority: PR-HZN-001 RESULT §3.3; T-ARCH-001 RESULT; Notation Scheme Decision §4.5 (designed, not shipped).

**Balancing loop (B)** — A feedback loop that counteracts change: an odd number of negative links around the cycle. Class letter B, fixed by the specification; numbered `LoopB1`… since v0.1.22 (run-invented at v0.1.21). Authority: `analyse` Step 5.

**Causal map** — The Step 5 artefact: a graded hypothesis about structure — variables, signed links, loops, tipping conditions, leverage points — not a simulation and not a forecast. It is part of the grade-locked spine. Authority: `analyse` Step 5; Architecture §5.3.1.

**Delay** — A material lag between cause and effect on a link, flagged in the link notation. A delay means no symptom appears until the delayed effect arrives — harm can accumulate before any indicator shows it. Authority: `analyse` Step 5.

**Dominates-now** — The second of a loop's two grades: whether the loop currently drives the system's behaviour. Capped at `[U]` permanently (the permanent set); evidence bearing on dominance is graded where it is checkable and travels with the routed question. Authority: `analyse` Step 5; the legend.

**Emergence** — Behaviour that arises from the interaction of parts and is in no single part — especially self-fulfilling expectations, where the shared narrative is itself a causal variable. Authority: `analyse` Step 5.

**Exists** — The first of a loop's two grades: whether the causal chain is real. Existence may be graded up to `[V]`. Every loop is graded twice: exists, and dominates-now. Authority: `analyse` Step 5; Architecture §5.3.1.

**Leverage point** — A place where a small intervention would move the system most — the dominant loop's entry node, a delay, or the driving expectations. Ranked, and graded twice: mechanism and effectiveness. Identifiers: `LevPoint1`… since v0.1.22; at v0.1.21 run-invented (`LP1`… in most runs, `L1`… in one). Authority: `analyse` Step 5.

**Link** — A directed causal connection between two map variables, written `Link1. Node2 --(+/−[, delay])--> Node5` with a grade and a one-line mechanism. The grade attests the mechanism exists in general, not that this arrow is the operative, correctly-directed, un-confounded cause in this case. Identifiers: `Link1`… since v0.1.22; at v0.1.21 run-invented (`L1`… in most runs, bare numerals in one). "Link" also means a hyperlink in one documentation site — see Section 7. Authority: `analyse` Step 5.

**Loop** — A closed causal chain in the map, reinforcing (R) or balancing (B). Under the loop-line rule, every loop line carries either its signs inline or its ordered link identifiers, so its polarity is readable from the line as written. Authority: `analyse` Step 5 (shipped v0.1.22); Notation Scheme Decision §4.4 (the design record).

**Loop cap** — The structural budget of the map: at most 8 variables, 5 loops, 4 tipping conditions, 5 leverage points — a sprawling map is itself false precision. "The cap binds" means more loops close than may be drawn; the run must then name each undrawn loop in one line, marked as ungraded self-report (disclosed truncation, v0.1.19). Distinct from the grade cap — see Section 7, "cap". Authority: `analyse` Step 5.

**Effectiveness (of a leverage point)** — The second grade: whether acting there will actually work. Capped at `[U]` permanently — it is a prediction about an intervention; evidence lifts the mechanism grade, never this one. Authority: `analyse` Step 5; the legend.

**Mechanism (of a leverage point)** — The first of a leverage point's two grades: why the point is structurally high-leverage. May be graded on evidence. Authority: `analyse` Step 5.

**Node** — A position in the causal map holding a variable. At v0.1.21 the specification fixed no node identifiers and runs invented their own (`V1`–`V8` in 8 of 15 retained runs, `S#` in 3, `N#` in 3, bare letters in 1 — 11 of 15 colliding with a grade symbol). Since v0.1.22 the specification fixes one series `Node1`–`Node8`, with the quantity rule (below). Authority: `analyse` Step 5; Notation Collision Fix Design §0–§1; Notation Scheme Decision §3.1.

**Polarity** — The sign of a link: `+` (an increase in A produces an increase in B) or `−` (an increase in A produces a decrease in B); also, of a loop, the reinforcing-or-balancing class its signs produce. A known failure is the sign-flip on decreasing language ("the less X, the less Y"), which the specification requires re-checking. Authority: `analyse` Step 5.

**Regime shift** — A transition of the system into a qualitatively different behaviour pattern. Candidate shifts are named as tipping conditions to watch, never predicted. Whether or when the system tips is in the permanent set. Authority: `analyse` Step 5.

**Reinforcing loop (R)** — A feedback loop that amplifies change: an even number (including zero) of negative links around the cycle. Class letter R, fixed; numbered `LoopR1`… since v0.1.22 (run-invented at v0.1.21). Authority: `analyse` Step 5.

**Reversibility** — The flag on each tipping condition: reversible / hard / irreversible — how recoverable the regime shift would be. Authority: `analyse` Step 5.

**Self-fulfilling expectations** — The emergence case where the shared narrative about the system is itself a causal variable driving the outcome it describes. One of the six systemic signs in the Step 5 trigger. Authority: `analyse` Step 5.

**Stock** — An accumulator: a variable that builds up or drains over time (marked as a stock in the variables list). Accumulation is one of the six systemic signs. Authority: `analyse` Step 5.

**Tipping condition / tipping point** — A candidate regime-shift threshold, stated as a condition to watch — never a date or a probability — with a reversibility flag and a grade (`[U]` unless a specific threshold is evidenced). Identifiers: `TipCond1`… since v0.1.22; at v0.1.21 run-invented (`T1`…). Authority: `analyse` Step 5.

**Variable** — The quantity a node holds; in practice "node" and "variable" are used interchangeably, and the shipped v0.1.22 scheme makes them one series by rule (a node that is not a variable has no licensed role). Authority: `analyse` Step 5; Notation Scheme Decision §3.1.

**Weaker promise** — The disclosed difference in what a tier means on a map link: `[V1]`/`[V2]`/`[V3]` on a link grade the support for that mechanism in general, not that this arrow is the operative cause in this case. Stated in Step 5 and, since v0.1.20, in the reader-facing legend. Authority: `analyse` Step 5; Architecture §4; Guide §7.

### Engine-and-record entries

**Boundary disclosure** — The one-line statement of whose problem-framing the map adopts, who is materially affected but absent from its sources, and what was placed outside its boundary — flagged as a value judgement, distinct from `[U]` evidential uncertainty. Authority: `analyse` Step 5 (v0.1.13).

**Flow** — A rate that fills or drains a stock. Observed as a node-typing annotation in run output (one run typed nodes S/F); the specification names stocks explicitly and flows by implication. Authority: `analyse` Step 5; run practice per the notation design documents.

**Loop parity** — The arithmetic consistency between a loop's declared class and its links: a reinforcing loop requires an even number of negative links (including zero); a balancing loop an odd number. Direction-independent. A parity error is a mechanical defect in the map. Authority: PR-HZN-001 RESULT §3.1 (the registered scoring rule); M-PARITY-001.

**Missing driver** — The closing omission check of the map: one line naming the most plausible driver *not* in the map that would change the call if it were real — the counter to omission, which no check on the drawn arrows can catch. Authority: `analyse` Step 5 (v0.1.12).

**Quantity rule** — The rule stating what the specification previously left implicit: every node is a quantity — something that can rise or fall. A state or condition enters as its level or degree; what cannot be put on an ordered scale is not a node and is carried as a finding or an assumption. Authority: `analyse` Step 5 (shipped v0.1.22); Notation Scheme Decision §3.1 (the design record).

**Topology (of a loop)** — Whether a loop's chain uses links the map actually declares — checked by matching the chain's node tokens to the link table. A topology error is a loop built from undeclared edges. Authority: PR-HZN-001 RESULT §3.1; Notation Words-vs-Identifiers Design §2.

**Variables table** — The short table at the head of the map pairing each node identifier with a short name. Present in run practice before v0.1.22; required by the specification since v0.1.22. Authority: `analyse` Step 5 (shipped v0.1.22); Notation Scheme Decision §5, Edit 2 (the design record).

---

## Section 4 — Identifier series and fixed symbols

This section serves the engine and test-record audience. A brief reader needs only the grade symbols (Section 1) and the layer note below.

### 4.1 Symbols fixed by the specification (SPEC — identical in every run)

| Symbol | Meaning | Authority |
|---|---|---|
| `[V]` / `[U]`, `[V1]`–`[V3]` | Grades and tiers (Section 1) | Legend; `verify`; Architecture §4 |
| The five `[U]` situations | Ordinal series carried in words, never numbered identifiers | Legend; `track` |
| `Link1. Node2 --(+/−[, delay])--> Node5` | The causal-link template (since v0.1.22; the v0.1.21 template's bare letters `A`/`B` were adopted literally as node names by one run) | `analyse` Step 5 |
| `R` / `B` | Loop classes: reinforcing / balancing | `analyse` Step 5 |
| **`L0`–`L6` (and L2.5)** | **Architecture layer tags**: L0 the model, L1 the provocation page, L2 verification, L2.5 the systems pass, L3 deep-core routing, L4 assembly, L5 rendering, L6 the workspace. **They are not link identifiers.** They print inside deliverables through the step headings ("Step 3 — The provocation pass (L0 + L1)"), which is why the v0.1.21 run practice of `L1`-numbered links collided with them — the first-ranked collision the shipped v0.1.22 scheme removes. | Architecture §3; Notation Scheme Decision §1 |
| Steps 1–12 | The `analyse` pipeline step numbers (consecutive since v0.1.16) | `analyse`; Architecture §6 |
| (a)–(e) | Decision-brief items | `analyse` Step 9 |
| Rungs A–D | Independence-ladder positions | `adjudicate` §5 |
| M, N, R | Adjudication panel-sizing count variables (cross-lab breadth, Opus panel size, runs-per-model) — prose variables, never numbered identifiers | `adjudicate` §5 |
| G0–G4 | The adjudication necessity-gate items | `adjudicate` §1 |
| OPEN / UPDATE / STATUS | `track` modes | `track` |
| FIXED / SLOW / VOLATILE | `track` volatility classes | `track` |
| HELD-FIRM / HELD-ERODED | Checked-and-held results | `track` |
| hardened / contested / narrator-only | Robustness Map tags | `render` |
| responded / contested / not offered the opportunity | Party-response marker on adverse findings | `analyse` Step 9 item 2 |
| reversible / hard / irreversible | Tipping-condition reversibility flags | `analyse` Step 5 |
| `CROSSLAB-BLOCKED [tag]` / `CROSSLAB-FAILED [tag]` | Harness status tags, matched by line-contains | `adjudicate` §6 |
| `[same-lineage]`, `[assumption — not stated]` and similar bracketed marks | Status and assumption marks sharing the square-bracket channel with grades; contents are disjoint, but brackets are not an exclusive grade channel | `adjudicate` §6; `analyse` Step 2; Notation Collision Fix Design §1.1 |
| real-catch-flipped · real-catch-refined · useful-not-decision-relevant · false-alarm · nothing | The monitor's frozen verdict codes | `monitor/README.md` |
| The 19 settings keys (`offer`, `crosslab`, `default_rung`, …) | Adjudication preference keys, schema v3 | `adjudicate` §2; `prefs/README.md` |

### 4.2 Run-numbered series — the shipped scheme, and the practice it replaced

Before v0.1.22 the specification was silent on every series below and each run invented its own forms. Since v0.1.22 the specification fixes one word-stem-plus-number series per register: a capitalised mixed-case stem followed by a number.

| Series (meaning) | Forms observed before v0.1.22 | Identifier since v0.1.22 |
|---|---|---|
| Map variables (each a quantity; ≤8; stocks marked) | `V1`–`V8` (8 of 15 runs), `S1`–`S8` (3), `N1`–`N8` (3), bare `A`–`H` (1) | `Node1`…`Node8` |
| Causal links, in the order drawn | `L1`… (12+ runs), bare numerals (1) | `Link1`… |
| Reinforcing / balancing loops | `R1`…, `B1`… | `LoopR1`…, `LoopB1`… |
| Tipping conditions | `T1`–`T4` | `TipCond1`… |
| Leverage points | `LP1`–`LP5` (most runs); `L1`, `L2` in one run | `LevPoint1`… |
| The Step 4 verification register (claims, any grade) | `C1`–`C25` | `ClaimReg1`… |
| Disconfirmation records | `D1`–`D5` (in at least one run `D` also numbered a displacement finding) | `Disconf1`… |
| Findings | `F1`–`F9` | `Find1`… |
| Party-held items | `P1`–`P6` | `PartyHeld1`… |
| Gate exchanges | `G0a`, `G0b`, `G1`–`G5` in some runs; `Q1`–`Q5` in others | `GateQ1`… (digits only; the numbering runs on) |
| Resilience-check assumptions | `A1`–`A4` | `Assump1`… |
| Deep-core open questions | `O1`–`O5` | `OpenQ1`… |

**The stems were fixed on 25 August 2026; five differ from those first proposed — `TipCond1`, `LevPoint1`, `ClaimReg1`, `Disconf1`, `Assump1`.** Authority for the final set is the identifier rule in `skills/analyse/SKILL.md`; the fixing decision is recorded in `2026-08-25-v0.1.22-Identifier-Set-LOCKED.md` in the project record.

**The reservation clause:** identifiers are a capitalised mixed-case stem followed by a number — never all capitals, never a bare letter, never a new series, and never `V` or `N`, which are grade symbols, not identifiers; identifiers come only from the listed stems. Authority: the identifier rule in `skills/analyse/SKILL.md` (shipped v0.1.22); design record: Notation Collision Fix Design §1.2 and §2; Notation Scheme Decision §4.

### 4.3 Test-record series (document-internal, defined per document)

The record's documents number their own items with short letter series, each introduced under a heading in its own document and never carried across documents: `P1`… and `Q1`… (pre-registered predictions), `C1`… (pass criteria), `K1`… (key case facts), `E1`… (expected structural elements), `L1`… (limitations — a further, document-internal use of the letter L), `R1`… (rulings in ADJ-001), `S1`–`S5` and `T1-x`/`T2-x` (review-item and tranche series in the optimisation and reconciliation documents), `G-…` (named gates in workspace registers). These are legitimate because each is defined where it is used, but the letters overlap the run series and the layer tags, so no cross-document reading of a bare letter-digit token is safe in the v0.1.21 corpus — the general problem the v0.1.22 shape rule addresses for future deliverables.

---

## Section 5 — Test-programme vocabulary

This section serves the engine and test-record audience; none of it appears in a decision brief.

**Anchoring** — Adopting a prior answer's framing or conclusion because it was seen, rather than deriving one independently. The blind adjudication pass exists to prevent it: the adjudicator is never handed the first model's reasoning. Authority: `adjudicate` §4; ADJ-006 §5.1.

**Arm** — One condition of a controlled comparison: the set of runs sharing one configuration (Arm A against Arm B). Distinct from a rung (ladder position) and from an archetype's structural branch — see Section 7. Authority: test record throughout; ADJ-006 §5.1.

**Bait / lift-bait / forecast-baiting** — A test input deliberately constructed to invite a specific violation: lift-bait invites lifting a permanently capped grade (T-SM-005); forecast-baiting invites a manufactured forecast (the T-SM safety gate). The noun names the test class and is protected; surrounding verbs are ordinary prose. Authority: T-SM-005; Architecture §8; ADJ-006 §§5.1, 5.3.

**Blind** — Performed without access to the material that could bias the result: blind subjects and raters score without knowing which arm produced a document; a blind adjudicator re-derives without the first model's reasoning. Authority: Architecture §8; `adjudicate` §4.

**Ceiling effect / tied at the ceiling** — A scoring outcome where both arms reach the maximum a measure can register, so the measure cannot separate them. Authority: Architecture §9.1 (T-ICD-001); ADJ-006 §5.1.

**Conformance run** — A run checking that shipped behaviour matches the specification's stated contract (legend present, permanent set held, sources cited), as distinct from a test of whether a feature adds value. PR-HZN-001 is a conformance run. Authority: PR-HZN-001 pre-registration §0.

**Control** — The comparison condition a treatment is measured against — a baseline arm, sometimes discipline-stripped. See Section 7 for the word's other senses. Authority: Architecture §8; T-FAB-001.

**Dispatch prompt** — The prompt actually sent to a run's isolated agent, which may carry test-only clauses that are not in the shipped skill (T-ARCH-001's two-sentence slot lives there). What is tested is the clause at that position, not the specification. Authority: T-ARCH-001 RESULT §6.

**Existence proof** — A single observed instance establishing that something is possible, claiming nothing about its rate. Authority: T-PIPE-001 as cited in the Grade-Transport Drop-in Edits; ADJ-001 R6; ADJ-006 §5.1.

**Fisher exact** — Fisher's exact test: the significance test used on small two-arm count tables (0/5 against 5/5 gives p ≈ 0.008 two-sided). Authority: T-ARCH-001 RESULT; ADJ-001 R6.

**Gate (test sense)** — A pass/fail requirement a feature must clear before shipping: a benefit gate (beats a strong baseline), a safety gate (no manufactured confidence under bait), a proportionality gate (does not fire where it should not), the page-revision A/B gate. "Wording/discipline class, no gate" means a release the engine's rules exempt from a benefit gate. Distinct from the Step 8 judgement gate and the adjudication necessity gate — see Section 7. Authority: Architecture §§5.2, 8; version table.

**Gold key** — The answer set fixed in advance of a test, against which output is scored. Authority: Architecture §8.

**Isolated agents** — Separate model instances with no shared context, one per run, so runs cannot influence each other. Authority: PR-HZN-001 RESULT §1; T-ARCH-001 RESULT §1.

**n** — The number of runs (or instances) per arm or condition; "n=5 per arm" and "achieved n" are stated so that no claim exceeds what the count supports. Authority: test record throughout; ADJ-001 R6.

**Noise** — Run-to-run variation in output under identical conditions. Authority: T-VAR-001; ADJ-006 §5.1.

**Noise floor** — The measured level of run-to-run variation below which an effect cannot be distinguished from noise; an effect claimed from one run per arm is only safe if it exceeds this floor. Authority: T-VAR-001 pre-registration and result.

**Null** — A result finding no effect: the tested addition did not beat the baseline. The programme's convergent meta-finding is a repeatedly replicated null on analytical prompt-moves. Also used of an observed zero rate ("the 0-of-7 archetype null"). Authority: Architecture §§2, 8; T-ARCH-001 RESULT.

**Power / powered** — The ability of a test design to detect an effect of a given size if it exists; an underpowered comparison (for example 4/5 against 1/5, p ≈ 0.21) settles nothing. Authority: ADJ-001 R6; ADJ-006 §5.1.

**Pre-registration** — The document fixing a test's measures, pass and fail criteria, predictions, and limitations before any run is dispatched, so results cannot be selected after the fact. Deviations are registered before dispatch or recorded as deviations. Authority: the `*-PREREGISTRATION` / `Pre-Registration` documents; Architecture §8.

**Prediction (test sense)** — A registered, scoreable expectation about a test's own output (P1…, Q1…), scored met / not met after the run. Not the world-forecast sense the method refuses — see Section 7. Authority: PR-HZN-001 §5; T-ARCH-001 §2.

**Rater** — An instance (LLM in all tests to date) scoring output against a rubric, blind to condition, at least three per test where merit is judged. Authority: Architecture §§8, 10.

**Replication** — Re-running a test or measurement to see whether its result reproduces; a finding that does not survive replication is withdrawn. Authority: Architecture §8; T-PAR-002/002R.

**Retained** — Kept on disk in re-scorable form (deliverables, maps, prompts, extractions), so anyone can recompute the figures. The opposite failure — describing artefacts in place of keeping them — made the 23 August AMA run permanently unusable. Authority: PR-HZN-001 RESULT §1; ADJ-002.

**Rule of three** — The statistical convention that zero observed events in n independent trials bounds the true rate at roughly 3/n with 95% confidence; used to state what a clean record does and does not establish. Authority: ADJ-006 §5.1 (protected); the record's zero-event readings.

**Shipped configuration** — The engine exactly as released and installed (the packaged skills, unmodified), as opposed to a test-harness or dispatch-prompt configuration. The 119-loop parity record was accumulated under the harness format, not the shipped configuration's output format — the distinction that made this term necessary. Authority: PR-HZN-001 RESULT §§3.2, 9.

**Smoke test** — A minimal, cheap run checking that a mechanism operates at all (the v0.1.19 grade-transport smoke; the cross-lab preflight `--live` smoke), not a measure of benefit. Authority: Architecture version table (v0.1.19); `adjudicate` §6; SMOKE-0119.

**Unassessable** — The status of a registered measure that the design as actually run cannot answer; recorded as unassessable rather than scored (T-ARCH-001's Q3). Authority: T-ARCH-001 RESULT §4.

**Void** — The status of a registered prediction whose measurement carries no information about what it was written to measure, through a defect in the pre-registration itself. Authority: T-ARCH-001 RESULT §§2, 4.

**Withdrawn** — The status of a previously asserted figure or claim that the record no longer stands behind; the assertion stays in place as history, under a dated correction banner, and is never silently edited. Authority: ADJ-001 banner; ADJ-002; ADJ-006 tranche 1.

---

## Section 6 — Abbreviations

Scope note: this section covers abbreviations that recur across the corpus. **One-off case-specific acronyms from a single analysis are deliberately excluded** — the Post Office Horizon material alone contributed 49 distinct all-caps acronym types (CCRC, NFSP, JFSA, UKGI, EWCA and the rest), which belong to their case documents, are expanded there, and are not corpus vocabulary. The measured consequence stands recorded: bare 4–5-letter all-caps tokens are acronym-shaped in this corpus, which is one reason the shipped identifier scheme uses mixed-case stems.

**ADJ-** — Document-id prefix: an adjudication document in the workspace record (ADJ-001 to ADJ-006), a Fable 5 audit or reconciliation of the engine, docs, or record.
**AMA** — Aha! Mystery Architecture: a Gemini-backed, dialogue-driven investigative mapping application used as a reference point in the 23–24 August comparisons. Not an engine component, and not an A/B arm (it is dialogue-driven, so its output partly reflects the analyst).
**API** — Application programming interface; in this corpus, the paid cross-lab call path and the AMA replication path.
**ASF** — Analytical Series of Frameworks: the earlier name of the SAF; survives in workspace folder and memory names.
**ContTest** — Readable name for the controlled-test class, written `T-<FAMILY>-<nnn>` in file names and citations, usually as a PREREGISTRATION / RESULT pair. 71 files on disk carry the `T-` form; `ContTest` is the reading name only. Family codes in the record: AB (version A/B comparisons), SM (systems map), L2 (deep-core attention, the streetlight tests), IM (incident mode), ICD (ICD-203 alignment), FMT (output format), PAR (loop parity), VAR (run variance), CAP (the loop cap), FAB (fabricated case), FRAME (framing capture), PIPE (pipeline grade transport), ARCH (archetype slot).
**HZN** — Case slug for the Post Office Horizon case in document ids (PR-HZN-001, the frozen case text, the run files). Case slugs name the case, not a method concept.
**ICD 203** — Intelligence Community Directive 203, *Analytic Standards* (ODNI, 2015 as amended): the analytic tradecraft standard the engine's grading vocabulary is deliberately aligned with. The engine is architected around its epistemic core; it is not "ICD-203 certified", and the Architecture states that bound explicitly.
**IE** — The Insight Engine (`insight-engine`, the plugin and repo).
**IIE** — Investment Insight Engine: the domain edition of the Insight Engine for investment analysis. A separate workspace project, not part of this repo.
**JSON / JSONL** — JavaScript Object Notation (and its line-delimited form): the AMA map format and the monitor ledger format (`ledger.jsonl`).
**K_MIN** — The monitor's read-out threshold: the number of real high-stakes runs (20) required before the frozen decision rule reads out.
**LLM** — Large language model.
**LoopPM** — Readable name for the measurement-document class, written `M-` in file names and citations (`M-PARITY-001`, the loop-parity measurement). A measurement of existing output, not a controlled test. The three files on disk carry the `M-` form; `LoopPM` is the reading name only. Note: `M-` names the class *measurement*, and the only instance so far is a loop-parity measurement — a measurement of something other than loops would not fit the name `LoopPM`.
**MIT** — The MIT licence, under which the repo is released.
**OCIR** — Operational Continuity in Resolution, the UK banking-regulation regime the OCIR case concerns. Case-specific; listed only because it appears in a document id.
**ODNI** — Office of the Director of National Intelligence, the issuer of ICD 203.
**PreReg** — Readable name for the pre-registered-run class, written `PR-` in file names and citations. A run registered before dispatch that is not a controlled test — a conformance or reference-point run (`PR-HZN-001` has a Pre-Registration and a RESULT under the same id). The two files on disk carry the `PR-` form; `PreReg` is the reading name only.
**RUM** — Real-Use Monitor (Section 2 supplement).
**SAF** — Series of Analytical Frameworks: the frozen 234-framework predecessor corpus, retired after apparatus-versus-bare testing; its tested content survives as the provocation page.
**SMOKE-** — Document-id prefix: a smoke-test result (SMOKE-0119, the grade-transport smoke).
**The five skill names** — `analyse`, `verify`, `render`, `track`, `adjudicate`: not abbreviations, but the fixed command vocabulary; each also names its layer (L2, L5, L6, and the Step 10 adjudication layer; `analyse` orchestrates all of them). Note: "track" the skill is distinct from "track-record" in "not a track-record calibration".
**TOSCA** — Trouble, Owner, Success criteria, Constraints, Actors: the problem-framing frame behind Step 2 scoping (*Cracked It!*, Garrette, Phelps and Sibony; the Actors element adapted into the party-held question).

---


## Section 7 — Terms currently carrying two or more meanings

This is the audit the glossary exists for: the word-level counterpart of the identifier collisions. Each entry states the meanings, the sites, whether context separates them reliably, and a recommendation — keep both, qualify, rename one, or reserve the word. Serves the engine and test-record audience. Verbatim run output, retained artefact bodies, and frozen titles are exempt from every recommendation below (the ADJ-006 §3 standing exemption): they are data and are never edited.

**1. cap** — *Two mechanisms, one word.* (a) The structural budget of the systems pass: ≤8 variables, ≤5 loops, ≤4 tipping conditions, ≤5 leverage points; "the cap binds" (`analyse` Step 5; T-CAP-001; PR-HZN-001 "all at the cap"). (b) The grade ceiling: "caps at `[U]`", "inheriting the cap" (situation 4), the permanent-set cap (`analyse` Steps 4–5; the legend; `verify`; `track`). Both senses occur inside `analyse` Step 5, sometimes in adjacent sentences. Context separates them *mostly*: the grade sense almost always carries the symbol ("caps at `[U]`") and the structural sense a number — but bare "the cap" appears in both ("if the cap binds" is structural; "inherits the cap" is grade). **Recommendation: keep both (both are §5.1-protected) and reserve the bare forms.** In new prose: the structural budget is "the loop cap" or "the map caps"; the grade mechanism is "the `[U]` ceiling" or "capped at `[U]`"; bare "the cap binds" is reserved for the loop cap, which is its established Step 5 and T-CAP-001 use. "Inheriting the cap" is fixed legend wording and stays as shipped — flagged, not changed.

**2. gate** — *Four referents.* (a) The forced judgement gate, Step 8 — the operator-owned checkpoint (`analyse`; Guide; Architecture §5.6). (b) The adjudication necessity gate G0–G4, plus the code-backed offer gate (`adjudicate` §1). (c) Test-programme and release gates: benefit gate, safety gate, proportionality gate, the page-revision A/B gate, "no gate required" (Architecture §§5.2, 8; version table). (d) The `GateQ` identifier series for gate exchanges (shipped at v0.1.22). Context separates (a) from (c) by document class, but (a) and (b) co-occur inside `analyse` (Step 8 and Step 10) and inside `adjudicate` (which re-opens items "at the Step-8 judgement gate" while running its own gates). **Recommendation: keep all; reserve the bare form.** Bare "the gate" means the Step 8 forced judgement gate — this is already the corpus's dominant usage and should be stated as a rule. Every other use is qualified: "the necessity gate", "a benefit gate", "the release gate", "the offer gate". `GateQ1` is machine-separable by shape and needs no further rule.

**3. link** — *Causal link against hyperlink.* (a) A causal link in the map (`analyse` Step 5; everywhere in the systems vocabulary). (b) An ordinary hyperlink: at v0.1.21, `docs/Foundations.md` §2 wrote "names its source with a link"; the v0.1.22 release changed it to "with a URL", matching the skills' own wording. One "download link" remains in PUBLISHING.md, where no map is present. The skills themselves say "URL" ("the named source with its URL"), so the collision is confined to the docs. A brief with a systems map contains both causal links and a sources section, so the collision reaches the reader tier. **Recommendation: none outstanding — the rename shipped with v0.1.22.** "Link" is reserved for causal links wherever a document also carries a map. (`Link1`, shipped at v0.1.22, is shape-separated.)

**4. claim** — *Term of art against ordinary word.* (a) The graded proposition — the unit the whole grade vocabulary attaches to (`verify`; the legend). (b) The ordinary noun and verb: "the honest claim" (`adjudicate`), "over-claim", "claiming nothing about rate", "an archetype name is a claim". Grammar and the attached grade separate them reliably; no misreading was found in the corpus. **Recommendation: keep both**, with one discipline for new authorial text: where the ordinary noun could be read as the term of art, prefer "statement" or "assertion" ("the honest statement of the layer's benefit"). The `ClaimReg1` series (shipped at v0.1.22) is shape-separated. Note that "an archetype name is a claim" (designed rule) deliberately *uses* sense (a): it makes the name a graded proposition — that is the point, not a collision.

**5. open** — *Five uses, two of them capitalised.* (a) "Irreducibly open" — the third router bucket (`analyse` Step 4; `verify`). (b) The deep-core OPEN list (`analyse` Step 6). (c) An open question — any routed item (the legend). (d) `track`'s OPEN mode (start a dossier). (e) "Re-open / re-openable / re-opener" — the wicked call's revisability (`analyse` Step 9). The two capitalised forms, (b) and (d), are distinct named things in different skills, and a `track` dossier carries both (its "Open (deep core)" section and its OPEN mode). Context separates for a careful reader; the collision cost falls on scorers and cross-document search. **Recommendation: keep all; qualify the capitals.** In any document carrying both, write "the deep-core OPEN list" and "track's OPEN mode" at first use. The fixed collocations ("irreducibly open", "re-open") need no rule. The `OpenQ1` series (shipped at v0.1.22) gives sense (b)'s items a shape-separable handle.

**6. rung** — *One meaning.* A position on the independence ladder (A–D), including derived uses ("declare the rung", "rung reached", "auto-descend a rung"). Checked against §5.1 and the corpus: no second sense found. **Recommendation: keep; no action.**

**7. arm** — *Test condition against archetype branch.* (a) A condition of a controlled comparison (Arm A / Arm B) — §5.1-protected. (b) A structural branch of an archetype: "the delay on the fundamental arm", "the reinforcing side-effect arm" (T-ARCH-001 RESULT §3, in authorial prose and in quoted run output). Both senses occur in the same document (T-ARCH-001 RESULT names its Arms and discusses archetype arms). Context separates because sense (a) is always capitalised with a letter, but the cost is real in exactly the documents that discuss archetype structure inside arm-labelled tests. **Recommendation: keep (a); prefer "branch" or "side" for (b) in authorial prose.** Quoted run output stays as written.

**8. blind** — *One literal core, three collocations.* (a) The blind adjudication pass and blind subagent; (b) blind subjects and raters in tests; (c) "blind spot" (§5.1-protected cited-literature term). All three mean acting or erring without access to something; no reading of one as another misleads. **Recommendation: keep all; no action.**

**9. null** — *One statistical family.* (a) A no-effect result; (b) an observed zero rate ("the 0-of-7 archetype null"), which T-ARCH-001 showed was a contract effect — the vocabulary was present, the output contract had no slot. Both are the statistical sense; the corpus never uses the logical or database sense. **Recommendation: keep; no action.** One care point: a null read on rung A after lineage monoculture must be read as loss of signal, not safety (Architecture §5.12) — a doctrine note, not a vocabulary problem.

**10. spine** — *One licensed sense; two decorative uses, both removed at v0.1.22.* The licensed sense (§5.1, "grade-locked claim set sense only"; ADJ-006 §5.3 "kept in its one defined sense only"): the grade-locked set of claims, grades, tiers, dominant unknown and caveat core that runs through every layer. Two sites used the word decoratively at v0.1.21 — Architecture §5.3.1 ("the spine of the pass") and Foundations §5 ("the tradecraft spine") — second senses of exactly the kind ADJ-006 §5.3 ruled out. Both were made literal in the v0.1.22 release (Architecture §5.3.1 now reads "what the whole pass rests on"; Foundations no longer uses the phrase). **Recommendation: none outstanding — both renames shipped with v0.1.22.**

**11. load-bearing** — *One meaning, wide application.* An element the conclusion materially rests on — applied to claims, links, loops, assumptions, and grades. §5.1-protected; the literal content is "if this element fails, the conclusion changes". No second sense found. **Recommendation: keep; no action.**

**12. ceiling** — *Three qualified terms, no licensed bare use.* (a) The hard ceiling — the permanent `[U]` cap on dominance, effectiveness and tipping (`analyse` Step 5). (b) The attribution ceiling — the blame rule (`verify`; Architecture §5.3). (c) Ceiling effect / tied at the ceiling — the scoring outcome (Architecture §9.1). Also "the prediction ceiling" (Foundations §2), a restatement of (a). Context separates because the corpus almost always qualifies; bare "the ceiling sentence" appears in the version table where the referent is unambiguous. **Recommendation: keep all three; reserve against bare use** — "the ceiling" alone is never written in new prose; one of the three qualified forms is.

**13. register** — *Claim register against audience register.* (a) The Step 4 verification register — the numbered list of graded claims (`C1`–`C25` at v0.1.21; `ClaimReg1`… since v0.1.22). (b) The linguistic register `render` transforms — tone and framing for a reader ("a register transform only"). A third, workspace-only sense — the SAF tracking register — is outside the engine corpus. Senses (a) and (b) live in different skills and no document was found carrying both ambiguously. **Recommendation: keep both, qualified:** "the claim register" and "audience register" where either could be misread. No rename.

**14. panel** — *Model panel against document panel.* (a) The rung C Opus panel and the multi-lab cross-lab panel — a set of model instances (`adjudicate` §5). (b) `render`'s comparative mode: "a labelled panel per audience" — a document section (`render` Modes). Different skills; an adjudicated multi-audience render is the one plausible co-occurrence. **Recommendation: keep both; qualify as "audience panel" wherever an adjudication document discusses a comparative render.**

**15. ledger** — *Run log against divergence table.* (a) The monitor's `ledger.jsonl` — the adjudication run log (`adjudicate` §§7–8; monitor README). (b) `render`'s Divergence Ledger — the per-node divergence table in comparative mode. Both are proper names. **Recommendation: keep both**; refer to (a) as "the monitor ledger" and (b) always by its full name "Divergence Ledger".

**16. call** — *Recommendation against API invocation.* (a) The call — decision-brief item (a), with its protected derivatives "flip the call", "decision-flip". (b) An API call — "the paid call is operator-initiated", "six API calls" (`adjudicate`; PR-HZN-001). Both occur throughout `adjudicate`, which exists to check calls in sense (a) by making calls in sense (b). Context separates because sense (a) takes "the" and sense (b) takes an article plus a qualifier — and `adjudicate` already writes "the paid call", "an API call". **Recommendation: keep both; always qualify sense (b)** ("the API call", "the paid cross-lab call"); never bare "the call" for an invocation.

**17. retention / retained** — *Three collocations.* (a) The coverage-retention re-scan (L2/L4). (b) Data-retention terms of a cross-lab counterparty (`adjudicate` §6, consent recap). (c) Retained test artefacts (Section 5). Each lives in a fixed collocation and none was found bare. **Recommendation: keep all; never write bare "retention"** — always "coverage-retention", "retention terms", or "retained".

**18. control** — *Test arm, absence of command, and settings.* (a) The control arm of a test (T-FAB-001 Arm B). (b) "Understanding and a defensible next step, not control or prediction" — the purpose statement's ordinary sense. (c) "Operator-controllable settings" (`adjudicate`). Document class separates them; in a test document, unqualified "control" means the control arm. **Recommendation: keep; state the test-document convention; no rename.**

**19. prediction** — *What tests require and deliverables refuse.* (a) In the test programme: a registered, scoreable expectation about a test's own output (P1…, Q1…), fixed before dispatch — mandatory good practice. (b) In the method: a forecast about the world — never graded above `[U]` inside the map's permanent set, routed unmarked outside it; "investigate, don't predict". The same word names an obligation in one document class and a refusal in the other. The classes are disjoint, and no confusion site was found — but the asymmetry is worth a stated rule. **Recommendation: keep both, with the usage rule: a deliverable's content is never described as "predictions"; a pre-registration's registered expectations always are.**

**20. The letter L** — *Four numbering uses across the corpus.* (a) Architecture layers `L0`–`L6`, printed inside deliverables via step headings. (b) Link identifiers `L1`… — v0.1.21 run practice. (c) Leverage points `L1`, `L2` in one retained run. (d) Limitation series `L1`–`L9` in result documents. The first-ranked identifier collision (one recorded false parity error came from a scorer extracting `L`-numbered tokens). **Recommendation: resolved at v0.1.22 for (b) and (c)** — the shipped stems `Link1` and `LevPoint1` remove them from all future deliverables; (a) stays as the layer vocabulary; (d) stays as a document-internal series always introduced under a Limitations heading. In the pre-v0.1.22 record no cross-document reading of a bare `L`+digit token is safe, and scorers must parse per document.

**21. monitor** — *Artefact against verb.* (a) The real-use monitor (RUM) — the ledger, scripts, and read-out rules. (b) The ordinary verb, including "what to monitor" for tipping conditions (Step 5 feed-forward). The noun with "the" and the RUM name separate reliably. **Recommendation: keep; no action.**

**22. verdict** — *Coded outcome against banned closure.* (a) The monitor's frozen verdict codes (real-catch-flipped … nothing). (b) The verdict a wicked call must not be ("a provisional stance, not a verdict"). Disjoint contexts. **Recommendation: keep both; in adjudication prose, "verdict" unqualified means the monitor code.**

**23. Bracketed single-letter markers** — *A recorded defect and its rule.* The first draft of this glossary marked its reader-tier entries with a bracketed single capital letter (the letter R in square brackets). That placed a new bracketed symbol in the square-bracket channel the corpus reserves for grades — the same defect class as the identifier collisions this vocabulary work exists to remove — and the letter R is already the reinforcing-loop class letter (`R1` at v0.1.21, `LoopR1` since v0.1.22). The marker was caught in review and removed before the glossary shipped; the reader tier is now carried by section and subsection structure (see "How to read this glossary"). **The rule this establishes: no document in this corpus introduces a bracketed symbol for anything other than a grade.**

**24. `n` / `N` / `K_MIN` — one count, three symbols.** *Meanings:* all three denote the number of runs in a sample. *Sites:* `monitor.py` line 82 compares them in a single expression — `if ro["n"] < K_MIN:` — lowercase `n` for the observed count against `K_MIN` for the threshold; the monitor README's Honest-limits paragraph then writes "N accrues slowly" with a capital; the test record uses lowercase `n` throughout (`n=5 per arm`, `n=3`, `n ≥ 5`). Neither the code comment nor the README expands the `K`. *Separability:* the reader must already know that `K` is a conventional count symbol and that all three name the same quantity; nothing in the corpus states it. *Recommendation:* **no rename** — operator decision, 24 August 2026, taken on the ground that `K_MIN` is a shipped code identifier and renaming it is a code change rather than a wording change. The equivalence is therefore stated here instead: `n`, `N` and the `K` of `K_MIN` all mean the number of runs, and `K_MIN` is the minimum number of runs before the pre-registered rule reads out. Any future edit to `monitor.py` should prefer `n` for consistency with the test record. **Resolved further, 30 August 2026:** the grade has vacated the letter. Until then `N` carried a reserved count meaning and the unverified grade at the same time, in one corpus — an overlap that produced a shipped defect when a receipt template wrote `(0 positions, N deferred)`, putting `N` in the slot reserved for `d`, where the two coincide only in that one state. With the rename to `[U]`, `N` now means a count and nothing else. The identifier reservation clause is amended accordingly: `V` and `U` are excluded as stems because they are grades, and `N` is excluded on separate grounds, as the reserved count symbol.

**Tally.** 23 terms audited: 2 renames recommended and shipped with v0.1.22 (the hyperlink sense of **link** → "URL"; the two decorative **spine** sites), 1 authorial-preference change (**arm** → "branch" for archetype structure), 7 reservation or qualification rules (**cap**, **gate**, **open**, **ceiling**, **call**, **retention**, plus the test-document conventions for **control** / **prediction** / **verdict**), 1 explicit decision not to rename (**`n` / `N` / `K_MIN`**, operator decision of 24 August 2026 — a shipped code identifier, so the equivalence is stated in the glossary instead), and 12 confirmed safe to keep with context (including **rung**, **blind**, **null**, **load-bearing**, **claim**, **register**, **panel**, **ledger**, **monitor**, and the letter **L**, resolved for future deliverables at v0.1.22). Entry 23 records one resolved defect and the rule it establishes. None of the recommendations touches a grade symbol, the canonical `[U]` wording, or the legend. *(That remains true of the 24 August audit's recommendations. It is not true of the corpus decision of 30 August 2026, which renamed the unverified grade `[N]` → `[U]` and added the two letter expansions to the legend — a change this glossary records rather than proposed.)*

---

## Section 8 — Governance

**Where the glossary lives.** In the repository, as `docs/Glossary.md`, to be linked from the README, from Architecture, and from the Guide (the three link edits were still outstanding at first publication). It landed with the **v0.1.22 release**, not before: it describes the v0.1.22 identifier scheme alongside v0.1.21 usage, and shipping it mid-version would have opened a docs-lead-plugin divergence window of the kind the v0.1.21 version-table row exists to record. Because `docs/` is not packaged into the `.plugin` (the build zips `plugin.json`, README, LICENSE, and `skills/` only), adding it forced no version bump of its own — it was included in the release it was timed for.

**Whether it ships as a public document.** Yes. The repo's docs are public, the glossary contains nothing case-confidential (case-specific acronyms are excluded by scope), and the two-tier design exists precisely so a public reader can use the reader tier. One consequence must be accepted knowingly: a public glossary is a second statement of the grade doctrine, and second statements are the surface on which the ADJ-006 defect class (local paraphrase drifting from the canonical wording) occurred. The mitigation is structural and must be kept: **this glossary quotes the canonical `[U]` block verbatim and is forbidden to restate it**, and any future edit to the legend must update the quotation by copy, never by paraphrase — the ADJ-006 §7 rule ("every surface takes the §1 block or its declared short form verbatim") applies to this document in full.

**Relationship to the fixed plain-language legend.** The legend is the canonical, versioned reader contract; it closes every full-pass deliverable verbatim and its wording changes only with a release, recorded in the Architecture version table. The glossary is a reference *about* the vocabulary; it does not travel with deliverables and therefore **does not replace the legend anywhere** — a deliverable must remain readable alone, so the legend stays. Precedence on any conflict: the shipped legend and Architecture §4 govern; the glossary is corrected to match them, never the reverse. The Guide's §11 glossary should become the reader-tier subset of this document — all of Section 1, plus the reader-tier subsections of Sections 2 and 3 — single-sourced from it, so the three statements (legend, Guide §11, this glossary) cannot re-diverge within a release cycle.

**Whether abbreviations must still be expanded at first use.** Yes, unchanged. Documents travel alone — a test result is read without the glossary open, and a brief is read without the repo. The glossary is a reference for resolving vocabulary after the fact, not a licence to stop expanding. The existing convention stands: every abbreviation is expanded at first use in each document; the glossary adds a place to check the expansion when a document fails that rule.

**The cost of shipping it.** (a) One new public file plus three link edits; no version bump of its own. (b) A standing maintenance duty: every release that adds, renames, or retires vocabulary must update the glossary in the same release — this belongs as one line in PUBLISHING.md's release steps, or the glossary will drift stale, which is worse than its absence because a stale glossary asserts wrong meanings with reference authority. (c) The divergence risk named above, mitigated by the verbatim-quote rule and single-sourcing Guide §11. (d) A small anchoring cost: fixing reservation rules (bare "the gate", bare "the cap binds") turns present dominant usage into obligations, and future prose that breaks them becomes a defect rather than a variation — that is the point, but it is a real constraint on authors. Net: cheap to ship, cheap to keep only if the release-checklist line is added.

**Fixed and flagged, not resolved here.** Three things this glossary records but must not and does not change: the grade symbols `[V]`, `[V1]`, `[V2]`, `[V3]`, `[U]` (fixed corpus-wide, the last renamed from `[U]` by the corpus decision of 30 August 2026); the canonical five-situation `[U]` wording (ADJ-006 §1, quoted verbatim in Section 1); and the fixed legend's exact text, including its use of "inheriting the cap", where the word "cap" carries the grade sense inside versioned wording — the one site the Section 7 "cap" reservation rule cannot reach, flagged here so no future sweep "fixes" the legend by accident.

---

## Two-tier summary

- **Reader tier:** all of Section 1, plus the reader-tier subsections of Sections 2 and 3 (the gate, the brief and its parts, the triage, the router, disconfirmation, the dossier, the ladder and rung, the map's reader terms — loop, dominates-now, tipping condition, leverage point, archetype). This tier is what the Guide §11 glossary should contain, and nothing in it requires knowing an identifier series or a test name.
- **Engine and record tier:** the engine-and-record subsections of Sections 2 and 3, including the Section 2 supplement, plus Sections 4–8 in full. This tier exists so that someone editing a skill, scoring a run, or auditing the record has one place where every term has exactly one stated meaning — or, where a word carries more than one, the collision is on the record with a rule.

---

*The Insight Engine Glossary — first published 27 August 2026 with v0.1.22, compiled 24 August 2026 by Fable 5 (`claude-fable-5`). Describes insight-engine v0.1.23 as shipped; the **Blind pass** and **Outbound-package preview** entries were revised on 29 August 2026 for the v0.1.23 adjudication blindness fix.*
