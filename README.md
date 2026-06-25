# Insight Engine

A light plugin for analysing high-stakes, complex, and wicked problems — the kind where the danger is that the important things hide, the evidence is mixed or interested, and the deciding questions are value judgements. **The model provides the insight; the engine makes it verified, defensible, and audience-ready.**

Built one controlled test at a time, keeping only what beats a strong plain pass. Every load-bearing claim is graded `[V]` (independently corroborated) or `[N]` (rests on an interested or self-reporting party), with strength tiers `[V1]`/`[V2]`/`[V3]`; once a grade is set it is never changed downstream — only re-expressed.

## The four commands

- **`/analyse`** — the main workflow: a fail-safe proportionality triage → a fixed "provocation page" pass → source-tiered web verification with a disconfirmation search → a **conditional systems-investigation pass** for feedback-driven problems (a graded causal map of loops, tipping *conditions*, and leverage — investigate, don't predict) → deep-core routing → grade-lock + an assumption-resilience check → a **forced judgement gate** you clear → a five-part decision brief.
- **`/verify`** — fact-check the load-bearing claims of an analysis against current sources; catch confidently-wrong facts; route what can't be verified online to the right place.
- **`/render`** — re-voice a finished analysis for a specific reader (board, counsel, regulator, family, adversary, or any named standpoint) without changing a claim or a grade.
- **`/track`** — keep an investigation live across sessions as new facts arrive.

## Documentation

- [**ICD-203 alignment**](docs/ICD-203-Alignment.md) — how the Insight Engine maps to the nine US Intelligence Community analytic tradecraft standards (blind-assessed at 92% vs a bare model's 75%), with the bounding "architected-around, not certified" caveat.

## Install

### Claude Code (CLI) — one-command install
```
/plugin marketplace add ComplexAR/Insight-Engine
/plugin install insight-engine@insight-engine-marketplace
```

`marketplace add` takes `owner/repo`, so the command above assumes the repo is named **`Insight-Engine`** — substitute your repo name if you call it something else. The part after the `@` is the marketplace's own name, set in `.claude-plugin/marketplace.json`. To pick up a new release later, run `/plugin marketplace update`.

### Claude Cowork (desktop app) — install from file
The desktop app installs plugins from a file rather than from a GitHub marketplace:

1. Download **`dist/insight-engine-0.1.7.plugin`** from this repo (or from the latest [Release](../../releases)).
2. In Cowork, open **Customize → Skills → Upload from file** and choose the `.plugin`.

## Version

**0.1.7.** For how releases are cut, see [PUBLISHING.md](PUBLISHING.md).

## License

No license is set yet. Add a `LICENSE` file (for example MIT) before sharing widely, so others know the terms on which they can use it.
