# Artifacts roadmap — inputs to assemble, and durable end-products

This note records both conditional **inputs** for a Geneva 2027 contribution (memos, briefs, a one-pager — the *I-series* below) and the **durable end-products** the initiative could ship with others (standards, software, a signable charter, a report index — the *#-series* below) that live in the world on their own. The maintainer's current implementation focus is Evidence-Gated Agents; the Geneva sequence resumes only when a concrete channel or collaborator justifies it.

## The distinction

- **Input** (the *I-series* below): a memo, brief, one-pager, or non-paper you carry into a meeting or process.
- **Final artifact** (the *#-series* below): a standard, a piece of software, a signable charter with a register, a public report index, a running governed utility, a procurement clause, a mark — a thing others use without you in the room.

## Geneva-track inputs (I1–I5; assemble when the track resumes)

*These are **inputs** — memos and briefs — for Geneva 2027 meetings and processes, not the active implementation backlog. Strong assets already exist (the published article collection, the bilingual non-paper, the verified-findings and linked-source base, the Charter Commitments, and a reviewed evaluation protocol). Assemble them when a route is live; don't write new manifestos.*

| Input | What it is | Seeds / role | Effort · when |
|---|---|---|---|
| **I1 — Keystone memo** | "Geneva 2027 Public AI Governance & Evidence Package" (~2–3 pp): problem → governance blueprint + one evaluation pilot + roundtable → the ask → honest status | the spine for every downstream route | Low · when a Geneva route resumes |
| **I2 — Forwardable one-pager** | a 1-page summary warm contacts can forward to international anchors | executive summary of I1 | Very low · derive from I1 |
| **I3 — Publication commitment** | abstract + outline + named venue + timeline (½ p) | a concrete publication plan | Very low · only for a live channel |
| **I4 — Evaluation package** *(the differentiator)* | method v0.3 + codebook + report skeleton + one public calibration set + a portable-harness *plan* — the [evaluation PoC scope](../wip/evaluation-poc-scope.md) operationalises this | **seeds durable artifact #1** (eval toolkit → standard); answers the process's "concrete tools" ask | Medium · channel-gated |
| **I5 — Governance blueprint** | the *how*: roles, anti-capture, no-secret-kill-switch, oversight, conflict-of-interest, audit path, external adjudicator, attestation-with-penalties (~2 pp) | substance for Route B conversations; **seeds durable artifact #4** (co-stewardship pack) | Medium · channel-gated |

**Produce on demand** (cheap, when a conversation needs it): a plain-language FAQ / anti-overclaim Q&A; a pre-sprint scoping doc (if a neutral convener engages); a roundtable concept (lowest urgency).
**Conditional:** a Swiss AI Action-Plan ~1-page input *only if* the [go/no-go bar](swiss-action-plan-contribution.md) is met; a co-authored "sovereignty not autarky" op-ed if a warm opportunity matures (avoid "constitution" / new-institution framing).
**Don't produce:** a new manifesto from scratch (use the published collection); a cold standalone Apertus governance proposal to SNAI; a Current AI submission (no open call — a relationship target, not a channel).
**First move when the Geneva track resumes:** refresh **I1** (keystone memo) against the live channel; then derive I2 rather than starting another document. Until then, prioritise the bounded EGA prototype work.

## The key insight

The hard intellectual content already exists — five obligations, eight duties, the three-layer assurance stack ([Charter Commitments](../Assurance/Framework/charter-commitments.md)) and a red-teamed [evaluation protocol](../Assurance/Protocol/grounding-faithfulness-and-contestability.md). What is missing is the **durable form** that lets it live independently. The [landscape scan](landscape-and-positioning.md) names the gap none of the peers fills — *"none certifies that a deployed system's claims are supported by the sources it cited"* — the **unoccupied grounding-faithfulness wedge**. That is the most differentiated artifact available. Peer initiatives supply the templates for the *forms*; nearly every artifact below is a **co-production**, not a solo output.

*Two series: **inputs I1–I5** (above) are the near-term things you carry into a room; **durable artifacts #1–#7** (below) are what others use without you. Some inputs seed an output (I4 → #1; I5 → #4). **Priority is shown by tier, not by number order** — the durable sequence reads #1, #3 (keystone), then #2, #6, then #4, #5, then #7.*

---

## Tier 1 — Keystone (pursue now)

### 1. Grounding-Faithfulness & Contestability evaluation method — as open-source toolkit, then a published standard
*Form precedent: AI Verify / Project Moonshot (Apache-2.0 toolkit); MLCommons AILuminate (benchmark task); RSF's JTI → CEN Workshop Agreement CWA 17493 (method → published standard).*
- **Minimum first release (a package, not just a brief):** for **one** use-case (English Q&A with cited sources) — method v0.3 + annotation codebook + the report skeleton (already in the protocol) + a rater workflow + one **public calibration/example set**, plus a documented **auditor-controlled held-out-set procedure** (the held-out queries stay private, per the protocol's anti-gaming design); and **eventually** a runnable/portable harness (a Project Moonshot recipe or a small open repo) that **wraps** existing detectors (HHEM/Lynx/RAGAS) rather than reinventing them.
- **Co-producer:** AI Verify Foundation (Moonshot) or MLCommons; standard track later via RSF-JTI / EFCSN / CEN.
- **Go / no-go:** need ≥1 external rater pair + adjudicator, one open-weight model to run on, and a statistician's sign-off on the single-use-case sampling **before** any published number. No-go if it would mean publishing an uncalibrated pass/fail.

### 3. Governed public-inference pilot → first public evaluation report + report index
*Form precedent: Public AI Inference Utility (publicai.co — the live international access *pattern*, serving Apertus among several models); DPGA registry (index model).*
- **Minimum first release:** a public-service charter for **one** running utility serving **one** model *to start, under model-plural rules* (origin, usage limits, safeguards, incident reporting, redress) — i.e. the policy-broker / evidence-plane controls of the [control-and-evidence one-pager](../Infrastructure/control-and-evidence-layer.md), including a data-provenance record and a **named adjudicator outside any single member** with graduated sanctions — plus one published evaluation report, listed in a minimal public index.
- **Co-producer:** the Public AI Inference Utility (publicai.co) as utility, with publicai.ch (Swiss chapter, cooperative in formation) / Metagov as coalition partners; SNAI/Apertus (model); an independent assessor; a neutral host for the index (OASIS / Linux Foundation).
- **Go / no-go:** a utility willing to **adopt** the public-service charter and expose a model; grant or volunteer raters to fund the eval. No-go if it reads as critique of Apertus/SNAI rather than docking onto it.

---

## Tier 1b — Connective, cheap, do early

### 2. Charter Commitments v1.0 + supporter/member register
*Form precedent: IFCN / EFCSN code + verified-signatory; OSI Open Source AI Definition (a released definition document).*
- **Minimum first release:** promote the current Charter Commitments draft (v0.19) → v1.0 only after resolving the "Open decisions" or marking them explicitly open; then publish a signable version + a public supporter-list page.
- **Co-producer:** 3–5 early endorsers; an anchor willing to be listed.
- **Go / no-go:** a handful of credible supporters ready to sign — otherwise it reads as a one-person idea (per the alliance-first [strategy](initiation-strategy.md)).

### 6. Model procurement clause / "evidence baseline" requirement
*Form precedent: procurement pledges; the protocol's own line — "demand is the engine."*
- **Minimum first release:** a ready-to-paste RFP/contract clause requiring the eight duties' evidence baseline (release risk assessment, legal-scope map, contestability route) for any AI a buyer procures.
- **Co-producer:** one willing public buyer (a canton, a public broadcaster, a university or library).
- **Go / no-go:** one buyer signals intent to reference it. Highest leverage per unit of effort — it makes #1 and #2 bite without a certification scheme.

---

## Tier 2 — Follow-on

### 4. Co-stewardship governance pack — adoptable, capture-resistant template
*Form precedent: governance models behind IFCN/Poynter, Creative Commons; the Charter Commitments' own "Open decisions → Governance pack".*
- **Minimum first release:** a short fill-in template — board composition, funding caps + conflict-of-interest, no-secret-kill-switch, appeals, audit/revocation — adoptable by any public-AI node.
- **Co-producer:** Public AI / Metagov, ICAIN, Current AI (accountability pillar).
- **Go / no-go:** one public-AI node willing to pilot the template — otherwise it stays abstract.
- **Partner-gated roadmap consideration — human governance competence:** if a public-AI pilot needs named competence criteria, or a credible training/personnel-certification partner wants to test an interface, add a small competence profile to this pack: role and authorized scope; required knowledge and practical abilities; competence evidence and issuer; issue, expiry, and reassessment; independence and support; and observed scenarios or decisions. Separately, derive bounded exercises from the runtime POC; neither the pack nor POC issues a credential. Activate only for a real pilot role or partner, a bounded scenario set, and independent review of the criteria. Keep course completion, credential verification, framework alignment, independent assessment, and the relevant scheme or credential's inclusion in an external accreditation scope visibly distinct.

### 5. Openness & accountability "card" spec
*Form precedent: model cards / audit cards / C2PA (open spec + conformance); LF Model Openness Framework.*
- **Minimum first release:** a one-page disclosure template (legal-scope map + responsibility map + release-risk summary) + one real model's card filled in. Pairs with the public-service charter (#3) as a single adoptable "service charter + card" template.
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

**Current implementation priority:** Evidence-Gated Agents within accountable AI decisions and actions. For the broader Geneva/public-infrastructure track, the **keystones remain #1 (the package/toolkit first, not the standard) and #3** — a toolkit you can run on an Apertus-class public model is a releasable artifact; a brief about it is only an input. **#2 and #6** are cheap connective tissue once external demand exists. **#7** remains a gated destination.

## Constraints to hold

- **You are a non-state actor — you cannot produce treaties or law.** The binding instruments in this space (Council of Europe Framework Convention; EU AI Act) are not yours to make. Your genuinely-binding artifacts are *contractual / voluntary-commitment*: a charter binding on signatories (#2), a procurement clause binding on buyers (#6), a mark license binding on holders (#7). The one route to *state* bindingness is the political track — the [Postulat](../Outreach/postulat.en.md) commissioning a Federal Council report — which is an input to lawmaking, produced by government.
- **Host inside existing bodies; don't found a new institution.** Every form above has a precedent host.
- **Start small (MVP).** One calibrated use-case, one model, one report — not a comprehensive scheme up front.
