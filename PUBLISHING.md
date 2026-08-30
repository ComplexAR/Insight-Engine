# Publishing &amp; releases

This repo is **both** a Claude Code plugin **and** a single-plugin marketplace. The plugin lives at the repo root; `.claude-plugin/marketplace.json` lists it with `"source": "./"`, meaning "the plugin is this same repo."

## The files that define it

- `.claude-plugin/plugin.json` — the plugin manifest (name, version, description, author, keywords). **The description must be ≤ 500 characters** (a longer one fails validation). `author` must be an object (`{ "name": "..." }`), and `keywords` must be an array — not strings.
- `.claude-plugin/marketplace.json` — the marketplace manifest. Its `name` field (`insight-engine-marketplace`) is what users type after the `@` when installing. The plugin's `version` here should match the version in `plugin.json`.
- `skills/*/SKILL.md` — the five skills (`analyse`, `verify`, `render`, `track`, `adjudicate`), plus `skills/analyse/references/provocation-page.md`. The `adjudicate` skill also ships `harness/`, `monitor/`, and `prefs/` subfolders.
- `dist/insight-engine-<version>.plugin` — the built file for Cowork users.

## First-time setup

1. Create a new GitHub repo named **`Insight-Engine`** under your account (`ComplexAR`), public so others can install it.
2. Put the contents of this folder at the repo root and push to the default branch (`main`). No special branch is needed — `/plugin marketplace add` reads the default branch.

## Cutting a new release

1. Make your changes to the skills.
2. **If the release adds, renames or retires any vocabulary — a grade symbol, an identifier series, a
   defined term — update `docs/Glossary.md` in the same release.** Not the next one. A stale glossary
   asserts wrong meanings with reference authority, which is worse than no glossary at all. Where the
   change touches the fixed legend, the Glossary's quotation of it is replaced **by copy** from the
   shipped legend, never retyped — local paraphrase is the recorded cause of the v0.1.20 legend
   defect. This step was called for by the Glossary's own governance section on 27 August 2026 and
   was not added until the convergence release of 30 August 2026, which is itself the demonstration
   of why it is needed: the release before it renamed the most-used symbol in the corpus and left the
   Glossary silent.
3. **Bump the version** in BOTH `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (keep them equal). The version is the update cache key: if you don't bump it, already-installed users will not see the change.
4. Rebuild the Cowork `.plugin` from the repo root (the `-D` flag keeps directory entries out of the zip, which the Cowork uploader requires):
   ```
   zip -D -X -9 -r dist/insight-engine-<version>.plugin .claude-plugin/plugin.json README.md LICENSE skills
   ```
   (Note: this packages `plugin.json` but **not** `marketplace.json` — the `.plugin` is the plugin alone.) The recursive `skills` argument also includes any runtime files, so before building **never package `skills/adjudicate/monitor/ledger.jsonl`** (the real-use run log) — delete or git-ignore it first. **Also exclude every `__pycache__/` directory and every `.pyc` file.** Running `monitor.py`, `prefs.py` or the cross-lab harness leaves Python bytecode caches beside the sources; a naive recursive zip picks them up. On 25 August 2026 a first build of 0.1.22 packaged seven of them, adding 127 KB of stale bytecode and taking the archive from 24 files to 31. Build from a staging copy that filters them out, and check the packaged file list against the previous release: it should differ only in the files this release changes. User adjudication preferences live outside the plugin at `~/.insight-engine/` and are never packaged.
5. Commit, then tag and push:
   ```
   git add -A
   git commit -m "insight-engine <version>"
   git tag -a v<version> -m "insight-engine <version>"
   git push origin main --tags
   ```
6. (Recommended) Create a GitHub **Release** for the tag and attach `dist/insight-engine-<version>.plugin` so Cowork users have a clean download link.

## Versioning

Semantic — MAJOR.MINOR.PATCH. A new capability that earned its place on a test → a minor bump (this is how 0.1.7 added the systems-investigation pass); a fix → a patch bump; a breaking change to how the skills behave → a major bump.

## If validation fails

Run `claude plugin validate --strict` from the repo root before pushing. If it reports a missing `owner.email`, add an `email` to the `owner` object in `marketplace.json`. Unrecognised fields are warnings, not errors, unless you use `--strict`.
