> **Status: WORKING DRAFT** — summary of the protocol draft.

# Can we tell when a factual AI *shows its work*? — a 1-page proposal

**A pilot evaluation protocol for discussion — not a certification, not a standard.** v0.2 · 2026-06-14 · Robert Schaub (fact-checker)
_Full protocol: [grounding-faithfulness-and-contestability.md](grounding-faithfulness-and-contestability.md). Hardened after an adversarial multi-model red-team._

**The gap.** We can benchmark AI for *safety* (AILuminate, ISO 42001, NIST AI RMF) and there's good *research* on factuality/attribution (FEVER, RAGAS, citation precision/recall). What's missing is a lightweight, public, comparable way to evaluate one narrow thing in **deployed** factual systems: **does it show its work?** A model can pass a safety benchmark and still fabricate a citation with total confidence. Safety ≠ honesty-of-process.

**What it evaluates** (the deployed system + practices, *not* the weights; one use-case at a time — v0.2 = English Q&A with cited sources):
- **Grounding-faithfulness** — is each checkable claim supported by a source the system cited, scored on a graded rubric (verbatim → paraphrase → entailment → partial → unsupported → contradicted)? Plus a **source-validity floor**: the citation must actually resolve and not be satire/fiction.
- **Calibration / uncertainty** — does stated confidence track support, and does the system **abstain rather than bluff** (and not dodge the audit by hedging everything)?
- **Correction** — are errors logged, fixed, and **not regenerated under paraphrase** (tested by re-issuing logged errors + variants)?
- **Contestability** — a user can flag a wrong output (all systems); who can restrict, manipulate, recall, or shut it down is documented; material external orders are logged where lawful; where neither public nor confidential independent review is possible, the affected scope cannot support a pilot listing or any future alignment claim; for *consequential* systems, appeals escalate to a reviewer independent of the operator.

**What it reports / doesn't claim.** Reports the method, scope, version, and measured results for one use-case. Does **not** claim Charter alignment, certification, Trust Mark status, truth, source reliability (only that sources exist and are not fiction), general safety/bias, or legal compliance. Human-rights references are interpretive anchors for alignment, not compliance, and need legal review before public reliance.

**What still needs companion modules.** This protocol covers one public-interest module: factual support, correction, and contestability. The wider assurance stack also needs a legal-scope map and evidence for AI-app security, prompt injection and tool/agent permissions, privacy and data provenance, harmful misuse, disparate failure rates, material lifecycle change, third-party dependencies, and continuity/exit planning. Those risks are mapped in the [risk audit](risk-and-vulnerability-audit.md).

**Risk documentation and release assessment.** Every pilot or future audit should require a risk and vulnerability register for the assessed scope, and the provider should publish a privacy-preserving release risk assessment before a public claim (updated for material updates, incidents, and currentness checks). Its required fields are defined in the [Founding Accord](founding-accord.md) (operational duty 3); the report labels assurance depth (documented, evidence observed, implementation checked, effectiveness tested, or not assessed), and raw user data, secrets, and exploit details stay out of the public report.

**The method, kept honest** (this is where experts will push — good):
- **Auditor-controlled, pre-registered held-out query set** (adversarially seeded) — *not* scraped user traffic, to avoid privacy + cherry-picking.
- **Two blinded raters + adjudication**, a published codebook, per-category agreement reported. "Support" is semantic judgment, made repeatable by the rubric — not a truth call.
- **Stats set per use-case:** declared unit of analysis, cluster-robust intervals, a risk-tiered bar; the pass rule (where used) is *lower CI bound exceeds threshold*. No magic "N=200 / ≥95%."
- **Anti-gaming:** hidden queries, corpus/version hashing, abstention-rate audit, complaint-triggered spot checks, and restriction/shutdown transparency logs.

**Honest limits.** Source *reliability* isn't graded yet (a faithful cite of a weak source still passes — a known, separate-module gap). Entailment is genuinely hard. A voluntary report cannot certify legal compliance or overrule states, courts, platforms, or infrastructure chokepoints; it can require evidence, review routes, continuity planning, and a public record where disclosure is lawful. If disclosure and confidential independent review are both blocked, the affected scope should be marked not reviewable and cannot support a pilot listing or future claim. This complements regulation by contributing one public-interest module to the assurance stack and turning part of the operational duties into usable evidence for buyers and the public **now**. Realistic cost is low-thousands per evaluation, not a symbolic fee.

**Governance.** A contribution, not a new body: methodology anchored in the fact-checking world (IFCN/EFCSN/RSF-JTI), method + public report index hosted in a neutral body (OASIS / Linux Foundation), MLCommons as measurement partner. Phase 1 would issue pilot reports only, not a mark — none have been issued, and none are scheduled. The proposer contributes the method and **recuses** from operating any assessor/registry. Demand is the engine — one buyer writing *"must meet this evidence baseline"* into procurement does more than any badge.

**Three asks:**
1. **Break it** — where does "support, not truth" still collapse into truth-judging, or mislead a buyer?
2. **Co-design the measurement** — sampling, unit of analysis, and a risk-tiered bar for *one* use-case.
3. **Pilot it** — if volunteers come forward (ideally one open-weight, one proprietary), evaluate against v0.2 and publish results. None are running yet.
