---
title: Our AI Charter
permalink: /
---

> **Status: WORKING DRAFT** - public GitHub Pages entry point. The original manifesto is published; this repository version, the charter, protocol, and certification model are open drafts.

# Our AI Charter

**Trustworthy AI, accountable to people.**

AI is becoming infrastructure for how people learn, decide, work, and form public opinion. That infrastructure cannot be left to a few private providers, opaque shutdown powers, unsafe or insecure systems, discriminatory failures, privacy leakage, coercive manipulation, or material factual claims that cannot be traced or challenged.

Our AI Charter is a public-interest draft for making AI more trustworthy in practice: bounded by purpose, answerable to people, safe and private enough to rely on, fair in practice, and open to evidence and correction.

[Read the program map](PROGRAM.md) · [Read the updated article](manifesto/trustworthy-ai-accountable-to-people.md) · [Read the Founding Accord](charter/founding-accord.md) · [Read the risk audit](background/risk-and-vulnerability-audit.md) · [Read the evaluation protocol](protocol/grounding-faithfulness-and-contestability.md) · [Read the certification model](protocol/certification-model.md)

## The Practical Demand

People who use, buy, study, regulate, or are affected by AI need more than promises. Public authorities, customers, media, researchers, and civil society should be able to demand answers to six questions:

1. **What is this system for?** Intended uses, prohibited uses, misuse boundaries, covered versions, limits, affected groups, and risk context must be stated before trust is claimed.
2. **Who controls it?** Operators, critical providers, models, data, tools, cloud/compute dependencies, update powers, restriction powers, shutdown powers, and external orders or pressure to use them must be named and logged where lawful.
3. **Who is accountable?** Each deployment needs an accountable owner, jurisdiction, contact route, and retained evidence for public claims, safety, security, privacy, fairness, and misuse handling.
4. **How can people challenge it?** Affected people need notice, a usable complaint route, response times, human review for consequential uses, and records of outcomes, including data-use, discrimination, restriction, or shutdown decisions where challenge is legally possible.
5. **Who can inspect it?** Public transparency, confidential audit access, lawful regulator access, protected research access, red-team evidence, security testing, privacy controls, and data provenance must be distinguished and scoped.
6. **Can its claims and failures be checked?** Material factual claims, consequential decisions, restriction orders, security/privacy/misuse incidents, disparate failure rates, corrections, significant changes, withdrawals, and exit paths must leave testable evidence.

These questions turn the published manifesto into a concrete charter and the first auditable modules.

## Five Public Obligations

### 1. Purpose-bound

An AI system should state what it is for, what it must not be used for, which version and use-case are covered, who may be affected, what risks are known, and what would trigger reassessment before trust is claimed.

### 2. Answerable to people

A named human institution should answer for the system's claims, harms, data use, incidents, and consequential decisions. People affected by the system need notice, a usable route to challenge, meaningful human review where risk warrants it, and remedy when things go wrong.

### 3. Safe, secure, private, and resilient

The system should protect people, data, infrastructure, and public-interest reliance. That means safety controls, cybersecurity, prompt and tool/agent boundaries, privacy and data-governance controls, dependency maps, incident response, continuity planning, and exit paths where reliance is material.

### 4. Fair in practice

Where an AI system may materially affect people, rights, opportunities, or access to services, it should be tested and monitored for materially uneven or discriminatory performance across relevant groups, languages, regions, and contexts. Known limits should be disclosed, credible harm signals escalated, and harms mitigated, corrected, constrained, or withdrawn where necessary.

### 5. Open to evidence and correction

For material claims, recommendations, decisions, and risk-relevant system behavior, the system and its operators should preserve enough evidence for appropriate review: outputs, claims, sources where used, uncertainty signals, known limits, incidents, material changes, drift signals, complaints, corrections, withdrawals, and unresolved risks should be inspectable by responsible parties, triaged, and acted on proportionately.

## Risk Coverage

The obligations are designed against the biggest real-world risks named in the [risk and vulnerability audit](background/risk-and-vulnerability-audit.md): concentrated infrastructure and market power; coercive switch-off or manipulation; hallucination and misinformation; AI-app security failures; privacy and data leakage; bias and discrimination; harmful misuse; opaque consequential decisions; hidden lifecycle change; resource or global-access asymmetry; false or overbroad legal-compliance claims; and evidence theatre. The test is practical: a system should not be able to claim the Charter while hiding any of these risks from users, buyers, affected people, assessors, or lawful oversight. These five public obligations are backed by more detailed operational duties in the [Founding Accord](charter/founding-accord.md).

Pilot participants and future Trust Mark candidates or holders should only make public claims for a specific assessed system, version, and use-case. Before the claim, they should publish a privacy-preserving **release risk assessment** for that assessed release, and update it for assessor-reviewable material updates, material incidents, and active-deployment currentness checks. In Phase 1, reports may say only that a named release was evaluated under a named method, duty, or module, with a stated result; they may not claim Charter alignment, certification, or Trust Mark status. The public assessment should state what scope is covered, the legal-scope map, baseline scope, responsibility map, which modules are covered or not assessed, which material risk classes are addressed, what safe summary of measures exists, what evidence types support them, what remains unresolved, claim status, validity period, and what would trigger re-check or withdrawal. Pilot reports and future audits should label assurance depth: documented, evidence observed, implementation checked, effectiveness tested, or not assessed. Raw user data, secrets, exploit details, and legitimate confidential evidence stay protected.

## Regulation and Certification

State regulation matters because it creates enforceable rights, duties, supervisory powers, and sanctions. But AI regulation is not uniform internationally. A public buyer, media organisation, school, or user cannot rely on one shared legal baseline across jurisdictions.

That is where a future certification scheme could help, but only if it separates three layers:

1. **Provider-declared legal scope.** The provider declares the markets, role, use-case, risk category, domain rules, and required legal artefacts for the assessed release. The Charter does not replace regulators, notified bodies, courts, lawyers, domain certification, or legal advice, and it does not grant market-entry permission.
2. **Common Charter baseline.** The five public obligations become auditable operational duties that apply across jurisdictions. Where local law is stricter, local law prevails. Where local law is weaker or silent, the baseline still applies.
3. **Public-interest modules.** Deeper tests cover the Charter's distinctive concerns: factual grounding and correction, contestability and remedy, coercive-control transparency, AI-app security and abuse resistance, privacy and provenance, fairness, resource/public-access impacts, and creator or copyright fairness where relevant. Modules are optional only where the risk is not material to the assessed release; **not assessed** does not waive baseline duties.

Certification would not replace regulation, weaken legal duties, or certify legal compliance in every jurisdiction. Its job is narrower: make operational duties independently checkable and comparable, while preventing a narrow module or management-system certificate from looking like whole-system assurance.

## How Verification Would Work

A trustworthy mark, if created, cannot be self-declared. It needs separation of roles:

1. A standard-setter writes the rules and owns the mark.
2. Independent assessors audit systems against the rules.
3. An accreditor licenses and polices assessors.
4. A peer body keeps accreditors honest.

The current practical step is lighter: a published evaluation protocol, independent pilot assessments, public reports, and visible withdrawal when a system stops meeting the pilot scope or when a report is cited beyond what was assessed. Nothing in this repository certifies anyone yet. A mark, registry of certified systems, assessor accreditation, and formal revocation rules are Phase 2 work.

## Document Index

- **Program map:** [Program Map](PROGRAM.md) - how this normative framework relates to the public FactHarbor technical infrastructure.
- **Published manifesto article:** [Trustworthy AI, Accountable to People](https://www.linkedin.com/posts/robertschaub_a-world-where-ai-is-a-shared-trustworthy-activity-7471667943433646080-cIIE) - the LinkedIn manifesto, updated on LinkedIn 19 June 2026. The accountability and evaluation thread.
- **Published article (German):** [KI-Souveränität und Resilienz](manifesto/ki-souveraenitaet-und-resilienz.md) - the [published LinkedIn article](https://de.linkedin.com/pulse/ki-souver%C3%A4nit%C3%A4t-und-resilienz-den-schweizer-nutzen-um-robert-schaub-aohze) of 20 June 2026: the public-AI-sovereignty and governance thread of the same umbrella - a transparent governance layer and an international, capture-resistant host for a Swiss open-model effort.
- **Launch post:** [Launch post](manifesto/launch-post.md) - the accompanying LinkedIn feed post.
- **Published comment:** [Who would actually certify this?](manifesto/certification-comment.md) - the short answer: build the test, borrow the machinery.
- **Updated repository article:** [Trustworthy AI, Accountable to People](manifesto/trustworthy-ai-accountable-to-people.md) - the working version updated with the current baseline and audit framing.
- **Charter:** [The Founding Accord](charter/founding-accord.md) - user needs, values, five public obligations, the legal-floor/common-baseline/module assurance stack, and operational duties that structure pilot reports and may later form a certification baseline.
- **Protocol:** [Grounding-Faithfulness & Contestability](protocol/grounding-faithfulness-and-contestability.md) - the first draft method for checking claim support, uncertainty, correction, and contestability in factual AI systems.
- **Short version:** [One-page protocol](protocol/one-pager.md) - the same method in brief.
- **Certification model:** [How certification could work later](protocol/certification-model.md) - future-state assurance stack, separation of powers, accreditation, funding, and revocation.
- **Human-rights background:** [What the world has already declared](background/what-the-world-has-already-declared.md) - how UDHR, UNESCO, and the Council of Europe AI treaty map to the obligations.
- **Risk audit:** [Risk and vulnerability audit](background/risk-and-vulnerability-audit.md) - the real-world risk coverage test for the obligations.
- **Mechanism synthesis:** [From Manifesto to Mechanism](background/from-manifesto-to-mechanism.md) - historical synthesis retained for traceability.
- **Landscape & positioning:** [Landscape & positioning](background/landscape-and-positioning.md) - WIP context on adjacent efforts and differentiation.
- **Public AI governance pickup:** [Public AI infrastructure governance pickup](background/public-ai-infrastructure-governance-pickup.md) - WIP note on international co-stewardship, national contributions, and capture-resistant public AI infrastructure governance.

## How To Help

This is an open draft, not a finished standard.

1. **Break it.** Where does the method fail, overclaim, or invite gaming?
2. **Co-design the measurement.** Help set a defensible evaluation design for one use-case.
3. **Pilot it.** Volunteer a system for an exploratory trial evaluation. No mark is issued; the protocol is itself under review.
4. **Place it.** Help bring the method into an existing body instead of creating a new silo.

Open a GitHub issue for public feedback. For suspected secrets, private material, or personal data, contact [info@factharbor.ch](mailto:info@factharbor.ch) instead of opening a public issue.

Repository: [github.com/robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter)
