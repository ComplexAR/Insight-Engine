# Corpus decision — the unverified grade symbol becomes `[U]`

**Decision taken 30 August 2026 by the operator (Complex-AR). Corpus-level and binding on every
edition of the Insight Engine.**

This document exists because the change was first made in a derivative edition, which inverts this
corpus's own precedence rule that canon leads and derivatives follow. It records the decision where
canon lives, so that the implementing releases are conforming acts rather than a derivative
overriding the original.

---

## 1. The decision

**The grade symbol set is `[V]` and `[U]`, corpus-wide, from 30 August 2026.**

- **`[V]`** — **verified**: independently corroborated. Tiers `[V1]`, `[V2]`, `[V3]` are unchanged.
- **`[U]`** — **unverified**: not independently verified.

`U` stands for *unverified*. **The definition remains the full phrase, "not independently verified",
and the word *independently* is load-bearing** — a claim resting only on an interested party has been
attested, just not by anyone independent, and that is situation 2. Read `[U]` as "unverified"; apply
it as "not independently verified".

## 2. What this changes, and what it does not

**Changes:** the symbol, and the expansion of both letters in the plain-language legend, which now
reads `[V] = verified, independently corroborated; [U] = unverified, meaning not independently
verified.`

**Does not change:** the five situations and the requirement that every line says which one it is;
the tier definitions; the rule that tiers are never re-based for a case; the permanent set; the
attribution ceiling; the no-grades-without-verification rule; or any other analytical content. This
is a symbol and a mnemonic, not a re-basing.

**A rule this makes explicit rather than implied.** *The grade never appears unbracketed* — not in
prose, a table header, a diagram label, or a legend gloss. The brackets are the reserved channel; the
Glossary's entry 23 already establishes that no bracketed symbol in this corpus means anything but a
grade, and this states the converse where the grades are defined.

## 3. What it supersedes

`docs/Glossary.md`, "How to read this glossary", currently reads:

> **Fixed corpus-wide, flagged and not resolved here:** the grade symbols `[V]`, `[V1]`, `[V2]`,
> `[V3]`, `[N]`; the canonical five-situation `[N]` definition (quoted verbatim in Section 1); and
> the wording of the fixed plain-language legend …

**That statement is superseded by this decision as to `[N]`, and only as to `[N]`.** The other
symbols, the five-situation definition and the legend's substance remain fixed. The Glossary is
corrected in the release that implements this, per its own §8 duty that every release renaming
vocabulary updates the Glossary in the same release.

## 4. The grounds

`N` is a count symbol nearly everywhere else in this corpus. An audit on 30 August found seven
distinct senses of the letter across the two editions, six of them numeric: the total number of gate
questions, the number of runs in a sample (`n` / `N` / `K_MIN`, Glossary entry 24), the rung-C Opus
panel size, a count argument in the monitor CLI, a numeric threshold placeholder, and the grade. The
operator decision of 24 August 2026 declined to rename `n` / `N` / `K_MIN` and stated their
equivalence in the Glossary instead — which leaves one letter carrying a reserved count meaning and
the grade meaning at the same time.

That overlap produced a shipped defect on 30 August: a receipt template written as
`(0 positions, N deferred)` put `N` in the slot the canonical line reserves for `d`, where the two
coincide only in that one state. `U` collides with nothing in either edition.

"N" also mapped awkwardly onto "not". `U` says what it means.

**And there is direct evidence of reader confusion, which §5 originally denied.** The operator — the corpus's primary user and tester — reports having been confused by and misread `[N]` on multiple occasions. This is the failure the symbol change prevents, reported by the reader whose misreadings matter most. It is testimony rather than a controlled observation, and it was given after the decision rather than before it; both qualifications are stated so the ground can be weighed for what it is. It nonetheless moves the rename from a structural argument with no observed harm to a structural argument with observed harm.

## 5. The case against, recorded rather than omitted

An independent assessment (Fable 5, 30 August 2026, held at
`Insight-Engine-Portable/reviews/2026-08-30-fable5-three-artefact-consistency.md`) argued the other
side before endorsing the change, and its objections are recorded here because a decision that only
records its own justification is not a decision anyone can review:

- The change was made in the derivative edition first, inverting the corpus's precedence rule. **This
  document is the remedy for that, not a denial of it.**
- It broke the Glossary's "fixed corpus-wide" declaration made three days earlier. Superseded above,
  explicitly, rather than silently.
- The 24 August precedent declined to rename `K_MIN` on the ground that renaming a shipped identifier
  is a larger act than a wording change — and `[N]` was the most-shipped symbol in the corpus.
- ~~**No reader was ever shown to misread `[N]` as a number.**~~ **Corrected the same day, before the
  implementing release: this was false.** The operator — the corpus's primary user and tester, and
  therefore the most relevant reader there is — reports having been confused by and misreading `[N]`
  on multiple occasions. That is direct evidence of the failure the rename prevents, and it was
  available and simply not asked for. It is recorded here rather than in a later document because a
  decision record whose stated case against turns out to rest on an untested assumption is exactly
  the kind of document this corpus exists to stop producing. The evidence is operator-reported and
  self-reported after the fact, which is worth stating plainly — but it is testimony from the one
  reader whose misreadings actually matter, and it makes the rename better grounded than §4 claimed,
  not worse. The remaining objections below stand as written.
- **The bracket channel already separated the grade from every numeric use of the letter**, so the
  collision was arguably contained before the rename. The assessment's own words: *"the safety case in
  the 2.0.0 changelog is stronger than the evidence behind it."* That judgement was formed without the
  operator's testimony above; with it, the safety case and the evidence are closer than the assessment
  could have known.

The decision proceeds notwithstanding, on the grounds in §4 and because the alternative — reverting —
would create a third symbol era and re-open a collision that has already produced one defect.

## 6. Migration

**Documents produced before 30 August 2026 carry `[N]` and remain valid exactly as written.** `[N]`
in an earlier deliverable and `[U]` in a later one are the same grade under different symbols.

- **Delivered documents are never retrospectively rewritten.** Test records, run artefacts, reviews,
  archived documents and genuine retained example outputs keep `[N]` as evidence of what was
  produced. Rewriting evidence to match a later vocabulary destroys the record.
- **A `track` dossier records the symbol it was opened under.** An UPDATE re-grades in the dossier's
  own symbol, or migrates the whole dossier explicitly and says so. It never mixes the two in one
  state object.
- The Glossary retains `[N]` as a dated historical entry carrying the equivalence, because the
  pre-2026-08-30 record reads `[N]` permanently and the Glossary is where a reader will look.

## 7. Implementation

1. **This record** — canon, dated, committed before the implementing releases.
2. **Portable Edition 2.0.1** — correct the statements the rename made false in that edition, and
   record the provocation-page substitution as a declared act under this decision rather than leaving
   its governance header asserting a discipline that was not applied.
3. **The plugin convergence release** — atomic: the five skills including the legend by **byte copy**
   never retyped, the provocation page, Architecture, the Guide, Foundations, the README, the
   Glossary in the same release, the `PUBLISHING.md` maintenance line, the `track` dossier
   symbol-continuity rule, and release notes carrying §6.
4. **Portable follow-up** — re-verify both fixed texts byte-identical to the new canon.

The citation-resolution rule and the standing-deferral gate state are **not** part of this decision
and ship separately, in the order the assessment sets out.
