---
name: privacy-guard
description: >-
  Redact strictly-personal content from text before it crosses a trust boundary,
  replacing each removed span with a typed placeholder (never the real value). Use
  automatically BEFORE: (1) sending text to an external model (scripts/agents/invoke-gpt
  or invoke-gemini, or text you propose the user paste into another AI); (2) writing or
  committing to a PUBLIC repo; (3) publishing, posting, or sharing text (issue, PR, email,
  site, or a DM to a third party). Also on request — "redact", "anonymise", "de-identify",
  "strip personal info / PII", or /privacy-guard. Does NOT redact text that stays inside a
  private repo for the maintainer's own use.
---

# privacy-guard

Keep **strictly personal** information out of places it doesn't belong — a public repo, a third-party AI, a published or shared artifact — by replacing each personal span with a **typed placeholder** rather than the content itself.

> This is model-applied judgement, not a hard technical block, and it cannot see text the user pastes directly into other apps. The optional denylist helper replaces configured matches only and is a no-op without a usable list; it does not guarantee removal of all private information.

## Trigger only on boundary crossings

Redaction protects text that is **leaving a safe place**. Do **not** scrub content that will simply stay inside a **private** repo for the maintainer's own records — that content is meant to be complete. Run a pass when text is about to:

- go **out to an external model**, or
- enter a **public repo**, or
- be **published / shared** with anyone but the maintainer, or
- be extracted or quoted **out of** a private repo.

## Redact → placeholder

- Private 1:1 correspondence (DMs, private email/chat) — verbatim or close paraphrase → `[REDACTED: private DM]`
- Personal contact / identity data — non-org email, phone, home/postal address, government ID → `[PRIVATE EMAIL]` `[PHONE]` `[ADDRESS]` `[ID]`
- Special-category data — health, personal religious practice, sexual orientation, ethnicity, precise location, biometrics → `[HEALTH]` `[RELIGION-PRIVATE]` …
- Financial / security — bank or salary details, credentials, API keys, tokens → `[BANK DETAIL]` `[SECRET]`
- Candid **private** assessment of a named living person, or a non-public identity link ("X is really Y") → `[PRIVATE ASSESSMENT]`
- A private third party's name where the surrounding context is sensitive → `[PERSON A]`, `[PERSON B]`

## Do NOT redact (avoid over-scrubbing)

- **Already-public** statements — published posts, public profile text, public comments, press.
- **Official / organisational** communications — a person acting as an org representative on an org channel.
- The **maintainer's own public identity** and already-public project facts.
- Generic, non-identifying ideas and abstractions.

When unsure whether something is public, treat it as private and redact; ask the maintainer.

## Rules

- Replace the **content**, keep a **typed** marker so the sentence still reads: `… she wrote [REDACTED: private DM] about the "operating system".`
- Same entity → same label within a document (`[PERSON A]` stays `[PERSON A]`).
- Never substitute a fabricated, real-looking value; a placeholder must look like a placeholder.
- Never leave the removed value in the redacted artifact. If a reversible mapping is genuinely needed, keep it in a gitignored `*.local.md` / `*.local.json` that the redacted file does not reference.

## Report

State the boundary being crossed and the redactions by **type and count** (not values), then give the redacted text. If nothing needed redacting, say so plainly.

## Deterministic backstop (stronger, optional)

A skill guides judgment. For configured-match filtering on the channel — text sent to third-party models — a redaction step in `scripts/agents/redact.cjs` (loaded by `invoke-gpt.cjs` / `invoke-gemini.cjs`) replaces entries from a gitignored denylist (`scripts/agents/.redact-denylist.local.json`) with placeholders before the request is sent. See `.redact-denylist.local.json.example` for the format.

This helper cannot discover unknown private facts, establish disclosure permission or ensure anonymization. Independently review the final outbound text against the authorized destination and scope. Do not send private material merely because a filter ran. No denylist or credential change is part of invoking this skill.

Scope: apply only to the current authorized task and explicit arguments. A skill invocation is not an active-editor selection or permission for external calls, publication or extra writes. Restricted reviewers return chat findings; shared record writes belong to the integrator.
