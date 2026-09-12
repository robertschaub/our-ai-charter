# Evidence-Gated Agents: aspiration and test

## Aspiration: mostly generic evidence-gated agents

Evidence-Gated Agents aims to use AI to determine what must be established before a consequential answer or action is justified, and to assess whether the available evidence meets those requirements.

“Mostly generic” means that the same process should work across different questions without people writing a bespoke evidence checklist for each one. Accountable people establish permissions, acceptance policies and relevant domain principles. AI applies those rules to the particular task.

The intended process is to:

1. Identify material claims, assumptions and dependencies in the proposed answer or action.
2. Propose the evidence requirements needed to justify them.
3. Have a separate review challenge whether those requirements adequately cover the proposed assurance.
4. Search permitted sources and assess supporting evidence, counterevidence and unresolved gaps.
5. Apply a separate gate that permits release, requires revision or holds the proposal for review. Material changes require renewed checks.

The aspiration includes discovering requirements the answering assistant overlooked. It also includes recognising when the available evidence cannot support a confident conclusion. Agreement between AI reviewers does not itself establish that their requirements or conclusions are adequate.

This is a research aspiration whose reliability and generality remain to be demonstrated.

## Test of the aspiration

The central test is whether AI can derive and critically review adequate evidence requirements for unfamiliar tasks, then reduce unsupported releases while preserving useful, supported answers.

The evaluation should:

- **Use held-out questions across different domains.** Freeze the workflow before evaluation. Supply reusable policies and domain context, but no hand-authored checklist for each question. Include sufficient evidence, missing support, conflicting sources, misleading citations and changed evidence.
- **Compare against credible alternatives.** Test an ordinary research agent, an agent with a general critique step, and EGA with its requirement-review step removed. Keep the acting model configuration fixed across approaches. Give each the same available sources, tools and resource limits, counting review-model usage within those limits.
- **Assess requirements and complete answers separately.** Domain-qualified reviewers should evaluate both requirement coverage and every material assertion in the released answer, including claims the AI failed to declare. Reviewers should be blinded to the approach used, consider valid requirements beyond their reference checklist and record unresolved disagreements.
- **Measure errors and usefulness together.** Report missed requirements, unsupported releases, unjustified blocking, useful qualified answers, successful reassessment after evidence changes, cost and latency. Record omissions shared by the answering and reviewing agents.
- **Test enforcement separately.** Attempt release after a failed or omitted check, modification of an approved answer, and reuse of an approval after relevant evidence changes. Blocking these attempts demonstrates enforcement integrity; semantic adequacy requires its own evidence.

Success requires a predeclared improvement in unsupported-release rates without an unacceptable loss of useful answers. Numeric thresholds, scoring rules and analysis methods must be fixed before evaluation. Blanket refusal cannot count as success.

Claims of generality must remain limited to the task families, domains and conditions actually tested.

The [user-workflow governance model](user-workflow-governance.md) describes the surrounding authority, evidence and action controls. The [runtime gates proof-of-concept specification](../../wip/runtime-gates-poc-spec.md) defines the bounded implementation work separately from this research aspiration.
