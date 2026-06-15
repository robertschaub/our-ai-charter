> **Status: WORKING DRAFT** — explainer accompanying the protocol.

# How could "trustworthy AI" be certified? — a one-page model

_Companion to the "Trustworthy AI, Accountable to People" manifesto, for the first question every expert asks: "Who certifies? Who's the authority?" Draft 2026-06-13. Grounded in how certification works in other industries._

This is a **future-state model**, not a scheme that exists today. The current phase is pilot evaluation reports only: no Trust Mark, no certificate, no accredited assessor, and no certification body.

## Short answer: no single authority — and that's the design.

Credible certification never rests on one anointed body's say-so. It rests on a **separation of powers**, so no one can mark their own homework. That structure — not a central authority with a kill-switch — is what makes a mark trustworthy. So the honest answer to "who appointed you?" is: *no one did. That's the point.*

## The model every mature scheme uses — four separated roles

1. **Standard-setter** — writes the rules. *(ISO/IEC; FSC; Fairtrade International; the IFCN Code of Principles.)*
2. **Certifier / audit body** — audits a system against the standard; independent of the audited party. *(FLOCERT for Fairtrade; IFCN's region-matched external assessors.)*
3. **Accreditor** — accredits and polices the certifiers; can suspend them. *(National accreditation bodies; IOAS, which both accredits and suspends organic certifiers.)*
4. **Peer-review of accreditors** — keeps accreditors honest and mutually recognised worldwide. *(The IAF, peer-evaluating accreditation bodies against ISO/IEC 17011.)*

"Who checks the checkers?" → the accreditor. "Who checks them?" → peer review. That chain is why a label can be trusted **without anyone holding absolute power over it.**

## For AI, this is already emerging — and it's thin

The EU AI Act includes **"notified bodies"** — independent third parties designated by member states — for some high-risk-AI conformity assessments. Article 43 is category-specific: many Annex III high-risk systems use internal-control conformity assessment without a notified body, while biometrics and product-law systems can require or involve third-party assessment in specified cases. The structure exists in law, but it does not create a single international information-integrity baseline for every AI system a buyer or user may rely on.

## The split: enforceable law vs common certification baseline

State regulation sets enforceable duties, rights, supervisory powers, and sanctions inside each jurisdiction. But those legal floors are not uniform internationally. A voluntary mark cannot replace law, weaken it, or certify legal compliance across every jurisdiction.

Certification would be useful for a different job. A future **common certification baseline** would be the minimum set of operational commitments any system carrying the Charter mark must meet, regardless of jurisdiction. Stricter local law prevails; weaker or silent local law does not lower the baseline. A builder or deployer could say, "we accept this international baseline, and an independent assessor can test whether we meet it in operation."

For this charter, the auditable evidence should track the practical questions users, buyers, researchers, media, and authorities need answered:

- **What is this system for?** Which system, version, intended uses, prohibited uses, foreseeable misuse, affected groups, limits, and risk context are being assessed?
- **Who controls it?** Who operates the system, controls models, data, tools, APIs, retrieval, cloud/compute dependencies, updates, restrictions, recalls, shutdowns, and material external orders where disclosure is lawful?
- **Who is accountable?** Which owner answers for this deployment, jurisdiction, support route, public claims, safety, security, privacy, discrimination, misuse, and incident handling?
- **How can people challenge it?** Can affected people get notice, flag errors or harms, appeal consequential decisions, challenge data use, discrimination, or restrictions where legally possible, and obtain a meaningful outcome?
- **Who can inspect it?** What is public, what can qualified assessors inspect confidentially, what can lawful oversight require, and what protected research is possible for red-team evidence, security tests, privacy controls, data provenance, and model/data-change records?
- **Can its claims and failures be checked?** Can factual claims, consequential decisions, external restriction decisions, security/privacy/misuse incidents, disparate failure rates, significant changes, withdrawals, corrections, and exit paths be traced to evidence and tested?

A future baseline must not become a narrow "factuality badge" that ignores the rest of the real risk surface. At minimum, the common baseline needs to make the risks in the [Risk and Vulnerability Audit](../background/risk-and-vulnerability-audit.md) inspectable: concentration and lock-in, coercive control, factual unreliability, AI-app security, privacy and provenance, bias and discrimination, harmful misuse, opaque consequential decisions, lifecycle drift, and resource/global-access asymmetry.

That means an audit should not merely test outputs. It should require a documented **risk and vulnerability register** for the assessed system: identified material risks, mitigations, monitoring, accountable owners, unresolved findings, incident triggers, and re-assessment triggers. The public report should summarise that register in safe form: what was assessed, which risks were in scope, what evidence was checked, what remains unresolved, and what would cause withdrawal or re-check. Raw user data, secrets, exploit details, and legitimate confidential evidence stay protected.

## The practical proposal — lean, phased, not a mega-authority

- **Phase 1 now:** a published method, independent pilot evaluators, public evaluation reports, and a public report index. No mark, certificate, accredited assessor, or certification claim.
- **Phase 2 only if demand appears:** a small standard-steward (a nonprofit "Trust Council," working name) owns the standard, the mark, and a **public registry** — and audits no one itself. Capture-resistant governance: multi-stakeholder board, capped influence, those-bound-help-write-the-rules, two-assessor + academic re-evaluation for contested cases. *(Models: IFCN/Poynter, GOTS, Creative Commons.)*
- **Independent accredited assessors** (ML + domain + regional expertise) would do the audits — independent of both vendor and steward.
- **Ride the accreditation infrastructure that already exists** (ISO/IEC 17065 + national accreditation bodies + IAF) instead of reinventing "who checks the auditors," once the scheme is mature enough to justify it.
- **Inclusion built in:** tiered (free self-assessment → audited mark), hardship waivers, a solidarity fund — so small and Global-South builders aren't priced out.
- **Funding diversified** — never dominated by logo/audit fees (the conflict that has eroded some eco-labels).
- **Teeth from demand, not a police force:** procurement preference, platform requirements, and alignment with legal duties where applicable. In Phase 1, a buyer can require the evidence baseline; in Phase 2, it could require the mark. *(In web security, browsers enforce trust by distrusting bad certificate authorities — the demand side is the enforcer.)*

## How it resists authoritarian switch-off or manipulation

No voluntary mark can stop a state, court, platform, or infrastructure provider from exercising power. The certification job is narrower and practical: make material control powers visible before reliance, require logs for restrictions and shutdowns, require lawful-basis and scope records, require review routes where available, and require continuity or exit planning for public-interest use. A system should not be able to claim the Charter while hiding who can bend it, silence it, or withdraw it.

## Who could drive this?

Certification schemes are rarely founded as standalone authorities — they're **convened by a credible initiator and incubated inside or beside a neutral host:**
- **A mission-driven NGO stewards it** — Reporters Without Borders drove the Journalism Trust Initiative; Poynter runs the IFCN code; Fairtrade International and FSC are dedicated nonprofits.
- **A neutral host incubates it** — the Linux Foundation hosts OpenSSF and open-model work; OASIS hosts the Coalition for Secure AI; CEN hosted JTI's standard. A host gives legal shelter and instant neutrality without founding a new institution.
- **A multi-stakeholder coalition runs it** — the CA/Browser Forum (browsers + certificate authorities); the AI Alliance; the Digital Public Goods Alliance.
- **A public anchor lends authority** — UNESCO, the Council of Europe, or relevant EU assurance structures, without implying that the Charter certifies legal compliance.

**Realistic model here:** *you convene; you don't run an audit empire.* The initiator is the founder + the early manifesto signatories (a small founding coalition); the standard is **hosted inside an existing neutral body** — strongest candidates given the information-integrity angle: a journalism-trust body (IFCN/EFCSN), a neutral standards/tech host (Linux Foundation, OASIS, CEN), or the Digital Public Goods Alliance — with anchor partners for substance (MLCommons for evaluation, the AI Alliance, Current AI). That's how JTI, IFCN, OpenSSF and CoSAI all started.

## How would it be financed?

The one rule from every scheme: **diversify — never let one stream dominate.**
- **Cautionary tales:** the Marine Stewardship Council earns the large majority of its revenue from logo licensing — a structural incentive to over-certify; and fact-checking's dependence on a few platform funders nearly collapsed when Meta exited its program in 2025. Single-source funding = capture.
- **The working mix:**
  - **Public-interest seed funding** to bootstrap — Germany's Sovereign Tech Fund (open infrastructure), the EU/UNESCO backing of the Journalism Trust Initiative, the Current AI foundation (public-interest, launched at the Paris summit).
  - **Tiered fees, capped** so they never dominate (ISO certification, B Corp).
  - **Cross-subsidy + hardship waivers + a solidarity fund** for inclusion — Fairtrade (large traders subsidise small producers), IFCN's fee waivers down to $0, the Montreal Protocol's Multilateral Fund (wealthier nations finance poorer ones' compliance).
  - **Diversified sustainability** — the Wikimedia mix (many small donors + an endowment + enterprise revenue), so no single patron holds the leash.
- **Firewall:** funders disclosed; no funder sets the criteria; the steward's budget is independent of any audited party's fees.
- **Phasing keeps it cheap early:** Phase 1 (a code + independent pilot evaluators + public reports) is grant-fundable; the costly accreditation pyramid comes only at Phase 2 — paid for by the mix once demand exists.
- **Demand funds it:** in Phase 1, procurement and platforms can require the evidence baseline; in Phase 2, if a mark exists, audit demand and the fee base can grow naturally.

_(Funding figures across these examples are illustrative — verify before citing; they shift year to year.)_

## How it would start — phased

- **Phase 1 (now):** a published code of obligations + independent pilot evaluators + public reports + visible withdrawal of pilot status. Cheap, credible, and honest about not being certification yet.
- **Phase 2 (at scale):** graduate to the full ISO/IEC-17065 + accreditation pyramid for hard, globally-recognised legitimacy.

## What it is deliberately NOT

- Not a new central authority that "owns" trustworthy AI.
- Not self-certification (the thing that discredits weak schemes).
- Not pay-to-pass — assessor independence and accreditation are non-negotiable.
- Not finished — a model to build and contest, not a body that exists today.

## The honest part

Standing up the full pyramid is hard and slow — which is exactly why Phase 1 matters. And the deepest legitimacy question answers itself: authority here is **manufactured by structure and transparency** (independent layers, public registry, revocation history), not granted to anyone.

---
_Sources: ISO/IEC 17065; the IAF (International Accreditation Forum); [EU AI Act Art. 43](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-43) (conformity assessment and notified-body routes); and certification analogues — Fairtrade/FLOCERT, GOTS/IOAS, IFCN, the Journalism Trust Initiative._
