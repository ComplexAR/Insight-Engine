IE 1.1.0 · host Cowork (Claude desktop app) · model Claude Opus 5 (as the model identifies itself; provider routing not independently confirmed) · SEARCH y PERSIST y MULTI y CODE y · declared 2026-08-30 · enforce: host-mechanism · gate: refused — 6/6 defaulted · verification: performed · legend: attached

# Eleven-storey block: combustible insulation and defective cavity barriers

NOTE FOR THE RECORD: this file is NOT the deliverable. It is a partial reconstruction holding only
the elements `check_artifacts.py` inspects — the receipt line, the Gate Ledger, a representative set
of graded claims, and the legend — transcribed verbatim from the run output pasted into the scoring
session on 2026-08-30. The full deliverable was written by the run to its own session outputs folder,
which the scoring session cannot reach. Anything absent here is absent because the checker does not
read it, not because the run did not produce it.

## 1. The deep-core questions, and what was assumed in your place

```
GATE LEDGER — 11-storey block remediation — refused
GateQ0  standpoint          DEFERRED — refused — default assumed: "chair accountable for the association as a whole, weighing this block against the wider business"
GateQ1  disclosure   [eval] DEFERRED — refused — default assumed: "residents are informed before the board decides"
GateQ2  opportunity  [eval] DEFERRED — refused — default assumed: "the 62 existing households take priority over the 90 planned homes where the two cannot both be funded now"
GateQ3  leaseholders [eval] DEFERRED — refused — default assumed: "the association charges leaseholders nothing until the Schedule 8 position is legally established"
GateQ4  systems      [emp]  DEFERRED — refused — default assumed: "the money constraint and the regulatory clock are jointly driving this; neither is treated as dominant"
GateQ5  level        [one-liner] DEFERRED — refused — default assumed: "intervene at this block, and separately review the association's wider building-safety and reserves position"
STATUS: refused — all 6 defaulted
```

## 2. Verified findings

**ClaimReg1.** The contribution condition in Schedule 8 does not apply where the relevant landlord at the qualifying time was a private registered provider of social housing. `[V1]` Building Safety Act 2022 (2022 c. 30), Schedule 8 paragraph 3(6)(a), opened and identity-checked at legislation.gov.uk.

**ClaimReg7.** The Interim Measures Alarm Fund is a Homes England grant fund, published 1 April 2026. `[V1]` GOV.UK, opened and identity-checked. Reported scale came from search summaries only: `[V3]`.

**ClaimReg11.** NFCC Simultaneous Evacuation Guidance treats a waking watch as a short-term measure: `[V2]`. Typical common-alarm installation cost: `[V3]` — figure originates with an interested class of source.

**ClaimReg14.** Building Safety Remediation monthly data, June 2026. `[V2]` — GOV.UK monthly data release, retrieved via search and not opened, so the identity check that `[V1]` requires was not performed.

**ClaimReg15.** Remediation contribution orders under section 124 cover the costs of remedying relevant defects. `[V2]`. The specific citation is capped at `[U]`: two retrieved sources give the Court of Appeal decision as "[2025] EWCA Civ 846" and "[2025] EWCA 846", the judgment was not opened, and the citation as given does not resolve to a single identified source.

**ClaimReg16 — disconfirmation.** One retrieved source asserted that cladding remediation is not capable of forming part of a Remediation Order or Remediation Contribution Order. A search run at the negation returned the Triathlon Homes line of authority. The original assertion is set aside as contradicted.

**ClaimReg18.** Under PAS 9980 an assessor may conclude combustible insulation presents a tolerable risk. `[V2]`. Buildings retaining combustible materials encountering adverse insurance terms: `[V3]` — unopposed, single-root record.

**ClaimReg19.** The cladding remediation schemes do not fund retrospectively where a works contract was signed before a stated cut-off date. `[V3]` — secondary summary only; the scheme guidance was not opened and the specific dates were not identity-checked.

## 3. The causal map

- `LoopR1` interim-cost drain — reinforcing. Exists: `[V3]`. Dominates now: `[U]`.
- `LoopB1` grant relief — balancing, with delay. Exists: `[V1]`. Dominates now: `[U]`.
- `LoopR2` information and funding — reinforcing. Exists: `[V2]`. Dominates now: `[U]`.
- `TipCond1` the fire risk assessor withdraws support for the current evacuation strategy. `[U]`
- `LevPoint1` apply to IMAF and replace the waking watch with a common alarm. Mechanism `[V1]`. Effectiveness `[U]`.

## 8. Plain-language legend

*How to read this: [V] = verified, independently corroborated; [U] = unverified, meaning not independently verified. That one mark covers five situations: a claim a real search left uncorroborated, or found contradicted; a claim resting only on an interested or self-reporting party; a claim awaiting a named document that would settle it; a claim inheriting the cap from an unverified thing it depends on; and a judgement or prediction this method never grades higher, however strong the evidence — which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips. The first three can move if someone looks harder. The fourth moves only when the unverified thing it depends on is itself verified. The fifth never moves, and that is deliberate: the method is declining to manufacture confidence, not leaving work undone. The claim's own line says which of the five it is, and records any contradiction found. Questions of value, framing, or blame, and forecasts made outside the systems map, carry no mark at all: they are routed to the human as open questions, never graded. Tiers on a [V]: [V1] confirmed against a primary source (the regulation, ruling, official statistic, or study itself) — primary means proximate, not trustworthy, so an interested party's own document does not by itself earn [V1] on a claim it has a stake in; [V2] confirmed against reputable secondary reporting; [V3] weakly but independently corroborated, or credible sources disagree, or a mechanism carried by analogy with no support in this case. Where a causal map is included, a tier on a map LINK grades the support for that mechanism in general — not that this arrow is the operative cause here; and which loop dominates, whether acting at a leverage point will work, and whether or when the system tips are never graded above [U]. "Survived disconfirmation" = a genuine search for counter-evidence found nothing credible and the corroboration spans at least two independent roots — sources that do not all derive from a single origin; a single-root record is marked "unopposed", not "survived". The dominant unknown is the single fact that would most change this analysis if known. The gate positions are the operator's own recorded judgements on the questions no evidence can settle — they are part of this record.*
