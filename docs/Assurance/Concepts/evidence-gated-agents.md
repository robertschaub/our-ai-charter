# Evidence-Gated Agents: aspiration and test

*Research aspiration and proposed evaluation, 2026-09-13. Reliability and generality remain to be demonstrated.*

## Aspiration: mostly generic evidence-gated agents

Evidence-Gated Agents aims to use AI to determine what must be established before a consequential answer or action is justified, and to assess whether the available evidence meets those requirements.

“Mostly generic” means that the same process should work across different questions without people writing a bespoke evidence checklist for each one. Accountable people establish permissions, acceptance policies and relevant domain principles. AI applies those rules to the particular task.

The intended process is to:

1. Identify material claims, assumptions and dependencies in the proposed answer or action.
2. Propose the evidence requirements needed to justify them.
3. Have a separate review challenge whether the requirements adequately cover the proposed answer or action, including material claims, assumptions or dependencies omitted in step 1.
4. Search permitted sources and assess supporting evidence, counterevidence and unresolved gaps.
5. Apply a separate, deterministic gate that enforces recorded requirements and review outcomes by rule: permit release, require revision or hold the proposal. The gate does not judge evidence adequacy, and a model verdict cannot itself authorize release. Material changes require renewed checks.

The aspiration includes discovering requirements the answering assistant overlooked. It also includes recognising when the available evidence cannot support a confident conclusion. Agreement between AI reviewers does not itself establish that their requirements or conclusions are adequate.

## Test of the aspiration

The central test is whether AI can derive and critically review adequate evidence requirements for unfamiliar tasks, then reduce unsupported releases while preserving useful, supported answers.

Before any evaluated approach receives held-out material, publish a dated evaluation protocol under `docs/Assurance/Protocol/` and identify its Git commit in every run record. Fix the comparisons below, numeric thresholds, scoring and adjudication rules, sample selection, workflow, model configurations and resource limits. Record hashes of the frozen questions and reference requirements; preserve failed attempts and report deviations separately.

The evaluation should:

- **Prevent question-specific checklist leakage.** Freeze reusable policies and domain context before held-out questions are authored or selected. Their authors must be separate from the question authors and have no access to the held-out questions. Permit no question-specific tuning. Include questions across domains with sufficient evidence, missing support, conflicting sources, misleading citations and changed evidence.
- **Match comparison conditions.** Keep the acting model configuration fixed across approaches. Give each the same available sources, tools and resource limits, counting review-model usage within those limits. Add a human-reference approach: the proposed workflow receives the frozen human requirements instead of AI-derived requirements. Report the human preparation effort separately. Its requirements, outputs and assessor feedback must not reach the AI-derived approaches.
- **Freeze contestable references and assess complete answers.** Domain-qualified reviewers prepare reference requirements before seeing any evaluated system output. Preserve that version; the frozen adjudication rules may credit justified alternatives. Assess both requirement coverage and every material assertion in the released answer, including undeclared claims. Normalize answer presentation and remove approach-identifying metadata without changing substantive content. Blind reviewers where possible and report where blinding fails, including recognizable requirements or receipts. Record unresolved disagreements.
- **Measure errors and usefulness together.** Report missed requirements, unsupported releases, unjustified blocking, useful qualified answers, successful reassessment after evidence changes, cost and latency. Record omissions shared by the answering and reviewing agents.
- **Test enforcement separately.** Attempt release after a failed or omitted check, modification of an approved answer, and reuse of an approval after relevant evidence changes. Blocking these attempts demonstrates enforcement integrity; semantic adequacy requires its own evidence.

Each comparison supports a different claim:

| Claim | Comparison and success rule |
|---|---|
| **The full workflow improves release quality.** | Compare it with both an ordinary research agent and an agent with a general critique step. Primary success requires the predeclared reduction in unsupported releases against each, while meeting the predeclared usefulness threshold. |
| **Requirement review adds value.** | Compare the full workflow with the proposed workflow with its requirement-review step removed. Claim an incremental review benefit only if it meets the predeclared requirement-coverage improvement threshold while satisfying the release-quality and usefulness safeguards. |
| **AI-derived requirements approach the human reference.** | Compare the full workflow with the human-reference approach, reporting gaps in requirement coverage, release quality and usefulness. Treat this as a diagnostic comparison; any claim of matching the reference requires predeclared noninferiority margins. The reference is not an infallible oracle. |

Blanket refusal cannot count as success. Neither the review ablation nor the human-reference comparison alone establishes generic requirement derivation.

Claims of generality must remain limited to the task families, domains and conditions actually tested.

The [user-workflow governance model](user-workflow-governance.md) describes the surrounding authority, evidence and action controls. The [runtime gates proof-of-concept specification](../../wip/runtime-gates-poc-spec.md) defines the bounded implementation work separately from this research aspiration.
