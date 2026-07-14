# Live cross-lab run — pre-flight checklist

Do these in order before (and during) the first live adjudication on whichever lab you choose.
Rung A can target OpenAI, Google Gemini, xAI Grok, or any OpenAI-compatible endpoint ("Other").

Work in your OWN local terminal — **PowerShell** is easiest on Windows (its output copies cleanly
back into chat). Keys are set by you in your shell, never pasted into chat, never committed.

1. **Choose the lab and model** (optional — the default is OpenAI / `gpt-5.6-sol`). From `../prefs`:
   `python prefs.py set crosslab_provider google` (or `openai` / `xai` / `other`), and optionally
   `python prefs.py set crosslab_model <model>` (else the provider's own default is used). Or override
   just this run with the `CROSSLAB_PROVIDER` / `CROSSLAB_MODEL` environment variables. For `other`,
   also set `crosslab_base_url` (https), the key-env name (`crosslab_other_key_env`), and
   `crosslab_other_lineage`.

2. **Verify the API shape** for the resolved provider. Open `crosslab.py`; confirm that adapter's
   endpoint, headers, and body match the lab's **current** API docs (each is a small dict — adjust
   if the schema moved). A Claude-lineage target is refused by the same-lineage guard (rung A must
   be a different lab; use rung B/C for a same-lineage check).

3. **Governance.** If the matter is privileged/confidential, cross-lab is blocked by default;
   overriding it is a deliberate act (`run_crosslab.py --privileged --override-privileged`), logged to
   the monitor. Set `egress_mode` to `redacted` (send the spine + contested claims, not raw docs) and
   arrange **zero-retention** terms with the lab you chose.

4. **Key.** Set the resolved provider's key in your own shell (PowerShell):
   - OpenAI:  `$env:OPENAI_API_KEY = Read-Host 'Paste key'`
   - Google:  `$env:GEMINI_API_KEY = Read-Host 'Paste key'`
   - xAI:     `$env:XAI_API_KEY = Read-Host 'Paste key'`
   - Other:   set whatever `crosslab_other_key_env` names.

   (macOS/Linux: `export OPENAI_API_KEY=sk-...`.) The key is read from the env, never logged.

5. **Offline pre-flight:** `python preflight.py` → expect all OK, the right `provider/model`, the
   resolved key shown as set, and "READY for --live".

6. **Live smoke (cheap):** `python preflight.py --live` → a tiny call that verifies the endpoint,
   request shape, and JSON parse for the resolved provider, for ~nothing, before any real spend.

7. **Full run:** `python run_crosslab.py --live` on a real finished analysis (edit `SAMPLE` to your
   case's blind package: facts + grade-locked spine + draft brief, **no reasoning**).

8. **Log it to the monitor** (rung A), from `../monitor`:
   `python monitor.py add --slug "<case>" --rung A-crosslab --verdict real-catch-refined --relevant 2 --items 7 --agreed --notes "..."`
   (add `--flip --observable "<the checkable fact>"` only for a genuine, call-changing catch).
9. `python monitor.py report` → the AMENDMENT-1 cross-lab read-out accrues the clean verdict.
