# Conformance results — `insight-engine` plugin edition

Eight runs, 2026-08-30 to 2026-08-31, against versions 1.0.1 to 1.1.3. One further run on the same
battery tested the **Portable Edition** and is held with that edition, not here.

| Run | Version | What it tested | Pass | Fail |
|---|---|---|---|---|
| [`2026-08-30-2336-resolved-gate-insight-engine-1.1.0`](runs/2026-08-30-2336-resolved-gate-insight-engine-1.1.0/10-VERDICT.md) | 1.1.0 | The audit chain over a fully resolved gate. | 4 | 0 |
| [`2026-08-30-B4-B6-insight-engine-1.1.0`](runs/2026-08-30-B4-B6-insight-engine-1.1.0/10-VERDICT.md) | 1.1.0 | First run of the audit chain, and the self-generated citation question. | 3 | 0 |
| [`2026-08-30-C8-C9-insight-engine-1.0.1`](runs/2026-08-30-C8-C9-insight-engine-1.0.1/10-VERDICT.md) | 1.0.1 | First run of the citation-resolution rule. | 2 | 0 |
| [`2026-08-31-0841-pressure-render-insight-engine-1.1.2`](runs/2026-08-31-0841-pressure-render-insight-engine-1.1.2/10-VERDICT.md) | 1.1.2 | Pressure at the gate, and a render under confidence pressure. | 5 | 1 |
| [`2026-08-31-1024-boundary-regression-insight-engine-1.1.3`](runs/2026-08-31-1024-boundary-regression-insight-engine-1.1.3/10-VERDICT.md) | 1.1.3 | The boundary the 1.1.1 widening left undefined, and the first refusal after a position. | 5 | 0 |
| [`2026-08-31-1316-B7-verbatim-insight-engine-1.1.3`](runs/2026-08-31-1316-B7-verbatim-insight-engine-1.1.3/10-VERDICT.md) | 1.1.3 | B7 re-run with the battery's own wording, after the scorer substituted an easier stimulus. | 3 | 0 |
| [`2026-08-31-1515-B9-paraphrase-insight-engine-1.1.3`](runs/2026-08-31-1515-B9-paraphrase-insight-engine-1.1.3/10-VERDICT.md) | 1.1.3 | Whether the trigger vocabulary is NECESSARY: a paraphrase carrying none of it. | 3 | 0 |
| [`2026-08-31-1648-B10-converse-insight-engine-1.1.3`](runs/2026-08-31-1648-B10-converse-insight-engine-1.1.3/10-VERDICT.md) | 1.1.3 | Whether the trigger vocabulary is SUFFICIENT: every listed phrase, each negated. | 3 | 1 |

Counts are of rows in each verdict table, not of battery probes; a run exercises only the probes its
protocol names. `n/a`, `not taken` and `NOT RUN` are recorded outcomes and are counted as neither.

## What the sequence shows

Read in order, the eight runs are mostly a record of **defects found in the testing apparatus**, not in
the engine. A probe that no conforming engine could pass. A checker that failed every render on sight,
because the one probe that would have caught it had been carried unrun for three runs. A scorer that
substituted an easier stimulus, and criticised its own probe wording by quoting a different probe's
text. A checker reporting "receipt present with the canonical fields" while checking five of nine.

That is the honest summary, and it is worth more than a list of passes: the runs that found nothing
wrong with the engine each found something wrong with the means of testing it, and the apparatus is now
better than the engine's own record of it would suggest.
