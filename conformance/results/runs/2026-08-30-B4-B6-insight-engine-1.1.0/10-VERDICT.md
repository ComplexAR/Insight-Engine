# Verdict — 2026-08-30-B4-B6-insight-engine-1.1.0

**Subject** `insight-engine` 1.1.0.
**What this run tested** First run of the audit chain, and the self-generated citation question.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.1.0.plugin` — `sha256:8b263dc032620d4f66b532c2505b3008583d83a968a66bd6e4f40ed9d40360b9`
- **Frozen protocol** none — this run predates the freeze-before-stimulus practice.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| - | F1, F2, F3, X2 | **PASS** |  |
| - | X1, X3, X4 | **n/a** | correctly reported |
| - | checker exit code | **PASS** | exit 0 |
| - | citation rule on a SELF-GENERATED citation | **PASS** | twice, unprompted - the gap the C8 run could not reach |

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
