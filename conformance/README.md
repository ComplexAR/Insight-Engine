# Conformance — the evidence for this edition's testing claims

**What this folder is.** The record of every conformance run against the `insight-engine` plugin: the
engine's own deliverables exactly as it wrote them, the mechanical checker's output, and a verdict
per run. Created 2026-08-31.

**Why it exists.** Before this date, `docs/Architecture.md` carried per-version narratives of what
testing had found, and this repository held **no evidence files at all** — the claims were here and
the artefacts were somewhere else. A testing claim a reader cannot check is an assertion.

---

## What is here

```
conformance/results/runs/<run-id>/
    10-VERDICT.md            what was tested, what happened, and the hashes that identify both
    40-CHECKER-OUTPUT.txt    the mechanical checker's output, reproducible
    capture/                 the engine's deliverables, verbatim
```

Run ids read `<date>-<slug>-insight-engine-<version>`. Eight runs, against 1.0.1 through 1.1.3.

## What is not here, and why

**The instruments are single-source in the Portable Edition** — the specification, the protocols, the
conformance battery, and `check_artifacts.py` all live there, and this repository holds none of them.
That is deliberate: two copies of a specification drift, and the drift is silent. This edition is a
sibling of the Portable Edition, not a copy, which is also why the compliance receipt reads `IE` here
and `IE-P` there.

**The frozen protocols and the scores are held privately.** They state the **pass conditions** and the
pre-registered predictions, and those are the reusable part of a probe: a condition survives being
reworded, a stimulus does not. Each verdict publishes its protocol's SHA-256, so a reader can confirm
the pre-registration was not rewritten once the outcome was known, and each protocol is published in
full when its probe retires.

**The stimuli are published, because they could not be withheld.** The engine quotes the operator's
words into its own deliverable by design, so any faithful record carries them. Working that out
changed the boundary: what is protected is not the wording of a probe but its conditions, which is
both narrower and more honest than the alternative.

## How to re-run any of this

```
git clone <the Portable Edition>            # the instruments
python conformance/check_artifacts.py <path-to-a-capture-file>
```

The checker is standard library only and opens no network connection. It reports on the document's own
declared contract, so a deliverable produced under a superseded grade contract is reported `prior`
rather than failed.

## The records are kept whole

Several carry findings that are unflattering to this project. The 1.1.2 run records a probe FAIL later
withdrawn as invalid at the time of the run. The 1.1.3 boundary run records that the scorer substituted
an easier stimulus than the battery specifies, in a document whose own conduct rule forbids
substitution. The B10 run's checker output was re-run under a widened check and now fails on a defect
that runs through **every** deliverable in the corpus.

A conformance record that shows only the passes is not evidence of anything.
