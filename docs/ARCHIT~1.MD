# The Insight Engine — Architecture, Build Philosophy, and Features

*Reference document for `insight-engine` v0.1.7 · 24 June 2026 (revised 25 June 2026 to add the §9.1 ICD-203 alignment).*

> Markdown edition for reading on GitHub. A formatted `.docx` is in [`originals/`](originals/).


## 1. What the Insight Engine is

The Insight Engine is a tool for analysing high-stakes, complex, or wicked problems — the kind where the danger is not that the answer is hard to compute but that the most important things sit where attention does not naturally go, where the evidence is mixed or interested, and where the decisive questions are value judgements no amount of analysis can settle.

It is the lightweight successor to the **SAF** (Series of Analytical Frameworks), a 234-framework analytical corpus that has now been frozen. The Insight Engine keeps almost none of the SAF's machinery and all of its hard-won judgement, distilled into a single page and wrapped in an assurance layer. It ships as a Claude/Cowork plugin (`insight-engine`, currently **v0.1.7**) with four skills: `analyse`, `verify`, `render`, and `track`.

Its one-line description is also its design thesis: **the model provides the insight; the engine makes that insight verified, defensible, and audience-ready.** The engine does not try to be smarter than the model. It tries to make the model's output *trustworthy* and *honest about its own limits* — and to force the human to own the parts that are theirs to own.

## 2. Build philosophy

The engine is the product of a controlled experimental program, not a design committee. Every feature it carries earned its place on a test; several plausible features were tested and deliberately left out. The philosophy below is therefore less a set of preferences than a set of findings.

**The corpus does not earn its keep at runtime.** The SAF's premise was that a large library of analytical frameworks, fanned out over a problem, would surface more than a general approach could. A program of apparatus-versus-bare tests found no top-tier benefit from the 234-corpus-as-runtime, or from framework fan-out, over "a strong model + a one-page distilled prompt + a web tool." The value did not live in the breadth of frameworks; it lived in **verification, grading, and forcing judgement**. So the SAF was frozen and the corpus relegated to a quarry (for audit, escalation, and one-time distillation), never the runtime.

**Light by design.** The engine applies the *same* one-page method to every problem. There is no per-problem framework selection, no fan-out, no tiering of analytical depth by category. The provocation page is worded identically on every run. Lightness is not a cost-saving; it is the source of the engine's reliability and the reason its heavy moves stay meaningful.

**The model provides the insight.** On a strong model, the analytical content is already there. The engine's job is the surrounding discipline: check what can be checked, grade how strongly it is established, separate fact from value, and refuse to let a confident-sounding answer pass as a verified one.

**Assurance over cleverness.** The engine's distinctive value is not analytical reach but *epistemic honesty* — provenance grading, source-strength tiering, an active search for disconfirming evidence, and a non-droppable caveat that travels with every conclusion. These are the moves that the field's tools, on the public evidence, mostly do not make.

**Human-in-the-loop, by construction.** The engine articulates the value structure of a decision; it does not resolve it. The questions that no evidence can settle — the framing, the legitimacy, the opportunity cost, the value trade — are routed to the human and *gated*: the analysis does not finalise until the operator has taken a position or explicitly deferred.

**Earn it by test; then stop — and know the difference between a prompt-move and a capability.** Across the test program, the consistent result is that, on a strong model, incremental analytical *prompt-moves* add little or nothing — the model already performs them — while the verification, grade-lock, disconfirmation, and the forced gate carry the value. That null held about five times over, and the directive that follows is to stop adding prompt-moves. The **systems-investigation pass** (v0.1.7) is the deliberate exception that confirms the rule: it is not a prompt-move but a *capability* — an explicit, graded causal-map representation the bare model does not structure on its own — and it is the first addition since v0.1.4 to beat a strong baseline on test, in two genres, while clearing a forecast-baiting safety gate and a proportionality gate. The proportionality triage (v0.1.6) and the systems pass (v0.1.7) are also the two moves that make the engine do *less*, or run *only when warranted*. The standing conclusion is unchanged: stop adding analytical prompt-moves; admit only a genuinely new capability, and only when it earns its place on a passed test; then put the engine to real use.

## 3. The architecture at a glance

The engine is best understood as a stack of conceptual layers, held together by an invariant spine and a human-in-the-loop owner. The `analyse` skill is the runtime orchestration of these layers; the other three skills expose individual layers (verify = L2; render = L5; track = L6) for standalone use.

| Layer | Name | Role |
|---|---|---|
| **L0** | The model | Provides the raw insight |
| **L1** | The provocation page | A fixed, one-page analytical method applied verbatim every run |
| **L2** | Verification | Three-bucket routing, source-tiered grading, and disconfirmation of load-bearing claims |
| **L2.5** | Systems-investigation pass *(conditional)* | A graded causal map — loops, tipping conditions, leverage — for genuinely systemic problems only; investigate, don't predict |
| **L3** | Deep-core routing | Separating the irreducibly un-verifiable questions from the verifiable ones |
| **L4** | Assembly | The grade-locked decision brief |
| **L5** | Rendering | Grade-locked re-expression for specific audiences |
| **L6** | Workspace | A living investigation that accumulates across sessions |
| **Spine** | Grade-lock | The invariant that runs through every layer: grades, the dominant unknown, and the non-droppable caveat core |
| **Owner** | Human-in-the-loop | The operator, who clears the forced judgement gate and owns the value calls |

Sitting in front of the whole stack is a **fail-safe proportionality triage** (added in v0.1.6): a pre-flight check that decides whether the full machinery should run at all, or whether the problem is unambiguously trivial enough for a short, proportionate answer. Its default is depth; down-scoping is the rare, guarded exception.

## 4. The grade-lock spine (the invariant)

Grade-lock is the single most important idea in the engine and the through-line of every other feature. It has three parts:

**Provenance grades.** Every load-bearing claim is marked `[V]` (independently corroborated) or `[N]` (rests on an interested or self-reporting party). A `[V]` is never bare — it carries a **source-strength tier**: `[V1]` primary (the statute or regulation text, an official statistic, a peer-reviewed study, a court ruling, the primary dataset); `[V2]` secondary (reputable reporting or interpretation resting on primaries); `[V3]` contested or weak (only weaker or interested sources corroborate, or credible sources disagree).

**The dominant unknown.** The single fact that, if known, would most change the conclusion. It is named explicitly and re-pointed whenever the evidence moves.

**The non-droppable caveat core.** All grades, plus the dominant unknown, plus a one-line reliability caveat naming what the analysis rests on (for example, a single interested source, or a `[V3]` the call leans on). This core appears in *every* output and every render.

The locking rule is strict: **once a grade is set, nothing downstream may change it — only re-express it.** A grade moves only on new evidence, recorded in a log. This is what lets a finished analysis be re-voiced for a board, a regulator, or a family without its epistemic backbone shifting, and it is what makes the output defensible after the fact.

## 5. The features in detail

### 5.1 L0 — A strong model
The engine assumes a top-tier model as its substrate, because the experimental finding that "the model already performs the analytical moves" only holds for a strong model. On a weaker model the calculus would differ; the engine is explicitly built for and around strong models.

### 5.2 L1 — The provocation page
A single page, worded identically on every run, that is the 234-framework corpus distilled to its load-bearing moves. It opens by reframing the analyst's fluent first reading as *the baseline a competent reader already has — not the finding*, and instructs the analyst to surface what is material but sits where attention does not go. It contains:

- **Two always-on moves.** (1) *Displacement / second-order*: for every apparent gain, ask where the cost went — onto an unmeasured node, an absent party, or the future. (2) *Provenance / verification*: mark each load-bearing claim `[V]`/`[N]`, name the single dominant unknown, and weight a self-damaging admission above a self-serving claim.
- **Candidate probes, kept where they fire.** Absent voice (who bears a cost but is not in the room); cui bono from the framing (who benefits from the question being posed this way); base rate & measurement (is the metric a gameable proxy?); normalised-as-natural (what assumption has become invisible through repetition?); spuriously present (what is loud and confident but doesn't merit the attention it pulls?); **conspicuously absent / omission sweep** (from the model's own knowledge, what would a thorough treatment of *this kind* of problem include that is missing here?); reflexive (what does the way this was handed to me make me likely to miss?).
- **A closing discipline.** Steelman the strongest findings and keep only what survives the best opposing reading; name every materially affected party; aim for the material set, not length — an over-claim costs more than a miss.

The **omission sweep** deserves emphasis: it is generated dynamically from the model's own domain knowledge, with no fixed checklist or taxonomy. This was a deliberate decision — a static checklist (even one distilled from the 234 frameworks) would be a narrow-taxonomy cage; the model's training is the far larger and more current "taxonomy."

### 5.3 L2 — Verification
The assurance layer with teeth. It turns "the model believes X" into "X is corroborated by a cited source of stated strength, has survived a search for its own counter-evidence, or it is not." It has four components:

- **The three-bucket evidence router.** Every load-bearing claim is sorted into: *web-verifiable* (a public fact, pattern, rule, or statistic → search and grade `[V]`/tier or `[N]`); *party-held* (a private document or internal figure → do not pseudo-verify; name the exact document that would settle it); *irreducibly open* (a value, framing, or forecast → do not grade; route to the human at L3).
- **Source-strength tiering.** Every `[V]` is tiered `[V1]`/`[V2]`/`[V3]` (see §4). A primary is preferred; when only a weaker source is reachable, the analysis says what primary source would lift it.
- **The disconfirmation pass.** For every claim the conclusion materially rests on, a *second* search is run at the claim's negation ("X is false / disputed / overstated"). Credible counter-evidence downgrades the claim to `[V3]` or `[N]` and records the dispute; a genuine negation search that finds nothing marks the claim *survived disconfirmation* — itself a real signal. This is the engine's answer to the field's most common failure mode, which is the opposite: confirmation bias.
- **The coverage-retention re-scan.** Concentrating on the load-bearing few narrows attention onto exactly those claims. Before finishing, the engine re-scans once for material issues that the focus deprioritised. "Sharpening the spotlight darkens its edges; this is the counter-sweep."

A standing heuristic runs through all of L2: **weight a self-damaging admission above a self-serving claim**, and correct the analysis's own confidently-wrong facts — a strong model asserts some, and this is where they get caught.

### 5.3.1 The systems-investigation pass (Step 2.5 — conditional; v0.1.7)
Some wicked problems are not merely hard to verify — they are *dynamic*: driven by feedback loops, accumulating stocks, delays between cause and effect, and the possibility of tipping into a different regime. For these, and only these, the engine runs a **systems-investigation pass** after verification (Step 2.5), building a graded causal map. It is conditional, and its discipline is the whole point.

**It runs only when the problem is genuinely systemic** — when two or more of these are materially present: feedback / circular causation; accumulation (stocks); material delays; multiple interacting actors; a possible regime shift; self-fulfilling expectations. Otherwise it skips with one line ("no material feedback structure — systems pass not warranted"). Importance, emotion, or difficulty does not make a problem a system, and a spurious causal map is a failure, not thoroughness — a proportionality discipline that was tested directly (§8).

**What it builds**, kept to the load-bearing few (≤8 variables, ≤5 loops, ≤4 tipping points, ≤5 leverage points — a sprawling map is itself false precision): the key variables and signed, graded causal links, with material delays flagged (a lag is where a system feels fine until it isn't); the reinforcing and balancing feedback loops, each graded *twice* — whether the loop *exists* (often `[V]`) and whether it *dominates now* (usually `[N]`, because which loop wins is the hard, often-unknowable part); candidate tipping points stated **as conditions to watch, never as dates or probabilities**, each with a reversibility flag; emergent behaviours, especially self-fulfilling expectations where the shared narrative is itself a causal variable; and a ranked set of **leverage points**, each graded twice — the *mechanism* (why it is structurally high-leverage) and the *effectiveness* (whether acting there will actually work — usually `[N]`).

**The hard ceiling is the spine of the pass, and its entire safety case: structure may be graded up to `[V]`; whether or when the system tips has a ceiling of `[N]` and routes to the human.** The map states the conditions under which the system *could* shift; it never states that it *will*, or when, or with what probability. It investigates structure; it does not simulate dynamics or compute outcomes — if genuine quantitative modelling is needed, the engine says so and routes to specialists and data. The map is a hypothesis to be falsified, not a model to be trusted.

The pass feeds the rest of the pipeline rather than standing alone: loop *dominance*, *regime*, and *timing* join the deep-core OPEN list for the gate (they are judgements, not facts); the ranked leverage points inform the call; the tipping conditions become what-to-monitor and what-would-flip-the-call; and the assumption-resilience check (§5.5) stress-tests the call against the map's load-bearing links. This is the engine's one concession to complex-systems analysis, and the only feature added after the program judged the engine feature-complete for prompt-moves — admitted because it is a *capability*, not a prompt-move, and because it earned its place on three gates and a replication (§8).

### 5.4 L3 — Deep-core routing
The material issues that are *not* externally verifiable — the framing of the decision itself; legitimacy and who is bound without a say; opportunity cost and unmodelled alternatives; value trade-offs — are separated into an explicit OPEN list. They are not resolved, not dropped, and never asserted as verified. They are the questions the operator must judge at the gate.

### 5.5 The assumption-resilience check
After grades are locked, the engine stress-tests the *conclusion*, not just the claims: it names the two-to-four assumptions the call most rests on, varies them *together*, and records whether the conclusion survives. This is an **assumption-fragility** check — deliberately *not* system modelling; it does not simulate feedback loops or tipping points and must not claim to (the conditional Step 2.5 systems-investigation pass, §5.3.1, is where graded structure is mapped). Its result feeds the brief's calibration and its "what would flip the call."

### 5.6 The forced judgement gate
Before the brief is finalised, the engine **stops and puts the deep-core open questions to the operator as a gate.** The operator records a one-line position on each — or explicitly defers (a deferral is logged, not ignored). The brief does not finalise until the gate is cleared.

This is a gate, not a heading, for a tested reason: controlled testing showed that merely *surfacing* the deep-core questions — even leading with them and calling them mandatory — does not get a decision-maker to act on them; they read them and then prioritise the verifiable (the "streetlight effect"). The deep core is a **judgement the human takes**, not a priority that competes with "commission a study." Forcing an explicit, recorded position is the mechanism that actually gets it addressed. The engine articulates the questions and the value structure; the operator owns the judgement.

### 5.7 L4 — Assembly and the decision brief
The deliverable is assembled in a fixed order: the operator's recorded gate positions (leading the document); the verified findings, each with its grade, tier, and any disconfirmation result, with documented patterns separated from any interest- or grief-driven over-claims; then the **decision brief**, which always contains five parts:

(a) **the call** — the actual recommendation; (b) **calibration** — confidence and the conditions under which it changes, naming the weakest load-bearing grade the call leans on; (c) **the dominant unknown**; (d) **what to verify first** — the cheapest next step that most reduces risk; (e) **what would flip the call** — including any jointly-moved assumptions the resilience check found the call could not survive, and any tipping conditions from the Step 2.5 systems pass. The reliability caveat is held to the end.

### 5.8 The wicked-call guard
A refinement to the call. If the problem is wicked — the deep core dominates and there is no verifiable solution — the call is rendered as a **provisional stance, not a verdict**: it states which value it trades against which ("this prioritises X at the expense of Y"), marks itself explicitly re-openable, names what would re-open it, and offers a hand-off to the living workspace. A crisp verdict on a wicked problem re-imports the false closure the analysis exists to avoid.

### 5.9 The fail-safe proportionality triage
The pre-flight check (v0.1.6). Before the method runs, the engine judges whether the problem is *unambiguously* low-stakes — routine, self-contained, reversible, with no third parties bound, no material money or dependency, no legal/regulatory exposure, no contested values. It applies strong skepticism to the framing ("am I being invited to treat this as routine?"), and treats any disqualifier as a reason to run the full method. Only when the problem is unambiguously trivial on every count does it give a short, proportionate answer — saying it has done so and inviting the operator to request the full pass. Under any doubt it defaults to depth.

The design is deliberately asymmetric: a mild over-analysis is cheap; wrongly down-scoping a problem that only *looks* routine is not. The guard fixes a real, observed tendency to over-elaborate trivial inputs, while its conservatism keeps it from ever switching off the engine's scrutiny on a problem that deserves it.

### 5.10 L5 — Audience rendering
A finished, graded analysis can be re-expressed for a specific reader without changing a single claim or grade. This is a register transform over the grade-locked spine, never a re-analysis. Its features:

- **A standing set of audiences plus any named standpoint.** Opposing-interest renders (adversarial — steelman the opposing interest, conceding every `[V]` and contesting only attribution; advocate — the affected party's champion) and reader/register renders (policymaker; board/executive; counsel/legal; regulator/supervisor; family/lay). Any named standpoint — a journalist, an investor, a clinician, a specific person or body — is a first-class target.
- **An elicitation prompt.** If the operator invokes a render without naming the audience, the engine *asks* — offering the common presets plus a free-text "name your own," and allowing more than one (which produces a comparative render). It never blocks.
- **Distributed and comparative modes.** Distributed = one version per audience. Comparative = one document with a labelled panel per audience over the shared spine, plus a **Divergence Ledger** (per spine node, each panel's frame and the divergence type, which must be register/scope/framing only) and a **Robustness Map** (each node tagged hardened / contested / narrator-only).
- **Hard invariants.** No claim or grade changes; the source tier is carried verbatim (a lay render may put it in plain words but must never upgrade a contested `[V3]` to sound settled); the non-droppable caveat core appears in every render; and a **tone rule** — show understanding through accuracy and respect, never ingratiating, saccharine, or over-familiar; empathy is carried by register, never by false certainty. A fidelity self-check asserts the claim/grade set is identical to the spine before any render is delivered.

### 5.11 L6 — The living workspace
For inquiries that accumulate over days or weeks, the engine maintains a living dossier (one operator-owned file, persisted across sessions) through three modes, each of which *asks* rather than guesses: **OPEN** (what are we tracking; carry a spine from an `analyse` run or start fresh; the watch-list of update triggers; cadence, optionally a scheduled re-verification); **UPDATE** (what arrived; re-verify the affected claims; re-grade explicitly with a before→after log; re-point the dominant unknown; re-derive the call); **STATUS** (read the current state without re-verifying). Grade-lock carries throughout: a grade changes only on new evidence, recorded in the log, never by re-expression. This layer is the newest and the least battle-tested (see §10).

## 6. The four skills

| Skill | Layer(s) | What it does |
|---|---|---|
| `analyse` | Orchestrates L0–L6 | The full pipeline, end to end |
| `verify` | L2, standalone | Router, source-tiering, disconfirmation, coverage-retention, dominant-unknown — to fact-check a claim-set or premise on its own |
| `render` | L5, standalone | Grade-locked addressee rendering of a finished analysis |
| `track` | L6, standalone | The living investigation workspace |

The **`analyse` runtime sequence** is: the proportionality triage (pre-flight) → Step 0 optional scoping (offered, never blocking) → Step 1 the provocation pass → Step 2 verification → **Step 2.5 the conditional systems-investigation pass** → Step 3 deep-core routing → Step 4 grade-lock and the resilience check → **Step 5 the forced judgement gate** → Step 6 assembly (coverage-retention re-scan, then the gate positions, the graded findings, the decision brief, and sources) → Step 7 offer follow-ons (render, track). The gate is canonically Step 5 and has stayed there through every revision; the systems pass sits at Step 2.5 because it needs the verified grades from Step 2 and feeds the deep-core list at Step 3.

## 7. The elicitation contract

A distinguishing property of the engine is *where it stops and asks the operator*. There are four such points, deliberately placed:

1. **The proportionality triage** (pre-flight) — implicit; it may offer a short answer and invite the full pass.
2. **Step 0 scoping** — optional and skippable: the decision at stake, the intended audience, the value frame, scope boundaries, any party-held material.
3. **The Step 5 forced gate** — mandatory: a recorded position on each deep-core question, or an explicit deferral.
4. **The render audience prompt** — asks who the output is for when not specified; and `track`'s OPEN/UPDATE/STATUS contract asks what to track and what has changed.

Everything else the engine produces on its own. The deliberate exception is *analytical depth*, which is generated rather than elicited — the engine does not ask the operator how deep to go; it judges that (via the triage) and defaults to depth.

## 8. How the architecture was earned

The engine's shape is the residue of a controlled-testing program with a consistent discipline: predictions pre-registered before running; gold keys fixed in advance where possible; blind subjects; at least three raters; cheapest-decisive tests first; any test allowed to kill a feature; and the scorer decoupled from the designer wherever it mattered.

**The findings that shaped it:**

- **The streetlight effect** (T-L2-005/006): decision-makers under-attend the deep core even when it is surfaced and called mandatory. *Consequence:* surfacing is not enough — hence the **forced gate**.
- **The gate is load-bearing, not cosmetic:** the deep core is a judgement, not a priority; forcing a recorded position is what gets it answered. Proven in first real use (a healthcare case), where the operator's override of the recommended framing materially reshaped the brief.
- **No generate-and-verify "discovery loop":** an inverted-Karpathy loop did not beat a single pass plus one verification and a one-line routing step; the loop was not built.
- **v0.1.5 beat v0.1.4** (T-AB-001): the omission sweep and the resilience check produced a unanimous, substance-not-padding improvement on a representative wicked case.
- **Two moves did not survive isolation** (T-AB-002/003): the wicked-call guard and coverage-retention proved largely redundant with a strong, probe-equipped baseline — kept because cheap and harmless, not because proven.
- **The proportionality guard passed its safety test** (T-AB-004): a fail-safe guard down-scoped none of three disguised-wicked traps while trimming genuinely-trivial inputs — the first post-v0.1.4 addition to earn its place on a passed test.
- **The convergent meta-finding** (three to four independent results): on a strong model, the value is verification / grade-lock / disconfirmation + the forced gate, not incremental analytical prompt-moves. The directive that follows is to stop adding moves.
- **The one capability that beat the null** (T-SM-001/002/003/004): a *systems-investigation pass* — an explicit, graded causal-map representation — is the first addition since v0.1.4 to add decision-relevant value over a strong baseline, replicated across two genres (an urban fiscal "doom-loop" and a critical-drug supply chain). It cleared a **forecast-baiting safety gate** (zero manufactured false confidence across three scenarios engineered to demand a forecast, against a discipline-stripped control that failed every one) and a **proportionality gate** (it skipped three genuinely non-systemic problems without inventing a map, while still firing on a disguised-systemic one). It breaks the null precisely because it is a *capability*, not a prompt-move — the standing distinction for any future addition.

**Version history:**

| Version | Change |
|---|---|
| v0.1.0 | Initial MVP: `analyse`, `verify`, `render`, `track` |
| v0.1.1 | The forced judgement gate (replacing mere "elevation" of the deep core) |
| v0.1.2 | Render audience elicitation — presets plus a free-text "name your own" |
| v0.1.3 | `track` hardened with the OPEN/UPDATE/STATUS elicitation contract |
| v0.1.4 | Source-strength tiering (`[V1]`/`[V2]`/`[V3]`) and the disconfirmation pass |
| v0.1.5 | Resilience check, wicked-call guard, coverage-retention, dynamic omission sweep |
| v0.1.6 | The fail-safe proportionality triage |
| v0.1.7 | The conditional systems-investigation pass (a graded causal map for feedback-driven problems; investigate, don't predict) |

## 9. Positioning against the field

The engine shares a name with a commercial category but not a purpose. The lineage once called "Insight Engines" is now Gartner's **Enterprise AI Search** — retrieval and RAG over a *trusted internal corpus*, where "verified" means access-controlled. The Insight Engine inverts that trust model: nothing is authoritative until graded, and it adjudicates *contested external* evidence on wicked problems.

Its true category is closer to an **LLM-operationalised intelligence-tradecraft instrument** (source grading in the spirit of ICD-203, competing-hypothesis discipline, red-teaming). On the public 2025–26 evidence, no shipped product fuses per-claim verification, source-strength tiering, self-disconfirmation, grade-lock, fact/value routing, and a forced human gate into one pipeline. Two of those moves — **disconfirmation** and the **forced gate** — run directly against the field's two documented failure modes (confirmation bias in AI-search/deep-research tools, and human rubber-stamping when "a human is in the loop"). Three independent research literatures — on AI in complex governance, on the wicked problem of AI in assessment, and on mitigating LLM-evaluation blind spots — were found to converge on the engine's core architecture without having informed it.

### 9.1 Alignment to the ICD-203 analytic tradecraft standards

The "in the spirit of ICD-203" remark above is worth making precise, because on the Insight Engine's own evidence ICD-203 is its closest conceptual relative — not a product but a doctrine. **Intelligence Community Directive 203, *Analytic Standards*** (ODNI, 2015 as amended) is the tradecraft every US intelligence analytic product is held to and evaluated against; it defines nine **Analytic Tradecraft Standards** governing how judgements are sourced, qualified, distinguished, and conveyed. It is a *process-and-presentation* standard, not a guarantee of being right — exactly the layer the Insight Engine occupies. The 2025–26 landscape review found no published LLM system shown to satisfy those standards `[V2 / absence-of-evidence]`.

**The mapping is strong but deliberately uneven.** The Insight Engine maps strongly to the *epistemic core* of ICD-203 — source characterisation (standard 1, via `[V1]`/`[V2]`/`[V3]` tiering and `[V]`/`[N]` provenance), uncertainty expression (2, via grade-lock, the dominant unknown, and conditions-not-dates), the fact/judgement distinction (3, via deep-core routing and the forced gate's logged assumptions), customer relevance (5, via the decision brief), and change-of-judgement (7, which `track`'s before→after grade log *is*). It maps *well* to analysis of alternatives (4, via the disconfirmation pass and the provocation probes). It is honestly *weaker* on two: clear-and-logical argumentation (6), where it imposes structure but runs no formal validity check and leans on the model; and effective visual information (9), which it largely does not do — the conditional systems-map is its only visual. On accuracy (8) its contribution is *consistent confidence conveyance*, not accuracy itself, which a strong model already supplies.

**The alignment is now assessed, not merely asserted.** A blind self-assessment (T-ICD-001) put a full `analyse` product and a bare strong-model briefing on the same wicked question — a 24-month semiconductor-supply-disruption assessment — to four independent raters, each scoring one product in isolation against the nine standards. The Insight Engine scored **16.5/18 (92%)** to the bare model's **13.5/18 (75%)**, and the edge fell exactly where the mapping predicts: standards 3, 4, 7, 8, and 9 — the structured-tradecraft moves a bare model does not reliably self-deliver. Two qualifications matter as much as the headline. The products **tied at the ceiling on standards 1, 2, and 5**: the bare model spontaneously tiered its sources and gave calibrated ranges — the same result as the verify-vs-bare tests, that a strong model self-supplies the sourcing-and-hedging half of ICD-203. And the Insight Engine **lost standard 6**, docked for density and jargon — a real clarity cost whose designed remedy already lives in the engine, in the `render` layer that re-voices a finished analysis for a reader without touching a grade.

The alignment is credible *because* it is uneven: a tool claiming to satisfy all nine would be over-claiming. The honest position is that the Insight Engine is, on the public evidence, the first LLM analysis tool explicitly **architected around the ICD-203 epistemic core and satisfying it by construction**, while not addressing the argumentation-audit and visualisation standards.

> **The caveat that bounds the claim.** "Architected around," and "assessed at 92% in one blind self-assessment," are *not* "ICD-203 compliant" or "certified." In the Intelligence Community, ICD-203 compliance is *assessed* by an analytic ombudsman against real products; no such review has been run on the Insight Engine, and — per the landscape review — none has been run on any LLM system. T-ICD-001 is n=1, with LLM raters scoring tradecraft *form* on an analogue (a semiconductor brief, not an IC product). The defensible claim is therefore architectural and directional: the Insight Engine is *architected around* the standards and satisfies the core *by design*, and was assessed once, favourably, by a method that cannot stand in for an Intelligence Community review.

## 10. Known limits and the road ahead

- **The living workspace (`track`) is untested at scale.** Its re-verification discipline is sound and it now has a real elicitation contract, but its behaviour accumulating over many updates has not been controlled-tested. This is the one genuine open corner.
- **All controlled tests have been synthetic.** They used LLM raters as a proxy for human decision-makers — directionally informative, not human-subjects results. The engine's marginal value over a strong model used well is well-argued but not yet shown in sustained *real* use.
- **The engine is feature-complete for analytical prompt-moves.** The convergent verdict of the test program is that further analytical *prompt-moves* do not pay on a strong model. The one post-verdict addition — the v0.1.7 systems-investigation pass — was admitted precisely because it is a *capability* (a representation the bare model does not structure on its own), not a prompt-move, and only after it cleared three gates and a replication. That is now the bar for any further addition. The remaining value is overwhelmingly in **real use** — and, secondarily, in stress-testing `track`.

The shortest honest statement of the road ahead: stop building, start using. Hand a genuine problem to `/analyse`, let the gate make you take a position, and let real use — not another feature — be the next source of signal.

---

*Reference document for `insight-engine` v0.1.7, compiled 24 June 2026 (revised 25 June 2026 to add the ICD-203 alignment, §9.1) from the engine's design and its controlled-testing record. The engine's own grade discipline applies to its self-description: the architecture and version history are recorded fact `[V1]`; the "feature-complete" judgement rests on a small, synthetic-rater test base and is held as a calibrated conclusion, not a proof.*
