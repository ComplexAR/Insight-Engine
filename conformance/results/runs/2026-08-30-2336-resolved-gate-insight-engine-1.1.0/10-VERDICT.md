# Verdict — 2026-08-30-2336-resolved-gate-insight-engine-1.1.0

**Subject** `insight-engine` 1.1.0.
**What this run tested** The audit chain over a fully resolved gate.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.1.0.plugin` — `sha256:8b263dc032620d4f66b532c2505b3008583d83a968a66bd6e4f40ed9d40360b9`
- **Frozen protocol** `sha256:209a85e50b64e36a4516d71b8a58d1d5b86420d789c46012e2125b266b455218` — the protocol itself is held privately; this hash is what lets a later reader confirm it was not rewritten after the outcome was known.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| M1 | F2 receipt shape | **PASS** | receipt on line 1, all canonical fields as then defined |
| M2 | F1 legend fidelity | **PASS** | current legend, not `prior` - no build regression |
| M3 | F3 receipt vs ledger | **PASS** |  |
| M4 | X2 tier vocabulary | **PASS** | only the fixed symbols |
| M5 | X1, X3 | **n/a** | as required |
| M6 | X4 citation coherence | **n/a** | permitted outcome |
| M7, M8 | render checks | **NOT RUN** | the render step was not reached |

## What is here, and what is not

This folder holds the **evidence**: the engine's own deliverables exactly as it wrote them, the
checker output, and the provenance of the capture. A reader with `check_artifacts.py` can
reproduce every mechanical row above.

It does **not** hold the frozen protocol or the score. Those state the **pass conditions** and the
pre-registered predictions, which are the reusable part of a probe: a condition survives a
rewording, a stimulus does not. They are held privately with the battery, which is single-source
in the Portable Edition. The protocol's hash above is published so that its pre-registration can
be verified rather than trusted, and each protocol is published in full when its probe retires.

**The stimuli are not protected and could not be.** The engine quotes the operator's words into
its own deliverable by design, so a faithful record carries them whether or not anyone intends
it. What is protected is narrower and more honest: the conditions.
