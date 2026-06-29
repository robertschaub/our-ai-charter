<!-- Status: DRAFT — operational rules for this repo. -->

# AGENTS.md

How AI agents (and humans) should work in the **Our AI Charter** repository.

This is the authoritative working-rules file. Tool-specific wrappers — [CLAUDE.md](CLAUDE.md) and [.github/copilot-instructions.md](.github/copilot-instructions.md) — point here. If they ever diverge, **this file wins**. If something is genuinely ambiguous, ask the maintainer before proceeding.

## What this repository is

- A **public, documentation-first** repository: a published manifesto, a signable charter, a draft evaluation protocol, and Public AI Network governance materials. Markdown remains authoritative; limited presentation assets and documentation-support tooling are allowed.
- **No application runtime, product code, package-managed app, or test suite.** The MkDocs site build, repository hooks, and small `scripts/agents/` review helpers are the documented exceptions.
- Keep imported FactHarbor practices scoped to documentation: agent rules, issue/PR templates, safety policies, and local destructive-git guards are appropriate; app runtime rules, generated indexes, database guards, test commands, and unrelated deployment workflows are not.
- **Status banners.** A status banner sits at the top of four kinds of page only: the **normative** docs that state rules, obligations, or guidelines (the Charter Commitments, the evaluation protocol, the certification model, the one-pager); the **outreach and parliamentary** drafts (the Non-Paper, the Aktionsplan, the Postulat); **`PUBLISHED`** pages; and the **`docs/wip/`** working notes. The banner is a plain `> **Status: …**` blockquote, **not** a typed callout (the `[!NOTE]` / `[!TIP]` / `[!WARNING]` headers read as advice or hazards, which is wrong for a status label), labelled `DRAFT` for the normative and outreach drafts, `PUBLISHED <date>` (ISO `YYYY-MM-DD`) for published pages, and `WORKING NOTES` for the raw `docs/wip/` material not yet anchored into the curated structure. All other pages — evidence, strategy, background, the About page, and the home page — carry **no** banner. Keep labels accurate; the README index still notes each document's status. Reserve `> [!WARNING]` / `> [!CAUTION]` for genuine in-body hazards, never for status.

## Program constellation

Our AI Charter is the public framework of principles and obligations in a broader program:

> Working to build a free and fair society where technology is used responsibly and enables well-grounded decision-making.

The public About page is [PROGRAM.md](docs/PROGRAM.md). This repository is the public home of **Our AI Charter**, a **Public AI Network** initiative. Its documents live under `docs/` (the website's content root): the **Overview** front door (`docs/network-overview.md`), the **AI-infrastructure pillar** (`docs/Infrastructure/`), the **published-article collection** (`docs/Published/`), and the campaign folders `docs/Strategy/`, `docs/Outreach/`, `docs/Evidence/`. The home page (`docs/index.md`) carries the orientation and reader paths. The one nested **building block** is **AI Assurance & Certification** (`docs/Assurance/`, the trust/evidence layer — including its cross-cutting **concept** notes under `docs/Assurance/Concepts/`). Repo-meta files (README, AGENTS, CHANGELOG, CONTRIBUTING, SECURITY, LICENSE, NOTICE) stay at the repo root.

Current agent priority:

- This repository is the public home of **Our AI Charter**, a **Public AI Network** initiative. It is organised as the network itself plus one building block:
  - **The Public AI Network** (the `docs/` root) — the public-AI **sovereignty, resilience, Swiss innovation-location, and international-values** work: the network overview, the federated public AI infrastructure pillar, and the strategy/outreach/evidence that advance it (*KI-Souveränität und Resilienz*).
  - **AI Assurance & Certification** (`docs/Assurance/`) — the **accountability, evaluation, Charter, and protocol** building block (*Trustworthy AI, Accountable to People*).
- Published article mirrors live together in `docs/Published/` regardless of topic; do not create topic-specific `Published/` subfolders.
- For the maintainer right now, the **Public AI Network (sovereignty/resilience) work is more urgent and higher priority**. When proposing next steps, choosing between open tasks, or deciding where to spend effort, agents should primarily invest there.
- Work on the **AI Assurance & Certification** building block only when the maintainer explicitly asks for it, when it is needed to support the Public AI Network work, or where there is clear low-hanging fruit that does not distract from it.
- Do not assume the evaluation-protocol or pilot-readiness path is the next priority merely because it is well developed in the repository.

Boundary rules for agents:

- Stay inside this repository root unless the maintainer explicitly names an external repository or path in the current task. The private administrative siblings (see *Private administrative siblings (maintainer-only)* below) are a standing named exception for maintainer-side agents.
- Maintainer-side agents may **read** a private administrative sibling repository when a task requires it (see *Private administrative siblings (maintainer-only)* below), but must **never copy, import, summarize, quote, or paraphrase its confidential or personal content into this repository or any public artifact produced from it.**
- Do not create public links, document dependencies, or process dependencies on private repositories, local machine paths, or unpublished operational records.
- Public cross-links should point to public URLs or public files only.

## Public-repo discipline (read first)

This repository is **public**, and it is the **default home for all Charter material** — published *and* draft. Two separate private administrative repositories exist for the narrow set of things that must stay private: `our-ai-charter-internal` (only personal DM/email correspondence with individuals, plus anything the maintainer explicitly marks INTERNAL) and `FactHarbor-internal` (finance, legal, banking, fundraising, Verein). Anything confidential belongs in one of those, never here.

- **Never commit personal correspondence, INTERNAL-marked, or otherwise confidential/personal data into this repo.** Drafts and works-in-progress are fine here — being unpublished does not make something private — but when you are unsure whether a specific item is sensitive, leave it out and ask the maintainer.
- **Never commit secrets** — API keys, tokens, credentials, `.env` files. GitHub **secret scanning + push protection** is enabled and will block known secret formats, but treat it as a backstop, not a license to be careless.
- If sensitive material appears in a working tree, diff, issue, or PR, stop and notify the maintainer privately; do not open a public issue containing the material. See [SECURITY.md](SECURITY.md).
- Do not create public links or process dependencies on private repositories. Keep non-public working material outside this repo.
- Assume everything committed is **permanent and worldwide** — forks, caches, and search indexes mean you cannot fully un-publish.

## Private administrative siblings (maintainer-only)

Confidential material never lives in this public repo. It is split across **two private sibling repositories**:

- **`our-ai-charter-internal`** — Our AI Charter's private sibling, now deliberately **narrow**: it holds only (1) personal DM/email correspondence with individuals acting in a private capacity, and (2) documents the maintainer has explicitly marked `<!-- Status: INTERNAL — <reason> -->`. Charter cooperation, outreach, strategy, and governance drafts are **no longer private by default** — they live in the public repo unless marked INTERNAL.
- **`FactHarbor-internal`** — the FactHarbor Verein's administrative repo: legal, finance, banking, fundraising, and Verein organisation records — **including Our AI Charter's finances and Verein records.**

Our AI Charter and FactHarbor are separate but related projects, both stewarded by Robert Schaub and the FactHarbor Verein. This public repository is the program's umbrella for the *public* normative and published work; the two private siblings are the home for anything confidential.

- **Access is restricted to the maintainer, Robert Schaub.** External contributors and their agents have no access to either and should not expect any.
- When the maintainer runs an AI agent on his own machine, that agent may be granted **read/write access to the private siblings** and may use them for cross-repo tasks.
- The hard invariant still holds: **never copy, quote, or derive confidential or personal data from a private repo into this public repo or any public artifact.** When in doubt, leave it out and ask the maintainer.

## Where new files go (route by content, not by cwd)

This public repo and the two private siblings are one program. Route every new file by what it contains, regardless of which repo the agent was launched in:

| Content | Home |
|---|---|
| Charter, manifesto, protocol, articles/posts/comments (**published _or_ draft**), public background, cooperation/outreach/strategy/governance notes — the default for anything not in a row below | **`our-ai-charter`** (here) |
| Personal DM/email correspondence with an individual acting privately; any file whose header is marked `<!-- Status: INTERNAL — reason -->` | **`our-ai-charter-internal`** (private) |
| Legal, finance, banking, fundraising, Verein organisation — including Our AI Charter's | **`FactHarbor-internal`** (private) |

- **What "INTERNAL" means.** A file is INTERNAL when its header carries `<!-- Status: INTERNAL — <reason> -->` (the pre-commit guard greps for it). INTERNAL files live only in `our-ai-charter-internal`; if one turns up in this public working tree, move it to the private sibling instead of committing it.
- **Drafts belong here too.** Articles, posts, comments, and adaptations live in this public repo whether or not they are published yet — being unpublished does not make something private. The only inherently private material is personal DM/email with an individual; and even that is **not** private when the person is acting as an official representative of an organisation.
- **Authoring is not the same as publishing what's private.** Freely create and edit clearly-public material here. But never, on your own judgement, move currently-private content into this repo, strip an INTERNAL marker, or commit material whose sensitivity is unclear — a public misroute is permanent and worldwide. When unsure, keep it private (or mark it INTERNAL) and ask the maintainer.
- This repo must **never** receive personal correspondence or INTERNAL-marked content, even temporarily in the working tree.
- **Do not `git commit` or `push` here without maintainer review.** A local `.githooks/pre-commit` guard — once activated per clone (`git config core.hooksPath .githooks`) — blocks commits that carry an INTERNAL/confidential banner (e.g. `Status: INTERNAL`); it's a backstop, not a substitute for the rule. Only Claude Code's hook enforces git safety automatically; other agents must self-enforce.
- Writing into a private sibling requires the agent's tool workspace to grant access to that path; if it is unreachable, do the public part here and leave the private part to the maintainer.

## Where to work from (primary base)

For Our AI Charter / Public-AI topics, prefer to run the agent from **this repo** (`C:\DEV\our-ai-charter`) as the working base, reaching into **`our-ai-charter-internal`** for the confidential Charter side (and `FactHarbor-internal` for finance/legal/Verein) as the task needs it. Agents based in a private sibling are **also allowed** to do this work and may reach back here — for Charter topics the default base is simply this repo. Content routing (above) is unchanged regardless of base.

## Git & safety

- **Work directly on `main` by default.** Solo maintainer + AI agents — commit straight to `main` for routine work. Do **not** create a branch or worktree unless the maintainer asks for one, or there is a strong reason to isolate the work (a large or risky change that may need rolling back, or parallel edits that would otherwise conflict). This overrides any general "branch off the default branch first" habit; the maintainer still decides *when* to commit and push.
- **Avoid destructive git unless the user explicitly asks.** A local Claude Code **PreToolUse hook** ([.claude/settings.json](.claude/settings.json)) hard-blocks `git reset --hard`, `git push --force` (without `--force-with-lease`), `git clean -f`, and `git checkout -- .`. To undo committed work, prefer a **new revert commit** or a targeted `Edit` — not history rewrites.
- **Hooks fire for the main session only** — *not* for subagents or Workflow agents. Never delegate a destructive or irreversible git step to a subagent; keep those in the main session.
- Commit messages follow **conventional commits**: `type(scope): description` (e.g. `docs(protocol): clarify the support rubric`).
- Do not add GitHub Actions or build/publish workflows copied from FactHarbor unless the maintainer explicitly asks for a document-only workflow.

## GitHub repository posture

- Repository visibility is **public**; non-public material belongs in a private administrative repository.
- Only the maintainer account should have direct repository access. Do not add collaborators, write deploy keys, webhooks, or GitHub Apps without explicit maintainer approval.
- Public issues and pull requests are enabled for feedback. The website is built with **MkDocs Material** from the Markdown under `docs/` and published to GitHub Pages by [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml) on every push to `main` (Pages source = "GitHub Actions"). The Markdown documents stay authoritative — the site is a presentation layer over them. Status banners appear on the published pages, the normative drafts, the outreach drafts, and the `docs/wip/` notes (labelled `PUBLISHED`, `DRAFT`, or `WORKING NOTES`); briefings, evidence, strategy, background, and navigational pages carry none. The notes under `docs/wip/` are part of the built site, grouped under a *Draft notes* nav section and flagged `WORKING NOTES`. Wiki and Projects should stay disabled. GitHub Actions must stay enabled for the Pages build (official `actions/*` plus `mkdocs build`); editing that build pipeline is fine, but do not add unrelated workflows unless the maintainer requests them.
- Do not copy FactHarbor's xWiki XAR import/export workflow or its bespoke viewer into this repo. The document set is small enough that MkDocs Material's built-in navigation and search suffice; keep the Markdown authoritative.
- `main` should be protected against force-pushes and deletion. Personal-account repositories cannot restrict protected-branch push access to a named user, so the practical control is keeping collaborators and write-capable integrations empty.
- GitHub secret scanning, push protection, Dependabot vulnerability alerts, and private vulnerability reporting should stay enabled.

## Working norms

- **Open drafts + a dated change log.** Record notable changes in [CHANGELOG.md](CHANGELOG.md) with an ISO date (`YYYY-MM-DD`).
- **Use Git for versioning.** Keep published article filenames stable, and keep each article's accompanying feed post and comments **in that same file** as labelled companion sections (e.g. `## Accompanying feed post`) — not as separate `*-post.md` / `*-comment.md` mirrors. Do not create dated or versioned copies such as `*-v2.md` or `*-2026-06-16.md`. Use Git history, status labels, changelog entries, and document notes to record versions and changes.
- **"Published" is an instruction to tag.** When the maintainer says a document is "Published", set its header status label to `PUBLISHED <date>` — ISO `YYYY-MM-DD`, using the date the maintainer states or today's date if it is being published now — and reconcile the README and site index. Handling any superseded earlier draft follows the next rule.
- **Publishing supersedes the draft — overwrite, delete, or (rarely) archive.** When an article or post is published, its earlier version/draft is either overwritten in place (same filename, status label updated), deleted, or — only when the old draft is worth keeping as a separate visible file — moved to `Archive/<building-block>/` (e.g. `Archive/Public AI Network/`). **Archiving is not the default**: Git history already preserves prior versions, so prefer overwrite or delete. The maintainer decides and executes this case by case; agents must not auto-overwrite, auto-delete, or auto-archive. Keep any archived files out of the README and site index.
- **Lean documentation by default.** Use `/doc-guard` ([.claude/skills/doc-guard/SKILL.md](.claude/skills/doc-guard/SKILL.md), mirrored at [.agents/skills/doc-guard/SKILL.md](.agents/skills/doc-guard/SKILL.md)) before adding a new document, substantially expanding or rewriting Markdown, or reviewing a documentation diff for clutter. State the reader need, the existing home, the chosen option (`tighten | amend | merge | move | delete | add`), and the lean test. Prefer tightening, merging, moving, or deleting before adding; cut filler, repeated background, placeholder sections, decorative structure, and generic values language.
- **Keep the README index and status labels in sync** whenever you add, rename, promote, or retire a document. The `/docs-update` skill ([.claude/skills/docs-update/SKILL.md](.claude/skills/docs-update/SKILL.md)) walks this.
- **Cite sources; prefer the smallest concrete improvement** over a grand rewrite (see [CONTRIBUTING.md](CONTRIBUTING.md)). Record minority interpretations rather than hiding them.
- **Licensing:** document text is **CC BY 4.0**; the initiative's name and any trust mark are **reserved** (see [NOTICE](NOTICE)). Do not paste in text under an incompatible license.

## Consulting other models (GPT, Gemini, Claude)

The limited documentation-support tooling includes small helper scripts under [`scripts/agents/`](scripts/agents), which let a maintainer-side agent consult another frontier model for a second opinion or cross-model review. Use them rather than improvising an API call.

- `node scripts/agents/invoke-gpt.cjs --prompt "…" [--system "…"] [--model gpt-5.5] [--max-tokens N]` — OpenAI; needs `OPENAI_API_KEY`.
- `node scripts/agents/invoke-gemini.cjs --prompt "…" [--system "…"] [--model gemini-3.1-pro-preview]` — Google; needs `GOOGLE_GENERATIVE_AI_API_KEY`.
- `node scripts/agents/invoke-claude.cjs --prompt "…"` — spawns the local `claude` CLI (Opus, max effort); extra `claude` flags pass through.
- Prompts can be piped via stdin instead of `--prompt`. Set `FH_INVOKE_{GPT,GEMINI,CLAUDE}_DRY_RUN=1` to print the request without sending it.
- **Keys** load from the environment or a gitignored `.env.local` / `.env` at the repo root — never commit them (`.env*`, `*.key`, `*.pem` are already ignored).
- These make **plain, ungrounded** calls (no web search). For a *grounded* review, enable the model's own web/search tooling instead.

## Platform

Windows. Use **PowerShell-compatible** commands (`$env:VAR`, not `$VAR`; `$null`, not `/dev/null`; backtick for line continuation).
