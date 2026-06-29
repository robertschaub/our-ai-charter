> **Status: WORKING NOTES** — the runnable plan for one pilot of the [grounding-faithfulness & contestability protocol](../Assurance/Protocol/grounding-faithfulness-and-contestability.md). Operationalises artifact #4 of the [production plan](artifact-production-plan.md) and the lead move of the [engagement plan](apertus-fit-and-engagement-plan.md): *bring results, not a framework*.

# Evaluation proof-of-concept — scope

*Working notes — 2026-06-29 · WIP · public-safe. Companions: [protocol](../Assurance/Protocol/grounding-faithfulness-and-contestability.md) ([1-pager](../Assurance/Protocol/one-pager.md)), [production plan](artifact-production-plan.md) #4, [engagement plan](apertus-fit-and-engagement-plan.md), [risk audit](../Assurance/Background/risk-and-vulnerability-audit.md).*

## Purpose

Turn the protocol into **one runnable evaluation** on **one public-interest deployment** of an open model (English cited-source Q&A), producing a publishable PILOT report. Per the [engagement plan](apertus-fit-and-engagement-plan.md), this is the asset that earns standing: the reviewers converged on *bring results, not a draft to review* — and an open model can be evaluated without anyone's permission. Apertus is the **anchoring case, not a client**.

## Two scoping rules to settle first

1. **Evaluate a *deployment*, not the weights.** The protocol scores a deployed factual system that *presents sources* (§2). Raw Apertus chat does not cite sources, so it would fail the use-case-validity check on its own. Choose one:
   - **(a)** target an existing **Apertus-based cited-source Q&A / RAG assistant** (a real public-interest deployment), or
   - **(b)** stand up a **minimal reference RAG + citation harness** over an Apertus endpoint (PublicAI inference / Hugging Face) so there is a deployable factual system to evaluate.
   Either way, state plainly that the result describes **that deployment**, not Apertus-the-model. *(This is also why the PoC fits the Charter's frame: the civic-assurance layer is about deployments of public models.)*
2. **Naming discipline.** Name Apertus **publicly** only with partner agreement ([production plan](artifact-production-plan.md)). Absent that, publish as *"an Apertus-class open public deployment."*

## What it measures (from protocol §4)

- **Source-validity floor** — every citation resolves and is not satire/fiction.
- **Graded support** — verbatim → close paraphrase → reasonable entailment → partial/qualified → unsupported → contradicted (judged from the source text alone, against a codebook).
- **Calibration / uncertainty** — does stated confidence track support; does it abstain rather than bluff; anti-over-hedge (abstention rate + sharpness).
- **Correction** — errors logged, fixed, and not regenerated under paraphrase (process evidence + paraphrase-regression).
- **Contestability** — a reachable error-flag route; documented restriction/recall/shutdown authority; consequential-escalation only if the deployment is consequential.

## Build steps (0–30 days)

1. **Pin the target** (a/b above): exact product + version + use-case + material configuration (prompts, retrieval, citation UI, logging).
2. **Design the query set** — auditor-controlled, pre-registered, **held-out**; adversarially seeded (controversial, time-sensitive, multi-source). Declare unit of analysis (claim) and handle clustering. Keep a hidden subset; publish a small calibration subset. *(Avoids the privacy + cherry-picking problems of scraped user traffic.)*
3. **Codebook** — adopt the §4.1 rubric with worked edge cases (esp. *partial/qualified* and *contradicted*).
4. **Run** — issue queries; capture outputs + citations; verify each citation resolves and is non-satire.
5. **Rate** — two blinded raters + adjudication; report raw agreement + a per-category coefficient (κ / Krippendorff α / Gwet AC1).
6. **Score** — supported-claim rate with a **cluster-robust** confidence interval; the support mix; the floor %; abstention/sharpness. Correction + contestability scored from process/doc evidence.
7. **Report** — the protocol's public report skeleton, labelled **PILOT, not a certification**; numbers illustrative; companion modules listed **not assessed**.

## Independence & honesty (non-negotiable)

*No one marks their own homework.* The method author does not evaluate a system and claim a result for it. A maintainer-run first pass is a **method dry-run / calibration** — explicitly **not** an independent evaluation and **not** a claim about the deployment; an **independent rater/assessor** is required for any published evaluation *of a system*. State this on every output; recuse from operating any assessor or registry.

## What it needs / honest constraints

- A reachable Apertus-based cited-source endpoint, or the minimal RAG harness (option b).
- Rater time — tens of person-hours for a few-hundred-pair sample (grant-funded or volunteer domain experts); realistic cost low-thousands to low-tens-of-thousands USD.
- A statistician to set sample size, threshold, and clustering per use-case — **no universal "N=200 / ≥95%."**
- Privacy: no raw user data in public; auditor-controlled queries avoid this by design.

This scope is the **runnable plan + report skeleton**, not executed results — a live evaluation needs the endpoint access, raters, and stats above.

## Outputs that earn standing

1. The method as a **portable recipe** (an AI Verify / Moonshot recipe or a small open harness) + codebook + report skeleton + a public calibration set.
2. **One PILOT report** on an Apertus-class deployment (named only with agreement).
3. Circulated **with** the [discussion note](geneva-2027-assurance-questions-note.md) to 3–5 credible reviewers and to summit / Metagov / ICAIN — feedback, not endorsement.
