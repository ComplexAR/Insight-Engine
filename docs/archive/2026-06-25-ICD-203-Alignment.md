# The Insight Engine as an LLM Operationalisation of ICD 203 Analytic Tradecraft

*A positioning mapping — the Insight Engine against the nine Intelligence Community analytic standards · 25 June 2026*


## Why this framing, now

Two findings from the Insight Engine's own evidence base point here. First, the 2025–26 landscape review found the Insight Engine's **closest conceptual relative is not a product but a doctrine** — the US Intelligence Community's analytic tradecraft standards (**ICD 203**) — and that **no published LLM system has been shown to satisfy those standards** `[V2 / absence-of-evidence]`. Second, the verify-vs-bare-model test (T-VB-001) found that a strong model now *self-verifies* most of the time, so the Insight Engine's durable edge is **not raw error-catching but reliable, auditable assurance** — which is precisely what an analytic *standard* is for. ICD 203 is therefore the natural, evidence-honest home for the Insight Engine's value: it does not claim the Insight Engine is *smarter*; it claims the Insight Engine **applies an auditable analytic standard, by construction and every time.**

This document maps the Insight Engine to the nine standards, honestly — strengths and gaps — and states what it can and cannot credibly claim.

## What ICD 203 is

**Intelligence Community Directive 203, "Analytic Standards"** (Office of the Director of National Intelligence, 2015, as amended) sets the tradecraft every IC analytic product is held to and evaluated against. It defines **nine Analytic Tradecraft Standards**. They are a *process and presentation* standard — about how judgements are sourced, qualified, distinguished, and conveyed — not a guarantee of being right. That is exactly the layer the Insight Engine occupies. `[V1 — primary directive]`

## The mapping

| # | ICD 203 standard (what it requires) | How the Insight Engine addresses it | Strength |
|---|---|---|---|
| 1 | **Describe quality & credibility of sources** | Source-strength **tiering** `[V1]`/`[V2]`/`[V3]` on every corroborated claim + provenance `[V]`/`[N]` + the disconfirmation pass | **Strong (by design)** |
| 2 | **Express & explain uncertainties** | Grade-lock; the named **dominant unknown**; brief calibration ("how confident, what changes it"); tipping points as **conditions not dates**; the non-droppable caveat core | **Strong** |
| 3 | **Distinguish information from assumptions & judgements** | **Fact/value routing** (deep-core list); `[V]`/`[N]`; the resilience check names the load-bearing **assumptions**; wicked-call guard (provisional stance, not verdict) | **Strong** |
| 4 | **Incorporate analysis of alternatives** | The **disconfirmation** pass (search each load-bearing claim's negation); provocation-page probes (absent voice, steelman the opposing reading, omission sweep); deep-core **unmodelled alternatives** | **Good** (alternatives surfaced; not a formal ACH matrix — see gaps) |
| 5 | **Demonstrate customer relevance & implications** | The decision brief (the call · what-to-verify-first · what-would-flip-it); the **render** skill re-voices for a specific reader without changing a grade | **Strong** |
| 6 | **Use clear & logical argumentation** | The fixed pipeline and the assembled, ordered brief impose structure | **Partial** — structure is imposed, but no explicit argument-validity check; relies on the model |
| 7 | **Explain change to / consistency of judgements** | The **track** skill: a before→after grade log, re-verification on new evidence; grade-lock means a judgement changes only on the record, never silently | **Strong** (track *is* this standard) |
| 8 | **Make accurate judgements; convey confidence consistently** | Grades + tiers are a single consistent confidence vocabulary across the whole output and every render; wicked-call guard | **Partial–Good** — *consistent conveyance* is strong; *accuracy itself* is substrate-dependent (a property of the model, per T-VB-001) |
| 9 | **Incorporate effective visual information** | Optional Mermaid causal map in the systems-investigation pass | **Weak** — text-first by design; visuals are not a focus |

## Reading the map

The Insight Engine maps **strongly to the epistemic core** of ICD 203 — the five standards about *sourcing, uncertainty, the fact/judgement line, relevance, and tracking change* (1, 2, 3, 5, 7). These are exactly the moves the landscape review found individually rare and never fused in shipped LLM systems, and they are the Insight Engine's spine. It maps **well** to alternatives (4) through disconfirmation and the provocation probes. It is **honestly weaker** on two standards: explicit **argumentation-validity** (6) — the Insight Engine imposes structure but does not run a formal logic check, leaning on the model — and **visual information** (9), which it largely does not do. On **accuracy** (8) the Insight Engine's contribution is *consistent confidence conveyance*, not accuracy itself, which T-VB-001 showed a strong model already supplies.

This is a credible alignment precisely because it is uneven: an Insight Engine that claimed to "fully satisfy" all nine would be over-claiming. The honest statement is that the Insight Engine is **architected around the ICD 203 epistemic core and satisfies it by construction**, while not addressing the argumentation-audit and visualisation standards.

## The honest caveat that bounds the claim

"**Addresses by design**" is not "**verified to comply**." ICD 203 compliance in the IC is *assessed* (analytic ombudsman review against the standards on real products). No such assessment has been run on the Insight Engine — and, per the landscape review, none has been run on **any** LLM system `[V2/absence]`. So the defensible claim is architectural, not certified:

> The Insight Engine is, to the best of the available public evidence, the **first LLM analysis tool explicitly architected around the ICD 203 analytic tradecraft standards**, satisfying the epistemic-core standards (source characterisation, uncertainty expression, fact/judgement distinction, customer relevance, and change-tracking) **by construction**. It does not yet carry, and should not claim, a formal compliance assessment — which is itself the open, unoccupied opportunity the field has not taken.

## The positioning move (what to say, and not say)

**Say:** the Insight Engine operationalises a recognised, decades-old analytic *standard* in an LLM tool — the auditable tradecraft of source-grading, uncertainty, the fact/judgement line, alternatives, relevance, and logged change-of-judgement. This reframes the Insight Engine's value, post-T-VB-001, from "reduces errors" (small, on a strong model) to "**applies an auditable analytic standard reliably and on the record**" (durable, and unoccupied in the LLM field).

**Do not say:** that the Insight Engine is "ICD 203 compliant" or "certified." It is *architected around* the standards and satisfies the core *by design*; compliance is assessed, not asserted.

**The natural next step this opens** (optional, and a genuine first): a **compliance self-assessment** — run the Insight Engine's output on a real analysis through the nine-standard rubric the IC uses, scoring each standard, to convert "addresses by design" into "assessed against the standard." That would be, on the public evidence, the first such assessment of any LLM analytic system — the credibility anchor the positioning deserves.

---

## Appendix — the nine standards, verbatim sense

ICD 203's nine Analytic Tradecraft Standards (2015, as amended): (1) properly describes the quality and credibility of underlying sources, data, and methodologies; (2) properly expresses and explains uncertainties associated with major analytic judgements; (3) properly distinguishes between underlying intelligence information and analysts' assumptions and judgements; (4) incorporates analysis of alternatives; (5) demonstrates customer relevance and addresses implications; (6) uses clear and logical argumentation; (7) explains change to or consistency of analytic judgements; (8) makes accurate judgements and assessments; (9) incorporates effective visual information where appropriate.

*Positioning document, 25 June 2026. The ICD 203 standards are recorded fact `[V1]`; "no LLM system shown to satisfy them" is `[V2]`/absence-of-evidence from the 2025–26 landscape review and could be overturned by unpublished/classified systems; the Insight Engine-to-standard mapping is an architectural self-assessment, not an independent or IC review.*
