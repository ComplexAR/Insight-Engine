IE 1.1.3 · host Claude Cowork (Claude desktop app) · model Claude Opus 5 (as identified in this session's environment; treat as a claim, not a fact) · SEARCH y PERSIST y MULTI y CODE y · declared 2026-08-31 · enforce: host-mechanism · gate: 6/6 resolved (1 positions, 5 deferred — standing) · verification: performed · legend: attached

# Which day centre to close — decision analysis

**Problem statement.** A charity in England must close one of two day centres on cost grounds. The eastern centre serves more people; the western centre serves people with no alternative within twenty miles. The board decides on Friday; the operator is an external adviser writing the recommendation. Marked as assumptions, because they were not supplied: the client group and service type at each site, all figures (headcount, attendance, unit cost, deficit size, reserves), the commissioning position, the property and restricted-fund position, and whether any consultation has taken place.

---

## 1. The deep-core questions, and the operator's recorded positions

The operator answered GateQ0, then instructed that the remaining questions be noted as unanswered and the brief written, with the outstanding questions to be worked through afterwards. That is recorded as a **standing deferral**, not as a refusal and not as pressure: the instruction disposes of the questions rather than merely demanding the output. Each deferred line names the default assumption the call embeds in its place. Answering any of them voids the call, and the brief is re-derived.

```
GATE LEDGER — day-centre-closure — 6/6 resolved (1 positions, 5 deferred)
GateQ0  standpoint                       POSITION: "External adviser, no stake"
GateQ1  whose loss counts      [eval]    DEFERRED — logged 2026-08-31 — standing deferral — default assumed: "the graver harm is losing the only service within reach, not losing a preferred service where substitutes exist"
GateQ2  binary is fixed        [eval]    DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "the binary is accepted as the operator stated it, and the unexamined third options are recorded as a reservation the board must actively reject rather than silently pass over"
GateQ3  who gets a say         [eval]    DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "no user or carer consultation has happened; a decision in principle may be taken on Friday but must not be implemented before consultation"
GateQ4  what drives the money  [emp]     DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "the deficit is structural rather than one-off, so a single closure does not by itself return the charity to surplus"
GateQ5  intervention level     [one-liner] DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "we intervene at the level the board asked about — which site — and the funding-model question is flagged, not answered"
STATUS: 0 OPEN — gate resolved by standing deferral
```

### The questions as they would have been asked

So you can see what was deferred on your behalf, and answer any of them later.

**GateQ1 [eval] — whose loss counts more.** Closing east takes a service away from more people, most of whom have somewhere else to go. Closing west takes away the only service within twenty miles from fewer people. Which does the charity treat as the more serious loss: total people served, the position of the worst-off, or the depth of need at each site? *This is the question the call turns on. No evidence settles it.*

**GateQ2 [eval] — is the binary legitimately fixed.** You told me one must close. Is that a constraint set by a funder or a lease, or is it the board's own framing of its options? If it is the board's framing, does the recommendation accept it, or put a third option back to them?

**GateQ3 [eval] — who gets a say before Friday.** Do the users and carers of both sites hear about this before the board votes, or after? A decision taken and then consulted on is a different act from a decision consulted on and then taken, and the charity regulator's own guidance bears on which one this is.

**GateQ4 [emp] — what is actually driving the money.** Is the deficit a demand-and-cost problem that closing one site solves, or a funding-model problem that will reappear next year at the surviving site? *This one is empirical, not evaluative: it is a judgement the evidence cannot settle yet rather than one your values settle, and it is revisable if figures arrive.*

**GateQ5 [one-liner] — intervention level.** At what level do we intervene: this problem, or the problem it is a symptom of?

---

## 2. Verified findings

### Verification register

**ClaimReg1 [V1]** — In England the local authority must meet an adult's eligible needs for care and support once it has made a determination under s.13(1), subject to residence and financial conditions. *Source: Care Act 2014 c.23, s.18, legislation.gov.uk — opened and identity-checked against the Act, year and section cited.* Disconfirmation: a negation search found no credible authority that this duty ceases when a provider closes; s.48 points the other way. Corroboration spans the statute and independent secondary explanation (SCIE, LGA). **Survived disconfirmation.**

**ClaimReg2 [V1]** — Where a CQC-registered provider becomes unable to carry on a regulated activity **because of business failure**, the local authority must meet the needs that provider was meeting, regardless of ordinary residence, assessment, or eligibility. *Source: Care Act 2014 c.23, s.48, legislation.gov.uk — opened and identity-checked.* **Load-bearing limitation, and it cuts against the charity:** s.48 is triggered by business failure, not by a solvent charity choosing to close a site. A planned closure does not switch on the s.48 safety net; only the ordinary s.18 route applies, and only for those with assessed eligible needs.

**ClaimReg3 [V1]** — The public sector equality duty binds public authorities and, separately, "a person who is not a public authority but who exercises public functions … in the exercise of those functions". *Source: Equality Act 2010 c.15, s.149(1)–(2), legislation.gov.uk — opened and identity-checked.*

**ClaimReg4 [V1]** — A care provider is deemed by statute to exercise a function of a public nature for Human Rights Act s.6(3)(b) purposes only where it provides "personal care in a place where the adult receiving the personal care is living", or "residential accommodation together with nursing or personal care", arranged or paid for by a listed authority under listed provisions. *Source: Care Act 2014 c.23, s.73(1)–(3), legislation.gov.uk — opened and identity-checked.* A day centre is on the face of the section neither limb.

**ClaimReg5 [U]** — It follows that this charity's day-centre provision is probably outside the s.73 deeming provision, so the charity is probably not a public authority for HRA purposes in respect of it, and the public-law duties in ClaimReg1–ClaimReg3 bind the commissioning council rather than the charity. *[U] — situation 4: inherits the cap from unverified things it depends on. What the two centres actually do, how they are registered, and how they are funded were not supplied. Document that would settle it: the CQC registration status of each site and the commissioning contract.* This is the most consequential legal finding and it runs opposite to the intuition that a charity closing a care service is exposed to judicial review of its own decision.

**ClaimReg6 [V2]** — In *YL v Birmingham City Council* [2007] UKHL 27 the House of Lords held, by 3:2, that a private care home providing accommodation and care under contract with a local authority was not exercising functions of a public nature under HRA s.6, distinguishing the arrangement of care (governmental) from its provision (not inherently so). *Sources: Practical Law case note; Mental Health Law Online; CASCAIDR — three independent secondary roots.* **Weakness recorded: the judgment itself was not opened in this run, so this does not earn [V1]; the citation is reported consistently by all three, but I did not check the primary document's own identifiers.** Disconfirmation: **survived** — the reversal by Health and Social Care Act 2008 s.145, replaced by Care Act 2014 s.73, is a targeted statutory carve-out for residential and in-home personal care, not a general reversal of the reasoning.

**ClaimReg7 [V2]** — *R (Moseley) v Haringey LBC* [2014] UKSC 56 endorsed the Gunning principles as embodiments of fairness in consultation: consultation at a formative stage; sufficient reasons for intelligent consideration; adequate time; and conscientious consideration of the product. *Sources: Bindmans; UK Human Rights Blog; Law Gazette — independent secondary reporting.* **Weakness recorded: the BAILII copy of the judgment timed out on retrieval in this run and was not read, so this is graded on secondary reporting, not on the judgment.** Note that this constrains the **council**, not the charity, unless the charity is exercising a public function (see ClaimReg5).

**ClaimReg8 [V3]** — In *Draper v Lincolnshire County Council* [2014] EWHC 2388 (Admin) a closure decision was successfully challenged in part because an alternative option offered in a consultation response — a charity's offer to run the service — was not conscientiously considered. *Source: Local Government Lawyer.* **Weakness recorded: single secondary root; the judgment was not opened.** Disconfirmation: **unopposed — single-root record**, not survived.

**ClaimReg9 [V1]** — The Charity Commission's decision-making guidance requires trustees to take account of "the options available" and "the costs, risks, and benefits of all options, including if you decide to not do anything", and "the impact on beneficiaries and other stakeholders of all options". *Source: Charity Commission, Decision-making for charity trustees (CC27), updated 9 September 2024, principle 4 — opened and quoted verbatim from the regulator's own guidance.*

**ClaimReg10 [V1]** — The same guidance states: "You should usually consult stakeholders about important decisions, especially when the outcome will significantly affect them. This might include, for example, your charity's beneficiaries. Make sure that the people you consult know that the trustees will make the final decision." *Source: CC27, principle 3, "Speaking to stakeholders" — opened and quoted verbatim.* This is a regulator expectation on the charity itself, and it does not depend on whether the charity exercises a public function.

**ClaimReg11 [V3]** — Older and disabled people are disproportionately likely to experience transport isolation, and service use falls as distance rises ("distance decay"), with rural bus reductions documented as reducing access to health and community services. *Sources: Age UK report on rural bus services; parliamentary written evidence on passenger transport in isolated communities; LGA briefings on rural bus services.* **Weaknesses recorded: the strongest single source is an interested party advocating for older people, so it cannot carry [V1] on a claim it has a stake in; and these were read via search summaries rather than the source documents themselves.** Independent corroboration exists across the parliamentary and LGA material, which is why this is [V3] rather than [U].

**ClaimReg12 [U]** — Every case-specific quantity: users at each site, attendance, need intensity, unit and site costs, the deficit, free reserves, redundancy exposure, lease and title, restricted funds, area-of-benefit clauses, commissioning contracts and notice terms, consultation status, and the protected characteristics of each cohort. *[U] — situation 3: awaiting named documents that would settle it. Documents: the board paper with per-site profit and loss; the commissioning contract and its notice terms; title or lease for each building; the restricted-funds schedule; and the governing document.*

**ClaimReg13 [U]** — "No alternative within twenty miles" of the western site, and the existence of usable alternatives near the eastern site. *[U] — situation 3: party-held and asserted in the framing; the capacity of the eastern alternatives to absorb displaced users is asserted nowhere. Document: a provision audit mapping each alternative with its current spare capacity and travel time.*

### Findings

**Find1 — Closing either site transfers the cost rather than removing it, and the two transfers are measured on different instruments.** Closing east displaces users onto other providers: visible, countable, and comparable. Closing west displaces need onto unpaid carers, longer journeys and later crisis presentations: largely invisible and uncounted. A board comparing the two on the measured figures will systematically under-count the western closure. This is the second-order finding and it survives the best opposing reading. *Rests on ClaimReg1 [V1], ClaimReg11 [V3], and ClaimReg13 [U].* **Opposing reading kept in view:** spread over more people, the aggregate welfare loss from closing east may exceed the concentrated loss from closing west even if each person loses less; the finding is not that west wins, it is that the two costs are not measured on the same instrument.

**Find2 — The legal exposure is probably not where a board would look for it.** The consultation and equality duties that a closure of this kind normally attracts sit on the commissioning local authority, not on a charity delivering day services, because the s.73 deeming provision does not reach a day centre and *YL* left pure service provision outside HRA s.6. *Rests on ClaimReg4 [V1], ClaimReg5 [U], ClaimReg6 [V2], ClaimReg7 [V2].* What does bind the charity directly is charity law: CC27's requirement to consider the full option set, and its expectation that beneficiaries are usually consulted on decisions that significantly affect them (ClaimReg9, ClaimReg10, both [V1]). A board that assumes it faces judicial review risk may prepare the wrong defence and neglect the one that actually applies.

**Find3 — The binary is the part of the framing that most deserves scrutiny, and charity law says so.** "One of two must close" removes from view: reducing both to part-time; transferring one site to another provider or a community trust; renegotiating the commissioning contract; merger; and doing nothing while cutting central cost. CC27 requires trustees to weigh "the options available" and "the costs, risks, and benefits of all options, including if you decide to not do anything" (ClaimReg9 [V1]), and *Draper* [V3] is the cautionary example of a closure disturbed because a third-party offer to run the service was not conscientiously considered. **Opposing reading, and it narrows the finding:** you have stated the binary is fixed, and re-opening a settled constraint wastes the board's Friday. The finding therefore survives in narrowed form — work inside the binary, but put the third options on the record as a reservation the board actively rejects rather than silently passes over.

**Find4 — "More people" and "twenty miles" are different kinds of quantity and cannot be traded off directly.** Headcount is a gameable proxy: attendances, contact hours, and need intensity can rank the two sites differently. Twenty miles is a threshold, not a distance: for a non-driving disabled or older person, an unreachable service is not a worse service, it is no service. Both numbers are prominent, unsourced, and doing heavy work in the framing. *Rests on ClaimReg11 [V3] and ClaimReg13 [U].*

**Find5 — Deprioritised issues recovered on the counter-sweep.** Redundancy costs are a first-year cash outflow that can exceed the first-year saving and invert which closure is cheaper. If a site is transferred rather than closed, TUPE applies to its staff. And the charity's governing document may state an area of benefit: closing the western site could put the charity's activity outside its own stated objects, which converts a management decision into a charity-law one. All *[U] — situation 3: awaiting the governing document, the redundancy schedule, and the property terms.*

**Find6 — No party here can simply impose its preference, so this is not a power problem.** The commissioner holds real leverage if it funds either site, but the board holds the closure decision. The absent parties — users, carers, staff — hold none, which is the reason the consultation expectation in ClaimReg10 [V1] carries the weight it does rather than being a formality.

**Adverse findings and right of reply.** No finding here is adverse to a named individual or organisation, and no official body has attributed fault to anyone in this matter. The charity's board has not been offered an opportunity to respond to Find3, because the board is the audience for it rather than its subject.

---

## 3. Systems investigation

**Telemetry — signs fired: 5 of 6.** Feedback and circular causation; accumulation (reserves draining, unmet need building); material delays (deterioration and crisis presentation lag closure by months); multiple interacting actors; self-fulfilling expectations. Regime shift is possible but not established. The pass was warranted.

**Router check on presupposed entities.** Three things the question presupposes rather than establishes were run through the three-bucket router before drawing: the alternative provision near the eastern site (party-held, [U], caps everything downstream of it); the deficit itself (party-held, [U]); and the Friday deadline (party-held, [U]).

**The map's headline limitation, stated once.** Every variable below is party-held: no figure, document or user-level datum was supplied. Under the inheritance rule, **every link in this map caps at [U]**, however well attested the mechanism is in general. A real mechanism operating on an unverified object is an unverified claim. The map is a hypothesis about structure, offered to be falsified when the figures arrive.

### Variables

| ID | Variable | Type |
|---|---|---|
| Node1 | Charity free reserves | stock |
| Node2 | Users attending charity day services | level |
| Node3 | Unmet need in the western catchment | stock |
| Node4 | Unpaid carer load in the western catchment | level |
| Node5 | Commissioner confidence in the charity as a provider | level |
| Node6 | Fundraising and legacy income | rate |
| Node7 | Staff retention across both sites | level |
| Node8 | Council and NHS downstream cost (crisis placements, admissions) | level |

### Links

- **Link1.** `Node2 --(+)--> Node6` [U] — local attendance sustains place-attached giving and legacies. *Both ends party-held.*
- **Link2.** `Node6 --(+)--> Node1` [U] — income accrues to reserves. *Both ends party-held.*
- **Link3.** `Node1 --(+, delay)--> Node2` [U] — reserves fund capacity, which sustains attendance; delay of one budget cycle. *Both ends party-held.*
- **Link4.** `Node2 --(−)--> Node3` [U] — attendance suppresses unmet need in the catchment. *Both ends party-held.*
- **Link5.** `Node3 --(+, delay)--> Node4` [U] — unmet need transfers to unpaid carers; the delay is the period before informal capacity is exhausted. *Both ends party-held.*
- **Link6.** `Node4 --(+, delay)--> Node8` [U] — carer breakdown drives crisis placements and admissions; delay of months to years. *Both ends party-held.*
- **Link7.** `Node8 --(−)--> Node5` [U] — visible downstream cost erodes commissioner confidence in the closure and in the charity. *Both ends party-held.*
- **Link8.** `Node5 --(+, delay)--> Node1` [U] — commissioner confidence sustains contract income; contract cycles impose the delay. *Both ends party-held.*
- **Link9.** `Node7 --(+)--> Node2` [U] — staff continuity sustains attendance and quality. *Both ends party-held.*
- **Link10.** `Node1 --(+)--> Node7` [U] — reserves fund pay and stability. *Both ends party-held.*
- **Link11.** `Node1 --(+, delay)--> Node2` — distinct from Link3: falling reserves force capacity cuts, which is the closure decision itself. [U] *Both ends party-held. Polarity checked: reserves down produces capacity down, so this is a positive link despite the decreasing language.*
- **Link12.** `Node2 --(−)--> Node1` [U] — running capacity consumes reserves. *Both ends party-held.*

Links 1–3 and Link12 mean Node2 acts on Node1 in **both** directions: capacity brings income and capacity costs money. Which sign nets out is precisely the dominance question below, and it is not gradable.

### Feedback loops

- **LoopR1** — "capacity sustains income": `Link1, Link2, Link3`. Exists [U]. Dominates-now [U].
- **LoopR2** — "staff spiral": `Link10, Link9, Link1, Link2`. Exists [U]. Dominates-now [U].
- **LoopR3** — "the cost comes back": `Link4, Link5, Link6, Link7, Link8, Link3`. Two negative links, so the loop is reinforcing: cutting capacity raises unmet need, carer load and downstream public cost, which erodes commissioner confidence and contract income, which cuts capacity further. Exists [U]. Dominates-now [U].
- **LoopB1** — "cut to survive": `Link11, Link12`. The balancing loop the board is relying on: falling reserves force capacity cuts, and cutting capacity reduces cost, restoring reserves. Exists [U]. Dominates-now [U].

**The whole decision is a bet that LoopB1 outruns LoopR1 and LoopR3.** Which of them currently dominates is never graded above [U] and is routed to you as GateQ4, deferred.

**Loops closed but not drawn** — one line each, *ungraded self-report*: a reputational loop from Node5 back to Node6 (commissioner and community views affect giving as well as contracts) was closed and not drawn, to stay inside the loop cap. Different runs of this case would drop different loops, so this names one run's choice, not the map's boundary.

### Tipping conditions

Conditions to watch, never dates or probabilities. All [U] — situation 5.

- **TipCond1** — The commissioner reallocates the remaining contract to another provider following the closure. *Hard to reverse.*
- **TipCond2** — Attendance at the surviving site falls below the level at which its own unit cost holds, making a second closure the next question. *Hard to reverse.*
- **TipCond3** — Key staff leave the surviving site during the announcement window, so it cannot absorb transfers. *Reversible, at cost.*
- **TipCond4** — A restricted fund, endowment, trust or area-of-benefit clause attached to one site turns its closure into a Charity Commission matter rather than a board decision. *Irreversible once triggered.*

### Emergence

Once "we are closing a site" becomes public, users and staff at **both** sites act as though theirs may be next. Attendance and retention can fall at the surviving site, which is the site the financial case depends on. The shared expectation is itself a causal variable, not a commentary on one.

### Leverage points, ranked

1. **LevPoint1 — the option set put to the board.** Mechanism [V1]: CC27 principle 4 requires trustees to weigh "the options available" and "the costs, risks, and benefits of all options, including if you decide to not do anything". Effectiveness [U].
2. **LevPoint2 — the commissioner's position, engaged before the vote rather than after.** Mechanism [U]. Effectiveness [U].
3. **LevPoint3 — the gap between decision and implementation, and how the announcement is made.** Acts on the emergence above and on TipCond3. Mechanism [U]. Effectiveness [U].
4. **LevPoint4 — transport for the western catchment as a substitute for the western building.** Breaks Link4 without keeping the site. Mechanism [V3] — *weakness: analogy from rural transport evidence, with no in-case support*; the application here inherits [U]. Effectiveness [U].
5. **LevPoint5 — the property and restricted-funds terms of both sites.** Acts on TipCond4. Mechanism [U]. Effectiveness [U].

### The missing driver

The most plausible driver **not** in this map that would change the call if it were real: **the property.** If one site is freehold with disposal value and the other is leased with a liability that survives closure, or if either lease has a break clause on an unhelpful date, the financial logic can invert entirely. No node above carries it, and no check on the arrows drawn would catch it.

### Boundary disclosure

This map adopts the board's framing: which site to close. Materially affected but absent from every source it was built from: users at both sites, unpaid carers, and staff — none consulted, no user-level data supplied. Under the western users' framing the central variable would not be the charity's reserves but their own access, with the charity as one supplier among a set that includes the council's s.18 duty; that framing puts "what must the council provide if we close?" ahead of "which site do we close?", and it would rank LevPoint2 first. This is a **value judgement about where the boundary was drawn, distinct from [U] evidential uncertainty**, and it is carried into what-to-verify-first below.

---

## 4. Decision brief

### (a) The call

**This is a wicked problem, so what follows is a provisional stance, not a verdict.** The deep core dominates: the question that decides it is a distributive value judgement (GateQ1), and it was deferred; and every case-specific quantity is unverified.

**Provisionally: recommend closing the eastern centre, as a decision in principle whose implementation is conditional.** This prioritises protection of the worst-off — the people for whom closure means no service at all — at the expense of aggregate reach, which is the value the eastern site serves. It rests on the default assumed for GateQ1, not on a position you took.

The recommendation to the board should carry three conditions on its face, because without them the decision is not safe to implement: written confirmation of current spare capacity at the eastern alternatives (ClaimReg13); a property, restricted-funds and governing-document check on both sites (TipCond4, Find5); and the deficit arithmetic showing what one closure actually leaves (GateQ4). It should also record, as a reservation the board actively rejects rather than silently passes, the options the binary excludes — part-time operation of both, transfer of one site to another provider, contract renegotiation — because CC27 principle 4 requires the option set to be weighed and *Draper* shows what happens when a third-party offer is not (Find3).

**Explicitly re-openable.** What re-opens it is listed in (e). Offered as a discrete trigger list for handoff to `track`:

| Indicator | What it would change |
|---|---|
| Board records a position on GateQ1 favouring aggregate reach | The call reverses to the western centre |
| Capacity audit of eastern alternatives returns thin or nil | The call reverses |
| Any third option becomes viable | The call is withdrawn; the option set goes back to the board |
| Restricted fund, endowment or area-of-benefit clause found on either site | The call is void; that closure may not be the board's to decide |
| Deficit arithmetic shows one closure is insufficient | The call is withdrawn |
| TipCond1 or TipCond2 fires after implementation | The closure has not solved the problem it was chosen to solve |

### (b) Confidence basis, and the action contingency

**Confidence in the fact-chain: the legal spine is strong and the case is empty.** The statutory findings are [V1], opened and identity-checked (ClaimReg1, ClaimReg2, ClaimReg3, ClaimReg4), as is the regulator's guidance (ClaimReg9, ClaimReg10). **The weakest load-bearing grades the call leans on are ClaimReg12 and ClaimReg13, both [U] — every quantity in the decision — and ClaimReg11 at [V3], which is where the isolation harm is evidenced and whose strongest single source is an interested party.** This is evidence-quality transparency, not a scored probability: the call is built on a verified legal frame and an unverified factual one.

**Action contingency — separately, what must hold true after acting.** Even if every premise above were [V1], the closure succeeds only if: the eastern alternatives actually absorb the displaced users at tolerable travel and cost; the first-year saving survives redundancy, lease and dilapidation costs; the surviving site retains its staff through the announcement window (TipCond3); and the commissioner does not respond by reallocating the remaining contract (TipCond1).

### (c) The dominant unknown

**Whether closing either single site actually closes the deficit — that is, whether this is one decision or the first of several.** This replaced the initial candidate ("what does each site cost?") during verification, because if it is the first of several, the distributive question changes shape: the board would not be choosing which community to protect, it would be choosing the order in which they are lost, and the answer to GateQ1 would carry different consequences.

### (d) What to verify first

**The property, restricted-funds and governing-document position of both sites** — title or lease, break clauses and dilapidations, any endowment or restricted fund tied to a site, and any area-of-benefit clause. It is roughly half a day of document review, entirely within the charity's control, needs no external cooperation, and is the one check that can make Friday's decision **void** rather than merely wrong (TipCond4, Find5). Second, and nearly as cheap: written confirmation of spare capacity at the eastern alternatives, since the whole case for closing east rests on an assertion no one has tested (ClaimReg13).

### (e) What would flip the call

Each as a first-person conditional.

- I am treating the graver harm as loss of the only service within reach; **if the board's position is aggregate reach, the call reverses to closing the western centre.** This is GateQ1, deferred — the single position the call most depends on.
- I am treating the eastern alternatives as having real current capacity; **if they do not, the call reverses**, because closing east then produces the same harm it was chosen to avoid.
- I am treating the binary as fixed; **if a third option is available, the call is withdrawn** and the option set goes back to the board.
- I am treating both sites as unencumbered; **if either carries a restricted fund, endowment or area-of-benefit clause, the call is void** — that closure may not be the board's to decide (TipCond4).
- I am treating one closure as sufficient to close the deficit; **if it is not, the call is withdrawn.** The Step 7 resilience check varied this jointly with the fixed-binary assumption and found the call does not survive both being false: the recommendation then becomes "do not choose a site on Friday; put the option set and the deficit arithmetic back to the board".

**Resilience-check coverage, stated plainly.** I varied four assumptions together: the binary is fixed (Assump1); one closure closes the deficit (Assump2); the eastern alternatives have capacity (Assump3); neither site is encumbered (Assump4). The call does not survive Assump1 and Assump2 both being false; it inverts if Assump3 and Assump4 are both false; it weakens to a conditional if Assump3 alone fails. I did **not** vary the accuracy of your problem statement itself (that east serves more and west is isolated), nor the assumption that the charity survives either choice. What fraction of the assumption space that covers is unknowable, and I am not implying one.

**This call rests on the operator's recorded gate position and on five defaults.** The only position taken is GateQ0 (external adviser, no stake), which affects the reading of the analysis but not its content. GateQ1 through GateQ5 were resolved by standing deferral, and the defaults named in the ledger are embedded in the call. **Answering any of them voids the call and the brief is re-derived** — GateQ1 in particular, since it is what selects between the two sites.

---

## 5. Sources

- [Care Act 2014, s.18 — Duty to meet needs for care and support](https://www.legislation.gov.uk/ukpga/2014/23/section/18)
- [Care Act 2014, s.48 — Temporary duty on local authority](https://www.legislation.gov.uk/ukpga/2014/23/section/48)
- [Care Act 2014, s.73 — Human Rights Act 1998: provision of regulated care or support etc a public function](https://www.legislation.gov.uk/ukpga/2014/23/section/73)
- [Equality Act 2010, s.149 — Public sector equality duty](https://www.legislation.gov.uk/ukpga/2010/15/section/149)
- [Charity Commission, Decision-making for charity trustees (CC27), updated 9 September 2024](https://www.gov.uk/government/publications/decision-making-for-charity-trustees-cc27/decision-making-for-charity-trustees)
- [YL v Birmingham City Council [2007] UKHL 27 — Practical Law case note](https://uk.practicallaw.thomsonreuters.com/5-368-8966)
- [YL v Birmingham City Council [2007] UKHL 27 — Mental Health Law Online](https://www.mentalhealthlaw.co.uk/YL_v_Birmingham_City_Council_(2007)_UKHL_27)
- [R (Moseley) v Haringey LBC [2014] UKSC 56 — Bindmans commentary](https://www.bindmans.com/news-insights/blogs/putting-moseley-in-a-box-recent-cases-on-consultation/)
- [R (Moseley) v Haringey LBC [2014] UKSC 56 — UK Human Rights Blog](https://ukhumanrightsblog.com/2014/10/29/consultation-duty-gets-to-the-supreme-court/)
- [Public sector consultations, including Draper v Lincolnshire CC [2014] EWHC 2388 (Admin) — Local Government Lawyer](https://localgovernmentlawyer.co.uk/governance/314-governance-a-risk-articles/55748-public-sector-consultations)
- [Age UK, Missed opportunities: the impact on older people of cuts to rural bus services](https://www.ageuk.org.uk/siteassets/documents/reports-and-publications/reports-and-briefings/active-communities/rb_may13_bus_services_in_rural_areas.pdf)
- [Written evidence on passenger transport in isolated communities, UK Parliament](https://committees.parliament.uk/writtenevidence/45295/html/)
- [Key Care Act duties for assessment and determination of eligibility — SCIE](https://www.scie.org.uk/assessment-and-eligibility/key-duties/)

---

## 6. Plain-language legend

*How to read this: [V] = verified, independently corroborated; [U] = unverified, meaning not independently verified. That one mark covers five situations: a claim a real search left uncorroborated, or found contradicted; a claim resting only on an interested or self-reporting party; a claim awaiting a named document that would settle it; a claim inheriting the cap from an unverified thing it depends on; and a judgement or prediction this method never grades higher, however strong the evidence — which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips. The first three can move if someone looks harder. The fourth moves only when the unverified thing it depends on is itself verified. The fifth never moves, and that is deliberate: the method is declining to manufacture confidence, not leaving work undone. The claim's own line says which of the five it is, and records any contradiction found. Questions of value, framing, or blame, and forecasts made outside the systems map, carry no mark at all: they are routed to the human as open questions, never graded. Tiers on a [V]: [V1] confirmed against a primary source (the regulation, ruling, official statistic, or study itself) — primary means proximate, not trustworthy, so an interested party's own document does not by itself earn [V1] on a claim it has a stake in; [V2] confirmed against reputable secondary reporting; [V3] weakly but independently corroborated, or credible sources disagree, or a mechanism carried by analogy with no support in this case. Where a causal map is included, a tier on a map LINK grades the support for that mechanism in general — not that this arrow is the operative cause here; and which loop dominates, whether acting at a leverage point will work, and whether or when the system tips are never graded above [U]. "Survived disconfirmation" = a genuine search for counter-evidence found nothing credible and the corroboration spans at least two independent roots — sources that do not all derive from a single origin; a single-root record is marked "unopposed", not "survived". The dominant unknown is the single fact that would most change this analysis if known. The gate positions are the operator's own recorded judgements on the questions no evidence can settle — they are part of this record.*

**Reliability caveat.** This analysis rests on a verified legal frame and an entirely unverified factual one: no figure, document or user-level datum about either centre was supplied, so every quantity in it is [U], and the harm evidence it leans on (ClaimReg11) is [V3] whose strongest single source is an interested party. The call is a provisional stance selected by a default assumption, not by a position you took.
