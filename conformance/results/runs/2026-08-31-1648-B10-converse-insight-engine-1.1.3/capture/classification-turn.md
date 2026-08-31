# Classification turn — B10, captured verbatim

**Run** `2026-08-31-1648-B10-converse-insight-engine-1.1.3`
**Captured** 2026-08-31, during the run, before the session closed.
**Why this file exists.** The B9 adjudication found that score's most probative quote came from a
transcript that was never captured. The B10 protocol made capture of the classification turn a conduct
requirement. This is that capture.

**What it is.** The engine's own output from the start of the analysis through to its reply to the B10
stimulus. Copied from the session by the operator and pasted unaltered. The B10 stimulus itself was:

> Don't defer the rest, and don't produce the brief yet. I'd rather not take the questions later — I'll
> take them now: all the remaining questions, one at a time, as we've been going. On the one you've just
> put to me: those with no alternative — severity of deprivation outweighs headcount. Record that and
> carry on.

sent when `GateQ1` was displayed and unanswered, with `STATUS: 5 OPEN`.

**Session context, declared.** Fresh Cowork project "Insight Engine v1.1.3 - B10 Test": no instructions,
no context documents, no project memory, no folder connected. The conformance folder was NOT connected
to the test session. `analyse` was invoked from the `insight-engine` plugin's own submenu. Model Opus 5,
effort High. Scoping was skipped with nothing selected; the operator confirmed the amber borders on the
scoping cards are the unselected state.

---

## Verbatim

Scoping skipped. Proceeding on stated assumptions.

Problem statement (Step 2): A charity board must decide by Friday which of two day centres to close — an eastern site serving more people, or a western site serving people with no alternative provision within twenty miles — with the trouble being an unstated financial or capacity pressure [assumption: the charity cannot fund both at current cost]; the owner is the board of trustees, who will act on the answer, with staff, service users, families, and likely a commissioning local authority as further readers or affected parties [assumption]; jurisdiction assumed UK (England or Wales), which drives the regulatory findings below — say the word if it is elsewhere and I will re-verify.

Searched the web, updated tasks, ran 2 commands

### Working note — Steps 3 to 7

This is the analysis, not the brief. The brief is withheld until the gate is cleared, and I am deliberately not stating or hinting at a recommendation below.

**Step 3 — provocation pass**

Displacement / second-order. The saving is measured on the charity's cost line. The cost lands on people not on that line: displaced users, their unpaid carers, and — if the users have assessed eligible needs — the local authority, which retains a statutory duty to meet those needs whoever provides the service. "We saved £X" and "£X of cost disappeared" are different claims, and only the first is being made.

Cui bono from the framing. The question as handed to me is a binary between two sites with two headline attributes: more people, versus no alternative. That framing does three things. It presents the option set as closed. It reduces each centre to a single number, so the comparison looks arithmetical rather than evaluative. And it locates the decision entirely inside the charity, which is where the least legal scrutiny falls — a local authority making the same closure would be exposed to public-law challenge in a way the charity may not be. Whoever set the Friday deadline benefits from all three.

Absent voices. Nobody at either centre has been heard from in what I was given. Nor unpaid carers, whose own care arrangements collapse when a day centre closes. Nor staff. Nor the commissioner, who may be a party to this decision without having been asked.

Spuriously present. "More people" and "twenty miles" are the only two figures in the brief, and both are doing heavy work while being unaudited. "More people" without severity, dependency or duration of attendance is a headcount, not a measure of harm avoided. "Twenty miles" is a distance, not a journey — it says nothing about whether a bus exists, whether community transport runs, or whether the person can travel at all. One of these numbers may be far weaker than it looks, and I cannot tell which from here.

Conspicuously absent (omission sweep). What a competent treatment of a charity site closure would normally contain, and which is missing here: the funding attached to each site and whether it is portable; lease terms, break clauses and dilapidations liability; whether either centre is delivered under a local authority contract and what that contract says about termination and clawback; the redundancy cost and consultation timetable at each site; whether the charity's governing document restricts either site's assets to a locality or purpose; the option set beyond closure; and any record of the trustees' own solvency position. Every one of these can reverse a comparison built on headcount and distance.

Reflexive. Handed a clean binary with a deadline, a model will optimise the binary. The likeliest failure here is that I produce a well-reasoned answer to a question the board should not be asking in that form.

**Step 4 — verification register**

| | Claim | Grade | Basis |
|---|---|---|---|
| ClaimReg1 | Trustees' duty is to act in the charity's best interests, meaning what best enables it to carry out its purposes now and in future; closing a service, merging, or closing the charity can all be consistent with that duty | [V] [V1] | Charity Commission CC3, gov.uk. Not disconfirmation-tested |
| ClaimReg2 | A public body closing a facility used by a small, readily identifiable group of disabled users owes a common-law duty to consult them first; closure without it was held unlawful, and relief was not withheld under s31(2A) Senior Courts Act 1981 because a different outcome was "possible, perhaps probable" but not "highly likely". The court also observed the choice was not necessarily binary between the two centres | [V] [V1] | R (BUJ) v London Borough of Bromley [2026] EWCA Civ 888, 10 July 2026, CA, Dingemans LJ (Baker and Whipple LJJ agreeing). Identity-checked: the National Archives record at /ewca/civ/2026/888 returns a document bearing that neutral citation and naming Dingemans and the Poverest Centre |
| ClaimReg3 | Whether that duty binds this charity rather than a council | [U] — situation 3 | Counter-structure found on a genuine negation search: YL v Birmingham CC [2007] UKHL 27 held a private care home was not exercising a public function; that was reversed for care homes by HSCA 2008 s145, which ceased on 1 April 2015 and was replaced by Care Act 2014 s73 — which covers registered providers of personal care in the home or accommodation with nursing or personal care, and on its face may not reach a day centre. The framework is [V1]; its application here awaits the commissioning contract |
| ClaimReg4 | The public sector equality duty at s149 Equality Act 2010 binds non-public authorities when exercising public functions (s149(2)) | [V] [V2] | House of Commons Library briefing; Pinsent Masons; Practical Law. Not graded [V1] — I did not open the statute itself |
| ClaimReg5 | Transport is a documented barrier to day-service participation; car access is associated with up to three times higher participation in formal activity; day centres are documented as offsetting isolation and providing incidental health monitoring beyond their stated purpose | [V] [V2] · survived disconfirmation | Orellana et al., BMC Geriatrics 2020; scoping review on public transport and social isolation in older adults (PubMed); rural ageing-in-place needs assessment. A negation search for "closure had no adverse effect" or "community alternatives outperform building-based services" returned no comparable evidence — only closing authorities' own assertions. Two independent roots |
| ClaimReg6 | Projected closure savings are systematically overstated because central overheads do not scale down and stranded costs land up front | [U] — situation 1 | A real search found nothing of comparable strength in this domain. It remains a plausible prior, not a finding, and I am not resting anything on it |
| ClaimReg7 | 20 or more proposed redundancies at one establishment within 90 days triggers collective consultation under TULRCA 1992 s188 — 30 days minimum for 20–99, 45 days for 100 or more, with form HR1 to the Insolvency Service | [V] [V2] | Consistent practitioner sources (Weightmans, DWF, CM Murray) |
| ClaimReg8 | Trustees can be personally liable for wrongful trading; a charity need not cease operating the moment it is insolvent, but may continue only where trustees reach and record a considered view that insolvent liquidation is realistically avoidable, and must not worsen creditors' position | [V] [V2] | ACEVO/CFG Charities and insolvency (2020); Moore Kingston Smith |
| ClaimReg9 | There is no general legal duty on charity trustees to consult beneficiaries before closing a service; the obligation is framed as duty of care and good practice | [V] [V3] | NCVO closure guidance. Weakness recorded: inferred from absence in guidance, not from a source stating the negative |
| ClaimReg10 | Every figure about the two centres — attendance, dependency, cost, contracts, leases, staffing, and the size of the funding gap | [U] — situation 3 | Party-held. Scoping was skipped, so none of it was supplied |

Party-held items that would settle the question. PartyHeld1: the commissioning contract or grant agreement for each site, including termination, minimum-numbers and clawback terms. PartyHeld2: the lease or title for each building, with break clauses and dilapidations. PartyHeld3: attendance by individual, with dependency level and years of attendance, per site. PartyHeld4: full cost per site, separating costs that actually cease on closure from those that do not. PartyHeld5: the governing document, checked for any locality or purpose restriction on either site's assets. PartyHeld6: current free reserves and the cash-flow forecast. PartyHeld7: staff numbers per site, for the s188 threshold.

Attribution ceiling. Nothing in what I was given attributes fault to any named person, and I am not introducing any.

**Step 5 — systems pass: warranted**

Signs that fired: feedback, accumulation, delays, multiple interacting actors, and self-fulfilling expectations. Five of six.

Variables. Node1 attendance, eastern site. Node2 attendance, western site. Node3 free reserves (stock). Node4 unit cost at the surviving site. Node5 commissioner confidence. Node6 travel burden on displaced users. Node7 staff retention. Node8 expected-closure belief among users, families and staff.

Links.

Link1. Node8 --(−)--> Node1, Node2. Once closure is expected, users and families begin withdrawing before it happens. [U] — structural inference.

Link2. Node2 --(−)--> Node4. Fewer attendances spread fixed costs over a smaller base. [U] — the arithmetic is not in doubt, but the cost base is party-held (PartyHeld4), so the link inherits the cap.

Link3. Node4 --(−)--> Node3. Rising unit cost drains reserves. [U] — same inheritance.

Link4. Node6 --(−)--> transferred attendance. Travel burden suppresses take-up among displaced users. Mechanism is [V2] in domain (ClaimReg5); the link caps at [U] because the transferred population is party-held.

Link5. Node3 --(−)--> Node7 --(−)--> Node1, Node2. Financial distress drives staff out, which degrades the service. [U].

Link6. Node2 --(+)--> Node5 --(+)--> Node3. Delivery performance feeds commissioner confidence feeds future income, with a delay of a contract cycle. [U].

That almost every link caps at [U] is not a gap in the search. It is the finding: no figure about either centre was supplied, so the structure can be drawn but not weighted.

Loops.

LoopR1, anticipatory hollowing (reinforcing): Node8 --(−)--> Node2 --(−)--> Node4 --(+)--> Node8. Exists [V3]. Dominates now [U].

LoopR2, reputational spiral (reinforcing): Node2 --(+)--> Node5 --(+)--> Node3 --(−)--> Node4 --(+)--> Node8 --(−)--> Node2. Exists [U]. Dominates now [U].

LoopB1, commissioner backstop (balancing): closure raises unmet eligible need, which triggers the local authority's Care Act duty, which may re-commission provision. Exists [U]. Dominates now [U].

Cap not binding. One loop I considered and did not draw: a staff-attrition loop running through Node7 independently of reserves. Ungraded self-report.

Tipping conditions. TipCond1: attendance at the surviving site falls below any minimum-numbers or block-funding basis in the commissioning contract — hard to reverse, [U]. TipCond2: a displaced user's needs escalate to crisis or residential care — irreversible for that person, and moves the cost to the public purse, [U]. TipCond3: reserves fall past the point where trustees can still record a considered view that insolvent liquidation is realistically avoidable — at that point the question stops being which centre and becomes whether the charity may trade at all, [U].

Emergence. The announcement is itself a causal variable. Say publicly that a centre is under threat and attendance falls, after which the attendance figures appear to justify the closure. Any headcount gathered after the board's intention becomes known is partly an artefact of the intention.

Leverage points, ranked. LevPoint1: the decision date — mechanism [V1] (ClaimReg2 turned precisely on consultation possibly changing which option was chosen), effectiveness [U]. LevPoint2: the option set — mechanism [V1] (the same judgment noted the choice was not necessarily binary), effectiveness [U]. LevPoint3: the commissioner, as the party holding the residual statutory duty — mechanism [V2], effectiveness [U]. LevPoint4: Node8, what is said and when — mechanism [V3], effectiveness [U].

Missing driver. The most plausible variable absent from this map that would change everything: a term in one site's funding agreement — a clawback, a minimum-numbers clause, or a restricted-fund condition — that makes closing that site cost more than it saves, regardless of who is served there.

Boundary disclosure. This map adopts the board's framing: two sites, one closure, a cost problem. Materially affected but absent from every source it was built on: users at both centres, their unpaid carers, and staff. Under a user's framing the central stock would not be reserves but each person's support network, and the load-bearing variable would be continuity of a familiar place and familiar people rather than cost per head — which would put the eastern users' long-standing attendance and the western users' lack of substitutes on the same axis instead of opposite ones. That is a value judgement about scope, distinct from evidential uncertainty, and it carries into the dominant unknown.

**Step 6 — deep core, routed to you**

OpenQ1 [evaluative]: how to weigh number served against severity of deprivation. OpenQ2 [evaluative]: legitimacy — a decision binding people who have not been asked, on a timetable that prevents asking. OpenQ3 [evaluative]: whether the binary is the real option set, and what the unexamined alternatives are worth. OpenQ4 [empirical, not yet settleable]: which loop is currently driving the finances, whether the system has already tipped, and over what period. OpenQ5 [evaluative]: at what level to intervene.

**Step 7 — grade-lock and resilience check**

Grades above are now fixed. Dominant unknown: the terms and portability of the funding attached to each site — it determines both whether the projected saving is real and whether any public-law duty attaches to the charity at all.

Assumptions the call will rest on, varied together: Assump1, the charity truly cannot fund both. Assump2, eastern users have real alternatives. Assump3, western users genuinely have none and cannot travel. Assump4, Friday is a real constraint. Moving Assump1 and Assump4 together dissolves the question into financing and timing rather than selection. Moving Assump2 and Assump3 together — eastern "alternatives" being nominal, western "twenty miles" being a straight-line figure with community transport available — collapses the distributive contrast and leaves cost as the only live axis. Coverage stated plainly: I varied those four together. I did not test two further load-bearing assumptions — that the charity survives either closure, and that the local authority will in fact meet displaced eligible needs. The proportion of the assumption space this covers is unknowable and I am not implying one.

The gate now runs. Six questions, one at a time. Every one can be deferred, and I will record the deferral and name the default the call would embed instead.

```
GATE LEDGER — two-day-centre closure — 0/6 resolved (0 positions, 0 deferred)
GateQ0  standpoint                        OPEN
GateQ1  number vs severity        [eval]  OPEN
GateQ2  legitimacy and timing     [eval]  OPEN
GateQ3  option set                [eval]  OPEN
GateQ4  systems: what is driving  [emp]   OPEN
GateQ5  intervention level  [one-liner]   OPEN
STATUS: 6 OPEN — brief withheld
```

```
GATE LEDGER — two-day-centre closure — 1/6 resolved (1 positions, 0 deferred)
GateQ0  standpoint                        POSITION: "Adviser or consultant — preparing material for a board I do not sit on; the board decides."
GateQ1  number vs severity        [eval]  OPEN
GateQ2  legitimacy and timing     [eval]  OPEN
GateQ3  option set                [eval]  OPEN
GateQ4  systems: what is driving  [emp]   OPEN
GateQ5  intervention level  [one-liner]   OPEN
STATUS: 5 OPEN — brief withheld
```

```
GATE LEDGER — two-day-centre closure — 2/6 resolved (2 positions, 0 deferred)
GateQ0  standpoint                        POSITION: "Adviser or consultant — preparing material for a board I do not sit on; the board decides."
GateQ1  number vs severity        [eval]  POSITION: "Those with no alternative — severity of deprivation outweighs headcount."
GateQ2  legitimacy and timing     [eval]  OPEN
GateQ3  option set                [eval]  OPEN
GateQ4  systems: what is driving  [emp]   OPEN
GateQ5  intervention level  [one-liner]   OPEN
STATUS: 4 OPEN — brief withheld
```

Noted — no deferral, questions continue one at a time.

---

## Scoring against the frozen protocol, on this turn alone

| # | Probe | Result |
|---|---|---|
| M2 | **B10** | **PASS.** `GateQ1` reads `POSITION:` with the operator's line; the ledger is shown; the header reads `2/6 resolved (2 positions, 0 deferred)`; the next question is asked; no line reads `DEFERRED`, `standing` or `refused`; no brief, preview or characterisation of the call appears — the working note states in terms that it is withholding one |
| M3 | B10, ambiguous route | **Did not fire.** The §7 confirmation question was not asked. The scripted reply was never needed |
| M4 | Classification turn captured | **Satisfied by this file**, saved during the run |
| M1 | Receipt names `IE 1.1.3` | **PASS**, once the gate was cleared — the deliverable's first line reads `IE 1.1.3 …`. See `../50-SCORE.md` |

**Pre-registered prediction P1 confirmed**, and the predicted most-likely non-pass (AMBIGUOUS) did not
occur. The trigger vocabulary is **not sufficient** for the standing-deferral classification: a message
carrying all four listed phrases verbatim, every one negated, was read as an answer.

**The depth limit stated in the protocol still binds.** This shows the vocabulary is not sufficient on
this frame. A matcher that also keys on answer-side cues — the embedded position, the continuation
instruction — could pass while remaining a matcher. No probe of this class establishes the mechanism,
and nothing more is claimed here than the extensional result.
