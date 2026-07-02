> **Status: DRAFT**

# Show-your-work evaluation for factual AI systems

**A pilot protocol for deployed systems that answer with cited sources - not a certification, standard, mark, or product.** v0.2 - 2026-06-14 - Robert Schaub, FactHarbor association (Verein), Zurich

_Full protocol: [grounding-faithfulness-and-contestability.md](grounding-faithfulness-and-contestability.md). Phase 1 is an open method contribution. FactHarbor is a paused alpha prototype, not an assessor or operating scheme._

## The gap

AI systems can pass a safety benchmark and still fabricate a citation with confidence. Existing safety, risk-management, and factuality research is valuable, but there is still no widely adopted, lightweight, public, comparable protocol for one narrow question in deployed factual systems:

**When the system cites sources, do its factual claims actually match the sources it gave?**

This protocol evaluates honesty-of-process, not ultimate truth.

## Scope

**In scope:** one deployed system, version, configuration, and use-case at a time. v0.2 is scoped to English factual Q&A that presents cited sources.

**Out of scope:** raw model weights, general model quality, truth certification, source reliability beyond a validity floor, legal compliance, general safety, bias, privacy, security, or a broad Charter alignment claim.

Legal, security, privacy, fairness, misuse, dependency, and continuity risks remain **not assessed** unless a defined module tested them.

## What the protocol measures

1. **Source-validity floor** - every cited source must resolve or be locatable, and must not be satire, fiction, or parody.
2. **Grounding-faithfulness** - each checkable claim is scored against the cited source: verbatim, close paraphrase, reasonable entailment, partial or qualified, unsupported, or contradicted.
3. **Calibration and abstention** - machine-readable confidence is scored for calibration; verbal hedging only as uncertainty signalling. Both should track support, without rewarding bluffing or blanket deflection.
4. **Correction** - logged errors are fixed and do not reappear under paraphrase; severity and time-to-fix are reported.
5. **Contestability** - users can flag factual errors; restriction, manipulation, recall, or shutdown powers are documented; consequential systems need independent escalation.
6. **Lifecycle control** - the report is tied to the assessed release, with re-checks after assessor-reviewable material updates or material incidents, silent configuration changes, and complaints.

## How a pilot would run

- Name the system, version, configuration, and use-case; collect its evidence pack and current public release risk assessment.
- Pre-register an auditor-controlled, held-out query set seeded with adversarial and edge cases.
- Run the configured system; capture answers, citations, and uncertainty signals; score support from the cited text alone.
- Use two blinded independent raters plus adjudication; publish the codebook, examples, agreement, and deviations.
- Declare the unit of analysis and handle clustering; report confidence intervals rather than a universal magic threshold.
- Check hidden queries, version hashing where possible, coverage and citation sufficiency, abstention, correction regression, and complaint-triggered spot checks.
- Publish a privacy-preserving report that states scope, method version, results, limitations, and modules not assessed.

## What the report can say

Within the named scope, it can report supported-claim and source-validity results, uncertainty and abstention behavior, correction regression, and contestability controls.

It cannot say that the system is true, safe, unbiased, lawful, generally trustworthy, Charter-aligned, certified, or covered outside the assessed scope.

## Why technical partners matter

The hard parts are query design, source capture, support scoring, inter-rater reliability, clustered estimates, anti-gaming, and lifecycle re-checks.

A maintainer-run dry run could calibrate the method. Any public evaluation requires an assessor independent of the vendor, blinded independent rating before adjudication, disclosed conflicts, and a flat fee independent of outcome.

## Three asks

1. **Break it:** where does "support, not truth" still collapse into truth-judging, or mislead a buyer?
2. **Co-design the measurement:** query-set design, unit of analysis, rating workflow, confidence intervals, and a risk-tiered bar for one use-case.
3. **Package a pilot:** identify the minimum runnable recipe - for example in a Project Moonshot-style workflow or another open harness - plus the evidence inputs and partner roles needed to publish one pilot report. No pilots are running yet.
