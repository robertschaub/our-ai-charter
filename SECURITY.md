<!-- Status: WORKING DRAFT - repository safety policy. -->

# Security and Public-Repo Safety

Our AI Charter is a public, documents-only repository. It has no application runtime, hosted service, production database, package dependencies, or supported software versions.

## Report Privately

Do not open a public issue or pull request if you find:

- a leaked secret, token, key, credential, or `.env` value;
- private, internal, unpublished-confidential, or personal data;
- material that belongs in the private `FactHarbor-internal` repository;
- a GitHub or repository-configuration problem that could expose non-public material.

Contact the maintainer privately, or use GitHub private vulnerability reporting if it is enabled for this repository.

## Public Issues Are For

Public issues are appropriate for document problems: unclear wording, missing sources, methodological objections, proposed improvements, and pilot offers.

## Handling Sensitive Material

- Never commit secrets or private material here.
- Treat GitHub secret scanning and push protection as a backstop, not as permission to be careless.
- If sensitive material is committed, do not assume deleting it in a later commit is enough. Git history, forks, caches, and search indexes may still expose it.
- Keep non-public drafts, notes, and coordination in `FactHarbor-internal`, not this repository.

## Local Safeguards

The shared agent guidance and Claude/Codex hook files block the most dangerous destructive git commands for main-session agent runs. They are not a substitute for human review, and they do not protect every tool or subagent context.
