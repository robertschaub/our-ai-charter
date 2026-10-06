**PUBLISHED 2026-10-05 to LinkedIn [Post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7512953020503105536/)**

***

An AI recommendation can sound convincing—but is there enough evidence to justify following it?

Evidence-Gated Agents (EGA) connects evidence examination with control over whether a consequential recommendation may be released. Its design actively searches for supporting evidence and contradicting evidence, checks authority and preserves a basis for inspection and challenge.

Two foundations already exist: FactHarbor Alpha searches and analyses evidence; a separate Runtime proof of concept demonstrates controls outside the acting AI. The next milestone is to integrate and evaluate them in one bounded recommendation workflow.

Explore the project and the cooperation opportunity:
https://robertschaub.github.io/our-ai-charter/Assurance/Concepts/evidence-gated-agents/

\#EvidenceGatedAgents #ResponsibleAI #AIAccountability

𝘍𝘶𝘭𝘭 𝘢𝘳𝘵𝘪𝘤𝘭𝘦 𝘣𝘦𝘭𝘰𝘸 ↓
***
[![Broader EGA design: Working AI submits a claim, decision or action instruction. The evidence service returns search results; EGA analyses support, contradiction and gaps and applies evidence, authority and disclosure rules. It releases the checked claim, decision or action instruction, or holds it. Releasing an instruction does not authorise execution; the resulting action requires its own authority and evidence checks. Restricted decision records support inspection and challenge; data protection applies throughout the system.](evidence-gated-agents-before-we-rely-cover.png)](evidence-gated-agents-before-we-rely.png)
***

*The diagrams show the output-release gate for claims, decisions and action instructions. The first integration targets consequential recommendations and instructions; it does not execute resulting actions. Integration and confidential-source handling remain to be built.*

# Evidence-Gated Agents: Before We Rely on an AI Recommendation

Imagine choosing a supplier for a service that must respond within a guaranteed time. An AI assistant recommends one, citing satisfied customers and excellent average performance. Neither establishes the guarantee your decision depends on.

A useful answer identifies that gap. But recognising it is only part of the problem: what prevents an unsupported recommendation from being released as ready to rely on?

**Evidence-Gated Agents (EGA) connects evidence examination with control over whether a consequential recommendation may proceed.** The aim is practical: help people make better-grounded decisions while retaining control and a route to challenge mistakes.

## Evidence before reliance

EGA's design places checks outside the acting AI to govern release of a claim, decision or action instruction. An evidence service returns material from permitted sources, with source references and search coverage; EGA analyses support, contradiction and gaps for the exact output. Its analytical verdict and reasons inform release controls alongside current authority and disclosure permissions. A favourable verdict alone does not authorise release.

For the supplier example, an unsupported guarantee means holding the recommendation. A narrower alternative needs its own check. The selected prototype targets consequential recommendations and instructions; ordinary answers follow a lighter path with authority and disclosure checks.

Routine checks run automatically within agreed limits. Human judgment is reserved for cases where the stakes justify interruption, an authorised person can make a difference, and the issue cannot be resolved within existing authority. Approval cannot replace missing evidence or permission.

The same evidence-service interface can support public sources and specialised company/private sources. Data protection applies across the system, including outgoing requests, search results, released outputs and record views. **Access, processing and disclosure are separate permissions**; checks precede use by a model or service and each disclosure. Decision records need limited content, access and retention. Separate oversight responsibilities keep operation, custody, independent review and remedy from resting with one operator; records support scrutiny rather than guaranteeing truth or effective remedy.

## Two foundations, one concrete milestone

[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor) already searches and analyses supporting and opposing evidence, making sources and uncertainty visible. It remains an Alpha with documented quality limitations.

The separate [Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first) is a runnable proof of concept demonstrating controls outside the acting model. Its synthetic scenarios include refusing an action outside the recorded mandate even after human approval. These demonstrations use local test effects.

**The next milestone connects these foundations in one bounded recommendation workflow.** FactHarbor provides existing retrieval and analytical capabilities for EGA; separate controls apply human-defined evidence rules and check release permission. The exact component integration remains to be specified. This integration remains to be built and evaluated. Releasing a supplier recommendation does not authorise a purchase. Wider confidential-source and independent-governance arrangements also require development.

The evaluation asks whether the combination reduces unsupported recommendations while retaining useful answers. It will need to expose unnecessary stops, missed decision components, cost and delay—not just successful examples. The result should support a decision to continue, revise or stop that line of work.

Automatically identifying adequate evidence requirements for unfamiliar decisions is a [broader research question](../Assurance/Concepts/evidence-requirements-research.md). Its reliability remains to be demonstrated; the first integration cannot establish it alone.

## Where cooperation can make a difference

Workflow partners can define a useful recommendation and the evidence it needs. Engineers can connect the foundations; researchers can shape and challenge the evaluation. Funding enables focused development and assessment of this milestone.

Cooperation agreements would define the workflow, success criteria and reporting arrangements, including confidentiality and publication. The wider research retains its separate public evaluation commitments.

**Bring a workflow, contribute expertise, or explore supporting the next stage.** A first conversation can use a brief description and synthetic examples; no confidential records are needed. Contact [Robert Schaub](https://www.linkedin.com/in/robertschaub/) or [info@factharbor.ch](mailto:info@factharbor.ch).

The [EGA project page](../Assurance/Concepts/evidence-gated-agents.md) brings together the design, current scope, supporting work and the FactHarbor association's stewardship commitments.
