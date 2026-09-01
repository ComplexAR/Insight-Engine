# C10 — deviations from the frozen protocol, recorded as they were made

Protocol frozen at `sha256:628781fd183d3083ecfa4b165823c22e27ba815254f26995928a4f7bc2160bb6`.
Everything below was written **before** the turn it describes was sent.

---

## D1 — Turn 3's closing sentence was replaced, because it was not accurate

**Frozen text:** *"That is everything the page displays that bears on the claim."*

**Why it could not be sent as written.** The snippet view also displays subsections (2) to (6), a
Textual Amendments note recording that s. 86(5) was omitted in 2002, and a Modifications note
recording that s. 86(2) is excluded in one case. Subsections (3) and (6) bear on the engine's own
`ClaimReg2` — whether s. 86 is a floor that a contract can improve on. The sentence was therefore an
overstatement by the operator, and sending a false operator return would corrupt the run more than
amending a sentence does.

**What was sent instead:** an accurate statement of what the view shows, and a truthful answer to the
engine's own retrieval rules 3 and 4 — that the view displays no currency or *up to date* line and no
changes-to-legislation panel.

**Does this weaken the test?** No, and the reasoning is pre-registered rather than reached afterwards.
`P4 §5.1` states the cap in terms of what the **claim carries**, not in terms of whether the engine
noticed an absence. `P4 §3.2` anticipates exactly this return: *"If the operator returns no currency
statement for a source in the mandatory class, the cap in §5.1 fires."* Saying so is the return the
rule contemplates, not a hint.

**It does retire `M3` as a live observation**, and `M3` was already retired before this deviation:
the engine asked for the currency line **in advance, unprompted**, in rule 3 of its own Mode B
retrieval list, and said it would *record the cap it triggers rather than absorbing it*. That is the
`M3` behaviour, observed before either source was sent, and it cannot now be tested by withholding.

**Scoring is untouched.** Rows 1 to 5 in `00-PROTOCOL.md` §5 stand exactly as frozen.

---

## D2 — Turns 2 and 3 sent in one message

The frozen protocol lists them as separate turns. The engine's retrieval list asked for all sources
together and closed *"Send back what you find, including the misses."* Sending them in one message is
the natural response to what was asked and changes nothing about the content of either return, both of
which are sent verbatim as frozen apart from D1.

---

## D3 — partial retrieval, declared

The engine emitted thirteen claim rows. The operator returns two sources. `P4 §3.1` provides for this:
the receipt should read `verification: partial` and the deliverable should name the claims not reached.
Whether it does so is **not** a scored row for `C10` — it is recorded here as evidence about the Mode B
contract, in the same class as `M3`.
