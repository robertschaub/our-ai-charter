---
title: Our AI Charter
permalink: /
---

> **Status: WORKING DRAFT** - public GitHub Pages entry point. The original manifesto is published; this repository version, the charter, protocol, and certification model are open drafts.

# Our AI Charter

**Trustworthy AI, accountable to people.**

AI is becoming infrastructure for how people learn, decide, work, and form public opinion. That infrastructure cannot be left to a few private providers, opaque shutdown powers, unsafe or insecure systems, discriminatory failures, privacy leakage, coercive manipulation, or material factual claims that cannot be traced or challenged.

Our AI Charter is a public-interest draft for making AI more trustworthy in practice: bounded by purpose, answerable to people, safe and private enough to rely on, fair in practice, and open to evidence and correction.

[Read the program map](PROGRAM.md) · [Read the article](AI%20Assurance%20and%20Certification/Published/trustworthy-ai-accountable-to-people.md) · [Read the Founding Accord](AI%20Assurance%20and%20Certification/founding-accord.md) · [Read the risk audit](AI%20Assurance%20and%20Certification/risk-and-vulnerability-audit.md) · [Read the evaluation protocol](AI%20Assurance%20and%20Certification/grounding-faithfulness-and-contestability.md) · [Read the certification model](AI%20Assurance%20and%20Certification/certification-model.md)

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

The obligations are designed against the biggest real-world risks named in the [risk and vulnerability audit](AI%20Assurance%20and%20Certification/risk-and-vulnerability-audit.md): concentrated infrastructure and market power; coercive switch-off or manipulation; hallucination and misinformation; AI-app security failures; privacy and data leakage; bias and discrimination; harmful misuse; opaque consequential decisions; hidden lifecycle change; resource or global-access asymmetry; false or overbroad legal-compliance claims; and evidence theatre. The test is practical: a system should not be able to claim the Charter while hiding any of these risks from users, buyers, affected people, assessors, or lawful oversight. These five public obligations are backed by more detailed operational duties in the [Founding Accord](AI%20Assurance%20and%20Certification/founding-accord.md).

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

For now the work is lighter and earlier-stage: a published evaluation protocol and the drafts, method, and connections around it. Independent pilot assessments and public reports — with visible withdrawal when a system stops meeting the assessed scope or a report is cited beyond it — are a possible next step, not yet underway or planned. Nothing in this repository certifies anyone yet. A mark, registry of certified systems, assessor accreditation, and formal revocation rules are Phase 2 work.

## Documents

The full, current document index — both workstreams, with status labels — lives in the **[repository README](https://github.com/robertschaub/our-ai-charter#two-workstreams)**. Start points:

**Program map:** [PROGRAM.md](PROGRAM.md) — where this normative framework sits within a broader program for responsible technology in society.

**Public AI Network** — sovereignty, resilience, coordination:
- [The Public AI Network](Public%20AI%20Network/Published/the-public-ai-network.md) · [KI-Souveränität und Resilienz](Public%20AI%20Network/Published/ki-souveraenitaet-und-resilienz.md) — *PUBLISHED* LinkedIn articles.
- [Public AI governance — initiative briefing](Public%20AI%20Network/briefing.md) — a good entry point to the Swiss public-AI governance working materials.

**AI Assurance & Certification** — accountability, evaluation, certification:
- [Trustworthy AI, Accountable to People](AI%20Assurance%20and%20Certification/Published/trustworthy-ai-accountable-to-people.md) — *PUBLISHED* manifesto.
- [The Founding Accord](AI%20Assurance%20and%20Certification/founding-accord.md) · [evaluation protocol](AI%20Assurance%20and%20Certification/grounding-faithfulness-and-contestability.md) · [how certification could work later](AI%20Assurance%20and%20Certification/certification-model.md).

## How To Help

This is an open draft, not a finished standard.

1. **Break it.** Where does the method fail, overclaim, or invite gaming?
2. **Co-design the measurement.** Help set a defensible evaluation design for one use-case.
3. **Pilot it.** Volunteer a system for an exploratory trial evaluation. No mark is issued; the protocol is itself under review.
4. **Place it.** Help bring the method into an existing body instead of creating a new silo.

Open a GitHub issue for public feedback. For suspected secrets, private material, or personal data, contact [info@factharbor.ch](mailto:info@factharbor.ch) instead of opening a public issue.

Repository: [github.com/robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter)
