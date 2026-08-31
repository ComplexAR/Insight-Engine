# Provenance — RUNID 2026-08-30-2336-resolved-gate-insight-engine-1.1.0

## The artefact

`capture/analyse-deliverable.md` — **46,619 bytes, the engine's own file.** Not a transcription, not
a reconstruction. Written by the run, supplied by the operator, copied byte-for-byte into the run
directory. This is the first run in this series whose deliverable survives as the original.

## A false finding I wrote and am withdrawing

An earlier version of this file recorded, as a finding, that the engine had "asserted a file path it
had not verified" and that this was "the citation-resolution failure in a different medium". **That
was wrong, and I am striking it rather than quietly editing it out.**

What actually happened:

1. The engine reported the deliverable saved, and gave its absolute path.
2. A `copy` against that path failed with "Cannot find path ... because it does not exist".
3. I concluded the engine had asserted an unverified location, and wrote that into this record.
4. The operator then opened the folder. **The file is there. Its timestamp is 31/08/2026 00:56 — after
   my copy attempt ran.**

The path was correct throughout. I tried to copy a file before it had been written, treated a
timing failure as a truth failure, and wrote an accusation into an evidence record on the strength of
one negative check I did not repeat.

**This is the exact error class this corpus spent the day cataloguing**, committed by the scorer, in
the scoring record, within an hour of correcting the same pattern elsewhere. The specific fault is
not carelessness about paths. It is that a single failed observation was promoted to a finding about
another party without being re-checked, and without asking what else could produce that observation.
A retry thirty seconds later would have settled it.

Recorded here permanently, not deleted, because a provenance file that hides the scorer's own errors
is not a provenance file.

## Environmental differences from the previous run, not scored as defects

- **No connected folder** (Amendment 1: the folder picker would not accept an empty directory). The
  receipt's host string differs: `host Claude Cowork (Claude Agent SDK)` here, `host Cowork (Claude
  desktop app)` before.
- **Declared date is 2026-08-31** — the run crossed midnight.
- **Model string differs in form**: `claude-opus-5` here, `Claude Opus 5` before. Same model, two
  spellings of the same field in the same fixed format. Recorded as an observation, not scored.

## Capture method, for the next run

The connected-folder route failed (picker will not take an empty directory). The copy-from-outputs
route failed **only because I ran it too early** — the method itself is sound. What worked was the
operator supplying the file directly once it existed.

The lesson for the next protocol is narrower than the one I first wrote: **do not attempt the copy
until the engine's file has been observed on disk**, and treat a single "does not exist" as a
question, not an answer.
