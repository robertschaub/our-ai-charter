> **Status: WIP / DISCUSSION** — earlier framing, superseded by the protocol.

# Contribution Brief v3 — AI Grounding, Provenance & Correction (GPC) Assurance
### Auditing whether a developer's deployed AI grounds its claims, calibrates confidence, and corrects errors — *not* whether its outputs are "true"

_Draft 2026-06-13, v3. Rebuilt after two adversarial red-team rounds (GPT-5.5 + Gemini). v3 closes the "false-assurance" contradiction that sank v2: it is renamed for what it actually certifies and adds a measurable behavioural floor. This is a CONTRIBUTION PROPOSAL for a working group — not a finished standard._

---

**The ask:** Add an auditable **GPC criterion** to existing AI-trust frameworks (AI Alliance Trust & Safety WG; DPGA AI track; aligned with MLCommons AILuminate & IEEE CertifAIEd), as an *extension*, not a new body. The proposer contributes the method and **recuses** from operating it.

## 0. What the mark promises — and doesn't (read first)
- **Promises:** on independent sampling, the deployed system's claims are **traceably grounded in the sources it cites**, its **confidence is calibrated**, and its **logged errors are corrected** to published thresholds.
- **Does NOT promise:** that every output is true; it does **not adjudicate contested facts**; it is **not** a safety/security certification; it is **not** a liability shield.

## 1. The gap
The technical pieces exist (factuality benchmarks — TruthfulQA, FActScore, HaluEval; provenance — C2PA; governance — NIST AI RMF, ISO/IEC 42001, EU AI Act transparency duties). **What's missing is an independent, revocable assurance *wrapper*** tying grounding/provenance/correction **practices + a behavioural floor** into one auditable, inclusive scheme at the deployed-system level.

## 2. Unit of assessment
The **deployed system / service configuration + the developer's practices** — never the weights. Open base-model publishers get a **separate, clearly-labelled "base-model documentation" track** (not the deployed GPC mark), because grounding/correction are app-layer properties.

## 3. What is assessed — two parts, both required
**A) Practices (process):** grounding/retrieval discipline; source-attribution mechanisms; uncertainty-disclosure UX; provenance logging; eval transparency; documented error-reporting, correction, and post-deployment monitoring.
**B) Behavioural floor (output sampling — the teeth):** independent sampling of the *deployed* system, including adversarial prompts, against **published, per-domain thresholds**:
1. **Grounding-support rate** — % of checkable claims actually supported by the cited source (*faithfulness, not truth*).
2. **Fabrication rate** — confident claims with no/contradicted support; invented or irrelevant citations.
3. **Calibration** — stated confidence vs. actual grounding support.
4. **Correction efficacy & latency** — logged errors fixed within a defined window and not regenerated.

*Scoring rules the working group must set:* a **common-knowledge exemption** (universally-accepted, low-risk uncited claims like "Paris is in France" are not penalised — the system must cite *when challenged*, not always, so the floor never forces citation-hallucination); **source snapshotting** (cited pages captured at test time, since pages change); and **explicit domain + language coverage** (passing English enterprise Q&A ≠ passing all domains/languages).

**Pass requires BOTH A and B.** Good process with a failing floor = fail. This is what stops it being a paperwork audit.

## 4. Why this escapes the "truth-tribunal" trap
We test **faithfulness** — *"is this claim supported by the source the system itself cited?"* — which is measurable and far more bounded and auditable than adjudicating truth. We do **not** test **truth** — *"is this contested claim correct?"* — and never adjudicate contested facts. Source-credibility and uncertainty criteria are **published, pluralistic, appealable, version-controlled** — contestable choices made in the open. We do not claim neutrality; we claim transparency and contestability.

## 5. Anti-gaming (Goodhart defences)
- Test citation **support**, not mere presence → kills citation-theatre.
- Penalise degenerate over-hedging/over-refusal by measuring **helpfulness retention** → kills "I might be wrong" boilerplate.
- **Private, rotating test sets** with continuous stewardship (MLCommons-style) → vendors can't teach to the test.
- Adversarial sampling, not just happy-path.

## 6. Revocation & change mechanics (so "revocable" has teeth)
Published complaint channel; incident-rate triggers for off-cycle review; a defined **"material change"** (system prompt, retrieval corpus, tools, routing, safety layer, fine-tune) forces **recertification**; public mark status; defined cure periods; appeals that do not auto-suspend; adversarial-complaint filtering.

## 6b. Certificate card + claims-use rule (closes the residual mis-marketing risk)
Every GPC mark must publish a short, machine-readable **certificate card** stating: covered **domains and languages**, **test date**, **thresholds** applied, **sample size + confidence interval**, the **source-eligibility policy**, and how **uncited claims** were treated. The card also fixes the **permitted marketing language — including the explicit line "GPC does not certify that outputs are true."** Misleading use of the mark (implying a truth guarantee, or claiming coverage beyond the tested domains/languages) is itself a **revocation trigger**. This is the last guard against a vendor turning the mark into a false-assurance shield.

## 7. Assessors
Mixed accredited panels — **ML engineers + domain experts + regional/linguistic expertise**; independent and **not paid by the assessed party**; accredit-the-accreditors; two-assessor + periodic academic re-evaluation (EFCSN model).

## 8. Conflict-of-interest firewall
Proposer contributes the method then **recuses** from certifying anyone; the **host body** (not any fact-checking org) operates it; **no proposer-affiliated entity profits** from assessments; multi-stakeholder co-authored; criteria changes require **supermajority + public comment**; no profession enshrined as gatekeeper.

## 9. Adoption (honest — the central risk)
Forcing functions: **EU AI Act transparency obligations** (a recognised conformance signal), **public-procurement preference**, **enterprise assurance** demand. Delivered as a **sub-module/annex of standards developers already engage** (ISO/IEC 42001 annex-style control; DPG Standard AI track) to minimise marginal burden. We do not assume adoption; we name the levers and concede they are not secured.

## 10. Funding (integrity-critical)
Diversified: host-body dues + public/philanthropic grants + assessment fees **capped so no single stream dominates** (MSC's ~93% logo-fee dependence is the anti-pattern); a **solidarity fund + hardship waivers** finance small/Global-South assessment; funders disclosed; **no funder controls criteria**.

## 11. Non-goals
Not a truth guarantee; not adjudicating contested facts; not auditing weights; not a safety/security replacement; not a liability shield; not enshrining any profession; not pay-to-pass; not a new org/silo.

## 12. Residual limitations (conceded openly)
Contestable epistemic choices are made transparent and bounded, **not eliminated**; adoption depends on external forcing functions; the behavioural floor reduces but cannot zero out gaming; open base models cannot carry the deployed mark.

## The ask (concrete)
1. Form/join a sub-group to draft **GPC as an annex** to the DPG Standard AI track / an AI Alliance Trust & Safety output.
2. **Pilot** on 3–5 diverse deployed systems (incl. open-app and Global-South), publish pass/fail/remediation openly.
3. Align labelling with **MLCommons AILuminate** and **IEEE CertifAIEd**.

**What the proposer brings:** standards-grade information-integrity expertise + the tested, sourced design above. Intent: **contribute, not found.**
