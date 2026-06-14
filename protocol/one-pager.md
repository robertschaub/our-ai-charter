> **Status: WORKING DRAFT** — summary of the protocol draft.

# Can we tell when a factual AI *shows its work*? — a 1-page proposal

**A pilot evaluation protocol for discussion — not a certification, not a standard.** v0.2 · 2026-06-14 · Robert Schaub (fact-checker)
_Full protocol: [grounding-faithfulness-and-contestability.md](grounding-faithfulness-and-contestability.md). Hardened after an adversarial multi-model red-team._

**The gap.** We can benchmark AI for *safety* (AILuminate, ISO 42001, NIST AI RMF) and there's good *research* on factuality/attribution (FEVER, RAGAS, citation precision/recall). What's missing is a lightweight, public, comparable way to evaluate one narrow thing in **deployed** factual systems: **does it show its work?** A model can pass a safety benchmark and still fabricate a citation with total confidence. Safety ≠ honesty-of-process.

**What it evaluates** (the deployed system + practices, *not* the weights; one use-case at a time — v0.2 = English Q&A with cited sources):
- **Grounding-faithfulness** — is each checkable claim supported by a source the system cited, scored on a graded rubric (verbatim → paraphrase → entailment → partial → unsupported → contradicted)? Plus a **source-validity floor**: the citation must actually resolve and not be satire/fiction.
- **Calibration / uncertainty** — does stated confidence track support, and does the system **abstain rather than bluff** (and not dodge the audit by hedging everything)?
- **Correction** — are errors logged, fixed, and **not regenerated under paraphrase** (tested by re-issuing logged errors + variants)?
- **Contestability** — a user can flag a wrong output (all systems); who can restrict/recall/shut it down is documented; for *consequential* systems, appeals escalate to a reviewer independent of the operator.

**What it does / doesn't claim.** Says: *honesty-of-process for this version + use-case.* Does **not** say outputs are true, that sources are *reliable* (only that they exist and aren't fiction), or anything about general safety/bias or legal compliance. It's **"aligned with"** UDHR / UNESCO / the Council of Europe AI treaty — never "compliant with."

**The method, kept honest** (this is where experts will push — good):
- **Auditor-controlled, pre-registered held-out query set** (adversarially seeded) — *not* scraped user traffic, to avoid privacy + cherry-picking.
- **Two blinded raters + adjudication**, a published codebook, per-category agreement reported. "Support" is semantic judgment, made repeatable by the rubric — not a truth call.
- **Stats set per use-case:** declared unit of analysis, cluster-robust intervals, a risk-tiered bar; the pass rule (where used) is *lower CI bound exceeds threshold*. No magic "N=200 / ≥95%."
- **Anti-gaming:** hidden queries, corpus/version hashing, abstention-rate audit, complaint-triggered spot checks.

**Honest limits.** Source *reliability* isn't graded yet (a faithful cite of a weak source still passes — a known, separate-module gap). Entailment is genuinely hard. A voluntary report isn't law — it complements regulation by giving buyers a usable signal **now**. Realistic cost is low-thousands per evaluation, not a token fee.

**Governance.** A contribution, not a new body: methodology anchored in the fact-checking world (IFCN/EFCSN/RSF-JTI), method + public index hosted in a neutral body (OASIS / Linux Foundation), MLCommons as measurement partner. The proposer contributes the method and **recuses** from operating any assessor/registry. Demand is the engine — one buyer writing *"must hold this"* into procurement does more than any badge.

**Three asks:**
1. **Break it** — where does "support, not truth" still collapse into truth-judging, or mislead a buyer?
2. **Co-design the measurement** — sampling, unit of analysis, and a risk-tiered bar for *one* use-case.
3. **Pilot it** — two volunteer systems (one open-weight, one proprietary), evaluated against v0.2, results published.
