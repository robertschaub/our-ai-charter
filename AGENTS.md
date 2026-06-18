<!-- Status: WORKING DRAFT — operational rules for this repo. -->

# AGENTS.md

How AI agents (and humans) should work in the **Our AI Charter** repository.

This is the authoritative working-rules file. Tool-specific wrappers — [CLAUDE.md](CLAUDE.md) and [.github/copilot-instructions.md](.github/copilot-instructions.md) — point here. If they ever diverge, **this file wins**. If something is genuinely ambiguous, ask the maintainer before proceeding.

## What this repository is

- A **public, documents-only** repository: a published manifesto, a signable charter, and a draft evaluation protocol — all Markdown.
- **No source code, build, tests, or dependencies.** Do not add a package manager, application tooling, or a CI build pipeline. Changes here are prose and structure.
- Keep imported FactHarbor practices **documents-only**: agent rules, issue/PR templates, safety policies, and local destructive-git guards are appropriate; app runtime rules, generated indexes, database guards, test commands, and deployment workflows are not.
- Every document carries a **status label** at the top — `PUBLISHED`, `WORKING DRAFT`, or `WIP / DISCUSSION`. Keep it accurate; it's how readers know what is final.

## Program constellation

Our AI Charter is the public normative framework in a broader research program:

> Researching how we can build a fair, stable, and sustainable society that uses new technologies responsibly.

The public program map is [PROGRAM.md](PROGRAM.md). This repository should contain only the public normative layer: charter, manifesto, evaluation protocol, and public background.

Boundary rules for agents:

- Stay inside this repository root unless the maintainer explicitly names an external repository or path in the current task.
- Do not read, import, summarize, or reference private operational material in this repository or any public artifact produced from it.
- Do not create public links, document dependencies, or process dependencies on private repositories, local machine paths, or unpublished operational records.
- Public cross-links should point to public URLs or public files only.

## Public-repo discipline (read first)

This repository is **public**. A separate private administrative repository exists for non-public material — that is where anything confidential belongs, never here.

- **Never commit private, internal, unpublished-confidential, or personal data into this repo.** When in doubt, leave it out.
- **Never commit secrets** — API keys, tokens, credentials, `.env` files. GitHub **secret scanning + push protection** is enabled and will block known secret formats, but treat it as a backstop, not a license to be careless.
- If sensitive material appears in a working tree, diff, issue, or PR, stop and notify the maintainer privately; do not open a public issue containing the material. See [SECURITY.md](SECURITY.md).
- Do not create public links or process dependencies on private repositories. Keep non-public working material outside this repo.
- Assume everything committed is **permanent and worldwide** — forks, caches, and search indexes mean you cannot fully un-publish.

## Git & safety

- **Solo maintainer + AI agents.** Direct commits to `main` are normal.
- **Avoid destructive git unless the user explicitly asks.** A local Claude Code **PreToolUse hook** ([.claude/settings.json](.claude/settings.json)) hard-blocks `git reset --hard`, `git push --force` (without `--force-with-lease`), `git clean -f`, and `git checkout -- .`. To undo committed work, prefer a **new revert commit** or a targeted `Edit` — not history rewrites.
- **Hooks fire for the main session only** — *not* for subagents or Workflow agents. Never delegate a destructive or irreversible git step to a subagent; keep those in the main session.
- Commit messages follow **conventional commits**: `type(scope): description` (e.g. `docs(protocol): clarify the support rubric`).
- Do not add GitHub Actions or build/publish workflows copied from FactHarbor unless the maintainer explicitly asks for a document-only workflow.

## GitHub repository posture

- Repository visibility is **public**; non-public material belongs in a private administrative repository.
- Only the maintainer account should have direct repository access. Do not add collaborators, write deploy keys, webhooks, or GitHub Apps without explicit maintainer approval.
- Public issues and pull requests are enabled for feedback. GitHub Pages is enabled as a simple document site from `main`; keep it branch/Jekyll-based unless the maintainer explicitly asks for a richer document viewer. Wiki and Projects should stay disabled. Actions may be enabled only to support GitHub Pages builds, with allowed actions restricted to local actions; do not add workflow files unless explicitly requested.
- Do not copy FactHarbor's xWiki XAR import/export workflow into this repo. If the site later needs richer navigation, port only the static presentation pieces needed for Pages and keep the Markdown documents authoritative.
- `main` should be protected against force-pushes and deletion. Personal-account repositories cannot restrict protected-branch push access to a named user, so the practical control is keeping collaborators and write-capable integrations empty.
- GitHub secret scanning, push protection, Dependabot vulnerability alerts, and private vulnerability reporting should stay enabled.

## Working norms

- **Open drafts + a dated change log.** Record notable changes in [CHANGELOG.md](CHANGELOG.md) with an ISO date (`YYYY-MM-DD`).
- **Use Git for versioning.** Keep published article and post mirror filenames stable; do not create dated or versioned copies such as `*-v2.md` or `*-2026-06-16.md`. Use Git history, status labels, changelog entries, and document notes to record versions and changes.
- **Lean documentation by default.** Use `/doc-guard` ([.claude/skills/doc-guard/SKILL.md](.claude/skills/doc-guard/SKILL.md), mirrored at [.agents/skills/doc-guard/SKILL.md](.agents/skills/doc-guard/SKILL.md)) before adding a new document, substantially expanding or rewriting Markdown, or reviewing a documentation diff for clutter. State the reader need, the existing home, the chosen option (`tighten | amend | merge | move | delete | add`), and the lean test. Prefer tightening, merging, moving, or deleting before adding; cut filler, repeated background, placeholder sections, decorative structure, and generic values language.
- **Keep the README index and status labels in sync** whenever you add, rename, promote, or retire a document. The `/docs-update` skill ([.claude/skills/docs-update/SKILL.md](.claude/skills/docs-update/SKILL.md)) walks this.
- **Cite sources; prefer the smallest concrete improvement** over a grand rewrite (see [CONTRIBUTING.md](CONTRIBUTING.md)). Record minority interpretations rather than hiding them.
- **Licensing:** document text is **CC BY 4.0**; the initiative's name and any trust mark are **reserved** (see [NOTICE](NOTICE)). Do not paste in text under an incompatible license.

## Platform

Windows. Use **PowerShell-compatible** commands (`$env:VAR`, not `$VAR`; `$null`, not `/dev/null`; backtick for line continuation).
