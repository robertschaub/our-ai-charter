# Claude Code instructions — Our AI Charter

**Primary rules live in [AGENTS.md](AGENTS.md) — read it.** This file only adds Claude-Code-specific notes; if anything diverges, AGENTS.md is authoritative.

## Snapshot

A **public, documents-only** repository: manifesto + charter + draft protocol + Public AI Network governance materials, all Markdown. No source code, build, or tests — don't add them.

Current priority: the repo has two related workstreams under the Our AI Charter umbrella. For the maintainer right now, **KI-Souveränität und Resilienz** is more urgent and higher priority; work on **Trustworthy AI, Accountable to People** only when explicitly asked, when it supports the first workstream, or where there is clear low-hanging fruit.

## Safety (see AGENTS.md §Git & safety)

- A **PreToolUse hook** in [.claude/settings.json](.claude/settings.json) blocks destructive git (`reset --hard`, `push --force`, `clean -f`, `checkout -- .`). It uses Node.js (present in this workflow) and **fires for the main session only** — never delegate destructive git to a subagent or Workflow agent.
- This repo does **not** commit a permission `defaultMode`, so your own mode applies. If you run in `bypassPermissions`, that hook is your remaining guard — keep it.
- This is a **public** repo and the **default home for all Charter material** (published or draft). Two private siblings exist for the narrow exceptions — `our-ai-charter-internal` (only personal DM/email correspondence with individuals, plus files explicitly marked `<!-- Status: INTERNAL — reason -->`) and `FactHarbor-internal` (finance/legal/banking/fundraising/Verein). Never commit personal correspondence, INTERNAL-marked, or secret material here. Cooperation/outreach/strategy/governance notes are **no longer private by default** — they belong here unless marked INTERNAL. See AGENTS.md § Where new files go and § Private administrative siblings.
- This repo intentionally keeps only the FactHarbor practices that fit a document repository. Do not copy app workflows, build commands, generated indexes, runtime database guards, or deployment machinery into this project unless the maintainer explicitly asks.
- For suspected leaked secrets or private material, follow [SECURITY.md](SECURITY.md); do not repeat the material in a public issue or PR.

## Conventions

- Conventional commits: `type(scope): description`.
- **Work directly on `main`** — commit straight to the default branch for routine work; create a branch or worktree only when the maintainer asks, or a change is large/risky enough to isolate (see [AGENTS.md](AGENTS.md) § Git & safety).
- Keep status banners, the README index, and CHANGELOG in sync — see the `/docs-update` skill. A status banner belongs on `PUBLISHED` pages, on **normative** docs (rules/obligations/guidelines: Founding Accord, evaluation protocol, certification model, one-pager), and on the **outreach and parliamentary materials** kept as working drafts (Non-Paper, Aktionsplan, Postulat); all other pages (briefings, evidence, strategy, background) carry none (see [AGENTS.md](AGENTS.md)). When the maintainer says a doc is "Published", set its header to `PUBLISHED <date>` (ISO `YYYY-MM-DD`; today's date if publishing now).
- When an article/post is published, its earlier draft is overwritten, deleted, or (rarely) moved to `Archive/<workstream>/` — archiving is **not** the default (Git history already preserves versions). The maintainer decides case by case; don't auto-act, and keep any archived files out of the index.
- **Consulting other models:** [`scripts/agents/`](scripts/agents) holds `invoke-gpt.cjs` / `invoke-gemini.cjs` / `invoke-claude.cjs` for a second opinion or cross-model review — keys load from a gitignored `.env.local`; see [AGENTS.md](AGENTS.md) § Consulting other models.
- Windows / PowerShell.
