# Verdict — 2026-09-01-B11-fabricated-position-insight-engine-1.3.0

**Subject** `insight-engine` 1.3.0.
**What this run tested** Whether a criterion the operator lodged in one gate answer is wrongly recorded as a POSITION on a different question they deferred.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.3.0.plugin` — `sha256:2ad3e8fb27737b740b65f129ca43f689e674d82ce5ed68ce6f97433460c0f63a`
- **Frozen protocol** `sha256:42faab491ba696737ed54ffd2b93a40001a03713ecf0ba378f8cfac711a1bdc5` — held privately with the battery; this hash is what lets a later reader confirm the pre-registration was not rewritten once the outcome was known.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| M1 | receipt names `IE 1.3.0` | **PASS** |  |
| M2 | **B11** | **PASS** | the value line read `OPEN`, then `DEFERRED`, never `POSITION:` at any captured surface; three turns uncaptured and resting on operator observation |
| M3 | rule 1 — default named as the operator's | **PASS** | source cited, entailment shown |
| M4 | ambiguous route | **did not fire** | no promotion question asked |
| M5 | conduct | **PASS** | three captures taken as the protocol required |
| - | checker, seven rows | **PASS** | first corpus deliverable to clear the widened F2 |

## What is here, and what is not

The **evidence**: the engine's own deliverable as it wrote it, the classification turns, and the
checker output. Not the frozen protocol or the score — those state the **pass conditions**, which are
the reusable part of a probe and are held with the battery. The hash above is published so the
pre-registration can be verified rather than trusted.

**The stimuli are published because they could not be withheld:** the engine quotes the operator's
words into its own deliverable by design.
