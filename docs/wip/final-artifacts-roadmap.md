# Final-artifacts roadmap — what this initiative could ultimately release

*Working notes — 2026-06-25 · WIP / DISCUSSION · public-safe.* Companion to [artifact-production-plan.md](artifact-production-plan.md), which covers **inputs** to assemble for Geneva 2027. This note covers the **durable end-products** the initiative could ship — together with others — that live in the world on their own.

## The distinction

- **Input** (the other note): a memo, brief, one-pager, or non-paper you carry into a meeting or process.
- **Final artifact** (this note): a standard, a piece of software, a signable charter with a register, a public report index, a running governed utility, a procurement clause, a mark — a thing others use without you in the room.

## The key insight

The hard intellectual content already exists — five obligations, eight duties, the three-layer assurance stack ([Founding Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md)) and a red-teamed [evaluation protocol](../AI%20Assurance%20and%20Certification/Protocol/grounding-faithfulness-and-contestability.md). What is missing is the **durable form** that lets it live independently. The [landscape scan](../AI%20Assurance%20and%20Certification/Background/landscape-and-positioning.md) names the gap none of the peers fills — *"none certifies that a deployed system's claims are supported by the sources it cited"* — the **unoccupied grounding-faithfulness wedge**. That is the most differentiated artifact available. Peer initiatives supply the templates for the *forms*; nearly every artifact below is a **co-production**, not a solo output.

---

## Tier 1 — Keystone (pursue now)

### 1. Grounding-Faithfulness & Contestability evaluation method — as open-source toolkit, then a published standard
*Form precedent: AI Verify / Project Moonshot (Apache-2.0 toolkit); MLCommons AILuminate (benchmark task); RSF's JTI → CEN Workshop Agreement CWA 17493 (method → published standard).*
- **Minimum first release:** a runnable eval harness for **one** use-case (English Q&A with cited sources) that scores claim-to-citation support + abstention on one deployed open model and emits the report skeleton already in the protocol — shipped as a Project Moonshot recipe or a standalone repo. Detection **wraps** existing tools (HHEM/Lynx/RAGAS), not reinvented.
- **Co-producer:** AI Verify Foundation (Moonshot) or MLCommons; standard track later via RSF-JTI / EFCSN / CEN.
- **Go / no-go:** need ≥1 external rater pair + adjudicator, one open-weight model to run on, and a statistician's sign-off on the single-use-case sampling **before** any published number. No-go if it would mean publishing an uncalibrated pass/fail.

### 3. Governed public-inference pilot → first public evaluation report + report index
*Form precedent: Public AI Inference Utility (publicai.co — the live access point for Apertus); DPGA registry (index model).*
- **Minimum first release:** a public-service charter for **one** running utility serving **one** model (origin, usage limits, safeguards, incident reporting, redress) + one published evaluation report, listed in a minimal public index.
- **Co-producer:** publicai.ch / Public AI / Metagov (utility), SNAI/Apertus (model), an independent assessor, a neutral host for the index (OASIS / Linux Foundation).
- **Go / no-go:** a utility willing to **adopt** the public-service charter and expose a model; grant or volunteer raters to fund the eval. No-go if it reads as critique of Apertus/SNAI rather than docking onto it.

---

## Tier 1b — Connective, cheap, do early

### 2. Founding Accord v1.0 + supporter/member register
*Form precedent: IFCN / EFCSN code + verified-signatory; OSI Open Source AI Definition (a released definition document).*
- **Minimum first release:** promote v0.14 → v1.0 (resolve the "Open decisions" minimally or mark them explicitly open), publish a signable version + a public supporter-list page.
- **Co-producer:** 3–5 early endorsers; an anchor willing to be listed.
- **Go / no-go:** a handful of credible supporters ready to sign — otherwise it reads as a one-person idea (per the alliance-first [strategy](../Public%20AI%20Network/Strategy/initiation-strategy.md)).

### 6. Model procurement clause / "evidence baseline" requirement
*Form precedent: procurement pledges; the protocol's own line — "demand is the engine."*
- **Minimum first release:** a ready-to-paste RFP/contract clause requiring the eight duties' evidence baseline (release risk assessment, legal-scope map, contestability route) for any AI a buyer procures.
- **Co-producer:** one willing public buyer (a canton, a public broadcaster, a university or library).
- **Go / no-go:** one buyer signals intent to reference it. Highest leverage per unit of effort — it makes #1 and #2 bite without a certification scheme.

---

## Tier 2 — Follow-on

### 4. Co-stewardship governance pack — adoptable, capture-resistant template
*Form precedent: governance models behind IFCN/Poynter, Creative Commons; the Accord's own "Open decisions → Governance pack".*
- **Minimum first release:** a short fill-in template — board composition, funding caps + conflict-of-interest, no-secret-kill-switch, appeals, audit/revocation — adoptable by any public-AI node.
- **Co-producer:** Public AI / Metagov, ICAIN, Current AI (accountability pillar).
- **Go / no-go:** one public-AI node willing to pilot the template — otherwise it stays abstract.

### 5. Openness & accountability "card" spec
*Form precedent: model cards / audit cards / C2PA (open spec + conformance); LF Model Openness Framework.*
- **Minimum first release:** a one-page disclosure template (legal-scope map + responsibility map + release-risk summary) + one real model's card filled in.
- **Co-producer:** LF Model Openness Framework, OSI, an open-model team (e.g. Apertus).
- **Go / no-go:** one model team willing to fill it. Cheap; low gate; feeds #1 and #3.

---

## Tier 3 — Long-horizon, conditional

### 7. Trust Mark + conformity scheme (trademarked, revocable, per-model-version)
*Form precedent: JTI certificate (ISO/IEC 17065); Nemko / TrustArc marks; Fairtrade / FSC.*
- **Minimum first release:** **none yet** — Phase 2. The first releasable precursor is the public report index (#3); scheme rules may be *drafted* but not *operated*.
- **Co-producer:** a neutral standard-steward host; the existing accreditation chain (ISO/IEC 17065 + national accreditation bodies + IAF).
- **Go / no-go:** build only when **all three** hold — demonstrated demand (buyers/platforms requiring it), a neutral institutional host, and completed pilots. Until then: name it as the destination, don't build it.

---

## Parallel track

**FactHarbor**, taken from alpha to a released product, is itself a "product/software" final artifact under the same mission — but it is **separate** from the Charter (the app does not author the Charter) and is more a solo build than a co-production.

## Priority and sequence

Workstream 1 (Public AI Network / sovereignty) leads. The **keystones are #1 (toolkit first, not the standard) and #3** — a toolkit you can run on Apertus is a releasable artifact; a brief about it is an input. **#2 and #6** are cheap connective tissue to do early. **#7** is the gated destination.

## Constraints to hold

- **You are a non-state actor — you cannot produce treaties or law.** The binding instruments in this space (Council of Europe Framework Convention; EU AI Act) are not yours to make. Your genuinely-binding artifacts are *contractual / voluntary-commitment*: a charter binding on signatories (#2), a procurement clause binding on buyers (#6), a mark license binding on holders (#7). The one route to *state* bindingness is the political track — the [Postulat](../Public%20AI%20Network/Outreach/postulat.en.md) commissioning a Federal Council report — which is an input to lawmaking, produced by government.
- **Host inside existing bodies; don't found a new institution.** Every form above has a precedent host.
- **MVP register.** One calibrated use-case, one model, one report — not a comprehensive scheme up front.
