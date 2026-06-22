---
name: docs-update
description: Keep the charter's documents, status labels, README index, and CHANGELOG in sync after adding, editing, promoting, or retiring a Markdown document in this repo. Use after any non-trivial change to a document.
---

# /docs-update — keep the document set coherent

A small, repeatable pass to run after you change a document, so the repository stays internally consistent. This repo is **documents-only**: "done" means the prose *and* its surrounding index, labels, and change log all agree.

## When to use

After you add, rename, substantially edit, **promote** (e.g. `WORKING DRAFT` → `PUBLISHED`), or retire any `.md` document under `public-ai-network/` or `ai-assurance-and-certification/`.

## Procedure

1. **Status label.** Confirm the document's top-of-file status is present and accurate: `PUBLISHED`, `WORKING DRAFT`, or `WIP / DISCUSSION`. If its maturity changed, update the label.
2. **README index.** Open the [README](../../../README.md). Its index is organised by workstream (Public AI Network / AI Assurance & Certification), with each document's status labelled inline. Move or add the document to the correct workstream with a one-line description that matches its current framing. Remove stale entries.
3. **Cross-links.** Check that links between documents (and from the README) resolve — relative paths and correct filenames. Fix anything a rename broke.
4. **CHANGELOG.** Add a dated entry (ISO `YYYY-MM-DD`) in the [CHANGELOG](../../../CHANGELOG.md): what changed and, for the protocol/charter, the version bump. Keep entries terse and factual.
5. **Public-repo check.** Confirm nothing private/internal or any secret was introduced — this is a public repo (see [AGENTS.md](../../../AGENTS.md)).
6. **Commit.** Use a conventional commit, e.g. `docs(protocol): tighten the support rubric` or `docs: promote founding-accord to published`.

## Output

A short summary: which document changed, its label before/after, the index/changelog edits made, and any broken links found and fixed.
