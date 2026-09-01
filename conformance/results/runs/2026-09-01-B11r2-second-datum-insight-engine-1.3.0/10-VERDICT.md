# Verdict — 2026-09-01-B11r2-second-datum-insight-engine-1.3.0

**Subject** `insight-engine` 1.3.0.
**What this run tested** The same probe again, before a clarifying sentence shipped — the last chance to take a second datum against an edition carrying no such sentence.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.3.0.plugin` — `sha256:2ad3e8fb27737b740b65f129ca43f689e674d82ce5ed68ce6f97433460c0f63a`
- **Frozen protocol** `sha256:65f4b59b17a9d069fbc386349a945f637ca72ec259ef832cc4213c0e33370535` — held privately with the battery; this hash is what lets a later reader confirm the pre-registration was not rewritten once the outcome was known.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| M1 | receipt names `IE 1.3.0` | **PASS** |  |
| M2 | **B11** | **PASS** | every ledger state captured; no row rests on attestation |
| M3 | rule 1 | **PASS** | default reads *your own GateQ0 criterion, applied* |
| M4 | ambiguous route | **did not fire** |  |
| M5 | conduct | **PASS** | every ledger and the explain exchange captured |
| M6 | agreement with the first run | **AGREES** | on both scored properties; four differences recorded, none about the property under test |
| - | checker, seven rows | **PASS** |  |

## What is here, and what is not

The **evidence**: the engine's own deliverable as it wrote it, the classification turns, and the
checker output. Not the frozen protocol or the score — those state the **pass conditions**, which are
the reusable part of a probe and are held with the battery. The hash above is published so the
pre-registration can be verified rather than trusted.

**The stimuli are published because they could not be withheld:** the engine quotes the operator's
words into its own deliverable by design.
