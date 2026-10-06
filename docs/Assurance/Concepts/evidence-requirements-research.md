<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Evidence requirements: what EGA needs to demonstrate

**Can AI work out what evidence a decision needs—and notice when something important is missing?** This research strand of [Evidence-Gated Agents (EGA)](evidence-gated-agents.md) asks how to reduce unsupported answers while preserving useful, well-supported ones.

A supplier may have good references and a fast average response time. Both facts could be correct while a recommendation requiring a guaranteed two-hour response remains unsupported. A useful answer would identify the missing contractual guarantee, explain what can still be concluded and qualify or withhold that recommendation. Here the criterion is stated; the harder research question is whether the workflow finds relevant premises when they are implicit.

<a id="aspiration-mostly-generic-evidence-gated-agents"></a>

## The research question

The ambition is to handle unfamiliar questions without people writing a bespoke evidence checklist for each one. Accountable people still establish permissions, acceptance policies and domain principles.

The proposed workflow identifies material claims, assumptions and dependencies; proposes evidence requirements; and has a **separate review challenge their adequacy**, including what the first pass missed. New or revised items receive reviewed requirements before searching permitted sources for support, counterevidence and gaps.

Search may reveal a missing premise or show that a requirement is ill-posed. That discovery returns to requirement proposal and review before further evidence assessment or release. It cannot lower the evidence standard to fit what was found: any relaxed or removed requirement must be justified against the frozen policy, reviewed and recorded.

A separate deterministic gate then applies the recorded rule to the requirements, review outcomes and evidence assessment: permit release, require revision or hold the proposal. It makes no semantic judgment of its own, and a model verdict alone cannot authorize release. Material changes require renewed checks. Agreement between reviewers is not proof that their requirements or conclusions are adequate.

## What goes into a check—and what comes out?

Before the acting model receives a request, checks establish whether that system may be used for the purpose and whether the request and context may be sent to that provider/model. Current permission is checked again when the model's output enters the workflow. Accountable people supply the authority, disclosure rules and acceptance policy; the agent cannot invent these.

Evidence examination takes **the user's request, the agent's exact proposed answer or decision, and the relevant context permitted for this use**. The proposal is checked against the request: factual statements may be correct while the answer still fails to justify the requested decision.

| Check | Inputs | Outputs |
|---|---|---|
| **Authority and disclosure** | Request and purpose; exact proposal when available; who is acting and receiving the result; current mandate; information and destination service/provider. | Permission or stop for the relevant step, with reasons. Checks precede the acting-model call, evidence-service submission and release. Permission for one disclosure does not authorize the others. |
| **Derive evidence requirements** — wider research | Request, exact proposal, permitted context and established domain/acceptance policies. | An inventory of material claims, assumptions and dependencies, with proposed evidence requirements for each. |
| **Review those requirements** — wider research | The same task and proposal, the inventory and proposed requirements. | An assessment of their adequacy, including missing items, required revisions and unresolved disagreement. Revised items return for review before evidence search. This assessment is not release permission. |
| **Retrieve material** | EGA-defined search/reference requests, authorised source scope and permitted retrieval/extraction processing. | Documents, faithful passages or structured source records with provenance and retrieval limits. The service does not classify support/contradiction or judge adequacy. No matches is not proof that evidence is absent. |
| **Analyse the evidence within EGA** | Exact request and proposal, permitted context and retrieved material. In the wider research, reviewed requirements also guide search. | An analytical verdict and report: what supports or opposes each material component, source references, scope limits, uncertainty and known gaps. An incomplete examination remains incomplete; a completed job does not imply sufficient evidence. |
| **Verify and control release** | The evidence result and applicable rule, exact proposal and recipient, and current authority, disclosure and freshness/binding checks. | Permission to release that exact proposal, or a stop with reasons. The release service checks permission again immediately before making it available. The assessment alone cannot authorize release. |

The first prototype uses **human-defined evidence rules** in place of the two research-only steps. EGA analysis produces a verdict and component assessments; release controls apply the rule through an explicitly reviewed mapping. The retrieval service returns what it finds through a common interface with public-source and specialised private-source implementations as the target. Query-relevance ranking and faithful extraction must expose their selection limits and must not suppress results based on support/contradiction judgments. FactHarbor offers reusable retrieval and analytical capabilities; exact integration remains open.

For the gated path, a receipt connects permitted evidence references, reasons and the recorded outcome. An assessment, release permission and actual release are distinct outputs. If release may have occurred but cannot be confirmed, the receipt records that uncertainty and names who must reconcile it. Availability is not proof of reading. Stop notices and receipts disclose only what their audience may see; reasons, previews and references must not expose withheld content or bypass access controls.

In the supplier example, the input is the proposed recommendation plus the two-hour guarantee criterion and permitted context. An assessment might find references and response-time statistics but no applicable guarantee. The release rule then determines whether that exact recommendation must stop. A qualified or narrower answer is a **new proposal to check**, not an automatic rewrite by the gate. Releasing a recommendation does not authorize a purchase.

<a id="path-from-the-prototype-to-wider-use"></a>

## What the first prototype can tell us

The selected prototype uses **human-defined evidence rules** and a dynamic EGA examination of an exact proposed decision, with planned reuse of FactHarbor capabilities. Authority and disclosure checks precede that examination; a release requires fresh verification of the bound decision, recipient and result. It releases a decision, not a resulting action. **This integration is not yet implemented.**

A preset, versioned trigger selects consequential responses for examination. Other responses follow an ordinary path with authority and disclosure checks and a minimal routing record, but no evidence examination or EGA receipt. Ambiguous routing stops. Misclassifying a consequential response as ordinary is a failure mode to assess.

Its planned evaluation covers enforcement integrity, unsupported releases, unjustified stops, useful qualified answers, missed decision components, language differences, selected repeat-run variation, latency and failures. FactHarbor may miss a consequential component; an allowed release is not proof of completeness. Existing foundations are FactHarbor Alpha and a Runtime proof of concept that exercises gate mechanisms in a synthetic scenario; neither establishes the integration.

The wider research asks whether AI can derive adequate requirements and whether separate requirement review improves them. The first prototype does not establish either capability. Additional domains, organisational sources or action workflows need their own scope, activation decision and evidence. See the [project overview](evidence-gated-agents.md#foundations-and-the-selected-next-step) for the existing foundations and selected direction.

<a id="test-of-the-aspiration"></a>

## What would count as progress?

For the wider research, success means fewer unsupported releases **while keeping useful answers above a predeclared threshold**. Release means making an answer or decision available to its recipient; delivered explanations accompanying a stop are also assessed. Measure and report missed requirements and claims, unsupported releases, omissions shared by the answering and reviewing agents, unjustified blocking, useful qualified answers, successful reassessment after evidence changes, cost and latency.

The comparisons below test different claims. Blanket refusal cannot count as success; neither removing requirement review nor comparing with human requirements alone establishes general requirement derivation. Scoring must distinguish factual support, missing premises and whether the conclusion is justified under the declared task criteria.

An unsupported release includes a released answer whose material conclusion is unjustified, or whose omissions make the decision basis misleading—not only unsupported factual statements. Report results for each kind of failure, including when only one kind improves.

| Research claim | Evidence needed |
|---|---|
| The full workflow improves release quality | A predeclared reduction in unsupported releases against **each** of two baselines—an ordinary research agent and an agent with general critique—while meeting the predeclared usefulness threshold. |
| The workflow improves on closely related structured methods | A predeclared reduction in unsupported releases against **each** included structured comparator—task-specific rubric generation and structured rubric-based verification—while meeting the predeclared usefulness threshold under matched conditions. An excluded or incompatible method supports no superiority claim about that method. |
| Requirement review adds value | Compare the full workflow with the same workflow without requirement review. Meet the predeclared requirement-coverage improvement threshold and the release-quality and usefulness thresholds. |
| AI-derived requirements approach a human reference | Compare coverage, release quality and usefulness with the proposed workflow using frozen human-prepared requirements in place of AI-derived requirements. This is diagnostic; a claim of matching the reference needs a predeclared maximum acceptable shortfall (a noninferiority margin). The reference is not an infallible oracle. |
| The workflow generalizes within its claimed scope | Predeclare domains or task families. The same frozen workflow must meet release-quality and usefulness rules in **every** declared group. Report results and uncertainty by group; pooled success is insufficient. |

The original comparisons remain necessary. A claim of progress beyond closely related methods additionally requires the structured comparisons and success rule above. Publish the selection and any adaptation or exclusion rationale before evaluation.

## Related research

Existing work supplies useful methods and comparisons, rather than validation of EGA's proposed combination:

- [FActScore](https://aclanthology.org/2023.emnlp-main.741/) and [SAFE](https://arxiv.org/abs/2403.18802v4) assess individual factual claims against knowledge sources. [ICAT](https://aclanthology.org/2025.findings-acl.693/) also examines coverage of expected aspects. These inform separate measures for support and omissions; factual accuracy alone does not establish decision sufficiency.
- [AutoSciRub](https://arxiv.org/abs/2608.31076v1), a work-in-progress preprint, derives task-specific rubrics before scientific research and uses them for verification and revision. [DeepVerifier](https://arxiv.org/abs/2601.15808v2) uses structured rubrics and verification feedback to improve research answers. Their methods make them relevant structured comparisons alongside general critique, although their tasks and reported results do not establish EGA's broader claims.
- A [critical survey of self-correction](https://aclanthology.org/2024.tacl-1.78/) identifies reliable external feedback and fair evaluation as central concerns. Its findings motivate testing the added value of requirement review rather than assuming that another model pass corrects omissions.

The open question is whether the proposed combination improves requirement coverage and justified, useful releases under the declared conditions. Separate tests must establish enforcement integrity.

## Evaluation commitments

Claims of generality must remain limited to the task families, domains and conditions actually tested.

Before any approach in the wider research receives held-out material—evaluation questions kept from it during development—publish a dated protocol under `docs/Assurance/Protocol/` in the public Charter repository and cite its Git commit in every run record. Fix the comparisons, numeric thresholds, scoring and adjudication rules, sample selection, workflow, model configurations and resource limits. Include hashes of the frozen questions, reference requirements, reusable policies and domain context in that protocol commit. Preserve failed attempts and report deviations separately.

<details markdown="1">
<summary><strong>How the comparisons will remain fair and inspectable</strong></summary>

- **Prevent checklist leakage.** Freeze reusable policies and domain context before held-out questions are authored or selected. Their authors must be separate from question authors and have no access to held-out questions. Permit no question-specific tuning.
- **Cover different evidence conditions.** Include sufficient evidence, missing support, conflicting sources, misleading citations and changed evidence across the declared domains.
- **Match conditions.** Keep the acting model configuration, available sources, tools and resource limits the same across approaches; count review-model usage within those limits.
- **Separate the human reference.** Feed frozen human requirements to the proposed workflow in place of AI-derived requirements. Keep its requirements, outputs and assessor feedback away from AI-derived approaches, and report human preparation effort separately.
- **Freeze contestable references.** Domain-qualified reviewers prepare and freeze reference requirements before the protocol commit, without exposure to system outputs. Preserve that edition; frozen adjudication rules may credit justified alternatives.
- **Assess complete answers.** Assess both requirement coverage and every material assertion in the released answer, including undeclared claims. Normalize presentation and remove approach-identifying metadata without changing substance. Blind reviewers where possible and report failures of blinding, including recognizable requirements or receipts; record unresolved disagreements.
- **Test enforcement separately.** Attempt release after failed or omitted checks, modification of an approved answer, and reuse of an approval after relevant evidence changes. Blocking these attempts demonstrates enforcement integrity; semantic adequacy needs its own evidence.

</details>

The [Charter Commitments](../Framework/charter-commitments.md) provide the governing principles; [user-workflow governance](user-workflow-governance.md) describes authority, evidence and action controls. The [Runtime specification](https://github.com/robertschaub/ai-charter-runtime/blob/main/docs/spec/runtime-gates-poc-spec.md) governs the separate, bounded runtime work.

These research goals do not amend ai-charter-runtime's adopted specification, acceptance criteria or milestones. Any Runtime extension requires a separately scoped, reviewed and approved specification or ADR change.

*This revision reorganizes the [earlier research note](https://github.com/robertschaub/our-ai-charter/blob/bb83a2c32ba785f9e10adc38a5217c164e8e54bb/docs/Assurance/Concepts/evidence-requirements-research.md) and adds related-method comparisons, a decision-sufficiency example and an evidence-discovered requirement loop. Its evaluation commitments remain in place.*
