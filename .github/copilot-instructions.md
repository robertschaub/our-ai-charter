# Copilot / AI agent instructions — Our AI Charter

> **Canonical source:** [/AGENTS.md](../AGENTS.md). This is a short summary for inline completions; if rules diverge, follow AGENTS.md.

- **Public, documents-only** repo (manifesto + charter + draft protocol, Markdown). No source code, build, or tests — don't add them.
- Import only document-repo-safe FactHarbor practices: agent rules, issue/PR templates, safety policy, and local destructive-git guards. Do not add app workflows, dependencies, generated indexes, or deployment machinery.
- **Public-repo discipline:** never commit private/internal material or secrets. A separate private administrative repository exists for non-public work. Treat every commit as permanent and worldwide.
- **Route new files by content** (see AGENTS.md → *Where new files go*): public charter/published material stays here; legal, finance, outreach, contacts, personal data, and strategy belong in the private sibling `FactHarbor-internal`. Unsure → private, and ask. Never put confidential or personal content in this public repo.
- For suspected leaked secrets or private material, use the private reporting path in `SECURITY.md`; do not put the material in a public issue or PR.
- **Git safety:** avoid destructive git (`reset --hard`, `push --force`, `clean -f`, `checkout -- .`) unless explicitly asked; prefer a revert commit or a targeted edit.
- **Conventions:** conventional commits; keep each document's status label (`PUBLISHED` / `WORKING DRAFT` / `WIP / DISCUSSION`), the README index, and CHANGELOG in sync; cite sources; smallest concrete change over a rewrite.
- **Licensing:** text is CC BY 4.0; the name and any trust mark are reserved (see NOTICE).
