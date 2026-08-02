> **Status: WORKING NOTES** — public-source architecture comparison, not an endorsement, partnership, interoperability claim, or assessment of an operational system.

# JusticeTree VBE and Our AI Charter — runtime crosswalk

*Working notes — 2026-08-02 · reviewed only against the public materials linked below. JusticeTree's branded terms are used solely to identify its published work; this note does not adopt them as Charter terminology.*

## Purpose and boundary

This note tests whether JusticeTree AI Systems' **Validation Before Execution™ (VBE)** design and the Our AI Charter runtime model describe compatible controls for one synthetic administrative action. It has three outputs: a concept crosswalk, a shared-case test matrix, and the questions that would need answers before any joint comparison or interoperability pilot. Teresa Villa, JusticeTree's founder, framed ten of the comparison questions in the public graphic accompanying her LinkedIn post; they are paraphrased here rather than reproduced.

The comparison is between **designs**, not implementations. JusticeTree describes VBE as a published framework and reference architecture, while stating that operational validation tools are in development, its Pilot 001 is not operational, and its simulator is educational. The Charter's runtime proof of concept is likewise a demonstrator specification, not an independent institution or certification claim. Unresolved points are labelled **Open** where needed; none of the anticipated results is reported as operationally proven.

JusticeTree states that VBE and its other original frameworks are JusticeTree-owned. Its Technology & Attribution page separately describes TraceStack as third-party work used under a non-commercial reference licence; this review did not inspect the licence text itself. No public reuse licence for VBE specifications or test material was identified in the reviewed pages. Compare and cite; do not copy branded schemas, language, or test assets without permission.

## Short assessment

The designs belong to the same control family:

- a probabilistic model may propose an action but does not authorize its own request;
- current, scoped authority and admissible evidence are checked before consequence;
- a failed or unresolved check leaves the action in a non-executing state;
- material changes invalidate earlier conclusions;
- the decision produces an action-scoped record that another party can inspect.

VBE's centre is a four-part release test — **authority, evidence, timing, execution** — expressed through concise architecture questions. The Charter's centre is a two-clock accountability model: lifecycle governance plus five action/gate pairs — **Plan → Authorize; Prepare → Submit; Check → Verify; Decide → Commit; Review → Rely** — surrounded by separated institutional roles, affected-person access, and remedy.

The strongest convergence is the pre-effect authority boundary. The strongest unresolved differences are what a human may do after a failed check, what "independent verification" proves, and whether a record of non-release can establish that no bypass path executed.

Two limits cut across both designs: a per-action record cannot expose an action or omission that was never lodged without an independent detection mechanism, and it cannot by itself establish population-level fairness.

This is not a priority or originality finding. Decision/enforcement separation has a dated standards antecedent in the 2013 XACML 3.0 architecture; transaction-specific authorization, least privilege, and downstream checks also appear in OAuth Rich Authorization Requests, OWASP's excessive-agency guidance, and NIST's agent-identity and authorization work. The useful comparison is what each design adds around those primitives.

## Concept crosswalk

The VBE concerns below are paraphrased from Teresa Villa's public ten-question graphic and the JusticeTree framework pages; the third column is this note's analysis.

| VBE concern | Charter counterpart | Convergence or point to resolve |
|---|---|---|
| **When authority is checked** | Authorize at the operating-envelope boundary; re-check exact current authority at Commit | Convergent. The Charter also re-arms intermediate gates when data, tools, models, evidence, or context change. |
| **Expiry and revocation** | Purpose-limited, scope-limited, time-limited, revocable action mandate | Convergent. The Charter additionally names target, service, data, ceilings, delegation, substitution, and replay constraints. |
| **What invalidates an earlier pass** | A ruling is bound to the frozen proposal, mandate and version, policy digest, acting model, service/action class, nonce, counters, and validity window | VBE names several material changes; an interoperable profile needs one exhaustive invalidation and propagation rule. |
| **Deterministic checks and human judgment** | Hard authorization rules are deterministic; model signals may only flag or escalate; disputed evidence and proportionality route to accountable judgment | Compatible if "judgment" resolves a declared question inside existing authority rather than bypassing a hard rule. |
| **Human action after failure** | An escalation permits only declared dispositions; a person cannot manufacture missing legal, policy, evidentiary, or institutional basis | Material ambiguity. "Override" should be split into resolving review, revising the proposal, exercising existing discretion, or issuing a separate mandate. A hard failure itself should not become an allow. |
| **Evidence sufficiency** | Submit checks whether data, sources, and instructions may enter under rights, privacy, and confidentiality constraints; Verify checks grounding, material uncertainty, contradiction, relevance, and fitness for the use | Convergent in aim. Authenticity and completeness can be partly mechanized; sufficiency and fairness often need a named evidentiary standard and accountable decision-maker. |
| **Exceptions** | A visible, scoped, expiring state transition; return to baseline; repeated exceptions can narrow the envelope or require re-authorization | VBE's exception record maps well. The Charter adds anti-normalization and aggregate-pattern consequences. |
| **Trust boundaries** | Entry boundary before reliance or inference; every model/tool hop re-arms Submit and Verify; commitment boundary before effect | The Charter treats trust as several transitions, not one system perimeter. The location and enforcer of each VBE boundary need to be explicit. |
| **Audit artifact creation** | Pre-effect commitment record plus post-effect outcome, intervention event, challenge route, and recovery owner | Convergent, with a Charter addition for crashes and partially committed workflows. |
| **Independent verification** | Tamper-evident record, external checkpoint, split custody, affected-person extract, outside review, and remedy | Cryptographic integrity, truthful capture, completeness, institutional independence, and binding adjudication are different claims and must be labelled separately. |

## Decision semantics

JusticeTree's current Architecture Center distinguishes four validation states from two downstream outcomes. The most plausible provisional mapping is:

| JusticeTree validation state or outcome | Charter machine result | Charter user effect | Rule for the shared comparison |
|---|---|---|---|
| **Pass** | `allow` | Silent or Flag | Valid only for the exact bound proposal and current state; an allow may carry a Flag except where the concern undermines the basis for the consequential transition. It is not a general trust or compliance verdict. |
| **Fail** | `deny` | May be Silent or Flag when a safe fallback exists; otherwise the user effect is not determined by `deny` alone | No execution token. A denial does not itself imply Stop, and a person cannot turn a missing basis into authority through a bare approval. |
| **Indeterminate** | `escalate` if an authorized reviewer can resolve the declared question; otherwise `deny` | Stop if escalated; a denial may remain non-interrupting where a safe fallback exists | Uncertainty remains distinct from a hard failure. Timeout cannot grant authority. |
| **Escalated** | `escalate` | Stop | The action remains non-executing until an authorized, single-use disposition resolves the declared question. |
| **Action Released / Action Withheld** | External effect / no effect | Consequence, not a validation verdict | Released follows a valid route to effect. Withheld is the umbrella non-release outcome for failed, indeterminate, or escalated actions; it is not a synonym for Fail. |

This mapping is **provisional**. Villa's ten-question graphic uses **REVIEW**, while the current Architecture Center enumerates Pass, Fail, Indeterminate, and Escalated and separately shows Action Released or Action Withheld. Until JusticeTree clarifies the relationship, this note treats review as a human route rather than normalizing it into a fifth result. It also remains open whether later human action produces a new decision or mutates the original result.

## Shared synthetic case

Use one fictional public-benefit case with the same generic public-benefit suspension scenario type as JusticeTree's simulator, expressed with the Charter's authority boundaries. No JusticeTree text, parameters, or fixtures are reproduced.

**Proposed action:** an agency system proposes to schedule the suspension of a fictional household benefit after an AI-assisted review reports missing eligibility evidence.

**Bounded roles and authority:**

- The **agency** is the principal and rule owner.
- The **AI assistant** may retrieve permitted records, compare them with the published criteria, identify uncertainty, and draft a recommendation. It may not decide or execute a suspension.
- A **case officer** may correct factual case material and recommend a disposition but cannot expand the agency mandate.
- An **authorized deciding official** may choose among legally and procedurally available dispositions after seeing the material evidence and uncertainty.
- The **benefit service** schedules a suspension only after re-verifying at the point of effect the exact household, ground, policy version, notice, waiting period, effective date, deciding role, mandate state, and single-use commitment reference.
- The **affected household** receives notice, a scoped decision extract and record receipt, and a usable challenge route.

All identifiers and records in the comparison are synthetic. The comparison performs no real eligibility determination, suspension, disclosure, or legal assessment.

## Comparison test matrix

The anticipated VBE outcomes are inferred from its public architecture and simulator, not confirmed implementation results. This note has not reviewed runnable Charter implementation or output; the Charter rows state expected behaviour from its public specification. A comparison can run once each side exposes suitable executable artifacts and can return actual results.

| # | Test stimulus | Anticipated VBE path | Charter path and expected evidence |
|---|---|---|---|
| 1 | Current authority, complete current evidence, valid notice period, exact execution parameters | All four volumes pass; action eligible for release | Authorize/Submit/Verify/Commit allow; service verifies; sealed commitment followed by effect outcome and affected-person receipt. |
| 2 | The assistant has no delegation for benefit suspension | Authority fails; remaining path withheld | Deny at Authorize and again at Commit if attempted; record the missing mandate; issue no commit token. |
| 3 | Delegation expired or was revoked after an earlier allow | Earlier pass invalidated; action withheld | Old ruling invalid; current mandate check fails closed; record revocation/expiry and attempted stale use. |
| 4 | A required eligibility record is absent or two current records conflict | Evidence unresolved; safe-state review | Verify escalates with all six intervention-contract fields: trigger and state; decision and route; decision basis; response bound and default; permitted dispositions; record and feedback consequences. |
| 5 | New material evidence arrives after a prior pass | Evidence and downstream conclusions re-evaluated | New input re-arms Submit and Verify; proposal revision invalidates the old ruling; no silent reuse of the earlier pass. |
| 6 | Statutory notice or waiting period has not elapsed | Timing fails; action withheld | Commit denies while the timing condition is unmet. It escalates only if an authorized person or reviewer can resolve a declared timing question before the deadline; no execution occurs before the condition is met. |
| 7 | Policy, jurisdiction, model/provider, or material data condition changes | Prior eligibility should be revalidated | The affected gate re-arms; changed policy or mandate invalidates the ruling; a provider change also re-checks permitted disclosure. |
| 8 | Household, effective date, amount, or ground differs from the approved proposal | Execution validation fails | Executing service rejects the parameter mismatch even if an upstream screen or person previously allowed the original proposal. |
| 9 | A person clicks "approve" despite absent authority or a hard prohibition | **Open:** public VBE language about governed override needs clarification | Commitment verification blocks the action. Any valid new authority is a separate, scoped mandate transition followed by a fresh ruling. |
| 10 | An uploaded document instructs the agent to ignore policy and suspend immediately | Trust-boundary or evidence failure; review/withhold | Submit screening may force escalation but can never allow; complete mediation prevents the document from becoming authority. |
| 11 | The orchestrator calls the benefit service directly, replays a ruling, or reuses a token | Execution path must fail for the release claim to hold | Service denies missing, mismatched, expired, or consumed authorization; nonce and idempotency evidence record the attempt. |
| 12 | The authorized reviewer is unavailable or the review times out | Safe state persists | The declared reversible fallback may run only if already authorized; otherwise Stop remains. A late approval is a recorded no-op. |
| 13 | The process crashes after commitment but before the service reports the effect | **Open:** expected VBE state and recovery ownership need definition | Pre-effect commitment survives; effect is `unknown` and reconciliation-required; a named recovery owner resolves, cancels, reverses, or compensates. |
| 14 | A record line is changed or the valid tail is removed | Independent verification should detect loss of integrity | Hash-chain verification detects modification; an external checkpoint is needed for tail rollback. Neither proves that the original event was truthful. |
| 15 | The household challenges a factual error | Review and audit route should expose the basis; Pilot 001 does not supply an independent reviewer or remedy decider | Rely reopens; scoped extract and receipt support challenge; correction and withdrawal of reliance are recorded; an empowered remedy decider remains an institutional dependency. |
| 16 | The system never creates or lodges the action record | **Open:** the reviewed public materials do not establish an independent omission-detection mechanism | Known blind spot: cryptography cannot expose an event never recorded. Requires a lodgment duty, notice entitlement, and independent oversight able to detect silence. |
| 17 | Individually admissible suspensions produce a repeated disparate group pattern | **Open:** outside a single release decision unless lifecycle feedback is defined; Pilot 001 does not supply an independent reviewer or remedy decider | Aggregate monitoring can trigger review, constraint, re-authorization, suspension, or withdrawal, but the POC does not supply an independent reviewer or remedy decider; a per-action gate cannot establish population fairness. |

## Questions raised by the public materials

1. **Normative source.** Which JusticeTree artifact governs when the ten questions, four validation volumes, framework pages, simulator, and architecture-centre views differ in terminology or sequence?
2. **Decision protocol.** How does the graphic's PASS/FAIL/REVIEW language relate to the Architecture Center's Pass/Fail/Indeterminate/Escalated states? Is review a non-executing route, and does a later disposition create a fresh decision with a new validity window?
3. **Authority after failure.** Can any human override a hard failure, or may they only resolve a question within existing authority, revise the proposal, or issue a separately governed mandate?
4. **Binding instant.** At what exact point does validation become binding, and what happens if authority, policy, evidence, or jurisdiction changes between decision and effect?
5. **Complete mediation.** Which component enforces the result at the effect-producing service, and what evidence demonstrates resistance to bypass, replay, substitution, and side-channel execution?
6. **Record claim.** What exact schema is produced before effect and after outcome? Which properties are merely signed, tamper-evident, externally witnessed, complete, independently reviewed, or adjudicated?
7. **Custody and privacy.** Who holds content and keys, what the affected person receives, how every access is controlled and logged, and how retention, deletion, secrets, and third-party privacy are reconciled?
8. **Independent institutions.** Who appoints and funds the verifier, who hears the affected person's challenge, and who can bind correction, reversal, compensation, or another remedy?
9. **Evidence and reproducibility.** Which rules are deterministic, which judgments are not, what evidentiary standard governs sufficiency, and what can an outside party reproduce without pretending that human judgment is deterministic?
10. **Status, tests, and reuse.** What implementation, conformance tests, threat model, pilot evidence, and reuse licence are available for an external comparison?

These questions arise from public materials; this note does not represent questions sent to JusticeTree or answers received. Corrections are welcome.

## How this comparison could be wrong

- **Abstraction mismatch.** It compares a concise founder graphic and public architecture pages with a more detailed Charter specification; apparent omissions may exist in unpublished or later JusticeTree material.
- **Shared antecedents.** Convergence is expected where both designs draw on established authorization, policy-enforcement, least-privilege, and assurance patterns. Similarity is not evidence of coordination or priority.
- **Record-family limits.** Fixtures 16 and 17 expose blind spots of the broader per-action-record family, not defects unique to either design.
- **The wrong-layer objection.** Per-action evidence is absent from many lifecycle-focused regimes and can close a real accountability gap. It does not replace lifecycle assurance, population-level evaluation, independent institutions, or remedy.

## Minimum deliverables for a real comparison

A bounded comparison should produce evidence, not a merged framework:

1. one shared synthetic case file and policy version;
2. one machine-readable proposed-action object and authority object from each design;
3. the same valid, invalid, incomplete, changed-state, bypass, replay, timeout, crash, challenge, and omission fixtures;
4. the decision and non-execution artifacts each implementation actually emits;
5. proof that the effect-producing service rejects unauthorized and stale requests;
6. an affected-person extract and a map of who may inspect the sealed evidence;
7. an explicit list of untested claims and architectural assumptions;
8. a short convergence/divergence report approved separately by each project, with no implied endorsement or shared ownership.

Success is not identical terminology. It is agreement on which transition is controlled, whose authority applies, what evidence is required, which component enforces the result, what record survives, and who can challenge the consequence.

## Charter position

- Do not create a sixth runtime gate or replace the five-gate model. VBE is best treated as a convergent external architecture that tests the consequential-action baseline.
- Preserve the Charter's explicit rule that a person cannot manufacture a missing basis and its distinction between functional separation from the acting model and institutional independence.
- Use generic control terms in any shared fixture unless JusticeTree grants permission to use branded specifications or assets.
- Treat timing as a useful explicit comparison dimension; in the Charter it spans mandate validity, evidence currentness, policy state, waiting periods, commitment, and lifecycle invalidation.
- Do not call a record immutable or claim proof of inaction without stating the capture, mediation, witnessing, and omission limits.
- Do not imply affiliation, certification, operational maturity, or a live joint pilot unless both projects state it publicly.

## Public sources reviewed

**JusticeTree / VBE**

- Teresa Villa, [LinkedIn post: ten architecture questions](https://www.linkedin.com/posts/teresa-villa-09402b292_artificialintelligence-aigovernance-responsibleai-share-7487688749007482880-a_k_) (reviewed 2026-08-02).
- JusticeTree AI Systems, [founder page](https://justicetreeai.us.com/founder/), [Validation Before Execution framework](https://justicetreeai.us.com/framework/), [four validation volumes](https://justicetreeai.us.com/volumes/), and [reference pipeline](https://justicetreeai.us.com/validation-before-execution-pipeline/) (reviewed 2026-08-02).
- JusticeTree AI Systems, [Validation Simulator](https://justicetreeai.us.com/validation-simulator/), [Pilot 001 — Proof of Inaction](https://justicetreeai.us.com/pilot-001/), [Architecture Center](https://justicetreeai.us.com/architecture-center/), and [Technology & Attribution](https://justicetreeai.us.com/technology-attribution/) (reviewed 2026-08-02).

**Our AI Charter**

- [Charter Commitments](../Assurance/Framework/charter-commitments.md) — consequential-action baseline.
- [When Should Runtime AI Governance Interrupt?](../Published/when-should-runtime-ai-governance-interrupt.md) — two clocks, five gates, and the shared practical test.
- [Runtime AI Governance Gets *When* Right — the Harder Question Is *Who Gets to Check?*](../Published/when-vs-who-ai-governance.md) — separated institutional roles.
- [User-workflow governance](../Assurance/Concepts/user-workflow-governance.md) — gate semantics and human-intervention contract.
- [Runtime gates POC specification](runtime-gates-poc-spec.md) — data contracts, transaction semantics, demo beats, and honest limits.
- [Split custody for per-action records](split-custody-per-action-records.md) — integrity, content, access, survivability, and omission limits.

**Established control antecedents**

- OASIS, [eXtensible Access Control Markup Language (XACML) Version 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) (OASIS Standard, 22 January 2013) — policy decision/enforcement separation.
- IETF, [RFC 9396 — OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396) (May 2023) — fine-grained transaction authorization.
- OWASP, [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) (2025 edition) — least privilege, downstream authorization, and approval for high-impact actions.
- NIST NCCoE, [Software and AI Agent Identity and Authorization](https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization) (concept paper published 5 February 2026) — current agent identity, authorization, audit, and non-repudiation work.
