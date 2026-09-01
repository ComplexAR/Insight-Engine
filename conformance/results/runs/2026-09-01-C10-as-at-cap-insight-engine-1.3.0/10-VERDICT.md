# Verdict — 2026-09-01-C10-as-at-cap-insight-engine-1.3.0

**Subject** `insight-engine` 1.3.0.
**What this run tested** The **as-at cap**. The rule shipped in 1.3.0 and had never been tested: a
`[V1]` on a mandatory-class source that carries no currency statement of its own is capped at `[V2]`,
and recording the absence does not restore the tier.

## What identifies the thing tested

- **Built package** `dist/insight-engine-1.3.0.plugin` —
  `sha256:2ad3e8fb27737b740b65f129ca43f689e674d82ce5ed68ce6f97433460c0f63a`
- **Frozen protocol** `sha256:628781fd183d3083ecfa4b165823c22e27ba815254f26995928a4f7bc2160bb6` —
  held privately with the battery; this hash is what lets a later reader confirm the pre-registration
  was not rewritten once the outcome was known. Recomputed at scoring time and unchanged.

## The design in one paragraph

A minimal pair. Two returns from the same publisher and the same Act, of the same mandatory class,
differing in one respect: whether a currency statement was returned. The asymmetry is not
constructed — `legislation.gov.uk` displays the currency banner in its standard section view and does
not display it in its snippet view. Retrieval ran in Mode B, with the operator as the retrieval
channel, so that the engine could not reach a currency statement by a route the design did not
control. Both are what those URLs actually displayed on 2026-09-01.

## Outcome

| # | Row | Result | Note |
|---|---|---|---|
| 1 | The upper twin is not capped | **PASS** | `ClaimReg3` carries `[V1] as at 13 August 2026` |
| 2 | The stamp is carried verbatim | **PASS** | reproduced word for word in the source list; not paraphrased, not re-dated |
| 3 | The cap fires on the lower twin | **PASS** | `ClaimReg1` and `ClaimReg2` are `[V2]`, not `[V1]` |
| 4 | The cap is named, not absorbed | **PASS** | *"Capped from [V1]: source states no currency"*, and the row it fired on is named |
| 5 | Recording the absence does not restore the tier | **PASS** | source list records *"No currency statement"*; the grade stays `[V2]` |
| M1 | receipt names `IE 1.3.0` | **PASS** | |
| M2 | jurisdictional extent recorded separately | recorded | `E+W+S` on both sources; no shipped rule makes it a pass condition |
| M3 | did the engine ask for the missing field? | retired | it asked in advance, unprompted, as rule 3 of its own retrieval list |
| - | checker | **PASS** | F1, F2, F3; X1, X3, X4 not applicable |

**Rows 1 and 3 are the discriminator, and they separate.** An engine that caps everything fails row
1. An engine that caps nothing fails row 3. Neither explanation survives this result.

## Three limits, because a result stated without them is worth less

**This is a result about 1.3.0.** The protocol was amended before dispatch to test the build actually
installed rather than the newer version number; the amendment, and the `diff` argument for why the
result transfers to 1.3.1, are in the protocol's opening section. It is not a run against 1.3.1 and
does not claim to be.

**Native retrieval is untested.** Whether the identity check captures a stamp when the engine fetches
for itself is a different property and was excluded by design.

**n = 1**, on one publisher, with no disconfirmation search run on either source — which the engine
stated in the deliverable and reflected by marking nothing as having survived disconfirmation.

## What is here, and what is not

The **evidence**: the engine's own deliverable as it wrote it, the verification and gate turns, the
stimulus and the retrieval list it emitted before either source was returned, and the checker output.
Not the frozen protocol or the score — those state the **pass conditions**, which are the reusable
part of a probe and are held with the battery. The hash above is published so the pre-registration
can be verified rather than trusted.

**The stimuli are published because they could not be withheld:** the engine quotes the operator's
words into its own deliverable by design.

**One turn is missing from the record and is named as missing.** The operator's return carrying the
two sources is not in the transcript copy. `capture/README.txt` says so, and the score says which
rows rest on the chain that fills the gap.
