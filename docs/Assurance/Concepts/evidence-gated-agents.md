# Evidence-Gated Agents

*Project overview and development direction. EGA is at an early stage; this page explains its goals and does not define implementation obligations.*

<a id="evidence-gated-agents-aspiration-and-test"></a>

Evidence-Gated Agents (EGA) aims to develop AI-assisted decision-making applications and reusable components that keep consequential answers and actions authorised, grounded in evidence, and open to inspection and challenge.

Consequential answers and actions include those affecting people’s rights, access to services or significant resources.

The goal is to help people and organisations make and justify decisions while retaining control over what AI may do and how errors can be corrected. This work serves a broader aim: a free and fair society in which technology supports democracy, justice and well-grounded decisions.

## Who it is for and what it could become

The intended users include people preparing or reviewing decisions, organisations responsible for AI-supported work, and developers integrating controls into their systems. People receiving or affected by the resulting answers and actions also need to understand their basis and have a route to question them.

Two possible development paths are being considered:

- **Applications and services** that organisations could use directly and configure for their needs and working environments.
- **Reusable architecture and components** that software providers or internal development teams could adapt and integrate into existing applications.

Both paths would need evidence of practical usefulness and suitability in their intended settings.

## What the project aims to make possible

The central rule is: **before AI gives a consequential answer or takes a consequential action, it must have permission and enough evidence to justify it.**

The intended approach connects five responsibilities:

1. **Establish authority and limits.** Accountable people define who may do what, for which purpose, using which data and tools. The basis of that authority must itself be reviewable.
2. **Use permitted information and examine the evidence.** Check both whether a source may be used and what it can establish. Make material claims, assumptions, supporting evidence, counterevidence and uncertainty visible. Assess whether that evidence is current and sufficient for the particular proposed use.
3. **Control what proceeds.** Checks outside the acting model govern whether the exact proposal may be released or executed. Before acting, the executing service requests a fresh verification of the approval and checks that the intended action matches it.
4. **Make the outcome inspectable.** Provide an accessible record connecting the answer or action, authority, evidence, decision and actual outcome, with access appropriate to the people involved.
5. **Support challenge and correction.** Let affected people question the basis, route disputes to responsible reviewers, and revisit decisions when evidence or authority changes.

The acting AI cannot authorise itself. Software can enforce recorded rules and decisions, while evidence adequacy and legitimate authority require accountable judgment. Human involvement should focus on decisions where a person can make a meaningful difference; an approval click cannot supply missing evidence.

As an illustrative future use, a procurement team might review an AI-generated supplier recommendation. A claim about guaranteed performance would need evidence addressing that guarantee; a generally positive report would not settle it. If that premise remained unsupported, the recommendation should be held or narrowed and checked again. The record should show the evidence, who authorised the next step and what actually happened.

## Foundations and the next step

EGA draws on three related pieces of work:

- **[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor)** assesses claims using supporting and opposing evidence and makes sources and uncertainty inspectable.
- **[Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first)** is a separate, unfinished proof of concept for controls outside the acting model. Its demonstrations use simulated scenarios and a local test action.
- **[Our AI Charter](../Framework/charter-commitments.md)** provides the broader principles for accountable AI use, including authority, evidence, oversight and remedy.

The proposed first EGA prototype, subject to funding and an agreed scope, would connect FactHarbor and the runtime in a bounded German/English answer-delivery path. It would use a prepared bundle of public evidence, check an answer before release, provide an inspectable receipt and support bounded challenges and correction. Answer delivery would be its only real action type; other actions would remain simulated.

This prototype checks the evidence dependencies the drafting model declares. Unsupported assertions it fails to declare can escape those checks; evaluation must examine that limitation.

## Longer-term development and open research

Later work could extend the same approach to evidence gathered when needed, permitted organisational sources, and further agent, tool and action workflows. Each extension would need suitable authority, privacy controls, evidence requirements and evaluation. Effective independent review and remedy would also require institutions with the power to act.

One research strand asks whether AI can identify adequate evidence requirements for unfamiliar questions, discover overlooked assumptions and have those requirements critically reviewed, without people writing a separate checklist for every question. This could broaden reuse; its reliability remains to be demonstrated.

Success means useful, supported answers and actions with fewer unjustified releases, understandable records and workable correction routes. Testing must also expose unnecessary blocking, missed claims, cost and practical limitations. Enforcing a gate does not establish that an answer is true, and agreement between AI reviewers does not establish that their judgment is adequate.

The [user needs and requirements](../../wip/evidence-gated-agents-requirements.md) and [technical specification](../../wip/evidence-gated-agents-spec.md) describe the proposed capabilities and their limits. Both are working drafts; an implementation baseline remains to be adopted.

## Research detail

- <a id="aspiration-mostly-generic-evidence-gated-agents"></a> [AI-derived evidence requirements](evidence-requirements-research.md#aspiration-mostly-generic-evidence-gated-agents)
- <a id="test-of-the-aspiration"></a> [Research questions and evaluation](evidence-requirements-research.md#test-of-the-aspiration)
- <a id="path-from-the-prototype-to-wider-use"></a> [Prototype-to-research coverage](evidence-requirements-research.md#path-from-the-prototype-to-wider-use)
