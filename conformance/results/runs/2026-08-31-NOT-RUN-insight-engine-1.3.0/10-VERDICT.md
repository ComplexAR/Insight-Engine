# Verdict — 1.3.0 was released without a conformance run

**Subject** `insight-engine` 1.3.0.
**What this run tested** Nothing. **This version shipped untested, deliberately, and this record exists
to say so.**

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.3.0.plugin` — `sha256:2ad3e8fb27737b740b65f129ca43f689e674d82ce5ed68ce6f97433460c0f63a`
- **Frozen protocol** none. No run was designed, so none was frozen.

## Outcome

| # | Probe | Result | Note |
|---|---|---|---|
| — | any battery probe | **NOT RUN** | no run was designed or executed against this version |
| — | port audit, 35 rules, against the unpacked package | **PASS** | mechanical; not a conformance run |
| — | Portable checker, 126 cases | **PASS** | the instruments' own tests, not a test of this build |

## Why this record exists

The release guard added on 2026-08-31 refuses to ship a version that no published record names. It
does **not** refuse to ship an untested version — it refuses to let one ship *silently*. Writing this
file is the cost of shipping without a run, and paying it is the whole mechanism.

**Two versions had already shipped that way the same day.** 1.2.0 and 1.2.1 were both released with no
conformance run against them, and nothing at the time noticed or recorded it. The guard was written
after them and would have stopped both. They are not retrospectively documented here, because a record
written after the fact about a run that never happened is not evidence of anything; what is recorded is
that the omission occurred, in `docs/Architecture.md` and in this note.

## What is known about this build without a run

The changes in 1.3.0 are the as-at stamp on the verification contract, and the absence-claim rule for
adjudication. Both are **specification text the engine must follow**, not code, so nothing mechanical
establishes that it does. The port audit confirms the rules are **present in the shipped package** —
which is a different and much weaker claim than that they are **obeyed**, and this project has an
explicit finding on that distinction: a probe is what tells the two apart.

The obvious next runs are the two the design named and deferred: a battery probe for the as-at stamp,
and one for the absence-claim rule scored on an adjudication output.

## What this record must not be read as

Not a pass. Not a partial pass. **Unassessed**, which the battery's own scoring section defines as
distinct from failed and requires be recorded as such. A reader comparing this version against 1.1.3 —
which has four records naming it, each carrying its package's hash — should treat the two as
differently evidenced, because they are.
