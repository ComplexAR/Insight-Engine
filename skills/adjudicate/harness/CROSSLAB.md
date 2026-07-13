# Cross-lab adjudicator (rung A) — interface, operation, governance

**What it is.** Rung A of the adjudication ladder: an **external-lab** frontier model (default OpenAI
**GPT-5.6 Sol**) as the strongest-independence adjudicator (different training lineage → most decorrelated
blind spots). It is the *dispatch* the layer needed; everything downstream (filter, rank, monitor) is unchanged.

**Interface** (`crosslab.py`):
```
CrossLabAdjudicator(model="gpt-5.6-sol", egress_policy="off", effort="high", timeout=120)
    .dispatch(blind_pkg, adjudicate_prompt, privileged=False, override_privileged=False) -> discrepancy_report (dict)
MockAdjudicator(...)   # identical interface + gates, canned report, no network/key/spend
```
- **Blind package** = facts + grade-locked spine + draft brief, **no reasoning**; `build_blind_text` injects it
  into `prompts/adjudicate.txt` (blind→adversarial two-pass contract, discriminating-observable requirement).
- **Request** = `POST https://api.openai.com/v1/responses`, body `{model, reasoning:{effort}, input}`, Bearer
  key from `OPENAI_API_KEY`. **Response** parsed to the strict-JSON discrepancy report (tolerates ```json fences),
  tagged `_adjudicator_model` + `_rung="A-crosslab"`.

**Governance (enforced in code, per build-spec §4a):**
- `privileged=True` → `EgressBlocked` (**blocked by default**; overriding is a deliberate typed act via `run_crosslab.py --privileged --override-privileged`, logged, never auto-taken).
- `egress_policy="off"` (default) → blocked; must be set `redacted` or `full` to run.
- Key read from the environment only, **never logged**; **zero-retention** terms arranged with the provider out of band.
- Minimise: send the spine + contested claims, not raw privileged source documents.
- **Failures are stable-tagged** for the skill to branch on (the tag begins the message): `CROSSLAB-BLOCKED [no-key|privileged|egress-off]` and `CROSSLAB-FAILED [auth 401|model-unavailable 404|quota 429|network|api NNN]` (HTTP-code classified, provider-agnostic).

**Run:**
- MOCK (offline, proven here): `python3 run_crosslab.py`
- LIVE (your environment, your key, **paid**): `OPENAI_API_KEY=sk-... python3 run_crosslab.py --live`
  → **Verify the request/response shape against current OpenAI docs first** — the body targets the Responses
  API as understood at build time and is a single dict, easy to adjust.

**Feeds the monitor.** Log each real cross-lab run with `adjudicator_rung:"A-crosslab"`; the monitor's
**AMENDMENT-1** cross-lab-specific read-out then isolates whether cross-lab *specifically* earned its place.

**Status:** adapter built + **mock-tested end-to-end**; all governance gates verified. The **live path is
built-to-spec but unverified against the real endpoint** (no API key is handled in this environment).
