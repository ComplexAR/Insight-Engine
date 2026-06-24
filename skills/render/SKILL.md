---
name: render
description: Insight Engine addressee rendering, grade-locked. Triggers when the user asks to re-express or re-render a finished analysis for a specific reader or audience — adversarial, advocate, policymaker, board or executive, counsel or legal, regulator or supervisor, family or lay reader, or any named standpoint — or to produce side-by-side multi-audience versions. If no audience is named, it asks (offering the standard set plus a free-text "name your own"). A register transform only: it never changes a claim or a grade.
---

# Insight Engine — render

Re-express a finished, graded analysis for one or more audiences. This is a register transform over a grade-locked spine — never a re-analysis.

## Hard invariants
1. **No claim or grade changes.** Carry every `[V]`/`[N]`, its source tier (`[V1]`/`[V2]`/`[V3]`), and the dominant unknown verbatim, and keep them visible. A lay render may put the tier in plain words ("well-established" vs "from a single weaker source") but must never upgrade a contested `[V3]` to sound settled. If you ever feel the need to change a grade to suit an audience, stop — that is the failure mode.
2. **The non-droppable caveat core** (all grades + the dominant unknown + the one-line reliability caveat) appears in EVERY render.
3. **Re-scope and re-frame for the reader, never distort.** You may re-order and select the audience-relevant subset; you may not bend a finding.
4. **Tone.** Show understanding through accuracy and respect — acknowledge plainly what is at stake. Never ingratiating, saccharine, or over-familiar; no performed warmth. Empathy is carried by register, never by false certainty.

## Audiences (standard set; any named standpoint is also accepted)
Two kinds:
- **Opposing-interest renders** (same facts, different interest): *adversarial* — steelman the opposing interest, conceding every `[V]` and contesting only attribution or causation, re-weighting emphasis but never downgrading a grade; *advocate* — the affected party's champion.
- **Reader / register renders** (same facts, different reader): *policymaker* (reform-oriented); *board / executive* (concise, risk-and-action framed for the decision-maker); *counsel / legal* (remedy- and liability-oriented); *regulator / supervisor* (compliance and supervisory-action oriented — distinct from policymaker, who reforms rather than enforces); *family / lay* (warm-but-plain and personal, within the tone rule above).

## Naming the audience — ask if not given (free text always allowed)
The standard set is a starting menu, not a closed list: **any named standpoint is a first-class target.** If the operator invokes render without naming the audience(s), do not guess silently — **ask.** Put the question to the operator with the question tool: offer a few of the common standpoints above as options **and** an open "name your own" free-text choice, so any reader not on the list can be given — a journalist or the press, an investor or shareholder, a clinician or practitioner, opposing counsel, a union or workforce, the general public, or a specific named person or body. Let the operator pick more than one (two or more selected means comparative mode). Whatever standpoint is named — preset or free-text — build its register from that reader's interests, leverage, and information needs, under the same hard invariants. Never block: if the operator declines to choose, default to the most decision-relevant reader for this analysis and state which you used.

## Modes
- **Distributed** — one rendered version per audience.
- **Comparative** — one document with a labelled panel per audience over the shared spine, plus a **Divergence Ledger** (per spine node: each panel's frame and the divergence type, which must be register / scope / framing only) and a **Robustness Map** (tag each node hardened / contested / narrator-only). Co-locate distinct labelled registers; never blend them into one voice.

## Fidelity self-check (hard)
For each render or panel, assert its claim/grade set is identical to the spine and the caveat core is present; for comparative, assert ledger purity (every entry is register/scope/framing only — never a changed fact or grade). On any drift, re-render once; if it drifts again, stop and report — never deliver a drifted render.
