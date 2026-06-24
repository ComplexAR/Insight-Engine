---
name: verify
description: Insight Engine verification layer. Triggers when the user asks to verify or fact-check the load-bearing claims of an analysis, re-grade claims [V]/[N] against current sources, check what has been asserted, or confirm a premise before relying on it. Retrieves external evidence, tiers source strength [V1]/[V2]/[V3], runs a disconfirmation pass on load-bearing claims, applies the three-bucket evidence router, runs a coverage-retention re-scan, and revises the dominant unknown.
---

# Insight Engine — verify

Verify the load-bearing claims of an analysis or claim-set against current external evidence. This is the assurance layer with teeth: it turns "the model believes X" into "X is corroborated by a cited source of stated strength, has survived a search for its own counter-evidence, or it is not." For each load-bearing claim, apply the three-bucket router:

- **Web-verifiable** (a public fact, pattern, rule, statistic, or current state of the world): search independent current sources; grade `[V]` with a citation and a source tier (below), or `[N]` if uncorroborated or contradicted. If a source contradicts the claim, say so plainly and revise the conclusion.
- **Party-held** (a private document, contract, or internal figure): do NOT pretend to verify; state exactly what document or evidence would settle it, and mark it pending.
- **Irreducibly open** (a value, a framing, or a forecast about the future): flag it for human judgement; it is not verifiable and must not be graded `[V]`.

## Tier every `[V]` by source strength (a `[V]` is not binary)
A claim is only as strong as what backs it. Tag every `[V]`:
- **`[V1]` primary** — the authoritative source itself: the statute or regulation text, the official statistic or regulator publication, a peer-reviewed study, a court ruling, the primary dataset or standard.
- **`[V2]` secondary** — reputable reporting or interpretation resting on primaries: an established news organisation, a professional body, a textbook, a well-regarded analyst.
- **`[V3]` contested / weak** — corroborated only by weaker or interested sources (a single blog, a content aggregator, advocacy or a party's own materials), OR credible sources disagree (true-but-disputed). Name the weakness.
Prefer a primary; when you can only reach `[V2]`/`[V3]`, say what primary source would lift it. The tier is part of the grade — it travels with the claim and is never dropped.

## Disconfirm the load-bearing few (red-team your own `[V]`s)
A single confirming search is how a wrong fact survives. For every claim the conclusion materially rests on, run a second search aimed at its NEGATION — "X is false / disputed / overstated / counter-evidence to X":
- Credible disconfirmation of comparable strength exists -> downgrade to **`[V3]` contested** (or `[N]` if the disconfirmation is strong) and record the dispute. A self-damaging or disconfirming finding from a credible source outweighs a self-serving confirmation.
- A genuine negation search finds nothing credible -> the claim is strengthened; mark it **survived disconfirmation** — a real signal for a defensibility reader.
Proportionate: red-team the load-bearing few, not every trivial fact.

## Coverage-retention (do not let focus narrow the field)
Concentrating on the load-bearing few — verifying, tiering, and disconfirming them — narrows attention onto exactly those claims. Before returning, re-scan once for material issues that this focus deprioritised, and name any that resurface. Sharpening the spotlight darkens its edges; this is the counter-sweep.

## Rules
- Verify before relying. Check premises too — a confidently-stated premise can be the error.
- Weight a self-damaging admission above a self-serving claim.
- Correct the analysis's own confidently-wrong facts; that is a primary purpose of this step.
- Name the single dominant unknown after verifying — the one fact that, if known, would most change the conclusion.

Return: a verification table (claim -> `[V1]`/`[V2]`/`[V3]`/`[N]` -> source -> disconfirmation result, or what document is needed), the corrections you made, the load-bearing claims that are `[V3]` or `[N]` (where the analysis is exposed), anything the coverage-retention re-scan recovered, and the revised dominant unknown. Any grade you set is locked — downstream skills may re-express it but never change it.
