---
name: docs-update
description: Keep the charter's documents, status labels, README index, and CHANGELOG in sync after adding, editing, promoting, or retiring a Markdown document in this repo. Use after any non-trivial change to a document.
---

# /docs-update — keep the document set coherent

A small, repeatable pass to run after you change a document, so the repository stays internally consistent. This repo is **documents-only**: "done" means the prose *and* its surrounding index, labels, and change log all agree.

## When to use

After you add, rename, substantially edit, **promote** (e.g. `DRAFT` → `PUBLISHED`), or retire any `.md` document under `docs/`.

## Procedure

1. **Status banner.** A top-of-file status banner — a plain `> **Status: …**` blockquote (not a typed callout) — belongs on the **normative** docs (Charter Commitments, evaluation protocol, certification model, one-pager) and the **outreach/parliamentary** drafts (Non-Paper, Aktionsplan, Postulat), labelled `DRAFT`; on `PUBLISHED <date>` pages; and on the `docs/wip/` notes, labelled `WORKING NOTES` — see [AGENTS.md](../../../AGENTS.md). If the doc is one of those, confirm its banner is present and accurate; otherwise (briefings, evidence, strategy, background) it carries **no** banner. The README index notes each document's status either way.
2. **README index.** Open the [README](../../../README.md). It presents **Our AI Charter / the Public AI Network** (this whole effort) — its overview, AI-infrastructure pillar, published articles, and the strategy/outreach/evidence — with **AI Assurance & Certification** as the trust-and-evidence building block, each document's status labelled inline. Move or add the document to the right section with a one-line description that matches its current framing. Remove stale entries.
3. **Cross-links.** Check that links between documents (and from the README) resolve — relative paths and correct filenames. Fix anything a rename broke.
4. **CHANGELOG.** Add a dated entry (ISO `YYYY-MM-DD`) in the [CHANGELOG](../../../CHANGELOG.md): what changed and, for the protocol/charter, the version bump. Keep entries terse and factual.
5. **Public-repo check.** Confirm nothing private/internal or any secret was introduced — this is a public repo (see [AGENTS.md](../../../AGENTS.md)).
6. **Integration.** Return the reviewed diff/evidence to the designated integrator. Commit only when the current task covers it and required review is complete; use a conventional message. This workflow does not authorize a push or deployment.

## Output

A short summary: which document changed, its label before/after, the index/changelog edits made, and any broken links found and fixed.

Scope: apply only to the current authorized task and explicit arguments. A skill invocation is not an active-editor selection or permission for external calls, publication or extra writes. Restricted reviewers return chat findings; shared record writes belong to the integrator.
