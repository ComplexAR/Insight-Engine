# Publishing &amp; releases

This repo is **both** a Claude Code plugin **and** a single-plugin marketplace. The plugin lives at the repo root; `.claude-plugin/marketplace.json` lists it with `"source": "./"`, meaning "the plugin is this same repo."

## The files that define it

- `.claude-plugin/plugin.json` — the plugin manifest (name, version, description, author, keywords). **The description must be ≤ 500 characters** (a longer one fails validation). `author` must be an object (`{ "name": "..." }`), and `keywords` must be an array — not strings.
- `.claude-plugin/marketplace.json` — the marketplace manifest. Its `name` field (`insight-engine-marketplace`) is what users type after the `@` when installing. The plugin's `version` here should match the version in `plugin.json`.
- `skills/*/SKILL.md` — the four skills (`analyse`, `verify`, `render`, `track`), plus `skills/analyse/references/provocation-page.md`.
- `dist/insight-engine-<version>.plugin` — the built file for Cowork users.

## First-time setup

1. Create a new GitHub repo named **`Insight-Engine`** under your account (`ComplexAR`), public so others can install it.
2. Put the contents of this folder at the repo root and push to the default branch (`main`). No special branch is needed — `/plugin marketplace add` reads the default branch.

## Cutting a new release

1. Make your changes to the skills.
2. **Bump the version** in BOTH `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` (keep them equal). The version is the update cache key: if you don't bump it, already-installed users will not see the change.
3. Rebuild the Cowork `.plugin` from the repo root (the `-D` flag keeps directory entries out of the zip, which the Cowork uploader requires):
   ```
   zip -D -X -9 -r dist/insight-engine-<version>.plugin .claude-plugin/plugin.json README.md skills
   ```
   (Note: this packages `plugin.json` but **not** `marketplace.json` — the `.plugin` is the plugin alone.)
4. Commit, then tag and push:
   ```
   git add -A
   git commit -m "insight-engine <version>"
   git tag -a v<version> -m "insight-engine <version>"
   git push origin main --tags
   ```
5. (Recommended) Create a GitHub **Release** for the tag and attach `dist/insight-engine-<version>.plugin` so Cowork users have a clean download link.

## Versioning

Semantic — MAJOR.MINOR.PATCH. A new capability that earned its place on a test → a minor bump (this is how 0.1.7 added the systems-investigation pass); a fix → a patch bump; a breaking change to how the skills behave → a major bump.

## If validation complains

Run `claude plugin validate --strict` from the repo root before pushing. If it reports a missing `owner.email`, add an `email` to the `owner` object in `marketplace.json`. Unrecognised fields are warnings, not errors, unless you use `--strict`.
