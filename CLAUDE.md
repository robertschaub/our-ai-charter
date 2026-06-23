# Claude Code instructions — Our AI Charter

**Primary rules live in [AGENTS.md](AGENTS.md) — read it.** This file only adds Claude-Code-specific notes; if anything diverges, AGENTS.md is authoritative.

## Snapshot

A **public, documents-only** repository: manifesto + charter + draft protocol, all Markdown. No source code, build, or tests — don't add them.

Current priority: the repo has two related workstreams under the Our AI Charter umbrella. For the maintainer right now, **KI-Souveränität und Resilienz** is more urgent and higher priority; work on **Trustworthy AI, Accountable to People** only when explicitly asked, when it supports the first workstream, or where there is clear low-hanging fruit.

## Safety (see AGENTS.md §Git & safety)

- A **PreToolUse hook** in [.claude/settings.json](.claude/settings.json) blocks destructive git (`reset --hard`, `push --force`, `clean -f`, `checkout -- .`). It uses Node.js (present in this workflow) and **fires for the main session only** — never delegate destructive git to a subagent or Workflow agent.
- This repo does **not** commit a permission `defaultMode`, so your own mode applies. If you run in `bypassPermissions`, that hook is your remaining guard — keep it.
- This is a **public** repo and the **default home for all Charter material** (published or draft). Two private siblings exist for the narrow exceptions — `our-ai-charter-internal` (only personal DM/email correspondence with individuals, plus files explicitly marked `<!-- Status: INTERNAL — reason -->`) and `FactHarbor-internal` (finance/legal/banking/fundraising/Verein). Never commit personal correspondence, INTERNAL-marked, or secret material here. Cooperation/outreach/strategy/governance notes are **no longer private by default** — they belong here unless marked INTERNAL. See AGENTS.md § Where new files go and § Private administrative siblings.
- This repo intentionally keeps only the FactHarbor practices that fit a document repository. Do not copy app workflows, build commands, generated indexes, runtime database guards, or deployment machinery into this project unless the maintainer explicitly asks.
- For suspected leaked secrets or private material, follow [SECURITY.md](SECURITY.md); do not repeat the material in a public issue or PR.

## Conventions

- Conventional commits: `type(scope): description`.
- Keep each document's status label (`PUBLISHED` / `WORKING DRAFT` / `WIP / DISCUSSION`), the README index, and CHANGELOG in sync — see the `/docs-update` skill.
- When an article/post is published, its earlier draft is overwritten, deleted, or (rarely) moved to `Archive/<workstream>/` — archiving is **not** the default (Git history already preserves versions). The maintainer decides case by case; don't auto-act, and keep any archived files out of the index.
- Windows / PowerShell.
