---
title: Our AI Charter™
description: Protect and strengthen free and fair societies in the digital age through public-AI governance and infrastructure that are accountable to people and support societal resilience and economic prosperity.
hide:
  - toc
---

# Our AI Charter™

<div class="tagline" markdown>
**Trustworthy AI for free, fair, and resilient societies.**
</div>

Our AI Charter is an **early public proposal for an international network of open AI models under shared public obligations**. The proposal includes a shared way to find, check and use participating AI systems, with governance and evidence separate from service provision.

## Five connected pillars

<div class="pillar-list" markdown>

1. **[Accountable AI decisions and actions](Assurance/Concepts/evidence-gated-agents.md){ .pillar-focus }**

    Who may authorise a consequential answer or action, on what evidence and within which limits? Its approval, refusal and execution outcome should be inspectable and open to challenge.

2. **[Open, plural models](network-overview.md#why-a-network)**

    Inspectable models across languages and regions, with meaningful choice and none privileged in the network's rules.

3. **[Data and provenance commons](network-overview.md#what-it-combines)**

    Documented sources, rights, restrictions and access conditions, handled collectively where possible.

4. **[Shared assurance and evaluation](Assurance/Framework/charter-commitments.md)**

    Checkable claims about AI systems and their operation, independent evaluation and review, correction and remedy.

5. **[Federated public AI infrastructure](Infrastructure/architecture.md)**

    Independently operated compute capacity connected through shared rules, with local control and fallback paths.

</div>

[Shared public obligations](Assurance/Framework/charter-commitments.md) and accountable human governance would apply across all five pillars, with routes to challenge and remedy. Models, data and infrastructure provide the resources; controls govern consequential answers and actions; independent assurance examines whether systems and their operation meet those obligations.

[How the pillars work together →](network-overview.md#what-it-combines)

AI is becoming the infrastructure people learn, work, decide, and form opinion with. Infrastructure that important should not depend on a few providers, unclear shutdown powers, hidden data practices, unverifiable factual claims, or systems that affected people cannot challenge.

<div class="mission" markdown>
<span class="mission-label">Our mission</span>
Protect and strengthen free and fair societies in the digital age through public-AI governance and infrastructure that are **accountable to people** and support **societal resilience** and **economic prosperity**.
</div>

## Where the work stands

*As of 14 September 2026.*

**Current focus — Evidence-Gated Agents.** Robert Schaub is defining and preparing the first EGA prototype. The public [project overview](Assurance/Concepts/evidence-gated-agents.md) explains the selected direction and its limits; the implementation baseline remains to be agreed.

**Existing foundations.** [FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor) structures claims with supporting and opposing evidence, sources and confidence levels. [Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first) is a separate, runnable but unfinished proof of concept for checks outside the acting model, exercised through simulated scenarios and a local test action. The [Charter Commitments](Assurance/Framework/charter-commitments.md) and [evaluation protocol](Assurance/Protocol/grounding-faithfulness-and-contestability.md) are public drafts.

**Selected prototype direction.** A bounded German/English path will let a normal AI agent answer a free request, ask FactHarbor to examine whether evidence supports the exact proposed decision, and release or stop that decision under checks outside the acting model. Every release and stop produces an inspectable receipt. The prototype releases decisions but does not execute resulting actions; API and Runtime integration remain to be implemented. See the [prototype scope](Assurance/Concepts/evidence-gated-agents.md#selected-prototype-dynamic-decision-examination).

**Broader network and assurance work.** The proposed international network and certification scheme remain in public drafting and connection-building; neither is operational and no systems are Charter-certified. The [network strategy](Strategy/initiation-strategy.md) retains the Geneva 2027 governance-and-evidence ambition, pursued internationally from a Swiss starting point. Building a partner mandate remains a prerequisite for wider network implementation.

## How to help

1. **Build or test** — Explore [Evidence-Gated Agents](Assurance/Concepts/evidence-gated-agents.md) and contribute practical use cases, development or evaluation expertise.
2. **Scrutinise the work** — Challenge specific claims, gaps or design choices against the [Charter Commitments](Assurance/Framework/charter-commitments.md) and [supporting evidence](Evidence/verified-findings.md).
3. **Connect people and institutions** — Introduce a potential collaborator, neutral convenor or policymaker. The [network strategy](Strategy/initiation-strategy.md) sets out the broader cooperation route.
4. **Back a concrete step** — Help fund a clearly scoped deliverable or support it in relevant policy venues.

See [how to take part now](network-overview.md#how-to-take-part-now) for what each role can do, [CONTRIBUTING](https://github.com/robertschaub/our-ai-charter/blob/main/CONTRIBUTING.md) for working norms, and [About](About.md) for stewardship. For suspected secrets, private material, or personal data, contact [info@factharbor.ch](mailto:info@factharbor.ch) instead of opening a public issue.

---

Sovereignty and resilience, not autarky. Open, inspectable AI models matter, but sovereignty and resilience come from what surrounds them: standards, public evidence, accountable governance, and federated public AI infrastructure designed to reduce dependence on any one provider or authority and make capture harder. Public AI needs more than open models — it needs a public-interest governance and evidence layer.
