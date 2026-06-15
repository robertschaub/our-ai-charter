---
title: Our AI Charter
permalink: /
---

> **Status: WORKING DRAFT** - public GitHub Pages entry point. The original manifesto is published; this repository version, the charter, protocol, and certification model are open drafts.

# Our AI Charter

**Trustworthy AI, accountable to people.**

AI is becoming infrastructure for how people learn, decide, work, and form public opinion. That infrastructure cannot be left to a few private providers, opaque shutdown powers, coercive manipulation, or systems whose factual claims cannot be checked.

Our AI Charter is a public-interest draft for making AI more trustworthy in practice: resilient enough that public-interest uses are not captive to one unreviewable provider, accountable enough that significant power and data use can be challenged, and corrigible enough that factual claims, safety controls, incidents, failures, and corrections can be tested and acted on.

[Read the updated article](manifesto/trustworthy-ai-accountable-to-people.md) · [Read the Founding Accord](charter/founding-accord.md) · [Read the evaluation protocol](protocol/grounding-faithfulness-and-contestability.md)

## The Practical Demand

People who use, buy, study, regulate, or are affected by AI need more than promises. Public authorities, customers, media, researchers, and civil society should be able to demand answers to six questions:

1. **What is this system for?** Intended uses, prohibited uses, misuse boundaries, covered versions, limits, affected groups, and risk context must be stated before trust is claimed.
2. **Who controls it?** Operators, critical providers, models, data, tools, cloud/compute dependencies, update powers, restriction powers, shutdown powers, and external orders or pressure to use them must be named and logged where lawful.
3. **Who is accountable?** Each deployment needs an accountable owner, jurisdiction, contact route, and retained evidence for public claims, safety, security, privacy, fairness, and misuse handling.
4. **How can people challenge it?** Affected people need notice, a usable complaint route, response times, human review for consequential uses, and records of outcomes, including data-use, discrimination, restriction, or shutdown decisions where challenge is legally possible.
5. **Who can inspect it?** Public transparency, confidential audit access, lawful regulator access, protected research access, red-team evidence, security testing, privacy controls, and data provenance must be distinguished and scoped.
6. **Can its claims and failures be checked?** Factual claims, consequential decisions, restriction orders, security/privacy/misuse incidents, disparate failure rates, corrections, significant changes, withdrawals, and exit paths must leave testable evidence.

These questions turn the published manifesto into a concrete charter and the first auditable modules.

## Three Obligations

### 1. Resilient and non-captive

Public-interest AI deployments should not leave people trapped behind one unreviewable provider, hidden dependency, fragile supply chain, resource bottleneck, or unilateral withdrawal. Where public reliance matters, users and buyers need credible continuity and exit options, and clear warning where those options do not exist.

### 2. Accountable and challengeable

Control is necessary. Unaccountable power is not. Significant power over systems, data, safety, security, privacy, access, or people should be attributable, proportionate, reviewable, and open to challenge when it causes harm or is used without a defensible basis.

This is where protection against authoritarian switch-off orders or manipulation belongs. The Charter cannot promise that a system will ignore lawful emergency, court, or regulator orders. It can demand that material restrictions, recalls, shutdowns, and control interventions are scoped, attributable, logged, time-limited where possible, reviewable through lawful channels, and visible to users, buyers, assessors, or oversight bodies unless disclosure is lawfully restricted. Where public reliance is material, there must also be continuity and exit planning.

### 3. Checkable and corrigible

Systems that make factual or consequential claims should not ask to be trusted on authority. Their claims, limits, safety and security controls, incidents, bias and failure rates, material changes, and corrections should be open to challenge and acted on when they are wrong.

## Risk Coverage

The obligations are designed against the biggest real-world risks named in the [risk and vulnerability audit](background/risk-and-vulnerability-audit.md): concentrated infrastructure and market power; coercive switch-off or manipulation; hallucination and misinformation; AI-app security failures; privacy and data leakage; bias and discrimination; harmful misuse; opaque consequential decisions; hidden lifecycle change; and resource or global-access asymmetry. The test is practical: a system should not be able to claim the Charter while hiding any of these risks from users, buyers, affected people, assessors, or lawful oversight.

Any provider claiming alignment with the Charter should publish a privacy-preserving **risk-measures report at least yearly** for each assessed system: what scope is covered, which risks are addressed, what measures are in place, what evidence exists, what remains unresolved, and what would trigger re-check or withdrawal. Pilot reports and future audits should verify that this public reporting exists, is current, and matches the confidential evidence pack. Raw user data, secrets, exploit details, and legitimate confidential evidence stay protected.

## Regulation and Certification

State regulation matters because it creates enforceable rights, duties, supervisory powers, and sanctions. But AI regulation is not uniform internationally. A public buyer, media organisation, school, or user cannot rely on one shared legal baseline across jurisdictions.

That is where a future certification scheme could help. A credible mark would define a **common certification baseline** for any model or deployed system that wants to claim the Charter publicly. Where local law is stricter, local law prevails. Where local law is weaker or silent, the baseline still applies. Higher tiers or modules can add stronger commitments.

Certification would not replace regulation, weaken legal duties, or certify legal compliance in every jurisdiction. Its job is narrower: make operational commitments independently checkable and comparable.

## How Verification Would Work

A trustworthy mark, if created, cannot be self-declared. It needs separation of roles:

1. A standard-setter writes the rules and owns the mark.
2. Independent assessors audit systems against the rules.
3. An accreditor licenses and polices assessors.
4. A peer body keeps accreditors honest.

The current practical step is lighter: a published evaluation protocol, independent pilot assessments, public reports, and visible withdrawal when a system stops meeting the pilot scope. Nothing in this repository certifies anyone yet. A mark, registry of certified systems, assessor accreditation, and formal revocation rules are Phase 2 work.

## Current Drafts

- **Original published article:** [Trustworthy AI, Accountable to People](https://www.linkedin.com/posts/robertschaub_a-world-where-ai-is-a-shared-trustworthy-activity-7471667943433646080-cIIE) - the LinkedIn manifesto and starting point.
- **Published comment:** [Who would actually certify this?](manifesto/certification-comment.md) - the short answer: build the test, borrow the machinery.
- **Updated repository article:** [Trustworthy AI, Accountable to People](manifesto/trustworthy-ai-accountable-to-people.md) - the working version updated with the current baseline and audit framing.
- **Charter:** [The Founding Accord](charter/founding-accord.md) - user needs, values, a future certification baseline, and voluntary higher commitments.
- **Protocol:** [Grounding-Faithfulness & Contestability](protocol/grounding-faithfulness-and-contestability.md) - the first draft method for checking claim support, uncertainty, correction, and contestability in factual AI systems.
- **Short version:** [One-page protocol](protocol/one-pager.md) - the same method in brief.
- **Certification model:** [How certification could work later](protocol/certification-model.md) - future-state separation of powers, accreditation, funding, and revocation.
- **Human-rights background:** [What the world has already declared](background/what-the-world-has-already-declared.md) - how UDHR, UNESCO, and the Council of Europe AI treaty map to the obligations.
- **Risk audit:** [Risk and vulnerability audit](background/risk-and-vulnerability-audit.md) - the real-world risk coverage test for the obligations.

## How To Help

This is an open draft, not a finished standard.

1. **Break it.** Where does the method fail, overclaim, or invite gaming?
2. **Co-design the measurement.** Help set a defensible evaluation design for one use-case.
3. **Pilot it.** Volunteer a system for an exploratory trial evaluation. No mark is issued; the protocol is itself under review.
4. **Place it.** Help bring the method into an existing body instead of creating a new silo.

Open a GitHub issue for public feedback. For suspected secrets, private material, or personal data, contact [info@factharbor.ch](mailto:info@factharbor.ch) instead of opening a public issue.

Repository: [github.com/robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter)
