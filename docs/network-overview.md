---
title: The proposed public-AI network
description: Why a public-AI network is needed, what it would add, how it would govern AI-supported action, and how to take part today.
---

# The proposed public-AI network

Open models are necessary, but they are not public infrastructure by themselves. Digital sovereignty is the capacity to inspect systems, help set their rules, contest decisions, and switch; this proposal connects the models, lawful data, evidence, governance, and federated compute needed to make that possible.

> **Where this stands today.** This proposed public-AI network is an **early-stage, voluntary** design. No public front door, admission body, assessor, adjudicator, public register, certification, or trust badge exists yet — only the proposal, the public drafts, and prospective partners. Taking part today means contributing, testing the case, or registering interest in a role — not endorsement or certification.

*The current [project statement](Published/our-ai-charter-public-ai-infrastructure.md) makes the fuller case; the [sovereignty argument](Published/swiss-autarky-illusion.md) explains why autarky is not sovereignty. See the [architecture](Infrastructure/architecture.md), [Charter Commitments](Assurance/Framework/charter-commitments.md), and [initiation strategy](Strategy/initiation-strategy.md) for technical, assurance, and coalition detail.*

## Why a network

AI is becoming infrastructure through which people learn, work, decide, and form opinion. An open model can still sit behind opaque routing, data practices, access controls, and failure review; a collection of national models is therefore not yet shared public infrastructure. A federation lets institutions keep local control while sharing standards, evidence, accountability, and fallback paths — widening access for researchers, public bodies, startups, and civic builders without dependence on one provider.

## What it combines

Four connected pillars:

1. **Open, plural models** — inspectable and comparable across languages and regions through shared interfaces, with none privileged in the network's rules.
2. **Data and provenance commons** — documented origin, permissions, opt-outs, restrictions, and access conditions.
3. **Shared assurance and evaluation** — scoped, checkable evidence, independent review, correction, and remedy.
4. **Federated public AI infrastructure** — independently operated compute nodes under shared rules and local control.

**AI Assurance & Certification** is the third pillar's trust-and-evidence building block: the obligations, evaluation method, and future assurance structure that make public-AI claims checkable.

The data commons does not assume that all useful training data can be open. Its benefit is **clear once, reuse many**: handle rights, provenance, and access conditions collectively instead of making every public model negotiate alone.

Here, **public** describes obligations, accountability, access, and governance — not an operator's legal form. Public, academic, cooperative, nonprofit, and mission-aligned commercial nodes could participate under the same disclosure, portability, evidence, and anti-capture rules.

**Values-bound** would not mean a bloc of self-described “free” states. Participation would depend on verifiable commitments to human rights, rule-of-law procedures, democratic accountability, transparency, and effective remedy.

Under all four sits **competence**. Infrastructure can be procured; the ability to understand, govern, and improve it must be built through education, research, managerial capability, and institutional learning — and kept broadly distributed. That is also an economic case: value creation, skilled work, and bargaining power grow where institutions help build and decide, not merely buy. **Anti-capture governance** and public-interest **demand** hold the pillars together.

## How it would work

The intended user path is **find → check → use**:

1. **Find** a system suited to the purpose, jurisdiction, language, openness, and capability needed.
2. **Check** its claims, reviewed evidence, known limits, and unverified areas ([questions to ask](index.md#what-must-be-checkable)).
3. **Use** it as an endpoint, assistant, agent, or evaluator under access rules suited to the user and data.

The same offering is an **AI system** when found, compared, or held to account and an **AI service** when served and used — two views, not separate layers.

Discovery must remain plural and neutral because whoever controls discovery can shape the market.

## How it would govern action and human consequences

Existing gateways, schedulers, registries, and identity systems mostly answer **can this run?** The proposed public-interest layer asks **may it run — for whom, for what purpose, on which node, with what model and data, under which evidence duties, and with what route to challenge and remedy?** Accountability therefore cannot stop at choosing a model or evaluating a release. The network would connect lifecycle governance — **design → deploy → operate → incident → remedy** — with [five activity/gate pairs for each AI-supported action](Published/when-should-runtime-ai-governance-interrupt.md): **Plan → Authorize; Prepare → Submit; Check → Verify; Decide → Commit; Review → Rely.** Across both, the [five public obligations](Published/trustworthy-ai-accountable-to-people.md#the-obligations) remain in force: purpose-bound; answerable to people; safe, secure, private, and resilient; fair in practice; and open to evidence and correction.

The rule is to govern every authority-bearing transition, not every inference. A component outside the acting model would return **allow, deny, or escalate**; the service producing an external effect would verify that decision again. Routine, reversible actions inside an authorized envelope could remain silent. External, irreversible, regulated, person-affecting, or out-of-bounds actions would stop when required authority or evidence is absent — human approval cannot manufacture the missing basis. Preserve an action-scoped record of authority, material evidence and uncertainty, effect, and challenge route — not every token or the whole conversation.

Those gates are also moments to [test AI-supported power](Published/a-practical-test-for-power.md#test-every-use-of-power) and reopen dialogue. Ask who has authority, who benefits and bears the cost, whether expected harm is necessary and proportionate and a less harmful path exists, and whether affected people can safely disagree, refuse, or challenge and obtain independent review and remedy. Check both specific people and population patterns: individually admissible actions can accumulate into a discriminatory or otherwise unauthorized effect.

[AI and Empathy: Dialogue, Correction and Human Answerability](Published/empathy-is-a-practice.md) treats empathy as observable, correctable behaviour that protects human agency — not artificial feeling. The [builder guideline](Published/how-to-build-ai-that-acts-with-empathy.md) turns that practice into engineering: keep distinct what a person said, what the system inferred, what the person confirmed, and what it has revocable permission to use or remember; seek affected perspectives; carry disagreement and uncertainty forward; and make correction, refusal, and escalation usable. Reopen dialogue only when an unresolved interpretation, permission, missing perspective, or observed consequence could change a transition, following **engage → act → observe → disclose → correct → re-engage**. **Sycophancy is not empathy:** models can support perspective-taking but cannot supply legitimate authority, independent review, or remedy. For builders: **train for perspective-taking; tune for truthfulness and agency; adapt only with consent; improve only through governed, testable releases.**

No body should control the accountability chain. Service roles — model or data provider, deployer, node operator — would remain distinct from the rule steward, evidence custodian, independent reviewer, and remedy decider ([why the roles must stay separate](Published/when-vs-who-ai-governance.md)). If the scheme matured, accreditation and peer review would check the reviewers.

## What would be built first

The proposed first pilot is deliberately small: a simple public model-and-provenance catalogue and access layer; a **model-plural policy broker** deciding whether and where a workload may run and what evidence must be kept; several public models; at least two independent nodes; and an **evidence-and-accountability plane**.

The nearest live starting pattern is an Apertus-backed inference and evaluation service following the Public AI Inference Utility pattern, extended with broker and evidence controls, then federated with a second node or provider and ideally a second model family. These are reference components, not an affiliation or active-pilot claim. Node control would stay local while policy, quota, accounting, evidence, and accountability are shared.

Evidence would be public where safe, protected and access-logged where review requires it, and not retained without lawful need; raw personal data would never enter the public evidence layer. The sequence is **define and align → prototype → federate → institutionalise**; the [pilot and rollout strategy](Infrastructure/pilot-and-rollout.md) holds the MVP and open decisions.

Success is not global scale. It is proving that public compute can be shared under inspectable rules.

## What happens next

The work is in **Phase 1: public drafting and connection-building**. The near-term target is a **Geneva 2027 Public AI Governance & Evidence Package**: a neutral clarification process, governance blueprint, one bounded evidence-and-evaluation pilot outline, and roundtable path. The route is **alliance and mandate first, lawmaking later**; Switzerland is a possible host, node, and bridge — not owner.

## How to take part now

- **Builders and researchers** — identify overclaims, duplication, and unrealistic evidence duties; later, offer a system for a bounded pilot.
- **Contributors** — critique, research, translate, or improve a draft through GitHub.
- **Connectors** — open one useful door to a neutral convenor, institutional anchor, partner, or venue.
- **Funders** — support one deliverable or contribute compute, staff, or a venue without controlling rules or findings.
- **Policy and institutional leaders** — test the question through procurement, policy, a pre-sprint, or Geneva 2027.
- **Users and the public** — apply the [checkable questions](index.md#what-must-be-checkable) when choosing, buying, evaluating, or challenging AI.

If operational roles are created, admission would be rules-based, appealable, role-specific, and proportionate. It could begin with signed commitments and self-attestation, then mature through independent review, public status, and consequences for false claims. Membership would never be a trust badge: only verified, scoped claims could be made.

To take part, open a [GitHub issue](https://github.com/robertschaub/our-ai-charter/issues) or, for introductions, funding, or anything not for public posting, write to [info@factharbor.ch](mailto:info@factharbor.ch). The initiator contributes the method but operates no assessor, adjudicator, or registry.

## Boundaries

This proposal contributes to the broader public-AI movement; it does not claim affiliation with an existing coalition unless explicitly stated. The **Public AI Inference Utility** (publicai.co) is a separately operated nonprofit service whose access pattern informs the design; **publicai.ch / SPIU** is a self-described Swiss chapter and proposed cooperative linked to that utility. Both are separate from this initiative.

- Not a new language model competing with Apertus or another public model.
- Not a new runtime, scheduler, marketplace, identity system, or standalone certification authority.
- Not a single global GPU pool or a claim of full-stack sovereignty.
- Not a way for funders, operators, model providers, or a host country to buy control over the rules or findings.
