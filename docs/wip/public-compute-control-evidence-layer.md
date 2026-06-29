> **Status: WORKING NOTES** — derived from the [federated public compute architecture](../Compute/federated-public-compute-architecture.md) note and a GPT-5.5 cross-model review (2026-06-28); citations web-verified. Promotable to a `DRAFT` Outreach/Strategy one-pager once a carrier group exists.

# The public-interest control-and-evidence layer

*Cooperator-facing one-pager: what the Public AI Network actually adds on top of existing compute. Model-plural and neutrally governed by design; not a new runtime, scheduler, model, or certification authority.*

## In one line

Existing runtimes, gateways, schedulers, identity systems, model registries, and telemetry answer one question — **can this run, fast, at scale?** (capability). None answers — **may it run: for whom, for what purpose, accountably, contestably?** (legitimacy and accountability). That second layer is unowned today, and it is what the Charter contributes.

Partial legitimacy controls *do* exist — cloud IAM, institutional review boards, export controls, grant-allocation systems, abuse teams, privacy compliance — but they are **fragmented, private/institution-specific, non-portable, and not built for federated public-interest accountability.** The Charter's layer makes the decision **public, portable, and per-workload**.

## Why this is feasible at the compute layer

Compute is **unusually governable** — detectable, excludable, quantifiable, and built on a concentrated supply chain ([Sastry, Heim et al., 2024](https://arxiv.org/abs/2402.08797)) — though not the only chokepoint (data, payment rails, and cloud accounts qualify too). That makes the compute layer a practical place to attach public-interest controls. Concretely, the layer is **a decision (the policy broker) plus a durable record (the evidence plane)** for eight questions.

## The eight questions

| Question | Exists today (capability) | The gap the Charter adds (control) | Evidence artifact | Grounded in |
|---|---|---|---|---|
| **Who gets access** | OIDC, API keys, SPIFFE/SPIRE, eduGAIN/Keycloak, node PKI — verify a valid token/cert | Eligibility/accreditation + tier + quota (a public-interest decision) | Allocation/eligibility record | NAIRR & NSF ACCESS allocations; eduGAIN AUP |
| **For what purpose** | Nothing binds a run to a purpose; model licences state prohibited uses but unenforced per request | Declared purpose + prohibited-use baseline at admission, **plus abuse/misuse monitoring** (a declaration is not a defence) | Workload spec + admission decision | [EU AI Act Art. 5](https://artificialintelligenceact.eu/article/5/) (prohibited practices); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) *Map* |
| **On which node** | Schedulers route by resource/locality, blind to jurisdiction/data class | **Two control points:** node admission (signed agreement, capability + dependency disclosure) and per-request data-class/jurisdiction routing | Node card + routing decision | GDPR transfer rules (not blanket residency); the CLOUD Act exposure problem; confidential computing/attestation |
| **With what model** | Registries store weights + an optional author card; no openness/trust tier; no binding to the deployed version | Openness/trust classification + model/eval cards **bound to the deployed version** | Model/openness card + pinned version | [Model Cards](https://arxiv.org/abs/1810.03993) (2019); [Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/) (Stanford CRFM; 2024 v1.1 / 2025); [EU AI Act Art. 53](https://artificialintelligenceact.eu/article/53/) GPAI transparency |
| **With what data** | Input/training/RAG data governance sits largely outside the serving stack | Provenance, consent, and IP basis for the data a workload touches — **the Charter's own headline** | Data-provenance record | Datasheets for Datasets; EU AI Act Art. 53 training-data-summary duty; GDPR lawful basis |
| **Under which evidence obligations** | OpenTelemetry/Prometheus metrics; eval harnesses (HELM, lm-eval-harness, [AILuminate](https://mlcommons.org/benchmarks/ailuminate/)) — ad hoc, private | Signed, privacy-minimised, **risk-tiered** records — incl. *what was not logged and why* — so others can re-check | Evidence-plane outputs (cards, accounting, eval records) | OpenTelemetry GenAI semantic conventions; reproducible builds + weight escrow |
| **With which redress path** | ~Nothing in the compute stack; clouds offer ToS + support, not public redress | Named accountable operator, incident channel, appeal, human approval for consequential agent actions | Incident + appeal records | IAEA inspectorate model; [EU AI Act Art. 73](https://artificialintelligenceact.eu/article/73/) (serious-incident reporting); AI Incident Database; GDPR data-subject rights |
| **With what protections against capture** | Legal form alone fails — EuroHPC kept vendor lock-in though the Commission holds [50% of the votes](https://www.eurohpc-ju.europa.eu/about/governance_en) ([Open Future, 2026](https://openfuture.eu/blog/who-controls-europes-ai-future/)) | Jurisdictional distribution; split-layer voting; funding decoupled from control; neutral host; multi-vendor **and** multi-model; autonomous verification | Published allocation rules, routing logic, partner credits, conflict-of-interest disclosures, accountability reports | CERN; SKA Observatory; ITER/IAEA; EUMETSAT |

## The load-bearing addition: assurance and adjudication

A signed record only proves *someone signed something*. For the evidence plane to mean anything it needs:

- **Assurance** — remote attestation, tamper-evident logs, key-custody rules, audit/sampling rights, reproducibility requirements, and **penalties for false attestation**. (Confidential computing/attestation and redundant execution + spot-checks are the technical substrate.)
- **Adjudication** — a **named adjudicator, sitting outside any single member**, with published evidentiary standards and **graduated sanctions**, to decide when an evaluation is contested, a node misreports, a purpose is misdeclared, or an incident warrants suspension.

Without this, the evidence plane is self-reporting and the controls are declaration theatre. With it, the proposal becomes an actual accountability system — and placing the adjudicator beyond any one member is also what stops a neutral host (Switzerland) from being read as covert control.

## Why this is the credible Charter contribution

- It **operationalises** norms that already exist but float free of compute — [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework), ISO/IEC 42001 (AI management systems), and the EU AI Act GPAI obligations are management frameworks / **provider-level** duties; none produces **portable, public, per-workload** evidence over federated compute, and no cloud does either. The Charter's layer is an **implementation profile** that binds those duties to the moment of execution and makes the record public and checkable.
- It is buildable by a small neutral convenor precisely because it is **not** a new runtime, scheduler, marketplace, or model.

## What it is not

Not a certification or audit authority, not a guarantee that "open models are safe," and not a claim that any single standard above is already solved for shared public compute. FactHarbor is at most an early open-source prototype exploring the evidence-record formats — not a maturity claim.

## Sources

Verified 2026-06-28. **Compute governability** — [Computing Power and the Governance of AI (Sastry/Heim et al., 2024)](https://arxiv.org/abs/2402.08797). **Transparency & evidence** — [Model Cards (2019)](https://arxiv.org/abs/1810.03993); [Foundation Model Transparency Index (Stanford CRFM)](https://crfm.stanford.edu/fmti/) (May 2024 v1.1; 2025 edition, arXiv 2512.10169); [MLCommons AILuminate v1.0](https://mlcommons.org/benchmarks/ailuminate/); [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework); ISO/IEC 42001:2023. **Regulatory anchors** — [EU AI Act Art. 5](https://artificialintelligenceact.eu/article/5/), [Art. 53](https://artificialintelligenceact.eu/article/53/), [Art. 73](https://artificialintelligenceact.eu/article/73/). **Governance precedents** — [EuroHPC governance (Commission 50% of votes)](https://www.eurohpc-ju.europa.eu/about/governance_en); [Who controls Europe's AI future? (Open Future, 2026)](https://openfuture.eu/blog/who-controls-europes-ai-future/). **Full architecture** — [Federated public compute architecture](../Compute/federated-public-compute-architecture.md).
