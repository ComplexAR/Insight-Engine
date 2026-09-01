# Verdict — 1.3.1 ships the sentence its own evidence was taken without

**Subject** `insight-engine` 1.3.1.
**What this run tested** Nothing. **No conformance run was made against this version, and the reason is
the point of the release.**

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.3.1.plugin` — `sha256:08aae5a2886516d6eeece22e2a39ffdb8e4426835a5d9cd229029ef97c9d565c`
- **Frozen protocol** none.

## Outcome

| # | Probe | Result |
|---|---|---|
| — | any battery probe | **NOT RUN** against 1.3.1 |
| — | `B11`, twice, against **1.3.0** | **PASS** both times — the evidence this release is written from |
| — | port audit, 37 rules, unpacked package | **PASS**; it correctly reported PORT GAP before the rebuild |

## Why this version was not run, and could not usefully be

1.3.1 adds one sentence to `analyse`'s ledger rules: **a `POSITION:` transcribes an answer the operator
gave to that line's question**, so a criterion stated elsewhere reaches another line only as a deferred
line's default — unless the engine puts the question and the operator confirms it, which is then an
answer to that line.

**The sentence was written to match behaviour already demonstrated, not to correct it.** Probe `B11`
was run twice against 1.3.0, which carried no such sentence, and passed both times. The second run's
engine articulated the distinction unprompted, before the question was put: *"You have stated a
starting point. GateQ1 asks you to fix it as the board's decision rule, which is a different act."*

**Running `B11` against 1.3.1 would test something different.** With the sentence present, a pass shows
rule-following; without it, a pass showed the engine reaching the distinction from the routing. Those
two 1.3.0 runs are the entire pre-sentence record and cannot be added to. That is why the runs were
taken **before** this release and why this one carries none.

**What the release buys, since it changes no demonstrated behaviour.** A citable sentence. The
constructive basis was adequate for the engine and inadequate for a human contesting a real ledger: a
failure had to be argued from routing with nothing to quote, which the first run's frozen protocol
pre-authorised as **"A FAIL will be contested on exactly this gap."** The pass became routine; the failure became decisive, and
a conformance battery exists for the failure branch.

## What this record must not be read as

Not a pass for 1.3.1. **Unassessed**, which the battery defines as distinct from failed. A reader
comparing this version with 1.3.0 — which has two records naming it, each carrying its package hash —
should treat them as differently evidenced, and should note that the 1.3.0 evidence is what this
version's sentence was derived from rather than tested against.

---

*Corrected 2026-09-01, before release, by the quote-fidelity scan. Two quotations in this file carried words their named sources do not contain. The engine sentence above was captured with an initial capital and a full stop, not a lower-case opening and a semicolon. The phrase *"contested on that gap, forever"* was attributed to the first run's score; `grep -rn "forever"` over both run directories returned only this file. Its source is the first run's frozen protocol, quoted correctly above, and a protocol is not a score. Both are the same failure class: a real sentence nearby, restated from memory, given quotation marks it had not earned. These are the seventh and eighth instances of the class counted on 2026-09-01; the sixth, and the argument for building the check, sits at `REG-27`.*
