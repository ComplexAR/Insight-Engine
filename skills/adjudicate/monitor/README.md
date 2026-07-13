# Real-Use Monitor (RUM) — independent adjudication

**Why this exists.** The seed batch proved adjudication's *benefit* can't be measured with constructed
cases (the disciplined method catches every error you can build-and-verify; the errors that would show
a benefit can't be planted or scored). Real problems contain those un-constructible errors. So this
turns the unanswerable experiment into an **accumulating observational base rate** from your genuine use.

**The one question it answers:** in real high-stakes use, does an independent second pass ever catch a
**decision-relevant** error the disciplined first pass missed — and does it ever **flip the call**?

## The loop (per real high-stakes /analyse)
1. Run `/analyse` normally on a genuine high-stakes problem; finish the brief.
2. Run the independent second pass (Fable now; a cross-lab model like GPT-5.6 Sol once built) — blind,
   then adversarial — on the finished analysis. (`../harness/prompts/adjudicate.txt`.)
3. Filter to observable-backed items, then **rank** and surface only the top ~3 (the reduced-test fix).
4. **You** code each: real catch? would it have changed your decision? (a flip needs a discriminating
   observable, not a hunch).
5. Append one line to the ledger: `python monitor.py log --json '{...}'` (schema in `ledger_schema.json`).

Rollup any time: `python monitor.py report`.

## Frozen coding & read-out rule (do not change without a dated amendment — that is the point)
- **Verdicts:** real-catch-flipped · real-catch-refined · useful-not-decision-relevant · false-alarm · nothing.
- **A "flip" counts only if** you agree, it names a discriminating observable, and it would have reversed
  or materially changed a real decision.
- **K_MIN = 20** real high-stakes runs before the rule reads out.
- **Read-out:** flips ≥ 1 → *adjudication earned its place* (build it properly, watch the false-alarm rate);
  0 flips at K_MIN → *decision-flip benefit is negligible in practice* (keep adjudication only as an
  optional refinement check). Secondary: decision-relevant catch-rate and false-alarm rate.

**One genuine, operator-agreed flip on a real high-stakes call outweighs any amount of constructed-case data — that is the whole point.**

## Honest limits
Observational, not controlled: only high-stakes runs are sampled; you code your own catches (hence the
observable requirement); N accrues slowly; there is no counterfactual for whether you'd have caught it
yourself on reflection. It yields a practical base rate, not a proof. `monitor.py` (rollup + read-out)
is tested; the data is yours to accrue.

## Amendment log
- **AMENDMENT-1 (2026-07-09, pre-registered before any cross-lab run):** added a rung-A-specific read-out so
  "cross-lab (rung A) earned its place" is a clean claim, not a blended one. `CROSSLAB_K_MIN=12` rung-A runs;
  `CROSSLAB_FLIP_THRESHOLD=1`. Fires: ≥1 operator-agreed observable-backed rung-A flip → *cross-lab earned its
  place*; 0 flips at ≥12 rung-A runs → *cross-lab decision-flip benefit negligible in practice*; else accruing.
  Independent of the blended (all-rung) read-out, which is unchanged.
- **AMENDMENT-2 (2026-07-13, pre-registered):** a **per-class, per-rung retirement rule** — the mechanism that
  decides, from the ledger rather than by argument, whether adjudication has become redundant for a given class
  of problem as analyser models strengthen. It answers the standing question "does a stronger analyser make this
  layer redundant?" empirically and reversibly, and never retires the layer wholesale. Requires one new ledger
  field, `class` (a short operator-set problem-class tag, e.g. `legal-exposure`, `contested-blame`,
  `financial-materiality`); runs without it fall into an `unclassified` bucket that is never auto-retired.
  - **Retire (redundant) for a class + rung** when, over the last **`RETIRE_N = 20`** adjudications in that class:
    (a) **zero** `real-catch-*` verdicts; **and** (b) `useful-not-decision-relevant` items that actually changed a
    caveat or grade occur in **under ~10%** of runs; **and** (c) those useful items merely duplicate what the
    `analyse` first pass had already flagged. Action: **demote the offer for that class to on-request only** —
    keep a **1-in-10 periodic audit run** so retirement stays a live hypothesis, not a permanent fact.
  - **Keep (warranted)** when, inside the window: any `real-catch-refined`, or an operator-agreed
    `real-catch-flipped` naming a discriminating observable; or `useful-not-decision-relevant` items that
    materially altered a caveat or grade; or the class itself shifts (new instrument, jurisdiction, or
    counterparty type) — **reset the window** on a class shift.
  - **Monoculture watch (instrument-health, not yield):** track rung-A **blind-pass divergence rate** over time.
    If cross-lab divergence trends toward zero across classes **while** ground-truth errors still surface
    elsewhere, that signals decorrelation collapse — treat rung A's silence as **loss of signal, not safety**,
    and do not read it as "models got good enough."
  - **Honesty bounds on this rule (do not soften):** convergence/agreement is evidence of low *yield* (the right
    variable for a cost decision), **not** proof the calls were correct. And because catches are tail events,
    `RETIRE_N = 20` bounds the catch rate only loosely — zero catches in 20 runs is consistent with a true rate
    up to ~14%. This rule therefore decides **economic redundancy, not tail safety**; retirement is per-class,
    reversible, and audited, never a claim that the class is now error-free.
