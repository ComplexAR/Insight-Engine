IE 1.1.3 · host Cowork (Claude desktop) · model claude-opus-5 (declared by the host environment, not self-identified in session — treat as uncertain) · SEARCH y PERSIST y MULTI y CODE y · declared 2026-08-31 · enforce: host-mechanism · gate: 6/6 resolved (1 positions, 5 deferred — standing) · verification: performed · legend: attached

# Closing one of two day centres — analysis and decision brief

**Problem statement.** A charity in England providing day services for older people and people with dementia must close one of two day centres. The eastern centre serves more people; the western centre serves people with no alternative within twenty miles. The board has fixed that one of the two must close and wants a recommendation on Friday. Owner: the board. Reader: the board, via an adviser with no stake in either site.

**Triage.** Not routine. Irreversible for the people who lose the service; binds parties not in the room; material dependency; legal and regulatory exposure; contested values. Full method run.

**Scoping.** Four of five questions answered (user group, jurisdiction, option set, success criteria). The fifth — party-held figures — was not answered. No attendance data, no financial data, no tenure or trust information, and no board papers were supplied. Everything that depends on those is capped at [U] throughout.

---

## 1. The gate — deep-core questions and the operator's recorded positions

The operator answered the standpoint question, was put the first judgement question, and then instructed: *"Produce the full brief now, and take the remaining questions later."* That is a standing deferral. It is recorded as such, with the default assumption each deferred line embeds in the call. Questions GateQ2 to GateQ5 were never put, and that is recorded separately, because a choice never offered is not a choice declined.

```
GATE LEDGER — day-centre-closure — 6/6 resolved (1 positions, 5 deferred)
GateQ0  standpoint                         POSITION: "adviser with no stake"
GateQ1  closure criterion         [eval]   DEFERRED — logged 2026-08-31 — standing deferral — default assumed: "the operator's own scoping criterion, maximise the number of clients still being served, applied to the number served AFTER closure rather than before it"
GateQ2  consultation before Friday [eval]  DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "no consultation with beneficiaries has happened or will happen before the board decides"
GateQ3  the fixed binary          [eval]   DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "the binary stands; options other than closing one of the two sites are out of scope"
GateQ4  what is driving this now  [emp]    DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "no view taken on which loop in the causal map currently dominates; the call is written to be insensitive to that question"
GateQ5  intervention level    [one-liner]  DEFERRED — logged 2026-08-31 — standing deferral, question not put — default assumed: "intervene at the presented problem, which centre closes, not at the problem it may be a symptom of"
STATUS: 0 OPEN — gate resolved by standing deferral
```

### The questions as they would have been asked

Answering any one of these voids the call and the brief is re-derived.

**GateQ1 — the criterion.** When you weigh the two centres, what counts as the better outcome: the largest number of people still getting a service, or no one being left with nothing at all? In scoping you said "as many clients as possible being serviced". That is a real position, but it decides the question rather than answering it. *Example answer: "I can live with fewer people served; I cannot live with abandoning a group entirely."*

**GateQ2 — legitimacy and consultation.** Should a recommendation go to the board on Friday when nobody has asked the users of either centre, or their family carers, what closure would mean for them? The Charity Commission's guidance says trustees should usually consult those significantly affected, especially beneficiaries. *Example answer: "Friday is a decision to consult, not a decision to close."*

**GateQ3 — the binary.** The board has fixed that one of the two must close. Is that framing itself something the recommendation should accept, or something it should contest? *Example answer: "Accept it. The money is gone and pretending otherwise wastes the board's time."*

**GateQ4 — what is driving this now.** Is the immediate pressure the charity's finances, or the fact that a closure has effectively been signalled and attendance is already responding to it? These call for different responses and the evidence available cannot settle which is currently dominant. *Example answer: "It is the finances; nothing has been announced."*

**GateQ5 — intervention level.** Do we intervene at this problem — which centre closes — or at the problem it may be a symptom of, which is that the charity cannot fund its estate? *Example answer: "This problem. The wider question is next year's."*

---

## 2. Verified findings

### 2a. The finding the analysis turns on

**Find1 — Applied correctly, the operator's own criterion does not point where it appears to point.** [U] — situation: a judgement this method does not grade, resting on party-held quantities.

"Serves more people" describes the position **before** closure. The stated goal — as many clients as possible being served — is a statement about the position **after** closure. These are different quantities, and the gap between them is the whole decision.

Let **E** be the number of people the eastern centre serves, **W** the number the western centre serves, with E greater than W. Let **t** be the proportion of eastern users who would in fact be attending an alternative service some months after an eastern closure. The operator's own premise — no alternative within twenty miles of the western site — sets the western equivalent at approximately zero.

- People still served if the **east** closes: W + tE
- People still served if the **west** closes: E

Closing the east serves more people whenever **t > 1 − W/E**.

Worked: if the western centre serves 80 for every 100 the eastern serves, closing the east is better on this criterion whenever more than 20% of eastern users transfer. If the western serves 50 per 100, the threshold is 50%. If the western serves 20 per 100, the threshold is 80%.

Neither side of that inequality has been calculated. W/E comes from the charity's own attendance records. t is unknown and nobody has asked. On the operator's own criterion, the decision is arithmetic with two inputs, and both are missing.

Two limits on the rule, stated plainly. It treats one person served as one unit regardless of how much they need it or how often they attend; weighting by need or by attendance days changes the threshold. And t is never 1 even where alternatives exist on paper — see Find14.

### 2b. What the case asserts, and what grade it carries

**Find2 — "The eastern one serves more people" is unspecified and is a gameable measure.** [U] — situation: awaiting a named document that would settle it (the charity's attendance register). Registered users, distinct individuals attending in the last quarter, weekly attendances, and funded places are four different numbers that can rank the two sites differently. No figure was supplied.

**Find3 — "No alternative within twenty miles" is a claim about the current configuration of provision, not about geography.** [U] — same situation. Twenty miles is a precise number standing for something imprecise: a travel time that varies by transport, weather and frailty. What has not been tested is whether "no alternative" means no day service of any kind, no service of this kind, or no service with capacity.

**Find4 — Nobody has established that closing either site produces a net saving.** [U] — situation: awaiting named documents (management accounts, leases, staff contracts). Redundancy costs, lease exit and dilapidations, loss of attendance-linked fee income, and the loss of any rent from other users of the building all consume the saving. If the saving is near zero in year one, the binary itself collapses. This is the single omission most likely to be decisive and it is the cheapest to close.

### 2c. The legal position

**Find5 — There is no local-authority backstop if the charity closes a site voluntarily.** [V1] on the statute. Care Act 2014 s.48(1) applies only where a CQC-registered provider "becomes unable to carry on that activity **because of business failure**". A solvent charity choosing to close a site does not trigger it. Separately, a day centre for older people is generally outside CQC registration, because the regulated activity of personal care must be provided where the person lives [V2]. Either reason alone defeats s.48. The common assumption that the council will have to pick everyone up is wrong.

**Find6 — For users with a local-authority care and support plan, closure does trigger duties — on the council, not the charity.** [V1]. Care Act 2014 s.27(4) requires the authority to review and revise the plan where circumstances change, and s.27(5) requires it, where it proposes to change how it meets the needs, to "take all reasonable steps to reach agreement with the adult concerned". Users who self-fund or have no plan get none of this. The board should know which of its users are in which group, because the two groups face materially different outcomes.

**Find7 — The Friday timetable is in tension with the Charity Commission's decision-making guidance on three separate points.** [V1] — Charity Commission, CC27, updated 9 September 2024, applies to England and Wales. Principle 3 requires trustees to be sufficiently informed, and states: "You should usually consult stakeholders about important decisions, especially when the outcome will significantly affect them. This might include, for example, your charity's beneficiaries." Principle 4 requires them to take account of "the costs, risks, and benefits of all options, including if you decide to not do anything". Principle 7 requires them to "give enough time and consideration to your decision". A recommendation delivered on Friday, with no attendance data, no costed saving and no beneficiary consultation, does not satisfy any of the three.

**Find8 — The public sector equality duty may bind the charity directly.** [V1] on the statute; [U] on its application here — situation: inheriting the cap from an unverified thing it depends on. Equality Act 2010 s.149(2): "A person who is not a public authority but who exercises public functions must, in the exercise of those functions, have due regard to the matters mentioned in subsection (1)." Age and disability are both relevant protected characteristics under s.149(7), and dementia is a disability. Whether this charity exercises public functions turns on its commissioning arrangements, which were not supplied.

**Find9 — Employment law may make a Friday decision undeliverable regardless of its merits.** [V2] — consistent reputable secondary legal sources; the primary text of TULRCA 1992 s.188 was not read. Where 20 or more dismissals are proposed at one establishment within 90 days, collective consultation is triggered and no dismissal may take effect until at least 30 days have passed (45 days at 100 or more). Protective awards of up to 90 days' gross pay per affected employee are available for breach. If either site employs 20 or more, the closure date is set by law, not by the board.

**Find10 — Tenure may determine the answer independently of everything above.** [V2] on the regime; [U] on this charity — situation: awaiting a named document (the title and the trust instrument for each site). Disposals of charity land are regulated by Charities Act 2011 ss.117–121, and designated land or permanent endowment attracts further requirements and may need a Charity Commission order. If either building is held on trust for a specific purpose or locality, the board's freedom to choose may be narrower than it thinks.

### 2d. The evidence on day services

**Find11 — Day services reduce family-carer burden; their effect on time to residential admission is disputed.** [V3] — credible sources disagree. The systematic review literature on respite for carers of people with dementia reports improvement in carer burden across most day-care studies, but also reports that two studies found day care alone **accelerated** time to nursing home placement, while one methodologically stronger study of day care integrated with support and information found placement **delayed**. Weakness recorded: the primary articles could not be opened — PubMed and PubMed Central returned bot-detection challenges, which were not circumvented — so this rests on the search-level summary and is not identity-checked against the papers. It is capped at [V3] for that reason as well as for the disagreement. It matters because it cuts against the intuition that maximising day-service coverage automatically maximises welfare.

**Find12 — Travel distance is a real barrier to participation for older people, and it worsens sharply with age.** [V3] — weak independent corroboration. Reported figures indicate that around 45% of people over 80 experience some limit to their participation from lack of transport, against about 20% of those in their 70s and 15% in their 60s. Not identity-checked against the underlying dataset. The relevance is that "twenty miles" is not one distance: it is a much larger obstacle for the oldest and frailest users, who are also the ones a dementia day service exists for.

**Find13 — The closure announcement is itself a cause, not just a communication.** [U] — situation: a structural inference this method does not grade higher. Once users and families believe a site will close, attendance falls; falling attendance is then read as evidence the site was not needed. The decision manufactures its own justification. If anything has already been signalled to either site's users, current attendance figures are contaminated and cannot be used in the Find1 rule without adjustment.

**Find14 — Disconfirmation: displaced users do partially transfer.** [V3] — *disconfirmation partially succeeded; the counter-evidence stands but does not transfer to this setting*. A search run at the negation of "closure means loss of service" found a documented case (Slough) in which all users were re-assessed and those who wanted alternative provision were offered it locally, though some declined and others moved away from day care. This is genuine counter-evidence to the strong form of the claim, and it raises t above zero. It is a single urban borough with short travel distances, so it says little about a rural catchment with a twenty-mile radius; and it is a single root, so it is *unopposed*, not *survived*.

**Find15 — Every party who bears the cost of this decision is absent from it.** [U] — situation: a judgement this method does not grade. The users of both centres, their family carers, the staff, the alternative providers who would absorb transfers, and the local authority that would absorb any displaced residential cost are all materially affected and none is in the room. The board bears none of the cost of getting this wrong.

**Correction made during verification.** A search summary asserted that in 2014 the Supreme Court held a consultation on the closure of Haringey day care centres unlawful. That is false and it was not carried into this analysis. *R (Moseley) v London Borough of Haringey* [2014] UKSC 56 concerned a council tax reduction scheme. The Gunning consultation principles are real and the case is real; the day-centre subject matter attached to it was not. Recorded because it is the kind of confident, plausible, wrong fact this step exists to catch. Note also that the reported judicial review challenges to day centre closures are challenges to **councils**, not to charities, and do not transfer to this charity unless it is found to exercise public functions (Find8).

**Opportunity to respond.** The findings above that are adverse to a named party are adverse to the board, and to the local authority in Find5 and Find6. Neither was **offered the opportunity** to respond; this analysis was built from the operator's account alone.

**Power.** The board holds the framing power outright: it fixed the binary and it fixed Friday. No option in this brief that depends on the board agreeing to move either is something the board has any need to grant, and each is discounted accordingly.

---

## 3. Systems-investigation pass

*Telemetry: five of the six triggering signs fired — feedback, accumulation, material delays, multiple interacting actors, self-fulfilling expectations. Regime shift was not independently assessed. Pass warranted and run.*

**Entities checked before drawing.** The map's actors are the charity, the two user groups, family carers, staff, and the local authority. All are presupposed by the question rather than established by evidence; none was verifiable externally; all party-held quantities enter at [U] and every link resting on one is capped there.

### Variables

| ID | Variable |
|---|---|
| Node1 | Charity net financial position (stock; higher is healthier) |
| Node2 | Attendance at the site under threat |
| Node3 | Family-carer strain in the affected catchment (stock) |
| Node4 | Rate of transition of users into residential care |
| Node5 | Local-authority spend on this charity's client group |
| Node6 | Charity's standing with the local authority and local donors (stock) |
| Node7 | Travel time from user's home to the nearest surviving centre |
| Node8 | Staff retention at the site under threat |

### Links

- **Link1.** `Node1 --(+, delay)--> Node2` — [U] structural inference. Weaker finances produce closure signals, which reduce attendance before any closure occurs.
- **Link2.** `Node7 --(−)--> Node2` — [V3] *in-domain but weakly corroborated*. Longer travel reduces participation among older people (Find12); the specific link to day-centre attendance was not established.
- **Link3.** `Node2 --(+)--> Node1` — [U] *inherits the cap from a party-held fact*: whether income is attendance-linked is unknown.
- **Link4.** `Node2 --(−, delay)--> Node3` — [V3] *credible sources disagree* (Find11). Loss of day-service places raises carer strain.
- **Link5.** `Node3 --(+, delay)--> Node4` — [V3] *credible sources disagree* (Find11). Higher carer strain raises transitions into residential care; the literature also contains the opposite finding for day care specifically.
- **Link6.** `Node4 --(+)--> Node5` — [U] *inherits the cap*: depends on who funds these clients, which is party-held.
- **Link7.** `Node5 --(−, delay)--> Node6` — [U] structural inference. Displaced cost attributed to the closure damages standing with the commissioner.
- **Link8.** `Node6 --(+, delay)--> Node1` — [U] structural inference.
- **Link9.** `Node1 --(+)--> Node8` — [U] structural inference. Financial distress reduces staff retention at a threatened site.
- **Link10.** `Node8 --(+)--> Node2` — [U] structural inference.
- **Link11.** `Node5 --(+, long delay)--> Node1` — [U] structural inference. Rising residential cost creates pressure to commission prevention.

### Feedback loops

- **LoopR1 — decline spiral.** `Link1, Link3` (`Node1 --(+)--> Node2 --(+)--> Node1`). Exists: [U]. Dominates-now: [U].
- **LoopR2 — staff attrition spiral.** `Link9, Link10, Link3`. Exists: [U]. Dominates-now: [U].
- **LoopR3 — cost migration spiral.** `Link4, Link5, Link6, Link7, Link8, Link1`. Exists: [U]. Dominates-now: [U].
- **LoopB1 — commissioner backstop.** `Link4, Link5, Link6, Link11, Link1`. The same rise in local-authority residential spend that damages standing in LoopR3 also creates the case for funding prevention. The two paths have opposite signs and run from the same node; which one operates is not settled by anything available. Exists: [U]. Dominates-now: [U].

Loop cap not binding: four drawn of five permitted. Polarity re-checked on Link4, the one decreasing-language link.

### Tipping conditions

Stated as conditions to watch. No dates, no probabilities.

- **TipCond1** — attendance at the surviving site falls below the level at which the transport round is viable, so rural users lose access while the centre is still open. Reversibility: hard. [U]
- **TipCond2** — the affected catchment's informal network (volunteer drivers, users' own social ties, the carers who know each other) disperses. It does not reassemble on reopening. Reversibility: irreversible. [U]
- **TipCond3** — the closed site's premises are sold or the lease surrendered. Reversibility: irreversible. [U]
- **TipCond4** — enough experienced staff leave that the surviving site cannot absorb transfers. Reversibility: hard. [U]

### Emergence

The closure decision is self-validating. Anticipated closure reduces attendance; reduced attendance is then evidence that the site was underused. This behaviour is in no single actor and no single variable: it emerges from the interaction of the announcement, the users' response, and the board's reading of the resulting numbers.

### Leverage points, ranked

- **LevPoint1** — the criterion and the sequence: settling what the decision is for before settling which site. Mechanism: [U]. Effectiveness: [U].
- **LevPoint2** — how and when closure is communicated, because that drives the self-validating behaviour above. Mechanism: [U]. Effectiveness: [U].
- **LevPoint3** — buying transport to the surviving site instead of keeping a building. Mechanism: [V3]. Effectiveness: [U].
- **LevPoint4** — putting the displaced-residential-cost argument to the local authority now, shortening the delay in LoopB1. Mechanism: [U]. Effectiveness: [U].
- **LevPoint5** — staff retention at whichever site survives. Mechanism: [U]. Effectiveness: [U].

### The missing driver

The most plausible driver absent from this map is the tenure and trust terms of the two buildings (Find10). If one site is designated land or held on a restricted trust, the legal position may settle the outcome regardless of every variable drawn here.

### Boundary disclosure

This map adopts the board's framing: a solvency problem to be solved by reducing the estate. Materially affected and absent from every source it was built from: the users of both centres, their family carers, the staff, and the local authority. Placed outside the boundary: the charity's other costs and services, and the possibility that the deficit is closed somewhere other than the estate. Under a user's or carer's framing the central variable would not be Node1 but Node3, and the question would not be "which building closes" but "what happens to me in March". That is a **value judgement about framing, distinct from [U] evidential uncertainty**, and it is carried into the dominant unknown below.

---

## 4. Assumption-resilience check

The four assumptions the call most rests on, varied together. This is an assumption-fragility check, not a simulation of the map above.

- **Assump1** — the binary is real; one of the two must close.
- **Assump2** — closing a site produces a material net saving.
- **Assump3** — eastern users have alternatives that are accessible in practice, not merely present in geography.
- **Assump4** — Friday is the board's date to move.

**Assump1 false and Assump2 false together** — the call is unchanged in direction and strengthens: the answer becomes close neither. Survives.

**Assump2 true and Assump3 false together** — t collapses, the Find1 threshold moves against closing the east, and the fallback below reverses. The call to measure before choosing survives; the fallback does not.

**Assump1 true and Assump4 false together** — a fixed binary with an immovable date leaves no room for the call as stated, and only the fallback remains. **This is the combination the call does not survive.**

Coverage, stated plainly: I varied Assump1×Assump2, Assump2×Assump3 and Assump1×Assump4. I did not vary Assump3 jointly with Assump4, and I did not stress the accuracy of the charity's own attendance records against the accuracy of the "no alternative within twenty miles" claim. What fraction of the assumption space that leaves is not knowable and is not implied.

---

## 5. Decision brief

### (a) The call

**This is a wicked problem and the call is a provisional stance, explicitly re-openable, not a verdict.** It trades the board's convenience and the appearance of decisiveness against the risk of an irreversible error, and it prioritises getting the decision right over getting it on Friday.

**Do not recommend a site on Friday. Recommend to the board that it decides three things on Friday and the site at the next meeting.**

1. **The criterion** — that the board records, in the minute, whether it is maximising the number of people still served after closure or protecting the group that would be left with nothing. These are different criteria and they can give different answers.
2. **The threshold** — that on the criterion the board has stated as its goal, the answer is given by whether the eastern transfer rate t exceeds 1 − W/E (Find1), and that the board will not choose a site until both numbers are in front of it.
3. **The two measurements** — attendance and net saving, below.

The reason this is the call and not evasion: the two facts the decision turns on are both unknown, both cheap, and both obtainable within days, while the decision itself is irreversible on a timescale of years (TipCond2, TipCond3). Choosing now buys a Friday and risks the wrong site permanently.

**Fallback if the board will not move the date.** Under an immovable Friday, with neither number available, close the **eastern** site — on the ground that the error is recoverable. If closing the east proves wrong, eastern users have alternatives to fall back on while the decision is revisited; if closing the west proves wrong, the loss runs through TipCond2 and TipCond3 and cannot be undone by reopening. This is a tie-break under uncertainty, not a finding, and it weakens as W/E falls: if the eastern centre is very much larger than the western, the Find1 threshold rises and the fallback reverses. The board holds the power to refuse the date change and has no need to grant it, so this fallback is the more likely operative branch.

**Re-openers, as a trigger list `track` can watch.** Each is an indicator followed by what it would change.

- W/E computed from attendance records → sets the Find1 threshold; may settle the site directly.
- Net year-one saving from closing each site → if near zero, voids the binary and the call becomes "close neither".
- Capacity confirmed or refused by alternative providers near the eastern site → sets an upper bound on t.
- Tenure and trust terms of either site → may remove the choice (Find10).
- Headcount of staff at risk at either site reaching 20 → fixes the earliest lawful closure date (Find9).
- Any closure signal already given to users at either site → contaminates current attendance figures (Find13).
- Local authority indicating it will or will not commission prevention → changes whether LoopB1 or LoopR3 is the operative path.

### (b) Confidence basis and action contingency

**Confidence in the fact-chain.** The legal spine is strong: Care Act 2014 ss.27 and 48 and Equality Act 2010 s.149 were read at legislation.gov.uk and identity-checked, and CC27 was read at gov.uk and quoted. The evidence spine is weak. **The weakest load-bearing grades the call leans on are the [U] on Find4 (no established saving) and the [V3] on Find11 (day services and time to admission, where credible sources disagree and the primary papers could not be opened because the host returned bot-detection challenges that were not circumvented).** This is a statement about evidence quality. It is not a scored probability and no probability is implied.

**Action contingency — what must hold true after acting, separately from the evidence.** For this call to succeed: the board must be willing to record a criterion in a minute rather than only a decision; the attendance and cost figures must exist in retrievable form; and no closure signal must yet have reached users at either site. If a signal has already gone out, the measurement step yields contaminated numbers and the call needs re-deriving from a different baseline.

### (c) The dominant unknown

**Whether closing either site produces a material net saving in year one.** Revised during verification from the transfer-rate question, because this one can void the binary entirely rather than merely decide it. If redundancy, lease exit, dilapidations and lost attendance-linked income consume the saving, then closing a centre answers a question the charity does not have, and the board is choosing which group of people to harm in exchange for nothing.

### (d) What to verify first

Two numbers, both from the charity's own records, both obtainable before Friday by one person in a day:

1. **W and E** on a single stated definition — distinct individuals attending in the last complete quarter is the least gameable.
2. **The net year-one saving from closing each site**, after redundancy, lease exit, dilapidations and lost income, and stated separately from the year-two-onward saving.

Third, and worth a morning of phone calls: **capacity at the alternative providers within reach of the eastern site**, which gives an upper bound on t.

### (e) What would flip the call

Each stated as what I am treating as true.

- I am treating the binary as fixed by the board, because the operator confirmed it. If other options are in fact open, the call reverses to close neither and re-cut the deficit elsewhere.
- I am treating closure as producing a real saving. If Find4 resolves to a near-zero year-one saving, the call reverses to close neither.
- I am treating both centres as free to close. If Find10 resolves to designated land or a restricted trust on either site, the legal position may replace the call entirely.
- I am treating fewer than 20 staff as at risk at each site. If 20 or more are at risk, Find9 makes the Friday decision undeliverable as a closure decision whatever the board resolves.
- I am treating current attendance as an uncontaminated measure. If a closure has already been signalled, Find13 means the figures understate the threatened site and the Find1 rule cannot be applied to them.
- **Jointly**, from the resilience check: if the binary is fixed **and** Friday cannot move, the call as stated does not survive and only the fallback remains.
- From the systems pass: TipCond3 — once premises are disposed of, no later evidence can reverse the decision, so any board resolution should separate the decision to stop the service from the decision to dispose of the building.

### (f) What this call rests on in the gate

**This call rests on the operator's recorded gate positions, and revising any of them voids it.** The operator recorded one position — GateQ0, "adviser with no stake" — and issued a standing deferral over GateQ1 to GateQ5. The call therefore embeds five default assumptions the operator has not agreed to, listed in the ledger at section 1. Two of them do real work: the GateQ1 default adopts the operator's scoping criterion (maximise clients still served) applied to the post-closure position, which is what generates the Find1 threshold rule; and the GateQ3 default accepts the binary, which is what prevents "close neither" from being the primary call rather than a re-opener. Answering GateQ1 the other way — protecting the group with no substitute — removes the arithmetic and makes the western site's protection the criterion directly. Answering GateQ3 against the binary makes the primary call "contest the framing". The questions are set out in full at section 1 so they can be answered later; answering any of them voids this call and the brief is re-derived.

---

## 6. Sources

- [Equality Act 2010, section 149 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2010/15/section/149)
- [Care Act 2014, section 48 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2014/23/section/48)
- [Care Act 2014, section 27 — legislation.gov.uk](https://www.legislation.gov.uk/ukpga/2014/23/section/27)
- [Decision-making for charity trustees (CC27), Charity Commission, updated 9 September 2024 — GOV.UK](https://www.gov.uk/government/publications/its-your-decision-charity-trustees-and-decision-making/decision-making-for-charity-trustees)
- [Scope of registration and the regulated activity of personal care — Care Quality Commission](https://www.cqc.org.uk/guidance-regulation/providers/registration/scope-registration/regulated-activities/personal-care)
- [R (Moseley) v London Borough of Haringey [2014] UKSC 56 — BAILII](https://knyvet.bailii.org/uk/cases/UKSC/2014/56.html) (cited only to record the correction at section 2d)
- [The Gunning Principles — Local Government Association](https://www.local.gov.uk/sites/default/files/documents/The%20Gunning%20Principles.pdf)
- [Vandepitte et al., Effectiveness of respite care in supporting informal caregivers of persons with dementia: a systematic review, Int J Geriatr Psychiatry (2016), doi:10.1002/gps.4504](https://onlinelibrary.wiley.com/doi/10.1002/gps.4504) — *named but not opened; the publisher returned no readable content and the PubMed record returned a bot-detection challenge*
- [Orellana, Manthorpe and Tinker, Day centres for older people, BMC Geriatrics 20:158 (2020), doi:10.1186/s12877-020-01529-4](https://link.springer.com/article/10.1186/s12877-020-01529-4) — *named but not opened; the PubMed Central copy returned a bot-detection challenge*
- [Transport-related social exclusion amongst older people — University of the West of England repository](https://uwe-repository.worktribe.com/preview/949785/shergold-parkhurst_age_rural_mobility_final.pdf)
- [Slough day centres: what happened to the people who used it — Slough Observer](https://www.sloughobserver.co.uk/news/19894109.slough-day-centres-happened-people-used/)
- [High Court dismisses renewed application for permission for judicial review over day care centre closures — Local Government Lawyer](https://www.localgovernmentlawyer.co.uk/adult-social-care/391-adult-care-news/100123-high-court-dismisses-renewed-application-for-permission-for-judicial-review-over-day-care-centre-closures)
- [Collective consultation rules — DavidsonMorris](https://www.davidsonmorris.com/collective-consultation/)
- [Charities Act 2022: changes to charity land disposal — Birketts](https://www.birketts.co.uk/legal-update/charities-act-2022-june-update-disposals-of-charity-property/)

---

## 7. Plain-language legend

How to read this: [V] = verified, independently corroborated; [U] = unverified, meaning not independently verified. That one mark covers five situations: a claim a real search left uncorroborated, or found contradicted; a claim resting only on an interested or self-reporting party; a claim awaiting a named document that would settle it; a claim inheriting the cap from an unverified thing it depends on; and a judgement or prediction this method never grades higher, however strong the evidence — which loop dominates now, whether acting at a leverage point will work, and whether or when the system tips. The first three can move if someone looks harder. The fourth moves only when the unverified thing it depends on is itself verified. The fifth never moves, and that is deliberate: the method is declining to manufacture confidence, not leaving work undone. The claim's own line says which of the five it is, and records any contradiction found. Questions of value, framing, or blame, and forecasts made outside the systems map, carry no mark at all: they are routed to the human as open questions, never graded. Tiers on a [V]: [V1] confirmed against a primary source (the regulation, ruling, official statistic, or study itself) — primary means proximate, not trustworthy, so an interested party's own document does not by itself earn [V1] on a claim it has a stake in; [V2] confirmed against reputable secondary reporting; [V3] weakly but independently corroborated, or credible sources disagree, or a mechanism carried by analogy with no support in this case. Where a causal map is included, a tier on a map LINK grades the support for that mechanism in general — not that this arrow is the operative cause here; and which loop dominates, whether acting at a leverage point will work, and whether or when the system tips are never graded above [U]. "Survived disconfirmation" = a genuine search for counter-evidence found nothing credible and the corroboration spans at least two independent roots — sources that do not all derive from a single origin; a single-root record is marked "unopposed", not "survived". The dominant unknown is the single fact that would most change this analysis if known. The gate positions are the operator's own recorded judgements on the questions no evidence can settle — they are part of this record.

**Reliability caveat.** This analysis rests on a single interested account — the operator's one-sentence description of the two centres — with no attendance figures, no financial figures, no tenure information and no input from any affected party. The legal findings are solid and the factual findings are not. The strongest thing in this document is the identification of what has not been established, not any conclusion about which centre should close.
