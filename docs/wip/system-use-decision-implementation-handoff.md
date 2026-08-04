> **Status: WORKING NOTES** — execution handoff for the runtime POC; it does not replace or amend the governing specifications.

# System-use decision — implementation handoff

Use this handoff only after M5.5 has passed exact-SHA review and the governing Charter sources have been reviewed and committed. The [system-use decision record](system-use-decision-record.md) defines the slice; the [runtime-gates POC specification](runtime-gates-poc-spec.md) defines the wider architecture and milestone boundary.

## Implementor prompt

```text
Work from the root of the `ai-charter-runtime` repository.

Implement the next bounded runtime slice, provisionally M5.6: the pre-ingress
system-use decision record.

Before changing code, read the runtime repository's AGENTS.md and current ADRs,
then read these governing sources completely in the reviewed `our-ai-charter`
source revision:

- `docs/wip/system-use-decision-record.md`
- `docs/wip/runtime-gates-poc-spec.md`

The Charter sources govern semantics. ai-charter-runtime owns its ADRs, schemas,
code, fixtures, and tests.

Prerequisite gate

1. Inspect git status and recent history.
2. Verify that the reviewed M5.5 implementation baseline,
   `1d992fa16c99decd1912c2bf7af60f3dc03ca7a2`, remains in the current history,
   its exact-SHA adversarial review passed, and later changes have not silently
   changed its runtime contracts.
3. Reproduce the documented pre-slice baseline: `npm run typecheck`, 4 Git-safety
   hook tests, 305 Vitest tests across 35 files, `git diff --check`, and both
   unchanged signed cards verified.
4. Confirm both governing Charter files are reviewed and committed, then
   re-review their exact committed content. Extend `docs/implementation-plan.md`
   under **Specification authority and provenance** from one pinned source to
   two: retain the runtime-gates specification and add the system-use decision
   record. For each source record its path, SHA-256, and immutable URL; bind both
   to and verify both against the same Charter commit. Move both pins together
   in the same runtime commit. A cross-link from the specification is not a pin.
5. If any prerequisite is missing, stop and report it. Do not start provider,
   browser, output-release, or M6 work.

Objective

Implement an authorization-owned, durable, replayable, and fail-closed
system-use decision prerequisite for the synthetic public-grant POC. A current
`approved` or `approved_with_conditions` decision is necessary for use but never
sufficient to authorize an action. It cannot create or broaden a mandate,
ruling, commitment token, escalation disposition, or effect.

Required work

1. Freeze an ADR covering the versioned schema, canonicalization and digest,
   lifecycle, current-decision resolution, exact binding, expiry, WAL/replay,
   bounded projections, and failure behaviour. The ADR must explicitly settle
   the M5.5 model-call failure taxonomy for a decision that becomes unusable:
   either add a distinct reason such as `system-use-invalidated` with disclosure
   derived from actual evidence, or document and review an amended mapping to
   `authorization-invalidated` with explicit disclosure semantics. Never assert
   `provider_disclosure: confirmed` unless disclosure evidence exists. Treat
   either choice as a substantive M5.5 contract amendment requiring exact-SHA
   review, not as an incidental schema edit.
2. Add authorization-owned, append-only decision state and deterministic replay.
   Corrections and resumptions create successors; terminal versions cannot be
   restored, overwritten, or rolled back.
3. Load one checked-in synthetic fixture through an authorization-process-only
   startup seam. Add no browser or HTTP mutation route.
4. Resolve the current decision internally. Callers cannot select or override
   its status, scope, evidence, conditions, version, or currentness.
5. Enforce exact scope, integrity, validity, and mechanically resolvable hard
   conditions at case creation/Authorize, model-call begin, output admission,
   ruling and `commit-verify`, and record/receipt production. Binding the decision
   reference into a ruling amends ADR-001 section 4's binding tuple: update that
   ADR and exercise its eager invalidation, lazy re-read, and `commit-verify`
   backstop rather than adding a free-form field.
6. Bind only the permitted decision id, version, digest, bounded status facts,
   and condition results into durable runtime records. Do not copy evidence
   packs, rationale detail, prompts, outputs, credentials, or personal data.
7. Evaluate expiry and currentness at every boundary; safety must not depend on
   a sweeper. Missing, ambiguous, stale, mismatched, terminal, expired,
   integrity-invalid, or condition-unsatisfied decisions fail closed.
8. If a decision becomes unusable after `model_call.open`, terminate before
   output admission, conversation persistence, or browser release, using the
   ADR-settled failure reason and only the disclosure state supported by evidence.
9. After core state and negative tests pass, add only the specified read-only
   governance view. Show evidence depth, provenance, limitations, conditions,
   currentness, and absent accountability roles—never a trust badge, aggregate
   score, certification result, or mutation control. The view inherits ADR-002's
   strict self-only CSP, `frame-ancestors 'none'`, no third-party browser code,
   no cookies, no CORS, fixed allowlist projections, metadata-only responses,
   and access logging.

Validation

Implement every acceptance test in the system-use decision record. Preserve all
existing M5.5 tests unchanged and green; the new tests will legitimately raise
the aggregate count above the reproduced pre-slice baseline. Add adversarial
coverage for every invalid state, binding mismatch, condition failure, lifecycle
change, replay/rollback attempt, integrity failure, disclosure-state claim, and
boundary timing named there. Use the runtime repository's established commands
and patterns.

Non-goals

- No general organisational approval workflow or real applicant data.
- No legal, conformity, ISO, Charter-certification, or independent-assessment
  claim.
- No caller-asserted authorization.
- No provider, browser, native ingress, output-release, or M6 capture work.
- No weakening of M5.5 containment behaviour or unrelated refactoring.

Handoff

Report prerequisite evidence and SHAs, ADR decisions, files changed,
enforcement boundaries, tests and complete command results, remaining limits,
git status, and a concise diff summary. Do not push. Prepare a coherent local
candidate commit for exact-SHA review only when repository rules and current
authorization permit it, then stop.
```

## Reviewer prompt

> Review this handoff against its two governing sources. Does it add the right post-M5.5 gate without weakening M5.5 or expanding into later milestones? Lead with blocking gaps.
