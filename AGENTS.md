<!-- Status: DRAFT — operational rules for this repo. -->

# AGENTS.md

How AI agents (and humans) should work in the **Our AI Charter** repository.

This is the authoritative working-rules file. Tool-specific wrappers — [CLAUDE.md](CLAUDE.md), [GEMINI.md](GEMINI.md), and [.github/copilot-instructions.md](.github/copilot-instructions.md) — point here. If they ever diverge, **this file wins**. System/developer instructions and the current user task take precedence. Read applicable nested AGENTS.md before target work. Resolve routine choices within task authority; ask only for a material missing decision.

## What this repository is

- A **public, documentation-first** repository: a published manifesto, a signable charter, a draft evaluation protocol, and Public AI Network governance materials. Markdown remains authoritative; limited presentation assets and documentation-support tooling are allowed.
- **No application runtime, product code, package-managed app, or test suite.** The MkDocs site build, repository hooks, and small `scripts/agents/` review helpers are the documented exceptions.
- Keep imported FactHarbor practices scoped to documentation: agent rules, issue/PR templates, safety policies, and local destructive-git guards are appropriate; app runtime rules, generated indexes, database guards, test commands, and unrelated deployment workflows are not.
- **Status banners and published-article openings.** A status banner sits at the top of the **normative** docs that state rules, obligations, or guidelines and the **outreach and parliamentary** drafts. Normative drafts include proposal-type concept notes that prescribe a policy, control, or operating model even when they explicitly say they are not adopted Charter text; descriptive concept and evidence notes do not receive a banner merely because they share the same folder. The banner is a plain `> **Status: DRAFT**` blockquote, **not** a typed callout. Published article mirrors use the lean opening `**PUBLISHED YYYY-MM-DD to LinkedIn [Post](URL)**`, then horizontal-rule-separated post content, picture, and article content; a translation not separately published begins `**TRANSLATION of PUBLISHED …**`. Evidence, background, the About page, navigation pages, and published article mirrors carry no status banner. This repository has no public WIP or archive section: unfinished but public material must have a durable subject home, while operational working material belongs in the authorized private workspace.

## Program constellation

Our AI Charter is the public framework of principles and obligations in a broader program:

> Working to build a free and fair society where technology is used responsibly and enables well-grounded decision-making.

The public About page is [About.md](docs/About.md). This repository is the public home of **Our AI Charter**, a **Public AI Network** initiative. Its documents live under `docs/` (the website's content root): the **Overview** front door (`docs/network-overview.md`), **AI Assurance & Certification** (`docs/Assurance/`), the **AI-infrastructure pillar** (`docs/Infrastructure/`), outward-facing drafts (`docs/Outreach/`), evidence (`docs/Evidence/`), and the stable published-article collection (`docs/Published/`). The home page (`docs/index.md`) carries the orientation and reader paths. Repo-meta files (README, AGENTS, CHANGELOG, CONTRIBUTING, SECURITY, LICENSE, LICENSE.md, LICENSES, NOTICE) stay at the repo root.

Current agent priority:

- The homepage presents five connected pillars: accountable AI decisions and actions; open, plural models; data and provenance commons; shared assurance and evaluation; and federated public AI infrastructure. These are complementary responsibilities, not sequential gates; public obligations and accountable human governance apply across them. This presentation does not change document ownership or folder locations.
- **Robert Schaub’s current focus is Evidence-Gated Agents (EGA)** within **Accountable AI decisions and actions** (focus updated 2026-09-14). When proposing next steps or allocating effort, prioritise the maintainer’s current EGA task. Its public overview remains at `docs/Assurance/Concepts/evidence-gated-agents.md`; the runtime implementation is a separate repository. This priority does not grant implementation, cross-repository write or publication authority.
- The broader **Public AI Network** work retains its sovereignty, resilience, Swiss and international coordination, and Geneva 2027 objectives. **AI Assurance & Certification** remains the trust-and-evidence building block supporting shared assurance and evaluation.
- Published article mirrors live together in `docs/Published/` regardless of topic; do not create topic-specific `Published/` subfolders. Preserve dated four-pillar articles as historical publications; current orientation pages carry the five-pillar framing.
- Do not infer the next task from document maturity; follow the maintainer’s current instructions and the task’s authorised scope.

Boundary rules for agents:

- Work in the task's authorized repositories and read/write scope. If another repository is needed, ask once, naming it, the purpose and read/write access; continue independent work while waiting. Approval covers this task and its handoffs until changed; do not ask again for the same scope.
- Authorized cross-repository reads may include private material; access is not disclosure permission. Keep confidential or personal content out of this repository and public artifacts. Use MCP only for its identified source repository; availability is not authority. If MCP is unavailable or unqualified, use authorized direct reads.
- Do not create public links, document dependencies, or process dependencies on private repositories, local machine paths, or unpublished operational records.
- Public cross-links should point to public URLs or public files only.

## Public-repo discipline (read first)

This repository is **public**, and it is the home for current, intentionally public Charter material — published *and* draft — organized by durable subject. Personal correspondence, operational strategy, explicitly INTERNAL material, superseded working records, and confidential administrative records belong in an authorized private home, never here. The current task identifies that home when needed; this public instruction does not grant access to it.

- **Never commit personal correspondence, INTERNAL-marked, or otherwise confidential/personal data into this repo.** A draft may be public when it has a durable subject home and a real public reader; raw WIP and operational strategy do not belong here. When you are unsure whether a specific item is sensitive, leave it out and ask the maintainer.
- **No public archive.** Do not create `Archive/`, `Strategy/`, or `wip/` sections in this repository. Git history preserves superseded public versions. Retain historical working material only in an authorized private archive, or delete it from the active tree when it has no continuing value. `docs/Published/` is the stable collection of intentionally published works, not an archive for drafts.
- **Never commit secrets** — API keys, tokens, credentials, `.env` files. GitHub **secret scanning + push protection** is enabled and will block known secret formats, but treat it as a backstop, not a license to be careless.
- If sensitive material appears in a working tree, diff, issue, or PR, stop and notify the maintainer privately; do not open a public issue containing the material. See [SECURITY.md](SECURITY.md).
- Do not create public links or process dependencies on private repositories. Keep non-public working material outside this repo.
- Assume everything committed is **permanent and worldwide** — forks, caches, and search indexes mean you cannot fully un-publish.

## Where new files go (route by content, not by cwd)

This is the home for current public Charter material, whether published or draft: manifesto, charter, protocol, articles/posts/comments, public background, evidence, concepts, infrastructure, and outward-facing proposals. Route each document to its durable subject folder; unpublished does not itself mean private.

- Personal DM/email correspondence with individuals acting privately, operational strategy, superseded working records, and material explicitly marked INTERNAL remain in an authorized private home. Official organisational communications are not private merely because unpublished; inspect sensitivity and disclosure authority before use.
- Confidential finance/legal/banking/fundraising/Verein records, including the Charter's, remain outside this public repo.
- Never move currently private content here, remove an INTERNAL marker, or commit unclear material on your own judgment. Access permission is not disclosure permission. Keep sensitive content out even temporarily; report a misroute privately rather than choosing an unassigned destination.
- Use repository-relative/public links only. Public work must be self-contained and must not depend on private checkouts or machine paths.

## Where to work from (primary base)

Use this repository for public Charter outputs, including authorized cross-repository tasks. Prefer direct reads when they avoid a workspace change. If a client setting must change, preserve unrelated settings and restore temporary access afterward without overwriting intervening edits. A settings change cannot erase loaded context: start a fresh session when a later task requires excluding previously loaded private context. Ignored settings are not clone defaults or proof of effective access.

## Git & safety

- **Routine work:** Use the primary checkout on `main` unless the task assigns another branch. State the repository, branch and edit scope before writing. Check known active tasks and existing edits; do not switch a dirty or actively owned checkout. Pause affected edits if ownership is unclear.
- **Parallel work:** Default to one writer and one Git operator per repository at a time, normally the same agent. Other agents may research or review without writing. Writers in different authorized repositories may work in parallel when they do not share mutable state. Coordinate with the maintainer's edits too.
- **Worktrees are exceptional:** If simultaneous writing in the same repository is required, assign each writer a separate owned worktree; keep one Git operator. Otherwise create a temporary worktree only for explicitly requested isolation. Before creating one, name the reason, path, branch, writer and integrator, and the integration/cleanup plan. Restricted writers return owned edits and evidence without Git mutations or shared-settings changes; the integrator handles shared records and Git operations. Keep pre-applied integrator-owned hunks separate from worker changes.
- **Pulls:** Keep repository-local `pull.ff=only`; use `git pull --ff-only` for authorized pulls. On divergence, stop that Git operation and report the state. Do not automatically override it with a merge, rebase, cherry-pick publication workaround or history rewrite; resolution needs current task authority.
- **Completion:** After an authorized push, verify the intended remote branch and report any difference from the primary checkout. Advance that checkout only when safe, authorized and not owned by another task; preserve pending work. The integrator removes completed temporary worktrees/branches only when inactive, with no unique work or retained local evidence (including ignored files), using ordinary non-force Git commands. Preserve recovery refs and backups; report anything retained.
- **Avoid destructive git unless the user explicitly asks.** A local **PreToolUse hook** ([.claude/settings.json](.claude/settings.json) for Claude Code, mirrored in [.codex/hooks.json](.codex/hooks.json) for Codex) screens `git reset --hard`, `git push --force` (without `--force-with-lease`), `git clean -f`, and `git checkout -- .`. To undo committed work, prefer a **new revert commit** or a targeted `Edit` — not history rewrites. **Known false positive:** the hook matches the whole shell command string, so a commit message that merely *describes* those operations (for example when documenting the guard itself) is blocked even though the command is only `git add` + `git commit`. Reword the message; never route around the hook.
- **Hook coverage is a backstop, not a guarantee.** Treat it as main-session-only — though in practice the hook has also been observed firing for a subagent Bash call (2026-08-01), so coverage varies by tool and version; rely on neither behavior. Never delegate a destructive or irreversible git step to a subagent; keep those in the main session.
- Commit messages follow **conventional commits**: `type(scope): description` (e.g. `docs(protocol): clarify the support rubric`).
- Do not add GitHub Actions or build/publish workflows copied from FactHarbor unless the maintainer explicitly asks for a document-only workflow.

## GitHub repository posture

- Repository visibility is **public**; non-public material belongs in a private administrative repository.
- Only the maintainer account should have direct repository access. Do not add collaborators, write deploy keys, webhooks, or GitHub Apps without explicit maintainer approval.
- Public issues and pull requests are enabled for feedback. The website is built with **MkDocs Material** from the Markdown under `docs/` and published to GitHub Pages by [`.github/workflows/deploy-docs.yml`](.github/workflows/deploy-docs.yml) on every push to `main` (Pages source = "GitHub Actions"). The Markdown documents stay authoritative — the site is a presentation layer over them. Status banners appear on normative or outreach drafts; published article mirrors use the compact publication/post/picture/article opening defined above; evidence, background, and navigational pages carry neither. Wiki and Projects should stay disabled. GitHub Actions must stay enabled for the Pages build (official `actions/*` plus `mkdocs build`); editing that build pipeline is fine, but do not add unrelated workflows unless the maintainer requests them.
- Do not copy FactHarbor's xWiki XAR import/export workflow or its bespoke viewer into this repo. The document set is small enough that MkDocs Material's built-in navigation and search suffice; keep the Markdown authoritative.
- `main` should be protected against force-pushes and deletion. Personal-account repositories cannot restrict protected-branch push access to a named user, so the practical control is keeping collaborators and write-capable integrations empty.
- GitHub secret scanning, push protection, Dependabot vulnerability alerts, and private vulnerability reporting should stay enabled.

## Working norms

- **Project naming.** Write **Evidence-Gated Agents** without ©, ® or ™. Do not claim that the term was coined here or is exclusive to this project. Describe the design's contribution; copyright and licence notices apply to the articles, diagrams and code, not to the project name. Naming rule adopted 2026-09-12.
- **Open drafts + a dated change log.** Record notable changes in [CHANGELOG.md](CHANGELOG.md) with an ISO date (`YYYY-MM-DD`).
- **Use Git for versioning.** Keep published article filenames stable, and keep each article's accompanying feed post, picture, article, and comments **in that same file** — not as separate `*-post.md` / `*-comment.md` mirrors. The opening order is publication line → post → picture → article, with horizontal rules between the content blocks and no redundant section labels; comments may follow the article under concise labelled sections. Do not create dated or versioned copies such as `*-v2.md` or `*-2026-06-16.md`. Use Git history, the compact publication line, changelog entries, and necessary document notes to record versions and changes.
- **"Published" is an instruction to tag.** When the maintainer says an article is "Published", set its first line to `**PUBLISHED <date> to LinkedIn [Post](<post-url>)**` — ISO `YYYY-MM-DD`, using the date the maintainer states or today's date if it is being published now — and reconcile the README and site index. Do not present a translation as separately published when it was not. Handling any superseded earlier draft follows the next rule.
- **Publishing supersedes the draft — overwrite or delete publicly.** When an article or post is published, overwrite the public draft in place when it has the same identity, or remove the superseded draft from the public tree. Git history preserves public versions. If a separate working copy has continuing internal value, move it to an authorized private archive with an INTERNAL marker; never create a public archive folder. The maintainer decides each retirement case.
- **Lean documentation by default.** Use `/doc-guard` ([.claude/skills/doc-guard/SKILL.md](.claude/skills/doc-guard/SKILL.md), mirrored at [.agents/skills/doc-guard/SKILL.md](.agents/skills/doc-guard/SKILL.md)) before adding a new document, substantially expanding or rewriting Markdown, or reviewing a documentation diff for clutter. State the reader need, the existing home, the chosen option (`tighten | amend | merge | move | delete | add`), and the lean test. Prefer tightening, merging, moving, or deleting before adding; cut filler, repeated background, placeholder sections, decorative structure, and generic values language.
- **Keep the README index and status labels in sync** whenever you add, rename, promote, or retire a document. The `/docs-update` skill ([.claude/skills/docs-update/SKILL.md](.claude/skills/docs-update/SKILL.md)) walks this.
- **Cite sources; prefer the smallest concrete improvement** over a grand rewrite (see [CONTRIBUTING.md](CONTRIBUTING.md)). Record minority interpretations rather than hiding them.
- **Licensing:** follow the per-content [license map](LICENSE.md): original documentary content is **CC BY 4.0**, repository-support software and machine configuration are **MIT**, and the initiative's name and any trust mark are **reserved** (see [NOTICE](NOTICE)). Do not paste in material under incompatible terms; identify third-party material where it appears.

## Task fit, review and model choice

Use one accountable implementer and proportionate verification. Trivial wording fixes need no multi-agent sequence, broad checks or completion file. Preserve sources, normative meaning, maturity and minority interpretations. Obtain independent review for material governance/privacy/public-claim changes or when requested; disposition follows evidence, not a model-count quorum. Reuse an existing task record for durable evidence.

Match the configured model's capacity/effort to the task and verify support in the actual client. Do not assume Claude aliases, prices or inherited tool access apply to Codex, Gemini or Cline. Record the actual read/write commands, state, control location, trust/activation and unknowns for restricted sessions. A role label or worktree is not containment; do not dispatch a writer if a required restriction cannot be established.

Pushes, deployments, live analyses, and provider-spending operations require current authorization covering the specific action and scope. Authorization already given in the task remains valid; preparation or review alone does not grant it. Local commits require the review/adoption mandated for that task; do not ask for the same authorization twice.

The three shared skills (doc-guard, docs-update, privacy-guard) are authoritative in `.claude/skills`; `.agents/skills` copies must match their shared frontmatter/body. No client-specific body differences are declared. Extra client metadata, if explicitly scoped, belongs separately. Bind skills to the current task and explicit arguments, not an assumed editor file.

## Consulting other models (GPT, Gemini, Claude)

The limited documentation-support tooling includes small helper scripts under [`scripts/agents/`](scripts/agents), which let a maintainer-side agent consult another frontier model for a second opinion or cross-model review. Use them only within current provider-spend and disclosure authority, rather than improvising an API call. Redaction replaces configured matches only; it cannot guarantee privacy and is a no-op without a usable denylist. Review outbound content and use public-safe context.

- `node scripts/agents/invoke-gpt.cjs --prompt "…" [--system "…"] [--model gpt-5.5] [--max-tokens N]` — OpenAI; needs `OPENAI_API_KEY`.
- `node scripts/agents/invoke-gemini.cjs --prompt "…" [--system "…"] [--model gemini-3.1-pro-preview]` — Google; needs `GOOGLE_GENERATIVE_AI_API_KEY`.
- `node scripts/agents/invoke-claude.cjs --prompt "…"` — spawns the local `claude` CLI (Opus, max effort); extra `claude` flags pass through.
- Prompts can be piped via stdin instead of `--prompt`. Set `FH_INVOKE_{GPT,GEMINI,CLAUDE}_DRY_RUN=1` to print the request without sending it.
- **Keys** load from the environment or a gitignored `.env.local` / `.env` at the repo root — never commit them (`.env*`, `*.key`, `*.pem` are already ignored).
- These make **plain, ungrounded** calls (no web search). For a *grounded* review, enable the model's own web/search tooling instead.

## Platform

Windows. Use **PowerShell-compatible** commands (`$env:VAR`, not `$VAR`; `$null`, not `/dev/null`; backtick for line continuation).
