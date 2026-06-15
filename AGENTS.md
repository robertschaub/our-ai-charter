<!-- Status: WORKING DRAFT — operational rules for this repo. -->

# AGENTS.md

How AI agents (and humans) should work in the **Our AI Charter** repository.

This is the authoritative working-rules file. Tool-specific wrappers — [CLAUDE.md](CLAUDE.md) and [.github/copilot-instructions.md](.github/copilot-instructions.md) — point here. If they ever diverge, **this file wins**. If something is genuinely ambiguous, ask the maintainer before proceeding.

## What this repository is

- A **public, documents-only** repository: a published manifesto, a signable charter, and a draft evaluation protocol — all Markdown.
- **No source code, build, tests, or dependencies.** Do not add a package manager, application tooling, or a CI build pipeline. Changes here are prose and structure.
- Keep imported FactHarbor practices **documents-only**: agent rules, issue/PR templates, safety policies, and local destructive-git guards are appropriate; app runtime rules, generated indexes, database guards, test commands, and deployment workflows are not.
- Every document carries a **status label** at the top — `PUBLISHED`, `WORKING DRAFT`, or `WIP / DISCUSSION`. Keep it accurate; it's how readers know what is final.

## Public-repo discipline (read first)

This repository is **public**. A separate, **private** repository (`FactHarbor-internal`) exists for non-public material — that is where anything confidential belongs, never here.

- **Never commit private, internal, unpublished-confidential, or personal data into this repo.** When in doubt, leave it out.
- **Never commit secrets** — API keys, tokens, credentials, `.env` files. GitHub **secret scanning + push protection** is enabled and will block known secret formats, but treat it as a backstop, not a license to be careless.
- If sensitive material appears in a working tree, diff, issue, or PR, stop and notify the maintainer privately; do not open a public issue containing the material. See [SECURITY.md](SECURITY.md).
- Do not create public links or process dependencies on the private sibling repository. Keep non-public working material in `FactHarbor-internal`, not here.
- Assume everything committed is **permanent and worldwide** — forks, caches, and search indexes mean you cannot fully un-publish.

## Git & safety

- **Solo maintainer + AI agents.** Direct commits to `main` are normal.
- **Avoid destructive git unless the user explicitly asks.** A local Claude Code **PreToolUse hook** ([.claude/settings.json](.claude/settings.json)) hard-blocks `git reset --hard`, `git push --force` (without `--force-with-lease`), `git clean -f`, and `git checkout -- .`. To undo committed work, prefer a **new revert commit** or a targeted `Edit` — not history rewrites.
- **Hooks fire for the main session only** — *not* for subagents or Workflow agents. Never delegate a destructive or irreversible git step to a subagent; keep those in the main session.
- Commit messages follow **conventional commits**: `type(scope): description` (e.g. `docs(protocol): clarify the support rubric`).
- Do not add GitHub Actions or build/publish workflows copied from FactHarbor unless the maintainer explicitly asks for a document-only workflow.

## Working norms

- **Open drafts + a dated change log.** Record notable changes in [CHANGELOG.md](CHANGELOG.md) with an ISO date (`YYYY-MM-DD`).
- **Keep the README index and status labels in sync** whenever you add, rename, promote, or retire a document. The `/docs-update` skill ([.claude/skills/docs-update/SKILL.md](.claude/skills/docs-update/SKILL.md)) walks this.
- **Cite sources; prefer the smallest concrete improvement** over a grand rewrite (see [CONTRIBUTING.md](CONTRIBUTING.md)). Record minority interpretations rather than hiding them.
- **Licensing:** document text is **CC BY 4.0**; the initiative's name and any trust mark are **reserved** (see [NOTICE](NOTICE)). Do not paste in text under an incompatible license.

## Platform

Windows. Use **PowerShell-compatible** commands (`$env:VAR`, not `$VAR`; `$null`, not `/dev/null`; backtick for line continuation).
