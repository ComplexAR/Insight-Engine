# Live cross-lab run — pre-flight checklist

Do these in order before (and during) the first live GPT-5.6 Sol adjudication.

1. **Verify the API shape.** Open `crosslab.py`; confirm the request body `{model, reasoning:{effort}, input}`
   and the endpoint match **current** OpenAI Responses-API docs. It's one dict — adjust if the schema moved.
2. **Governance.** If the matter is privileged/confidential, cross-lab is blocked by default; overriding it is a deliberate act (`run_crosslab.py --privileged --override-privileged`), logged to the monitor. Set the egress
   policy to `redacted` (send spine + contested claims, not raw docs) and arrange **zero-retention** terms with OpenAI.
3. **Key.** `export OPENAI_API_KEY=sk-...` in your shell (never commit it; it is read from env, never logged).
4. **Offline pre-flight:** `python3 preflight.py`  → expect all OK + "READY for --live".
5. **Live smoke (cheap):** `OPENAI_API_KEY=$OPENAI_API_KEY python3 preflight.py --live`
   → a tiny call that verifies endpoint + request shape + JSON parse for ~nothing, before any real spend.
6. **Full run:** `python3 run_crosslab.py --live` on a real finished analysis (edit `SAMPLE` to your case's
   blind package: facts + grade-locked spine + draft brief, **no reasoning**).
7. **Log it to the monitor** (rung A), from `../monitor`:
   `python3 monitor.py add --slug "<case>" --rung A-crosslab --verdict real-catch-refined --relevant 2 --items 7 --agreed --notes "..."`
   (add `--flip --observable "<the checkable fact>"` only for a genuine, call-changing catch).
8. `python3 monitor.py report` → the AMENDMENT-1 cross-lab read-out accrues the clean verdict.
