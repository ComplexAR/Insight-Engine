# Capture procedure (copy per real run)

After a genuine high-stakes `/analyse`, before you act on the brief:

1. **Dispatch the adjudicator** on the finished analysis (blind package = facts + grade-locked spine +
   draft brief, NOT your reasoning). Prefer a different-lab model if built & egress-permitted; else Fable;
   else an Opus panel. Prompts: `../harness/prompts/adjudicate.txt` (blind), then
   `../harness/prompts/adversarial.txt` (adversarial, after the blind verdict returns).
2. **Filter** each returned item: keep only those with a genuine discriminating observable.
3. **Rank** the survivors by "would acting on this change my call or a grade?" — surface the **top 3**.
4. **Code the run** honestly against the top items:
   - `real-catch-flipped` (+ `would_have_flipped_call:true` + the `discriminating_observable`) — it would
     have changed your decision. THIS is the metric that matters.
   - `real-catch-refined` — a real, decision-relevant sharpening that did not flip the call.
   - `useful-not-decision-relevant` / `false-alarm` / `nothing` otherwise.
5. **Log it:** `python monitor.py log --json '{"problem_slug":"...","stakes_tier":"high","adjudicator_rung":"B-fable","items_raised":8,"items_decision_relevant_after_rank":2,"operator_verdict":"real-catch-refined","would_have_flipped_call":false,"operator_agreed":true,"discriminating_observable":"","notes":"..."}'`
   - For a **rung-A (cross-lab)** run, also record which lab: add `"provider":"openai"` (or `google` / `xai` / `other:<name>`) to the JSON, or use `python monitor.py add ... --provider openai`.

Keep slugs/notes free of confidential detail. Review with `python monitor.py report` after each run;
the pre-registered read-out fires at 20 runs.
