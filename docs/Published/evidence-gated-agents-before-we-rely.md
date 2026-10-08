**PUBLISHED 2026-10-07 to LinkedIn [Post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7513710861446873088/)**

***

An AI recommendation can sound convincing—but is there enough evidence to justify following it?

Evidence-Gated Agents (EGA) connects evidence examination with controls outside the acting AI. Its design repeats the same check at relevant boundaries: before using information, releasing output or taking action.

Any check can seek evidence, including evidence of permission and authority. EGA analyses supporting and contradicting evidence, checks the applicable requirements and records the basis for Proceed or Do not proceed—with human judgement where needed. Where permitted, Working AI can revise and submit a new proposal for checking; the rejected step stays blocked.

Two foundations already exist: FactHarbor Alpha and the Our AI Charter Runtime proof of concept. The next milestone connects them in one bounded recommendation workflow and tests whether it reduces unsupported recommendations while retaining useful answers.

Explore the design and cooperation opportunity:
https://robertschaub.github.io/our-ai-charter/Assurance/Concepts/evidence-gated-agents/

\#EvidenceGatedAgents #ResponsibleAI #AIAccountability

𝘍𝘶𝘭𝘭 𝘢𝘳𝘵𝘪𝘤𝘭𝘦 𝘣𝘦𝘭𝘰𝘸 ↓
***
[![Simplified EGA design: Working AI proposes a step within existing permission. An EGA check can request evidence and applies evidence, authority and permission requirements. Proceed stays within checked scope; Do not proceed gives a reason and permitted route. A continuation loop returns to Working AI after the checked step to plan further work; a separate revision loop permits correction and renewed checks. Human judgment, people receiving or affected by results, restricted records and oversight are visible.](evidence-gated-agents-before-we-rely.png)](evidence-gated-agents-before-we-rely.png)
***

# Evidence-Gated Agents: Before We Rely on an AI Recommendation

Imagine choosing a supplier for a service that must respond within a guaranteed time. An AI assistant recommends one, citing satisfied customers and excellent average performance. Neither establishes the guarantee your decision depends on.

A useful answer identifies that gap. But what prevents an unsupported recommendation from being released as ready to rely on?

**Evidence-Gated Agents (EGA) connects evidence examination with controls outside the acting AI.** Its design governs whether a claim, decision or action instruction may proceed—and preserves a basis for inspection and challenge.

## The same check at each relevant boundary

Working AI can plan and prepare within existing permission. EGA checks recur when it proposes a protected step: using new information, sending content to a service, releasing output or taking action. Each check asks: **may this step proceed under its applicable requirements?** Trusted rules select those requirements; the acting AI cannot authorise itself.

Any EGA check can request evidence, including evidence of permission, authority or delegation. The evidence service returns what it finds, with source references and search coverage. **EGA assesses supporting evidence, contradicting evidence and gaps.** The service does not decide what the material proves or whether the step may proceed.

For the supplier example, missing evidence of the required guarantee means the recommendation does not proceed. A narrower recommendation needs a new check. A favourable analytical verdict alone cannot replace authority or permission to disclose the content.

**Proceed** permits the checked step within its scope. After that step, Working AI may plan further work within current permission; each new protected transition faces its applicable checks. **Do not proceed** records the reason and next permitted route. Where permitted, Working AI receives feedback and prepares a corrected or narrower proposal within its current permission. The revised proposal must pass all applicable checks in a new attempt; the rejected step stays blocked and closed attempts stay closed. Uncertain work or delivery must be reconciled before any next step that could duplicate it. Human judgement is sought where an authorised person can resolve a specific issue and the stakes justify interruption. It cannot supply missing evidence or reopen a stopped attempt.

The evidence-service interface can support public sources and specialised company/private sources. Access, processing and disclosure are separate permissions. Data protection applies throughout the system, including outgoing requests, released content and records. Decision-record access is restricted; separate oversight responsibilities support inspection, challenge and correction.

[![Full EGA design: Working AI prepares within existing permission, passes a before-use check, carries out permitted work and submits a step for a release or action check. Both checks can request evidence. After the checked step, a continuation loop returns to preparation for further work and applicable checks. Refusals lead to Do not proceed, conditional human judgment and permitted revision before renewed checks. People receiving or affected by results, five oversight roles, restricted records and system-wide data protection are shown.](../Assurance/Concepts/evidence-gated-agents-release-workflow.png)](../Assurance/Concepts/evidence-gated-agents-release-workflow.png)

*The full design shows the same EGA check at two example boundaries. After the checked step, Working AI may plan the next step within current permission; new protected transitions require their applicable checks. If revision is permitted, Working AI prepares a changed proposal that must undergo the applicable checks in a new attempt. People receiving or affected by the result remain visible alongside human judgment and oversight. The first integration remains recommendation release only; integration and confidential-source handling remain to be built.*

## Two foundations, one concrete milestone

[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor) already searches and analyses evidence, exposing sources and uncertainty. It remains an Alpha with documented quality limitations.

The separate [Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first) is a runnable proof of concept demonstrating controls outside the acting model. Its synthetic scenarios include refusing an action outside the recorded mandate even after human approval; demonstrations use local test effects.

**The next milestone connects these foundations in one bounded recommendation workflow.** EGA analysis uses a human-defined evidence checklist; separate controls apply the evidence rules and check release permission. The exact component integration remains to be specified, built and evaluated. The first prototype releases a checked recommendation; it does not execute the resulting action. Ordinary answers retain authority and disclosure checks without the full consequential-output examination.

Evaluation must reveal unsupported releases, unnecessary stops, missed decision components, useful answers, cost and delay. Automatically identifying adequate evidence requirements for unfamiliar decisions remains a [broader research question](../Assurance/Concepts/evidence-requirements-research.md).

## Where cooperation can make a difference

Workflow partners can define a useful recommendation and the evidence it needs. Engineers can connect the foundations; researchers can shape and challenge the evaluation. Funding enables focused development and assessment of this milestone.

Cooperation agreements would define the workflow, success criteria and reporting arrangements, including confidentiality and publication. The wider research retains its separate public evaluation commitments.

**Bring a workflow, contribute expertise, or explore supporting the next stage.** A first conversation can use a brief description and synthetic examples; no confidential records are needed. Contact [Robert Schaub](https://www.linkedin.com/in/robertschaub/) or [info@factharbor.ch](mailto:info@factharbor.ch).

The [EGA project page](../Assurance/Concepts/evidence-gated-agents.md) brings together the design, scope, supporting work and stewardship commitments.
