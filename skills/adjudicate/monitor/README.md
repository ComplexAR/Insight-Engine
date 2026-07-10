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
