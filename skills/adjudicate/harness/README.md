# harness/ — the cross-lab adjudicator (rung A)

- `crosslab.py`      — the rung-A adapter: the `PROVIDERS` registry (OpenAI / Google / xAI / Other +
                       operator adapter files), `CrossLabAdjudicator` (governance gates, same-lineage
                       guard, provider routing), and a `MockAdjudicator` for offline tests. Stdlib only;
                       reads only `CROSSLAB_*` env (never imports prefs).
- `crosslab_env.py`  — resolves adjudication prefs → `CROSSLAB_*` env before crosslab is imported
                       (shell env wins > standing pref > default; provider auto-inference from the model).
- `run_crosslab.py`  — MOCK (default) / LIVE (`--live`, paid) run on a blind package; `--privileged` /
                       `--override-privileged` drive the governance gate.
- `preflight.py`     — offline checks (import, prompt, mock dispatch, gates, per-provider parse + tagged
                       errors, same-lineage guard, routing/mismatch, the "Other" mode, and the adapter
                       loader) plus a cheap `--live` smoke against the resolved provider.
- `prompts/adjudicate.txt` — the pass-1 prompt. Blind: facts + spine, the call withheld.
- `prompts/adversarial.txt` — the pass-2 prompt, sent only after pass 1 returns, with the brief revealed.
- `CROSSLAB.md` — interface / operation / governance.  `PREFLIGHT.md` — the per-lab live-run checklist.

Stdlib only. Keys are read from the environment, never logged. `~/.insight-engine/` (preferences and any
operator adapter files) lives outside this folder and is never version-controlled.
