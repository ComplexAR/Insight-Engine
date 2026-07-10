# harness/

- `tadj.py`     — frozen constants (`T`, from the LOCK), case model, manifest checks, blind-package
                  assembly, endpoint computation (P1–P8, MC1–3), gate dispositions (§6), report.
- `adapters.py` — `AgentDispatchAdapter` (emit prompts for the Agent tool) and `ApiAdapter`
                  (Anthropic/OpenAI call shapes, keys from env, stubbed). `ARM_SPEC` = model/rung/mode/effort/temp per arm.
- `run.py`      — CLI: `validate` | `emit` | `report`.
- `selftest.py` — synthetic end-to-end proof of the deterministic core (no model calls).
- `prompts/`    — author (arm A), adjudicate (blind→adversarial), filter (different-lineage), rater (coding + P7).

Thresholds are the LOCK's; do not edit `T` without a dated pre-registration amendment.
