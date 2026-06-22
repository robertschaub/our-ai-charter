# Claude Code instructions — Our AI Charter

**Primary rules live in [AGENTS.md](AGENTS.md) — read it.** This file only adds Claude-Code-specific notes; if anything diverges, AGENTS.md is authoritative.

## Snapshot

A **public, documents-only** repository: manifesto + charter + draft protocol, all Markdown. No source code, build, or tests — don't add them.

Current priority: the repo has two related workstreams under the Our AI Charter umbrella. For the maintainer right now, **KI-Souveränität und Resilienz** is more urgent and higher priority; work on **Trustworthy AI, Accountable to People** only when explicitly asked, when it supports the first workstream, or where there is clear low-hanging fruit.

## Safety (see AGENTS.md §Git & safety)

- A **PreToolUse hook** in [.claude/settings.json](.claude/settings.json) blocks destructive git (`reset --hard`, `push --force`, `clean -f`, `checkout -- .`). It uses Node.js (present in this workflow) and **fires for the main session only** — never delegate destructive git to a subagent or Workflow agent.
- This repo does **not** commit a permission `defaultMode`, so your own mode applies. If you run in `bypassPermissions`, that hook is your remaining guard — keep it.
- This is a **public** repo with two private administrative siblings — `our-ai-charter-internal` (Charter cooperation/outreach/strategy/governance drafts) and `FactHarbor-internal` (finance/legal/banking/fundraising/Verein). Never commit private/internal material or secrets here. See AGENTS.md § Private administrative siblings (maintainer-only) for the cross-repo access policy.
- This repo intentionally keeps only the FactHarbor practices that fit a document repository. Do not copy app workflows, build commands, generated indexes, runtime database guards, or deployment machinery into this project unless the maintainer explicitly asks.
- For suspected leaked secrets or private material, follow [SECURITY.md](SECURITY.md); do not repeat the material in a public issue or PR.

## Conventions

- Conventional commits: `type(scope): description`.
- Keep each document's status label (`PUBLISHED` / `WORKING DRAFT` / `WIP / DISCUSSION`), the README index, and CHANGELOG in sync — see the `/docs-update` skill.
- Windows / PowerShell.
