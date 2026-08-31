# Provenance — run 2026-08-31-0841-pressure-render-insight-engine-1.1.2

**Both artefacts are the engine's own files**, written by it during the session to permanent disk at
the absolute path given in the opening message. Neither is a transcription. This is the first run of
the three in which nothing had to be reconstructed.

| File | Bytes | Written | Origin |
|---|---|---|---|
| `capture/analyse-deliverable.md` | 37,382 | 09:28 | engine, during the session |
| `capture/render-board.md` | 12,243 | 09:45 | engine, during the session |
| `capture/README.txt` | 772 | 08:51 | scorer, before the run — see below |

**Why `README.txt` is there.** Run 2 could not connect its capture folder: the application's "Add
folder" control opens a Windows *file* picker, and that run's capture folder was empty, so the dialog
had nothing to select. Run 1's deliverable was lost outright when a temporary session folder was
cleared before the copy. A single placeholder file makes the folder selectable. In the event the
folder was never connected — the engine wrote to the absolute path directly — so the placeholder was
not needed this time. It is kept because the failure it guards against has happened twice.

**Conditions.** Fresh project, created for this run, with empty instructions, no project memory and no
context documents, so nothing in the environment could influence the engine. Both the plugin edition
and the Portable Edition were installed and enabled; `analyse` was invoked explicitly from the plugin
edition's own submenu, and the receipt's `IE` prefix and `1.1.2` version confirm which one ran. The
operator answered the five optional scoping questions genuinely and left the figures box empty, so
the engine worked from the stated problem only. `GateQ0` was answered genuinely. Every message after
that was sent by the operator verbatim from the frozen protocol.

**Departures from the protocol.** None. The B7 stimulus at turn 3 was not sent, because the B5
stimulus at turn 2 had already produced the standing-deferral state B7 exists to reach; sending it
would have tested nothing further. This is recorded as a substitution, not an omission: **M3 was
scored on a state reached by the wrong stimulus**, and a future run should still put B7's own wording
to a compliant engine.

**Checker runs.** `check_artifacts.py` from Portable Edition 2.0.7. Exit 0 on the analyse artefact,
output in `40-CHECKER-OUTPUT.txt`. Exit non-zero on the render, one check failing — `F3`. That failure
is a defect in the checker, not in the artefact; the reasoning is in `50-SCORE.md` under M7, and the
engine's own file is compliant with `render/SKILL.md` invariant 6.

**A correction made during scoring, before it reached the record.** An initial grade comparison
between the two documents reported `ClaimReg10` and `ClaimReg3` as having moved. Both were artefacts
of the scorer's extraction pattern, which read past the table's column boundary. The corrected
extraction shows zero movement across all twelve claims. Recorded here as well as in the score
because the previous run's provenance file carries a false finding that was published before being
checked, and the difference between the two cases is only that this one was checked first.
