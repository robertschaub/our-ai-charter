<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->
# Evidence requirements: what EGA needs to demonstrate

**Can AI work out what evidence a decision needs—and notice when something important is missing?** This research strand of [Evidence-Gated Agents (EGA)](evidence-gated-agents.md) asks how to reduce unsupported answers while preserving useful, well-supported ones.

A supplier may have good references and a fast average response time. Both facts could be correct while a recommendation requiring a guaranteed two-hour response remains unsupported. A useful answer would identify the missing contractual guarantee, explain what can still be concluded and qualify or withhold that recommendation. Here the criterion is stated; the harder research question is whether the workflow finds relevant premises when they are implicit.

<a id="aspiration-mostly-generic-evidence-gated-agents"></a>

## The research question

The ambition is to handle unfamiliar questions without people writing a bespoke evidence checklist for each one. Accountable people still establish permissions, acceptance policies and domain principles.

The proposed workflow identifies material claims, assumptions and dependencies; proposes evidence requirements; and has a **separate review challenge their adequacy**, including what the first pass missed. New or revised items receive reviewed requirements before searching permitted sources for support, counterevidence and gaps.

Search may reveal a missing premise or show that a requirement is ill-posed. That discovery returns to requirement proposal and review before further evidence assessment or release. It cannot lower the evidence standard to fit what was found: any relaxed or removed requirement must be justified against the frozen policy, reviewed and recorded.

A separate deterministic gate then applies the recorded rule to the requirements, review outcomes and evidence assessment: permit or withhold release. Withholding records the reason; the workflow may end with the step stopped, or follow an optional permitted route such as Working AI revising the proposal within its existing permission. A revised proposal starts a new attempt through all applicable checks. The gate makes no semantic judgment of its own, and a model verdict alone cannot authorize release. Agreement between reviewers is not proof that their requirements or conclusions are adequate.

## What goes into a check—and what comes out?

EGA repeats a common check pattern at protected transitions, with applicable requirements selected by trusted rules. Any check may retrieve permitted evidence, including evidence of permission and authority; retrieved material does not itself grant permission. A reusable check does not imply automatic derivation of adequate evidence requirements, which remains the research question here.

Before the acting model receives a request, checks establish whether that system may be used for the purpose and whether the request and context may be sent to that provider/model. Current permission is checked again when the model's output enters the workflow. Accountable people supply the authority, disclosure rules and acceptance policy; the agent cannot invent these.

Evidence examination takes **the user's request, the agent's exact proposed answer or decision, and the relevant context permitted for this use**. The proposal is checked against the request: factual statements may be correct while the answer still fails to justify the requested decision.

| Research stage | What it establishes |
|---|---|
| **Propose evidence requirements** | An inventory of material claims, assumptions and dependencies, with proposed requirements grounded in the request, exact proposal, permitted context and established policies. |
| **Review their adequacy** | Challenge missing items and proposed requirements; record revisions and unresolved disagreement. New or revised items receive reviewed requirements before search. Review is not release permission. |
| **Retrieve permitted material** | Documents, faithful passages or structured source records with provenance and retrieval limits. No matches is not proof of absence. Retrieval does not judge support, contradiction or adequacy. |
| **Analyse and apply the rule** | Assess support, counterevidence, scope, uncertainty and known gaps; apply the recorded rule through a reviewed mapping. A completed job is not necessarily sufficient evidence, and controls make no new semantic judgment. |

Authority and disclosure checks precede model use, examination submission and release. Permission for one disclosure does not authorise another. Release controls check current permission, exact proposal, recipient, evidence result and freshness/bindings; at commitment they freshly adjudicate permission and bind the exact release, which the executor then validates. Timing and Runtime compatibility remain to be specified. The [prototype description](evidence-gated-agents-prototype.md#release-and-recording) explains that separation from evidence assessment.

The retrieval target includes public-source and specialised private-source implementations. Query-relevance ranking and faithful extraction expose their selection limits; they must not suppress results based on service-created support/contradiction judgments. FactHarbor offers retrieval and analytical capabilities, but exact integration remains open. The first prototype supplies human-defined requirements in place of the first two research stages.

For the gated path, a receipt connects permitted evidence references, reasons and the recorded outcome. An assessment, release permission and actual release are distinct outputs. If release may have occurred but cannot be confirmed, the receipt records that uncertainty and names who must reconcile it. Availability is not proof of reading. Stop notices and receipts disclose only what their audience may see; reasons, previews and references must not expose withheld content or bypass access controls.

In the supplier example, the input is the proposed recommendation plus the two-hour guarantee criterion and permitted context. An assessment might find references and response-time statistics but no applicable guarantee. The release rule then determines whether that exact recommendation must stop. A qualified or narrower answer is a **new proposal to check**, not an automatic rewrite by the gate. Releasing a recommendation does not authorize a purchase.

<a id="path-from-the-prototype-to-wider-use"></a>

## What the first prototype can tell us

The [first prototype](evidence-gated-agents-prototype.md) uses **human-defined evidence rules** to examine an exact proposed decision and control recommendation release. **The integration is not yet implemented.** Its [evaluation](evidence-gated-agents-prototype.md#evaluation-and-reporting) tests enforcement and useful, justified releases, including routing errors and missed components. Its retained trigger can leave standalone consequential factual claims outside examination; passing does not establish completeness.

It does not establish whether AI can derive adequate requirements for unfamiliar decisions or whether separate requirement review improves them. Those are the wider research claims below. Additional domains, organisational sources or action workflows need their own scope, activation decision and evidence. See [the current foundations](evidence-gated-agents.md#foundations-and-the-selected-next-step) and the prototype's [scope and limits](evidence-gated-agents-prototype.md#scope).

<a id="test-of-the-aspiration"></a>

## What would count as progress?

For the wider research, success means fewer unsupported releases **while keeping useful answers above a predeclared threshold**. Release means making an answer or decision available to its recipient; delivered explanations accompanying a stop are also assessed. Measure and report missed requirements and claims, unsupported releases, omissions shared by the answering and reviewing agents, unjustified stops, useful qualified answers, successful reassessment after evidence changes, cost and latency.

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

*This note builds on the [earlier research note](https://github.com/robertschaub/our-ai-charter/blob/bb83a2c32ba785f9e10adc38a5217c164e8e54bb/docs/Assurance/Concepts/evidence-requirements-research.md) and adds related-method comparisons, a decision-sufficiency example and an evidence-discovered requirement loop. Its evaluation commitments remain in place.*
