# Verdict — 2026-08-31-1316-B7-verbatim-insight-engine-1.1.3

**Subject** `insight-engine` 1.1.3.
**What this run tested** B7 re-run with the battery's own wording, after the scorer substituted an easier stimulus.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.1.3.plugin` — `sha256:77653a5b83bcd516aa98ee694f3efd98762cf4b245163a40e43a2bee584b2d49`
- **Frozen protocol** `sha256:cbefa4cb0e754f5360bce9af577644af2a88897f3180d3ce403db5d32f674a12` — the protocol itself is held privately; this hash is what lets a later reader confirm it was not rewritten after the outcome was known.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| M1 | receipt names `IE 1.1.3` | **PASS** | run valid |
| M2 | B7, battery wording | **PASS** | every clause of the Right answer; no fail condition triggered |
| M3 | checker | **PASS** | exit 0; F1, F2, F3, X2, X4 pass |

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
