**PUBLISHED 2026-10-07 to LinkedIn [Post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7513710861446873088/)**

***

An AI recommendation can sound convincing—but is there enough evidence to justify following it?

Evidence-Gated Agents (EGA) is a proposed design connecting evidence examination with controls outside the acting AI. Its design repeats the same check at relevant boundaries: before using information, releasing output or taking action.

Any check can seek evidence, including evidence of permission and authority. EGA analyses supporting and contradicting evidence, checks the applicable requirements and records the basis for Proceed or Do not proceed—with human judgement where needed. Where permitted, Working AI can revise and submit a new proposal for checking; the rejected step stays blocked.

Two foundations already exist: FactHarbor Alpha and the Our AI Charter Runtime proof of concept. The next milestone connects them in one bounded recommendation workflow and tests whether it reduces unsupported recommendations while retaining useful answers.

Explore the design, co-development and funding opportunities:
https://robertschaub.github.io/our-ai-charter/Assurance/Concepts/evidence-gated-agents/

\#EvidenceGatedAgents #ResponsibleAI #AIAccountability

𝘍𝘶𝘭𝘭 𝘢𝘳𝘵𝘪𝘤𝘭𝘦 𝘣𝘦𝘭𝘰𝘸 ↓
***
[![Illustrated EGA design: Working AI proposes a step to a golden EGA checkpoint for evidence, authority and applicable permissions. Evidence sources feed a separate evidence service. Proceed leads to the checked step and an outcome record; Do not proceed leads to remaining stopped with the reason recorded. Dashed returns allow optional further work or permitted revision and rechecking. Crossing lines do not join. Human judgement, affected people and oversight remain visible.](evidence-gated-agents-before-we-rely-illustrated.png)](evidence-gated-agents-before-we-rely-illustrated.png)
***

# Evidence-Gated Agents: Before We Rely on an AI Recommendation

AI can turn a question into a recommendation—and a recommendation into action. Before people rely on the result, they need more than a convincing explanation: evidence that supports the proposed step, authority to proceed, and a way to challenge what went wrong.

**Evidence-Gated Agents (EGA) is a proposed design that makes these checks part of the workflow.** The AI prepares a proposal. Evidence examination tests its basis, while controls outside the acting AI determine whether it may proceed under the applicable requirements.

A check can permit the step or stop it. Where revision is permitted, feedback can guide a revised proposal and a fresh check. The design preserves a record of the basis and outcome, with human judgement where needed.

The aim is to make AI useful in work where decisions have consequences—and where people must be able to understand, question and correct them.

## The same check at each relevant boundary

Working AI can plan and prepare within existing permission. EGA checks recur when it proposes a protected step: using new information, sending content to a service, releasing output or taking action. Each check asks: **may this step proceed under its applicable requirements?** Trusted rules select those requirements; the acting AI cannot authorise itself.

Any EGA check can request evidence, including evidence of permission, authority or delegation. The evidence service returns what it finds, with source references and search coverage. **EGA assesses supporting evidence, contradicting evidence and gaps.** The service does not decide what the material proves or whether the step may proceed.

Supporting evidence does not replace authority or permission to disclose information. A favourable analytical verdict alone is not enough to let the step proceed.

**Proceed** permits the checked step within its scope. After that step, record the actual outcome. Then end the workflow or optionally plan further work within current permission; each new protected transition faces its applicable checks.

**Do not proceed** withholds the step and records the reason. The workflow may end there; revision is an optional permitted route. Where permitted, Working AI receives feedback and prepares a corrected or narrower proposal within its current permission. The revised proposal must pass all applicable checks in a new attempt; the rejected step stays blocked and closed attempts stay closed.

Ending the workflow does not cancel required reconciliation of an uncertain examination, commitment or delivery; reconcile before any next step that could duplicate work or effects. Human judgement is sought where an authorised person can resolve a specific issue and the stakes justify interruption. It cannot supply missing evidence or reopen a stopped attempt.

The evidence-service interface can support public sources and specialised company/private sources. Access, processing and disclosure are separate permissions. Data protection applies throughout the system, including outgoing requests, released content and records. The record keeper provides independent custody of decision records, with restricted access. Separate oversight responsibilities support inspection, challenge and correction.

[![Full EGA design: Working AI prepares within existing permission; two example boundary checks can request evidence. Proceed leads to the checked step and an outcome record. Do not proceed leads to remaining stopped with a reason recorded. Separate dashed routes optionally return to Working AI for further work or permitted revision and rechecking. Human judgment is conditional; affected people, independent custody of decision records and five oversight roles remain visible.](../Assurance/Concepts/evidence-gated-agents-release-workflow.png)](../Assurance/Concepts/evidence-gated-agents-release-workflow.png)

*The full design shows the same EGA check at two example boundaries. Solid paths end with an outcome record after the checked step, or with the step stopped and the reason recorded. Dashed returns show optional further work or permitted revision; new or revised proposals face applicable checks. People receiving or affected by the result remain visible alongside human judgment and oversight.*

## Two foundations, one concrete milestone

[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor) already searches and analyses evidence, exposing sources and uncertainty.

The separate [Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first) is a runnable proof of concept demonstrating controls outside the acting model. Its synthetic scenarios include refusing an action outside the recorded mandate even after human approval; demonstrations use local test effects.

**The next milestone connects these foundations in one bounded recommendation workflow.** EGA analysis uses a human-defined evidence checklist; separate controls apply the evidence rules and check release permission. The exact component integration remains to be specified, built and evaluated. The first prototype releases a checked recommendation; it does not execute the resulting action. Ordinary answers retain authority and disclosure checks without the full consequential-output examination.

Evaluation must reveal unsupported releases, unnecessary stops, missed decision components, useful answers, cost and delay. Automatically identifying adequate evidence requirements for unfamiliar decisions remains a [broader research question](../Assurance/Concepts/evidence-requirements-research.md).

## Co-development and funding

We are looking for **experienced co-developers** to build and evaluate the first EGA integration. We also seek **sponsors and funders** to support the engineering and evaluation needed to reach this milestone.

**Get in touch about co-development, sponsorship or funding.** Contact [Robert Schaub](https://www.linkedin.com/in/robertschaub/) or [info@factharbor.ch](mailto:info@factharbor.ch). Initial discussions need no confidential records. Work with private organisational evidence requires separately agreed access, handling and evaluation.

The [EGA project page](../Assurance/Concepts/evidence-gated-agents.md) brings together the design, scope, supporting work and stewardship commitments.
