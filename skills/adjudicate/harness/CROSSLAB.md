# Cross-lab adjudicator (rung A) — interface, operation, governance

**What it is.** Rung A of the adjudication ladder: an **external-lab** frontier model as the
strongest-independence adjudicator (a different training lineage → most decorrelated blind spots).
Multi-provider: choose OpenAI (default `gpt-5.6-sol`), Google Gemini (`gemini-3.5-flash`), xAI Grok
(`grok-4.5`), or **Other** (any OpenAI-compatible endpoint, or an operator-written adapter file). It is
the *dispatch* the layer needed; everything downstream (filter, rank, monitor) is unchanged.

**Interface** (`crosslab.py`):
```
CrossLabAdjudicator(model=None, provider=None, base_url=None, egress_policy="off", effort="high", timeout=120)
    .dispatch(blind_pkg, adjudicate_prompt, privileged=False, override_privileged=False) -> discrepancy_report (dict)
MockAdjudicator(...)   # identical interface + gates, canned report, no network/key/spend
```
- **Blind package** = facts + grade-locked spine + draft brief, **no reasoning**; `build_blind_text` injects it
  into `prompts/adjudicate.txt` (blind→adversarial two-pass contract, discriminating-observable requirement).
- **Request** is provider-specific, from the `PROVIDERS` registry in `crosslab.py`:
  - **openai** — `POST https://api.openai.com/v1/responses`, `{model, reasoning:{effort}, input}`, Bearer `OPENAI_API_KEY`, response `output[].content[].text`.
  - **google** — `POST .../v1beta/models/{model}:generateContent`, `{contents:[{parts:[{text}]}]}`, `x-goog-api-key` header (never a URL key), `GEMINI_API_KEY`, response `candidates[0].content.parts[].text`.
  - **xai** — `POST https://api.x.ai/v1/chat/completions`, `{model, messages:[{role,content}], reasoning_effort}`, Bearer `XAI_API_KEY`, response `choices[0].message.content`.
  - **other** — the OpenAI-compatible `chat/completions` shape against `CROSSLAB_BASE_URL`, or an operator adapter file's `PROVIDER`.
  The response is parsed to the strict-JSON discrepancy report (tolerates ```json fences), tagged `_adjudicator_model` + `_adjudicator_provider` + `_rung="A-crosslab"`.

**Governance (enforced in code, per build-spec §4a):**
- `privileged=True` → `EgressBlocked` (**blocked by default**; overriding is a deliberate typed act via `run_crosslab.py --privileged --override-privileged`, logged, never auto-taken).
- `egress_policy="off"` (default) → blocked; must be set `redacted` or `full` to run.
- Key read from the environment only, **never logged**; **zero-retention** terms arranged with the provider out of band.
- Minimise: send the spine + contested claims, not raw privileged source documents.
- **Failures are stable-tagged** for the skill to branch on (the tag begins the message): `CROSSLAB-BLOCKED [no-key|privileged|egress-off|same-lineage|provider-unknown|provider-model-mismatch|no-base-url|no-model|lineage-undeclared|adapter-off|adapter-path|adapter-missing|adapter-shape|adapter-changed]` and `CROSSLAB-FAILED [auth NNN|model-unavailable 404|quota 429|network|api NNN]`.
- **Resolution** (done by the runners via `crosslab_env.py`, not the adapter): shell env wins > standing pref (`prefs/`) > provider default — for the provider and model (and, for `other`, base_url / key-env-name / lineage / adapter). Exception: for provider `other` the standing `crosslab_model` is NOT exported — a per-run `CROSSLAB_MODEL` or the adapter's `default_model` supplies it, so a predefined-lab model is never sent to a foreign endpoint. `crosslab.py` stays pure and reads only the `CROSSLAB_*` env vars. Provider `auto` infers from the model name; an explicit provider wins; a provider/model mismatch is refused.

**Run:**
- MOCK (offline, proven here): `python3 run_crosslab.py`
- LIVE (your own local terminal, your key, **paid**): in **PowerShell** (recommended over Command Prompt — its output copies cleanly back into chat), set the key then run — `$env:OPENAI_API_KEY = Read-Host 'Paste key'` then `python run_crosslab.py --live`. (The `OPENAI_API_KEY=sk-... python3 run_crosslab.py --live` one-liner is bash / macOS-Linux only.)
  → **Verify the request/response shape against the resolved provider's current docs first** — each adapter's
  body targets that lab's API as understood at build time and is a single dict, easy to adjust.

**Feeds the monitor.** Log each real cross-lab run with `adjudicator_rung:"A-crosslab"`; the monitor's
**AMENDMENT-1** cross-lab-specific read-out then isolates whether cross-lab *specifically* earned its place.

**Status (v0.1.18).** OpenAI (the rung-A default) is **live-verified** — a real smoke returned a clean parse.
The **Google Gemini and xAI Grok adapters are built to each lab's current published API (verified 2026-07-09)
but NOT live-smoked** (no billing set up for those labs); they are live-verified only when you run
`preflight.py --live` with that lab's key. All governance gates, the same-lineage guard, provider routing,
the OpenAI-compatible "Other" mode, and the pluggable-adapter loader are offline-tested end-to-end in `preflight.py`.
