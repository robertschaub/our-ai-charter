> **Status: DRAFT** — explainer accompanying the protocol.

# How could "trustworthy AI" be certified? — an assurance-stack model

_Companion to the "Trustworthy AI, Accountable to People" manifesto, for the first question every expert asks: "Who certifies? Who's the authority?" Draft updated 2026-06-25. Grounded in how certification works in other industries._

This is a **future-state model**, not a scheme that exists today, and the phased steps below are proposals — not work that is underway or scheduled. No pilot evaluations have been run; there is no Trust Mark, certificate, accredited assessor, or certification body. The current work is drafting and building connections.

## Short answer: no single authority — and that's the design.

Credible certification never rests on one anointed body's say-so. It rests on a **separation of powers**, so no one can mark their own homework. That structure — not a central authority with a kill-switch — is what makes a mark trustworthy. So the honest answer to "who appointed you?" is: *no one did. That's the point.*

## The model every mature scheme uses — four separated roles

1. **Standard-setter** — writes the rules. *(ISO/IEC; FSC; Fairtrade International; the IFCN Code of Principles.)*
2. **Certifier / audit body** — audits a system against the standard; independent of the audited party. *(FLOCERT for Fairtrade; IFCN's region-matched external assessors.)*
3. **Accreditor** — accredits and polices the certifiers; can suspend them. *(National accreditation bodies; IOAS, which both accredits and suspends organic certifiers.)*
4. **Peer-review of accreditors** — keeps accreditors honest and mutually recognised worldwide. *(The IAF, peer-evaluating accreditation bodies against ISO/IEC 17011.)*

"Who checks the checkers?" → the accreditor. "Who checks them?" → peer review. That chain is why a label can be trusted **without anyone holding absolute power over it.**

## For AI, this is already emerging — and it's thin

The EU AI Act includes **"notified bodies"** — independent third parties designated by member states — for some high-risk-AI conformity assessments. Article 43 is category-specific: many Annex III high-risk systems use internal-control conformity assessment without a notified body, while biometrics and product-law systems can require or involve third-party assessment in specified cases. General-purpose AI providers have separate documentation, copyright-policy, training-summary, systemic-risk, incident-reporting, and cybersecurity obligations. Transparency rules also create duties around AI involvement, generated-content marking or labelling, and related user-facing disclosures where relevant. The structure exists in law, but it does not create a single international information-integrity baseline for every AI system a buyer or user may rely on.

## The assurance stack: provider-declared legal scope, common baseline, public-interest modules

State regulation sets enforceable duties, rights, supervisory powers, and sanctions inside each jurisdiction. The EU AI Act is one such legal floor for systems, roles, and markets within its scope. But legal floors are not uniform internationally. A voluntary mark cannot replace law, weaken it, or certify legal compliance across every jurisdiction.

Certification would be useful for a different job if it is structured as a three-layer assurance stack:

1. **Provider-declared legal scope (the legal floor).** The assessed release declares its markets, role in the value chain, use-case, risk category, domain regimes, and required legal artefacts. The Charter complements legal regimes by making scope, evidence, limitations, and public-interest modules inspectable; it does not certify legal compliance, provide legal advice, replace a notified body, override a regulator, or grant market-entry permission. The evaluator or future assessor checks that the public claim is limited to the declared scope and records missing, disputed, or out-of-scope legal artefacts as limitations. Regulators, courts, notified bodies, domain certification bodies, and the provider's own legal assessment decide legal compliance.
2. **Common Charter baseline.** The five public obligations become operational duties that can be checked consistently across jurisdictions. Stricter local law prevails; weaker or silent local law does not lower the baseline.
3. **Public-interest modules.** Additional modules test the Charter's distinctive concerns beyond ordinary compliance — factual grounding, contestability, coercive-control transparency, AI-app security, privacy and provenance, fairness, resource and public-access impacts, and the other public-interest module candidates set out in the [Founding Accord](founding-accord.md). Modules are optional only where the risk is not material to the assessed release. A module marked **not assessed** does not waive baseline duties, and a full Charter alignment claim cannot omit material modules.

A builder or deployer could then say, "we have declared the legal scope for this assessed release, we accept the common Charter baseline, and an independent assessor can test which modules we meet in operation."

This avoids three common traps: pretending a voluntary mark is legal approval, treating a management-system certificate as product assurance, or using a narrow factuality test as if it covered the whole risk surface.

For this charter, the auditable evidence should answer — as testable evidence, not just disclosure — the six practical questions the [Founding Accord](founding-accord.md) frames in full:

- **What is it for?** — assessed version, intended/prohibited uses, affected groups, limits, risk context.
- **Who controls it?** — operator, models, data, tools, dependencies, and any update, restriction, or shutdown power.
- **Who is accountable?** — the named owner, jurisdiction, and support route that answers for it.
- **How can people challenge it?** — notice, error-flagging, appeal of consequential decisions, and remedy.
- **Who can inspect it?** — what is public, what assessors see confidentially, and what lawful oversight can require.
- **Can its claims and failures be checked?** — claims, incidents, disparate failures, and corrections traceable to evidence.

A future baseline must not become a narrow "factuality badge" that ignores the rest of the real risk surface. At minimum, the common baseline needs to make the risks in the [Risk and Vulnerability Audit](../Background/risk-and-vulnerability-audit.md) inspectable: concentration and lock-in, coercive control, factual unreliability, AI-app security, privacy and provenance, bias and discrimination, harmful misuse, opaque consequential decisions, lifecycle drift, resource/global-access asymmetry, false legal-compliance claims, and evidence theatre.

That means an audit should not merely test outputs. It should require a documented **risk and vulnerability register** and a privacy-preserving **release risk assessment**, published before a public claim and kept current for the release — its required fields and the assurance-depth labels (documented, evidence observed, implementation checked, effectiveness tested, or not assessed) are defined in the [Founding Accord](founding-accord.md) (operational duty 3). The audit checks that the public assessment covers the required risk areas, matches the confidential evidence pack, and keeps protected evidence — raw user data, secrets, exploit details — out of the public summary.

ISO/IEC 42001 is useful here as a management-system reference because it requires a living system for AI governance and risk management. ISO/IEC 42005 is useful for impact assessment. ISO/IEC 42006 is useful because it sets expectations for bodies auditing and certifying AI management systems. None of those, by itself, proves that a specific public release's factual claims are grounded, that affected people can challenge harms, or that coercive control interventions are reviewable. Those are Charter module questions.

## The practical proposal — lean, phased, not a mega-authority

- **Phase 1 (the proposed first step, not yet underway):** a published method, then — if it proceeds — independent pilot evaluators, public evaluation reports, and a public report index. No mark, certificate, accredited assessor, or certification claim. Today only the method and drafts exist.
- **Phase 2 only if demand appears:** a small standard steward, hosted in or accountable to an existing neutral body, maintains the standard, mark rules, and **public registry** — and audits no one itself. Capture-resistant governance: multi-stakeholder board, capped influence for those bound by or helping write the rules, and two-assessor plus academic re-evaluation for contested cases. *(Models: IFCN/Poynter, GOTS, Creative Commons.)*
- **Independent accredited assessors** (ML + domain + regional expertise) would do the audits — independent of both vendor and steward.
- **Ride the accreditation infrastructure that already exists** (ISO/IEC 17065 + national accreditation bodies + IAF) instead of reinventing "who checks the auditors," once the scheme is mature enough to justify it.
- **Inclusion built in:** tiered (free self-assessment → audited mark), hardship waivers, a solidarity fund — so small and Global-South builders aren't priced out.
- **Funding diversified** — never dominated by logo/audit fees (the conflict that has eroded some eco-labels).
- **Teeth from demand, not a police force:** procurement preference, platform requirements, and alignment with legal duties where applicable. In Phase 1, a buyer can require the evidence baseline; in Phase 2, it could require the mark. *(In web security, browsers enforce trust by distrusting bad certificate authorities — the demand side is the enforcer.)*

## How it resists authoritarian switch-off or manipulation

No voluntary mark can stop a state, court, platform, or infrastructure provider from exercising power. The certification job is narrower and practical: make material control powers visible before reliance, require logs for restrictions and shutdowns, require lawful-basis and scope records, require review routes where available, and require continuity or exit planning for public-interest use. A system should not be able to claim the Charter while hiding who can bend it, silence it, or withdraw it. If a material control intervention cannot be disclosed publicly and cannot be independently reviewed under confidentiality or lawful oversight, the affected scope should lose the pilot listing or future mark claim.

## Who could drive this?

Certification schemes are rarely founded as standalone authorities — they're **convened by a credible initiator and incubated inside or beside a neutral host:**
- **A mission-driven NGO stewards it** — Reporters Without Borders drove the Journalism Trust Initiative; Poynter runs the IFCN code; Fairtrade International and FSC are dedicated nonprofits.
- **A neutral host incubates it** — the Linux Foundation hosts OpenSSF and open-model work; OASIS hosts the Coalition for Secure AI; CEN hosted JTI's standard. A host gives legal shelter and instant neutrality without founding a new institution.
- **A multi-stakeholder coalition runs it** — the CA/Browser Forum (browsers + certificate authorities); the AI Alliance; the Digital Public Goods Alliance.
- **A public anchor can lend context or convening legitimacy** — UNESCO, the Council of Europe, or relevant EU assurance structures, without implying endorsement, legal approval, or that the Charter certifies legal compliance.

**Realistic model here:** *you convene; you don't run an audit empire.* The initiator is the founder + early manifesto signatories as a small founding coalition. Treat the host question as a two-track outreach hypothesis, not a settled decision: journalism and fact-checking bodies such as RSF/JTI, IFCN/Poynter, or EFCSN can supply information-integrity legitimacy and process analogues; neutral open-standards or open-source hosts such as OASIS, the Linux Foundation, a CEN-style workshop route, or the Digital Public Goods Alliance can supply stewardship infrastructure depending on scope. Substance should be anchored with measurement and public-interest AI partners such as MLCommons, the AI Alliance, and Current AI. The verified analogues are mixed: RSF convened JTI and CEN published it as CWA 17493; Poynter hosts IFCN; the Linux Foundation consolidated existing open-source-security efforts into OpenSSF; and OASIS hosts CoSAI. They support the pattern, but they are not one template.

Where the Charter is applied to public AI infrastructure, legal form is secondary to stewardship. A credible host or steward should let partners inspect evidence, challenge claims, participate in governance, and support the work only under disclosed, capped, conflict-managed funding rules. Model operation, standard-setting, evaluation, accreditation, and funding decisions should be institutionally separate or strongly firewalled; the steward maintains the standard and registry, but does not audit or operate the infrastructure itself.

## How would it be financed?

The one rule from every scheme: **diversify — never let one stream dominate.** Single-source funding is capture: the Marine Stewardship Council draws most of its revenue from logo licensing (a structural incentive to over-certify), and fact-checking's reliance on a few platform funders nearly collapsed when Meta exited its program in 2025.

The working mix:
- **Public-interest seed funding** to bootstrap (Germany's Sovereign Tech Fund; the EU/UNESCO-backed Journalism Trust Initiative).
- **Tiered, capped fees** that can't crowd out the rest (ISO certification, B Corp).
- **Cross-subsidy, hardship waivers, and a solidarity fund** so small and Global-South builders aren't priced out (Fairtrade; IFCN waivers down to $0).
- **Diversified, durable revenue** — the Wikimedia mix of many small donors, an endowment, and enterprise income.

**Firewall:** funders disclosed; no funder sets the criteria; the steward's budget is independent of any audited party's fees. Grant funding carries the cheap early phase; the costly accreditation layer arrives only with Phase 2 demand (see *The practical proposal* above).

_(Funding figures here are illustrative — verify before citing; they shift year to year.)_

## What it is deliberately NOT

- Not a new central authority that "owns" trustworthy AI.
- Not self-certification (the thing that discredits weak schemes).
- Not pay-to-pass — assessor independence and accreditation are non-negotiable.
- Not legal approval — the Charter can require a legal-scope map, but regulators, notified bodies, courts, and domain laws still decide legal compliance.
- Not finished — a model to build and contest, not a body that exists today.

## The honest part

Standing up the full pyramid is hard and slow — which is exactly why Phase 1 matters. And the deepest legitimacy question answers itself: authority here is **manufactured by structure and transparency** (independent layers, public registry, revocation history), not granted to anyone.

---
_Sources: ISO/IEC 17065; ISO/IEC 42001, ISO/IEC 42005, and ISO/IEC 42006; the IAF (International Accreditation Forum); [EU AI Act Art. 43](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-43) (conformity assessment and notified-body routes), [Art. 53](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) (GPAI provider obligations), and [Art. 55](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-55) (GPAI systemic-risk obligations); and certification, standards, and public-interest analogues including Fairtrade/FLOCERT, GOTS/IOAS, [IFCN/Poynter](https://ifcncodeofprinciples.poynter.org/about), [EFCSN](https://efcsn.com/code-of-standards/), [JTI](https://journalismtrustinitiative.org/jti-the-standard/) and [CWA 17493](https://www.cencenelec.eu/media/CEN-CENELEC/CWAs/ICT/cwa17493.pdf), [OpenSSF/Linux Foundation](https://www.linuxfoundation.org/blog/blog/open-source-security-foundation-openssf-reflection-and-future), [OASIS/CoSAI](https://www.oasis-open.org/2024/07/18/introducing-cosai/), [DPGA](https://www.digitalpublicgoods.net/standard), [MLCommons AILuminate](https://mlcommons.org/benchmarks/ailuminate/), [AI Alliance Trusted Evals](https://thealliance.ai/core-projects/trusted-evals), and [Current AI](https://www.currentai.org/)._
