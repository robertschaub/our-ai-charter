# Federated public AI infrastructure for the Public AI Network

How to build the Public AI Network's AI-infrastructure pillar as federated, governed public capacity — not a single global GPU pool.

*Naming: throughout, **the Public AI Network** is the umbrella effort; **the federation** (the federated public AI infrastructure) is the concrete system designed here — see the [overview](../network-overview.md).*

_As of June 2026; re-verify figures and program statuses before public citation. Sources at the end._

## Conclusion

The pillar should be **federated public AI infrastructure**: many independently operated compute nodes — public HPC centres, universities, public-service media, NGOs and cooperatives, sovereign and mission-aligned commercial clouds, and authenticated citizens — exposed through shared rules, with an evidence layer on top. Each node keeps local control; the federation shares identity, policy, accounting, and accountability.

> **Federated public AI infrastructure** — compute capacity contributed by public, academic, cooperative, nonprofit, and **mission-aligned commercial or sovereign-cloud** operators, for inference, evaluation, adaptation, and (later) co-training, brokered under common rules for identity, eligibility, quota, routing, jurisdiction, provenance, safety, and accountability, while each node keeps local operational and jurisdictional control. What qualifies a node is the **public-interest terms it accepts** — disclosure, portability, and no control over governance or findings — not its tax status.

1. **Start from what's already live; stay model-plural.** The public-inference-utility pattern (PublicAI — chat, API, distributed inference, public-governance posture) is the closest live access layer to wrap and extend, not compete with. Apertus is the strongest live *fully-open* model to start the first pilot with — Switzerland's contribution — but the federation is **model-plural**: no model, and no country, is privileged in the rules.
2. **Lead with what works.** Inference, evaluation, adaptation, and constrained agent execution are feasible now. Cross-border frontier-scale *training* is not — promise "operate, adapt, and govern," not "train at the frontier."
3. **The missing layer is not a GPU scheduler.** Runtimes exist (vLLM, Kubernetes/Kueue, Slurm, Ray, gateways). The gap is the **public-interest control-and-evidence layer** — the Charter's contribution.
4. **Capture is dual and documented.** Compute can be switched off by one state and held by one firm; the architecture defeats **both** by design.

**Local economic benefit is legitimate.** Public AI infrastructure builds domestic skills, suppliers, and AI-capable firms while widening access for researchers, startups, SMEs, and public bodies that cannot buy frontier capacity alone — much of why states fund AI Factories, NAIRR, and national compute programmes. That is how this pillar serves the Charter's mission of public AI that supports societal resilience and economic prosperity, and it stays compatible with a shared federation only if funding, routing, and governance remain openly governed and capture-resistant.

## Charter fit — the five public obligations

This architecture exists to make compute answer to the Charter's five public obligations (set out in the [Charter Commitments](../Assurance/Framework/charter-commitments.md)), not only to run models:

| Obligation | How the architecture serves it |
|---|---|
| **Purpose-bound** | The policy broker binds every workload to a stated purpose and a prohibited-use baseline; the workload spec carries `purpose`, data class, and risk class. |
| **Answerable to people** | Every node has a named operator under a signed agreement (civic peering / PKI); the evidence plane plus an appeal/redress path makes someone accountable; consequential agent actions require human approval. |
| **Safe, secure, private, resilient** | Data-class + jurisdiction routing (PII to the trusted core only); confidential computing/attestation; sandboxed agents; multi-site resilience and an emergency inference reserve; weight escrow for continuity. |
| **Fair in practice** | Transparent, published quota and allocation rules; equitable public tiers; Global-South access on the ICAIN model; no single-actor capture of routing or visibility. |
| **Open to evidence and correction** | The evidence plane records model/node/evaluation cards, incidents, unresolved-risk notes, and public reports; redundant verification lets others check what ran. |

## 1. Trust model: civic peering, not permissionless

It is a federation of **known, accountable entities** that peer like **Eduroam or BGP** — not an anonymous, permissionless swarm. Membership runs on a **PKI / certificate authority with signed participation agreements (not a blockchain)**: every node holds a verifiable certificate, so a misbehaving node can be identified, quarantined, and held to account. This is what lets the federation meet the Charter's accountability and privacy obligations that a trustless token network cannot — and it is why the design avoids crypto/DePIN compute markets (§5).

## 2. What exists, and what is feasible

### Feasibility by workload

| Workload | Feasibility today | Notes |
|---|---|---|
| Public chat / API **inference** | **High** | Proven: the [Public AI Inference Utility](https://publicai.co/stories/utility) already serves public and sovereign models through chat/API access; its developer portal exposes an OpenAI-compatible API (`api.publicai.co/v1`) with `swiss-ai/apertus-8b-instruct` among the listed models ([PublicAI Platform — API endpoints](https://platform.publicai.co/api/~endpoints)). For the Sept 2025 Apertus launch it allocated ~115k GPU-hours across ~20 donated clusters in 5+ countries ([PublicAI, Sep 2025](https://publicai.co/stories/apertus)) — re-verify current standing capacity. |
| **Evaluation / red-team / batch** | **Very high** | Embarrassingly parallel; the natural first public-interest lane. |
| **Agent** workloads | High **with strict controls** | Tools can execute code and access data — needs a tighter safety envelope than plain inference. |
| **Adaptation** (LoRA, RAG, domain tuning) | High | Run near the data, under jurisdiction controls. [FlexOlmo](https://allenai.org/blog/flexolmo) lets owners contribute and **withdraw** experts without centralising data. |
| **Continued pretraining** on bounded models | Medium | Within a region first; cross-site only where justified. |
| **Cross-border frontier-scale training** | **Low–medium** | A research track, not a first deliverable (see frontier caveat). |
| **Emergency inference reserve** | High | Pre-configured failover for civic/public services — a resilience argument in its own right. |

### What already exists (borrow the discipline, not the whole stack)

| Pattern | Examples | What to borrow | Maturity / limit |
|---|---|---|---|
| **Public inference utility** | [Public AI Inference Utility](https://publicai.co/stories/utility), [PublicAI Platform/API](https://platform.publicai.co/docs), [PublicAI chat](https://chat.publicai.co/); the customer-owned cooperative [publicai.ch / SPIU](https://publicai.ch/), in formation | Public API/UI over open & sovereign models; OpenWebUI-style frontend; vLLM + OpenAI-compatible endpoints; global routing/load balancing; national prompts/RAG; public governance posture; the **cooperative ownership** model | Nearest live MVP; PublicAI has a production Apertus deployment blueprint (AWS Zurich / Intel / EKS) but this is not yet the full public broker/evidence layer; publicai.ch/SPIU cooperative in formation (not yet registered) |
| **Research-resource broker** | [NAIRR](https://www.nsf.gov/focus-areas/ai/nairr), [NSF ACCESS](https://access-ci.org/) | Resource catalogue, eligibility, allocations, provider partnerships, reporting discipline | National/research-only; NAIRR funding politically exposed |
| **National public-compute programmes** | [EuroHPC AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories_en) (19 factories + 13 antennas as of Jun 2026) and [AI Gigafactories](https://www.eurohpc-ju.europa.eu/ai-gigafactories_en); CSCS **Alps** (>10M GPU-h for [Apertus](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html)); India AI Mission, UK AIRR, Canada, Japan, Korea | Serious public compute, expert support, public mandate; allocation/subsidy and sovereignty-screen ideas | Mostly national/regional; HPC is batch-first; access terms vary; US-silicon dependent |
| **Federated research grid** | [Open Science Grid / PATh](https://path-cc.io/), [EGI](https://www.egi.eu/federation/egi-federation/), WLCG | Federation-before-centralisation: local owners, shared identity, job routing, accounting, monitoring | Not LLM-native; adapt for GPUs/serving/safety |
| **Cloud-native serving & scheduling** | [Kubernetes Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/), [Envoy AI Gateway](https://aigateway.envoyproxy.io/release-notes/v1.0/), [Kueue/MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/), [Volcano](https://volcano.sh/), [Slurm federation](https://slurm.schedmd.com/federation.html), [KServe](https://kserve.github.io/website/), [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html), [vLLM](https://docs.vllm.ai/) | Don't build a scheduler/runtime/gateway from scratch — use these as node- and gateway-level building blocks | Technical only; no legitimacy, eligibility, redress, or anti-capture; MultiKueue is still beta, but already defines multi-cluster dispatch |
| **Federated model development** | [AI Alliance Project Tapestry](https://thealliance.ai/projects/tapestry); [NVIDIA FLARE](https://developer.nvidia.com/flare), [Flower](https://flower.ai/); low-comm training ([Decoupled DiLoCo](https://deepmind.google/blog/decoupled-diloco/)); modular data-owner contribution ([FlexOlmo](https://allenai.org/blog/flexolmo)) | "Shared base, sovereign derivatives"; data/compute stay local; only weights/modules travel | Later lane; Tapestry is Phase 0 / active-now (Jun 2026) with frontier scale contingent on proof points, partners, compute, data, and funding |
| **Operational federated learning (sensitive data)** | [CERN CAFEIN](https://cafein.web.cern.ch/) — clinical FL platform-as-a-service (stroke prediction under Horizon [TRUSTroke](https://arxiv.org/abs/2410.13869); atrial-fibrillation and cancer-prevention work) | Production cross-silo FL on data that legally cannot move; CERN as a neutral platform host running real federated AI infrastructure today, not only a governance model | Health/science-specific; not LLM-native; cross-silo FL carries real cost/coordination overhead |

### What is in specification or active development

The live specification layer is **model-aware routing and multi-cluster dispatch**: Kubernetes Gateway API Inference Extension, Envoy AI Gateway, and Kueue/MultiKueue already cover much of the gateway and scheduling ground. The research layer is **low-communication training and federated contribution**: Decoupled DiLoCo, Covenant-72B, Tapestry, and FlexOlmo show what may become feasible later. The trust layer is **attestation and confidential computing**: NVIDIA Attestation and GPU TEEs help C1/C2 confidentiality, but are not sufficient on their own.

Existing co-stewardship precedent worth naming: **[ICAIN](https://icain.ch/)** — Swiss-led (FDFA + ETH/EPFL/CSCS + CSC Finland), giving the Global South access to Alps/LUMI. The closest live model for "Switzerland as host/bridge," though its independent legal entity is **not yet built** — a template *and* a cautionary note.

### Starting from what's live: the PublicAI pattern and the Apertus model

**PublicAI is the access pattern.** Its public-inference utility already offers chat/API access, OpenAI-compatible endpoints, distributed inference, national prompts/RAG experiments, and stated public-governance principles — a live multi-country pattern to wrap and extend, not a Swiss asset. **Apertus is the first model anchor.** The Swiss AI Initiative family (EPFL, ETH Zurich, CSCS) has open weights, data, code, methods, and documented training/evaluation; current releases include 8B/70B and **Apertus Mini** 0.5B/1.5B/4B. It is the strongest fully-open sovereign starting point, not the strongest model overall.

The federation stays **model-plural and neutrally governed**. The first pilot should add broker/evidence controls around a PublicAI-style access layer serving Apertus: eligibility, quota/allocation, node admission, data-class/jurisdiction routing, model/node/evaluation cards, incident/redress paths, and public usage reports. The second proof point is an independent node/provider and, ideally, a second model family under the same rules.

### The frontier caveat (why "operate/adapt/govern," not "train")

Distributed training is real but bounded, and that boundary sets the promise. Prime Intellect's ~106B **INTELLECT-3** was trained on a **centralised 512×H200 cluster**, not over the internet ([Prime Intellect, Dec 2025](https://www.primeintellect.ai/blog/intellect-3); confirm before citing). [Decoupled DiLoCo](https://deepmind.google/blog/decoupled-diloco/) cut inter-datacentre bandwidth from 198 Gbps to 0.84 Gbps and trained a 12B model across four US regions, and [Covenant-72B](https://arxiv.org/abs/2603.08163) reached a 72B over-the-internet run (on a token-incentivised blockchain network — the crypto/DePIN substrate §5 rules out). Even so, a standing **~1.5–6× efficiency tax** keeps over-the-internet training off the frontier: the largest decentralised networks remain far behind frontier datacentres ([Epoch AI, Dec 2025](https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale)). For this federation, the realistic horizon is mid-scale continued pretraining, adaptation, evaluation, and resilient inference.

## 3. Architecture: PublicAI today, broker/evidence next

### Layers: node → AI service → model → workload

Four layers are easy to conflate, so name them explicitly:

- A **node** is *where* compute runs — a locally operated, locally governed cluster, sovereign-cloud deployment, or volunteer-device pool, each under a named, accountable operator (§1).
- A node serves one or more **AI services** — what users and developers actually consume. These are *not* peers of one another:

| AI service | What it is |
|---|---|
| **Inference endpoint** | a model served behind an API (OpenAI-compatible) |
| **Assistant / chatbot** | a conversational application over endpoints, often with RAG or national prompts |
| **Agent** | a system that plans and uses tools to act, under the agent-lane safety envelope (workload lanes below) |
| **Evaluator / verifier** | a service that tests, red-teams, or fact-checks any of the above — the Charter's distinctive lane |

- Every AI service runs on one or more **models** — the open/sovereign artifacts (LLM, SLM, multimodal, embedding) the federation stays plural about (§2).
- Each request becomes a **workload** the broker routes and accounts for (inference, evaluation, adaptation, agent, co-training — the lanes below).

In short: **a node serves AI services, built on models, producing workloads.** "LLM," "chatbot," and "agent" are a model, an application, and a tool-using system respectively — three layers, not three siblings.

**System vs. service — a lens, not a layer.** The same artifact is an **AI system** when you find, compare, or hold it to account (who owns it, what it must comply with) and an **AI service** when it is served and used. *Model* names the artifact underneath; *system* and *service* are two views of what's built on it.

### Current Apertus/PublicAI reference architecture

This diagram is a **source-informed map of the current public architecture**, not a claim about a formal Public AI Network governance layer. It combines PublicAI's utility description (chat/API, vLLM, partner clusters, global routing) with its published AWS/Intel Apertus deployment blueprint (AWS Zurich, EKS Auto Mode, Intel/GPU serving, guardrails, storage/state services).

```mermaid
flowchart TB
  U["Users"] --> C["PublicAI chat<br/>OpenWebUI-style frontend"]
  D["Developers / apps"] --> API["PublicAI Platform API<br/>/v1/chat/completions"]
  C --> EDGE["Edge / access controls<br/>CloudFront + WAF in AWS blueprint"]
  API --> EDGE
  EDGE --> AUTH["Auth / accounts<br/>Amazon Cognito (SSO / API keys)"]
  AUTH --> ROUTER["PublicAI routing layer<br/>global load balancing"]
  ROUTER --> AWS["AWS Europe (Zurich)<br/>EKS Auto Mode deployment"]
  ROUTER --> PARTNER["Partner / donated clusters<br/>OpenAI-compatible vLLM servers"]
  AWS --> GUARD["Guardrails (inline, per request)<br/>Bedrock Guardrails in AWS blueprint"]
  GUARD --> V8["vLLM serving<br/>Apertus 8B on Intel R8i EC2"]
  GUARD --> V70["vLLM serving<br/>Apertus 70B on GPU instances"]
  AWS --> STATE["State and artifacts<br/>Aurora / ElastiCache / S3 / EFS / ECR"]
  PARTNER --> PVLLM["Distributed inference<br/>vLLM + OpenAI-compatible APIs"]
  APERTUS["Apertus weights<br/>8B / 70B + Mini variants"] -.->|deployed on| V8
  APERTUS -.->|deployed on| V70
  APERTUS -.->|deployed on| PVLLM
```

What exists already: a live public-model access surface, Apertus as the flagship Swiss model family, API/chat access, distributed inference, and at least one documented production deployment pattern. What is not yet shown here: public allocation rules, formal node admission, common data-class routing, signed evidence cards, redress, and anti-capture governance. Note the tension this map makes visible — the flagship anchor today runs partly on a **US hyperscaler (AWS Zurich) with US-rooted Bedrock Guardrails**, the very stack §4 shows one jurisdiction can toggle. That is not a reason to avoid it; it is the clearest reason the broker, portability, and multi-vendor layers below exist.

### Proposed federated broker (model-plural, neutrally governed)

```mermaid
flowchart TB
  U["Users, civic apps, public-interest agents"] --> A["Public access layer<br/>Apertus/PublicAI-compatible chat + API"]
  A --> G["AI gateway<br/>model-endpoint routing"]
  A --> W["Workload API<br/>evaluation, adaptation, agent tasks"]
  G --> B["Policy broker"]
  W --> B
  B --> I["Identity and eligibility"]
  B --> Q["Quota and allocation ledger"]
  B --> P["Policy engine"]
  B --> C["Capability registry<br/>several open/sovereign models"]
  B --> Z["Evidence requirements"]
  B --> R["Node/tier dispatch<br/>routing & scheduling adapter"]
  R --> N0["C1: reference inference node<br/>PublicAI-style utility — one of several"]
  R --> N1["C1: trusted public HPC / sovereign clusters"]
  R --> N2["C2: institutional federation"]
  R --> N3["C3: civic agent grid"]
  N0 --> E["Evidence and accountability plane"]
  N1 --> E
  N2 --> E
  N3 --> E
  E --> M["Model & node cards"]
  E --> O["Observability and accounting"]
  E --> V["Evaluation records"]
  E --> X["Incidents, redress, public reports"]
  O -.->|accounting feeds quota| Q
  X -.->|incidents inform policy| P
```

- **Public access layer** — the front door to those AI services: PublicAI-compatible chat/API where useful, a batch endpoint for evaluation, a budgeted agent-task endpoint, and a published model list with model + evidence cards. Simple by design; complexity lives behind it.
- **Policy broker** — the core public-interest addition beyond today's PublicAI/Apertus access layer. Decides *whether* a workload may run, *where*, and *what evidence must be kept*: identity & affiliation, eligibility & public-interest purpose, quota/budget/contribution accounting, jurisdiction & data-class routing, model/node trust tiers, abuse-response + appeal, and signed execution records.
- **Compute nodes** — locally operated and locally governed; a live public-inference-utility node (PublicAI-style, serving Apertus in the first pilot) is the first reference node, and additional nodes publish capability records (Appendix), grouped into the three tiers below.
- **Evidence & accountability plane** — **where the Charter is strongest**: model/openness cards, node + dependency cards, evaluation records, workload summaries, incidents + mitigations, quota/allocation reports, unresolved-risk notes, and an explicit note of *what was not logged and why*. Distinguish public evidence from confidential assessor evidence from data that must not be retained.

### The missing layer, concretely

The bottom-line claim unpacks into eight decisions the **policy broker** makes and the records the **evidence plane** keeps — each a public-interest control on a capability primitive that already exists but is blind to the public interest (existing identity, scheduling, registry, and telemetry systems answer *can this run?*, not *may it — for whom, accountably, contestably?*):

1. **Who gets access** — eligibility/accreditation, tier, and quota, not merely a valid token → allocation record.
2. **For what purpose** — a declared purpose and prohibited-use baseline checked at admission, backed by abuse/misuse monitoring (a declaration is not a defence) → admission decision.
3. **On which node** — node admission (signed agreement; capability + dependency disclosure) and, separately, per-request data-class/jurisdiction routing → node card + routing decision.
4. **With what model** — an openness/trust classification and model/evaluation cards bound to the deployed version → model card + pinned version.
5. **With what data** — input, training, and retrieval provenance, consent, and IP basis (the Charter's own headline) → data-provenance record.
6. **Under which evidence obligations** — signed, privacy-minimised, **risk-tiered** records, including *what was not logged and why* → evidence-plane outputs.
7. **With which redress path** — a named accountable operator, an incident channel, appeal, and human approval for consequential actions → incident + appeal records.
8. **With what protections against capture** — the §4 design rules (distribution, split-layer voting, funding decoupled from control, neutral host, multi-vendor *and* multi-model, autonomous verification).

The load-bearing addition is **assurance and adjudication**: a signed record only proves *someone signed*, so the layer needs attestation, audit/sampling rights, and penalties for false attestation, plus a **named adjudicator outside any single member** with evidentiary standards and graduated sanctions. Without it the evidence plane is self-reporting; with it, placing the adjudicator beyond any one member is also what stops a neutral host from being read as covert control.

### Workload lanes

Separate lanes because each has different latency, cost, risk, and governance needs: **(1) public inference**, **(2) evaluation & evidence**, **(3) adaptation**, **(4) federated co-training** (later), **(5) agent compute** (constrained). Agent-lane minimum controls: per-task token/GPU/time budget; model/tool allowlists by risk; sandboxed execution; source/retrieval logging that minimises personal-data retention; claim- and citation-check hooks; human approval for consequential actions; hard stop on budget/policy/safety breach. MCP helps tool interoperability but its own spec flags consent, data-access, and code-execution risks — for public agents these controls are mandatory.

### Compute tiers (trust × latency)

Lanes say *what* runs; **compute tiers (C1–C3)** say *on whose hardware*, matched to trust and latency. The broker routes each request to the tier its privacy and latency demand:

| Tier | Compute | Best for | Integrity mechanism |
|---|---|---|---|
| **C1 — Fast core** | Trusted public HPC / sovereign clusters (CSCS, EuroHPC); K8s/Ray | Synchronous, low-latency, **privacy-sensitive** queries — PII routes here only | Operator trust + confidential computing / attestation |
| **C2 — Institutional swarm** | Peered institutions pooling datacentre/workstation GPUs; mostly site-local serving plus burst/batch/adaptation capacity; cross-site pipeline serving only where links and operations justify it | Mid-latency inference, evaluation, adaptation, and burst capacity for non-sensitive workloads | mTLS + node certificates + redundant cross-checks; TEEs/attestation where available, without treating enclaves as a full trust substitute |
| **C3 — Civic agent grid** | Volunteer idle compute (citizens, small orgs); quantized local models via llama.cpp behind a secure job queue | **Latency-tolerant, parallelisable agentic/batch** work on **public data** (e.g. open fact-checking, source verification, dataset embedding) | Redundant execution, spot checks, deterministic packaging where possible, provenance logs, and human adjudication for consequential outputs; no PII; sandboxed worker |

The C2 pipeline-parallel pattern was pioneered by **Petals** (BigScience) — a useful proof-of-concept but effectively dormant (last release 2023). Treat cross-site pipeline serving as an exception, not the default: it is fragile without predictable high-bandwidth links and disciplined operations. C3 is "Folding@Home for public-interest AI agents": it fits latency-tolerant, embarrassingly-parallel work on public data, and is the most direct route to **citizen participation** in public AI.

### Reference implementation stack

| Layer | Starting point |
|---|---|
| Gateway / routing | Kubernetes Gateway API Inference Extension and/or Envoy AI Gateway v1.0; keep OpenAI-compatible endpoints where useful |
| Inference runtime | vLLM or SGLang; KServe or Ray Serve LLM for orchestration; Triton/TensorRT-LLM where already in use |
| Batch scheduling | Kueue/MultiKueue (quotas, beta multi-cluster dispatch); Volcano for HPC-style batch |
| HPC integration | Slurm adapter first; Slurm federation where clusters already coordinate |
| Identity | Node-level **PKI/CA with signed SLAs** for institutional peers; OIDC/eduGAIN-style federation and Keycloak for users; SPIFFE/SPIRE for service identity |
| Policy | Open Policy Agent-style checks; keep public-AI policies readable and versioned |
| Observability | OpenTelemetry GenAI conventions, Prometheus, GPU + token/cost accounting, privacy-minimised event records |
| Evidence registry | Signed Markdown/JSON cards in Git for v0; append-only registry with public exports later |

Build the **broker, evidence schema, governance rules, and adapters** — not a new runtime, scheduler, marketplace, or identity system.

## 4. Governance & anti-capture

What makes "no single power can switch off or capture" defensible rather than a slogan.

### Why it is necessary — documented, not hypothetical

- **Switch-off by one state:** US GPU export controls are toggled as policy (H100→H20→**H200 case-by-case licensing for China after a Dec 2025 policy announcement / Jan 2026 BIS rule**, [BIS](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)).
- **Cut-off by sanctions:** AWS/Microsoft/Google suspended Russian cloud (2022) and forced firms off in 2024 ([TechCrunch](https://techcrunch.com/2022/03/10/amazon-microsoft-and-google-have-suspended-cloud-sales-in-russia/)).
- **Weaponised dependency:** after US sanctions on the ICC prosecutor, his Microsoft email was reportedly cut; the ICC moved to open-source by Oct 2025 ([The Register](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/)).
- **No sovereignty on a US stack:** Microsoft France told the French Senate under oath (June 2025) it **could not guarantee** data against the US CLOUD Act ([databalance.eu](https://www.databalance.eu/en/microsoft-cloud-sovereignty-2026/)).
- **Concentration (2026, re-verify):** the three US hyperscalers (AWS, Azure, GCP) hold roughly two-thirds of global **cloud-infrastructure-services** revenue (Synergy estimated 28% / 21% / 14% in Q1 2026, via [CRN](https://www.crn.com/news/cloud/2026/cloud-market-share-q1-2026-aws-microsoft-google-battling-in-ai-era)); NVIDIA remains the dominant data-centre AI accelerator platform, with analyst/methodology estimates around **80–90%** of AI-capex going to NVIDIA-based data centres ([Epoch AI methodology](https://epoch.ai/data/ai-chip-owners-documentation/methodology)), reinforced by CUDA lock-in. (Figures are estimates on differing bases — revenue, capex, shipment, installed capacity — so treat as orders of magnitude.)

### Precedents and what each teaches

| Precedent | Rule | Anti-capture lesson |
|---|---|---|
| **CERN** | One state, one vote; unweighted | Gold standard vs. *political* capture; open-access mandate |
| **SKA Observatory** | Treaty IGO, one-member-one-vote | Modern (2019) template; host-state ratification gate |
| **ITER / IAEA** | Majority for ops, **unanimity to amend** | Split the layers: act by majority, change the constitution by unanimity; autonomous inspectorate |
| **EUMETSAT** | GNI-proportional funding | Funding scales with economy **without** governance collapsing to it |
| **EuroHPC** | Commission holds 50% of votes | *Cautionary*: legal form alone did not stop EU-dominance or vendor lock-in ([Open Future, Feb 2026](https://openfuture.eu/blog/who-controls-europes-ai-future/)) |
| **ICAIN** | Aspiring independent association | The live Swiss nucleus — but the neutral legal entity is unbuilt |

Background: compute is unusually governable (detectable, excludable, concentrated supply chain — though not the only chokepoint; data, payment rails, and cloud accounts are governable too) — [Computing Power and the Governance of AI](https://arxiv.org/abs/2402.08797) (Feb 2024) — and the [CERN-for-AI blueprint](https://cfg.eu/building-cern-for-ai/) supplies concrete oversight mechanisms. "Sovereignty not autarky" has direct backing: [Chatham House (Feb 2026)](https://www.chathamhouse.org/2026/02/how-middle-powers-can-weather-us-and-chinese-ai-dominance) names "share sovereignty" and "hedge" as two of four middle-power strategies.

### Design rules (apply to any node, broker, or co-stewardship deal)

1. **Physical + jurisdictional distribution** — many sites, many legal regimes; no single off-switch.
2. **Split-layer voting** — majority for operations; supermajority/unanimity for budget, director, admissions, and cost-share.
3. **Funding decoupled from control** — contribution buys access, not the rules.
4. **Neutral host** — Switzerland's actual comparative advantage (rule of law, IGO-hosting).
5. **Open, multi-vendor, multi-model stack** — break the NVIDIA/CUDA + hyperscaler chokepoint (LUMI's AMD/ROCm path is the existing hedge), and avoid single-model dependency: the broker serves several open and sovereign model families, with no model privileged in the rules.
6. **Autonomous verification** — evaluation/inspection outside any single member's hands.

**Residual risk to state honestly:** silicon. Every pool except China's runs on US accelerators under US licences. This is "sovereignty not autarky," truthfully — mitigate with multi-vendor procurement and jurisdictional spread; do not claim full-stack independence.

## 5. Trust & integrity layer

Capture-resistance and confidentiality come from boring, production-grade engineering — not exotic cryptography:

- **Portability on open standards** (open weights/formats, portable orchestration) — the single biggest anti-capture lever; the difference between "portable" and "captured."
- **Confidential computing (TEEs) + remote attestation** — verify hardware/firmware and protect sensitive code/data in use on infrastructure you do not own ([NVIDIA Attestation](https://docs.nvidia.com/attestation/index.html)); early H100 benchmarks suggest low single-digit overhead for large-model inference ([benchmark](https://phala.com/posts/confidential-computing-on-nvidia-h100-gpu-a-performance-benchmark-study)). Fits C1–C2 institutional nodes. Caveats: TEEs do not eliminate operator, firmware, vendor-root, side-channel, or physical-access risk ([TEE.fail, Oct 2025](https://tee.fail/)); accept multiple roots, require operational controls, and keep a non-TEE fallback.
- **Redundant execution + spot-checking** — the integrity mechanism for untrusted C3 volunteer nodes that lack server TEEs; useful for anomaly detection and confidence, not a mathematical proof of truth.
- **Federated learning + differential privacy** for data that legally cannot move (mature cross-device; costlier cross-silo).
- **Weight escrow + reproducible builds** — continuity if a provider exits.
- **Avoid crypto/DePIN compute markets as an anchor** — real for some inference/rendering, but unproven for serious training, token-fragile, with a GPU-spoofing history (io.net, 2024), and reputationally entangling for a public-interest network. Borrow their verification ideas (e.g. TOPLOC), not their token markets.

## 6. Access governance tiers

Distinct from the compute tiers C1–C3 (§3): these classify *users and data*, not hardware.

| Tier | Access | Workloads |
|---|---|---|
| **0 — public demo** | Anonymous, rate-limited, public models | demos, education, low-cost Q&A |
| **1 — authenticated public-interest** | Accounted projects, quotas, public/synthetic data | civic apps, public evaluations, basic agents |
| **2 — institutional/research** | Approved institutions, stronger logging, data agreements | batch eval, adaptation, restricted research data |
| **3 — sensitive-local** | Local node only, strict legal basis, no default cross-border routing | sensitive public-sector / regulated work |

The first pilot stays in tiers 0–1; tier 2 follows with formal partners; tier 3 is **not** part of the first public claim.

## 7. Risks & controls

| Risk | Control |
|---|---|
| **Overclaiming** a global training cluster | Frame as a federation; start with inference/eval/batch/agent/fine-tune |
| **Compute capture** (one state/funder/cloud/lab) | Publish allocation rules, routing logic, partner credits, conflicts of interest, accountability reports; apply the §4 design rules |
| **Jurisdiction confusion** | Data classes, jurisdiction constraints, sovereign-only routing, auditable operator profiles |
| **Node tampering / poisoning** | Node certificates (civic peering); redundant cross-checks (C2); redundant execution, spot checks, and adjudication for C3 |
| **Agent abuse** | Tool allowlists, scoped permissions, sandboxing, budgets, human approval, full traces |
| **HPC usability gap** | Dual stack: HPC for training/batch, cloud-native for APIs/serving/agents |
| **Silicon / vendor lock-in** | Multi-vendor procurement, open formats, portability, weight escrow |
| **Sustainability blind spot** | Energy/carbon metadata in node profiles + scheduler policy |

> **Rollout, decisions & messaging.** The Geneva-2027 pilot/MVP, the development sequence, the open decisions, and the anti-claims (messaging discipline) now live in the **[pilot & rollout strategy](pilot-and-rollout.md)** — this doc keeps the architecture and its risk controls.

## Appendix — minimum schemas (v0)

```yaml
ComputeNode:
  operator: "named institution"        # public operator preferred
  jurisdiction: "CH"                    # legal regime of the node
  tier: "fast-core | institutional-swarm | civic-agent-grid"
  aiServices: ["inference-endpoint", "assistant", "agent", "evaluator"]  # AI services this node serves
  workloadClasses: ["inference", "batch-evaluation"]
  accelerators: [{ type: "GH200|H100|MI300", countDisclosure: "banded" }]
  schedulers: ["kueue", "slurm-adapter"]
  dataClassesAllowed: ["public", "synthetic", "non-sensitive-research"]
  retentionProfiles: ["metrics-only", "short-lived-debug"]
  trustTier: "tier-1-authenticated"
  identity: { certificate: "publicai-CA", slaSigned: true }
  telemetry: { utilization: true, carbonSignal: true, auditLogs: true }
  publicDependencies: ["cloud/provider or facility disclosure"]
  incidentContact: "public-contact@example.org"
```

```yaml
PublicAIWorkload:
  project: "geneva-2027-evidence-pilot"
  responsibleInstitution: "named public-interest host"
  workloadClass: "batch-evaluation"
  purpose: "evaluate a public model on source-grounded civic tasks"
  model: { requested: "apertus-or-compatible", opennessRequirement: "open-enough-to-evaluate" }
  data: { class: "public", personalData: false, allowedRegions: ["CH", "EU"], retentionProfile: "metrics-only" }
  budget: { maxGpuHours: 50, maxTokens: 20000000, maxWallTimeHours: 12 }
  evidence: { publishSummary: true, retainPrompts: false, retainMetrics: true, requiredCards: ["model", "node", "evaluation"] }
  policy: { trustTierRequired: "tier-1-authenticated", prohibitedUsesProfile: "public-ai-baseline", humanReviewRequired: false }
```

## Bottom line

The architecture is a **model-plural, neutrally governed broker with an evidence plane**. PublicAI/Apertus supplies the nearest live access pattern; the Charter contribution is the public-interest control-and-evidence layer: who gets access, for what purpose, on which node, with what model and data, under which evidence duties, with which redress path, and with what protections against capture.

## Sources

Operational anchors — [Apertus](https://apertvs.ai/) · [Apertus technical information](https://apertvs.ai/pages/documentation/) · [Apertus Mini](https://apertvs.ai/articles/2026-06-apertus-mini/) · [Apertus for Ticino](https://apertvs.ai/articles/2026-03-ticino/) · [Public AI Inference Utility](https://publicai.co/stories/utility) · [PublicAI Platform/API](https://platform.publicai.co/docs) · [PublicAI Apertus deployment note](https://publicai.co/stories/apertus) · [PublicAI AWS/Intel deployment blueprint](https://aws.amazon.com/blogs/apn/how-public-ai-delivers-sovereign-llm-inference-on-aws-and-intel/) · [publicai.ch / SPIU](https://publicai.ch/) · [EuroHPC AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories_en) · [EuroHPC AI Gigafactories](https://www.eurohpc-ju.europa.eu/ai-gigafactories_en) · [CSCS Alps / Apertus (ETH, Sep 2025)](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html) · [ICAIN](https://icain.ch/) · [NAIRR](https://www.nsf.gov/focus-areas/ai/nairr) · [NSF ACCESS](https://access-ci.org/) · [CERN CAFEIN](https://cafein.web.cern.ch/). Implementation/spec layer — [Kubernetes Gateway API Inference Extension](https://gateway-api-inference-extension.sigs.k8s.io/) · [Envoy AI Gateway v1.0](https://aigateway.envoyproxy.io/release-notes/v1.0/) · [Kueue/MultiKueue](https://kueue.sigs.k8s.io/docs/concepts/multikueue/) · [Slurm federation](https://slurm.schedmd.com/federation.html). Distributed training & data contribution — [Decoupled DiLoCo (DeepMind, Apr 2026)](https://deepmind.google/blog/decoupled-diloco/) · [INTELLECT-3 trained centrally (Prime Intellect, Dec 2025)](https://www.primeintellect.ai/blog/intellect-3) · [Covenant-72B (arXiv, Mar 2026)](https://arxiv.org/abs/2603.08163) · [FlexOlmo (Ai2, Jul 2025)](https://allenai.org/blog/flexolmo) · [Project Tapestry](https://thealliance.ai/projects/tapestry) · [Epoch AI, Dec 2025](https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale). Trust — [NVIDIA Attestation](https://docs.nvidia.com/attestation/index.html) · [Confidential computing on H100 (benchmark)](https://phala.com/posts/confidential-computing-on-nvidia-h100-gpu-a-performance-benchmark-study) · [TEE.fail, Oct 2025](https://tee.fail/) · [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices). Governance & political economy — [Computing Power and the Governance of AI (Feb 2024)](https://arxiv.org/abs/2402.08797) · [Building CERN for AI](https://cfg.eu/building-cern-for-ai/) · [Who controls Europe's AI future? (Open Future, Feb 2026)](https://openfuture.eu/blog/who-controls-europes-ai-future/) · [Chatham House — middle powers (Feb 2026)](https://www.chathamhouse.org/2026/02/how-middle-powers-can-weather-us-and-chinese-ai-dominance). Capture precedents — [BIS H200 licensing rule (Jan 2026)](https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china) · [ICC moves off Microsoft (Oct 2025)](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/) · [Microsoft France / CLOUD Act (Jun 2025)](https://www.databalance.eu/en/microsoft-cloud-sovereignty-2026/).
