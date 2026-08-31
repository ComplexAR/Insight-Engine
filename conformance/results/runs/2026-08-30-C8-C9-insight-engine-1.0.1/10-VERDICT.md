# Verdict — 2026-08-30-C8-C9-insight-engine-1.0.1

**Subject** `insight-engine` 1.0.1.
**What this run tested** First run of the citation-resolution rule.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.0.1.plugin` — `sha256:681116d19cff2182f8007c2a33977c5ff225eaa2464e9f8ae869c3e01bb9b2d0`
- **Frozen protocol** none — this run predates the freeze-before-stimulus practice.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| - | C8 citation resolves to the source it names | **PASS** |  |
| - | C9 inline control | **PASS** |  |
| - | compliance receipt | **ABSENT** | the plugin instructed no receipt in any version at that date; the finding that led to the plugin receiving one |

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
