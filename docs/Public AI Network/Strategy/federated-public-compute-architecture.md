# Federated public compute architecture for the Public AI Network

How to build the Public AI Network's compute pillar as federated, governed public capacity — not a single global GPU pool.

_As of June 2026; re-verify figures and program statuses before public citation. Sources at the end._

## Conclusion

The compute pillar should be **federated public compute**: many independently operated nodes — public HPC centres, universities, public-service media, NGOs and cooperatives, sovereign and mission-aligned commercial clouds, and authenticated citizens — exposed through shared rules, with an evidence layer on top. Each node keeps local control; the network shares identity, policy, accounting, and accountability.

> **Federated public compute** — capacity contributed by public, academic, cooperative, nonprofit, and **mission-aligned commercial or sovereign-cloud** operators, for inference, evaluation, adaptation, and (later) co-training, brokered under common rules for identity, eligibility, quota, routing, jurisdiction, provenance, safety, and accountability, while each node keeps local operational and jurisdictional control. What qualifies a node is the **public-interest terms it accepts** — disclosure, portability, and no control over governance or findings (see §10) — not its tax status.

Homepage form: _federated public compute that no single power can switch off or capture._

1. **Lead with what works.** Inference, evaluation, adaptation, and constrained agent execution are feasible now. Cross-border frontier-scale *training* is not — promise "operate, adapt, and govern," not "train at the frontier."
2. **The missing layer is not a GPU scheduler.** Runtimes exist (vLLM, Kubernetes/Kueue, Slurm, Ray, gateways). The gap is the **public-interest control-and-evidence layer** — the Charter's contribution.
3. **Capture is dual and documented.** Compute can be switched off by one state and held by one firm; the architecture defeats **both** by design.

**Local economic benefit is a legitimate driver.** Public compute is also industrial policy: building and operating nodes develops domestic skills, suppliers, and AI-capable firms, and gives each participating country a real economic stake — much of why states fund AI Factories, NAIRR, and national compute programmes. That economic development is a fair reason to invest, and it is fully compatible with a shared, governed network so long as the network stays openly governed and capture-resistant. It also widens access for researchers, startups, SMEs, and public bodies that cannot buy frontier capacity alone. This is how the compute pillar serves the Charter's mission of a public AI network that drives **societal resilience and economic prosperity**.

## Charter fit — the five public obligations

This architecture exists to make compute answer to the Charter's five public obligations (set out in the [Founding Accord](../../AI%20Assurance%20and%20Certification/Framework/founding-accord.md)), not only to run models:

| Obligation | How the architecture serves it |
|---|---|
| **Purpose-bound** | The policy broker binds every workload to a stated purpose and a prohibited-use baseline; the workload spec carries `purpose`, data class, and risk class. |
| **Answerable to people** | Every node has a named operator under a signed agreement (civic peering / PKI); the evidence plane plus an appeal/redress path makes someone accountable; consequential agent actions require human approval. |
| **Safe, secure, private, resilient** | Data-class + jurisdiction routing (PII to the trusted core only); confidential computing/attestation; sandboxed agents; multi-site resilience and an emergency inference reserve; weight escrow for continuity. |
| **Fair in practice** | Transparent, published quota and allocation rules; equitable public tiers; Global-South access on the ICAIN model; no single-actor capture of routing or visibility. |
| **Open to evidence and correction** | The evidence plane records model/node/evaluation cards, incidents, unresolved-risk notes, and public reports; redundant verification lets others check what ran. |

## 1. Trust model: civic peering, not permissionless

The network is a federation of **known, accountable entities** that peer like **Eduroam or BGP** — not an anonymous, permissionless swarm. Membership runs on a **PKI / certificate authority with signed participation agreements (not a blockchain)**: every node holds a verifiable certificate, so a misbehaving node can be identified, quarantined, and held to account. This is what lets the network meet the Charter's accountability and privacy obligations that a trustless token network cannot — and it is why the design avoids crypto/DePIN compute markets (§5).

## 2. What exists, and what is feasible

### Feasibility by workload

| Workload | Feasibility today | Notes |
|---|---|---|
| Public chat / API **inference** | **High** | Proven: the [Public AI Inference Utility](https://publicai.co/) serves open models behind one router; in its first month (Sept 2025) it drew on ~115k GPU-hours across ~20 donated clusters in 5+ countries ([HF, Sep 2025](https://huggingface.co/blog/inference-providers-publicai)) — re-verify current standing capacity. |
| **Evaluation / red-team / batch** | **Very high** | Embarrassingly parallel; the natural first public-interest lane. |
| **Agent** workloads | High **with strict controls** | Tools can execute code and access data — needs a tighter safety envelope than plain inference. |
| **Adaptation** (LoRA, RAG, domain tuning) | High | Run near the data, under jurisdiction controls. [FlexOlmo](https://allenai.org/blog/flexolmo) lets owners contribute and **withdraw** experts without centralising data. |
| **Continued pretraining** on bounded models | Medium | Within a region first; cross-site only where justified. |
| **Cross-border frontier-scale training** | **Low–medium** | A research track, not a first deliverable (see frontier caveat). |
| **Emergency inference reserve** | High | Pre-configured failover for civic/public services — a resilience argument in its own right. |

### What already exists (borrow the discipline, not the whole stack)

| Pattern | Examples | What to borrow | Maturity / limit |
|---|---|---|---|
| **Public inference utility** | [Public AI Inference Utility](https://publicai.co/); customer-owned cooperative [publicai.ch / SPIU](https://publicai.ch/) | Public API/UI over open & sovereign models; vLLM + OpenAI-compatible endpoints + global router; the **cooperative ownership** model | Operational; governance not yet codified |
| **Research-resource broker** | [NAIRR](https://www.nsf.gov/focus-areas/ai/nairr), [NSF ACCESS](https://access-ci.org/) | Resource catalogue, eligibility, allocations, provider partnerships, reporting discipline | National/research-only; NAIRR funding politically exposed |
| **National public-compute programmes** | [EuroHPC AI Factories & Gigafactories](https://www.eurohpc-ju.europa.eu/ai-factories_en); CSCS **Alps** (>10M GPU-h for [Apertus](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html)); India AI Mission, UK AIRR, Canada, Japan, Korea | Serious public compute, expert support, public mandate; allocation/subsidy and sovereignty-screen ideas | Mostly single-nation; HPC is batch-first; US-silicon dependent |
| **Federated research grid** | [Open Science Grid / PATh](https://path-cc.io/), [EGI](https://www.egi.eu/federation/egi-federation/), WLCG | Federation-before-centralisation: local owners, shared identity, job routing, accounting, monitoring | Not LLM-native; adapt for GPUs/serving/safety |
| **Cloud-native serving & scheduling** | [Kueue/MultiKueue](https://kueue.sigs.k8s.io/), [Volcano](https://volcano.sh/), [Slurm federation](https://slurm.schedmd.com/federation.html), [KServe](https://kserve.github.io/website/), [Ray Serve LLM](https://docs.ray.io/en/latest/serve/llm/index.html), [vLLM](https://docs.vllm.ai/), [Envoy AI Gateway](https://aigateway.envoyproxy.io/) | Don't build a scheduler/runtime/gateway from scratch — use these as node- and gateway-level building blocks | Technical only; no legitimacy, eligibility, redress, or anti-capture |
| **Federated model development** | [AI Alliance Project Tapestry](https://thealliance.ai/projects/tapestry); [NVIDIA FLARE](https://developer.nvidia.com/flare), [Flower](https://flower.ai/); low-comm training (DiLoCo) | "Shared base, sovereign derivatives"; data/compute stay local | Later lane; Tapestry is Phase-0 (Apr 2026), unproven |

Existing co-stewardship precedent worth naming: **[ICAIN](https://icain.ch/)** — Swiss-led (FDFA + ETH/EPFL/CSCS + CSC Finland), giving the Global South access to Alps/LUMI. The closest live model for "Switzerland as host/bridge," though its independent legal entity is **not yet built** — a template *and* a cautionary note.

### The frontier caveat (why "operate/adapt/govern," not "train")

Distributed training is real but bounded. Low-communication methods cut bandwidth needs 400×–10,000× ([Decoupled DiLoCo, Apr 2026](https://deepmind.google/blog/decoupled-diloco/)); the largest published decentralised pretraining is ~40B params. But there is a standing **~1.5–6× efficiency tax**, Prime Intellect's ~106B **INTELLECT-3 was reported to train on a centralised cluster** ([implicator.ai, Nov 2025](https://www.implicator.ai/prime-intellects-intellect-3-open-source-ambition-meets-centralized-reality/); confirm against Prime Intellect's own report before citing), and Epoch AI concludes decentralised training **"won't catch up to the frontier this decade"** ([Dec 2025](https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale)). Mid-scale, cross-institution adaptation is the realistic horizon.

## 3. Architecture: a federated broker with an evidence plane

```mermaid
flowchart TB
  U["Users, civic apps, public-interest agents"] --> A["Public access layer"]
  A --> G["AI gateway and model router"]
  A --> W["Workload API"]
  G --> B["Policy broker"]
  W --> B
  B --> I["Identity and eligibility"]
  B --> Q["Quota and allocation ledger"]
  B --> P["Policy engine"]
  B --> R["Routing and scheduling adapter"]
  B --> C["Capability registry"]
  R --> N1["C1: trusted public HPC"]
  R --> N2["C2: institutional swarm"]
  R --> N3["C3: civic agent grid"]
  N1 --> E["Evidence and accountability plane"]
  N2 --> E
  N3 --> E
  E --> M["Model & node cards"]
  E --> O["Observability and accounting"]
  E --> V["Evaluation records"]
  E --> X["Incidents, redress, public reports"]
```

- **Public access layer** — the front door: OpenAI-compatible API where useful, a batch endpoint for evaluation, a budgeted agent-task endpoint, and a published model list with model + evidence cards. Simple by design; complexity lives behind it.
- **Policy broker** — the core public-interest addition. Decides *whether* a workload may run, *where*, and *what evidence must be kept*: identity & affiliation, eligibility & public-interest purpose, quota/budget/contribution accounting, jurisdiction & data-class routing, model/node trust tiers, abuse-response + appeal, and signed execution records.
- **Compute nodes** — locally operated and locally governed; each publishes a capability record (Appendix), grouped into the three tiers below.
- **Evidence & accountability plane** — **where the Charter is strongest**: model/openness cards, node + dependency cards, evaluation records, workload summaries, incidents + mitigations, quota/allocation reports, unresolved-risk notes, and an explicit note of *what was not logged and why*. Distinguish public evidence from confidential assessor evidence from data that must not be retained.

### Workload lanes

Separate lanes because each has different latency, cost, risk, and governance needs: **(1) public inference**, **(2) evaluation & evidence**, **(3) adaptation**, **(4) federated co-training** (later), **(5) agent compute** (constrained). Agent-lane minimum controls: per-task token/GPU/time budget; model/tool allowlists by risk; sandboxed execution; source/retrieval logging that minimises personal-data retention; claim- and citation-check hooks; human approval for consequential actions; hard stop on budget/policy/safety breach. MCP helps tool interoperability but its own spec flags consent, data-access, and code-execution risks — for public agents these controls are mandatory.

### Compute tiers (trust × latency)

Lanes say *what* runs; **compute tiers (C1–C3)** say *on whose hardware*, matched to trust and latency. The broker routes each request to the tier its privacy and latency demand:

| Tier | Compute | Best for | Integrity mechanism |
|---|---|---|---|
| **C1 — Fast core** | Trusted public HPC / sovereign clusters (CSCS, EuroHPC); K8s/Ray | Synchronous, low-latency, **privacy-sensitive** queries — PII routes here only | Operator trust + confidential computing / attestation |
| **C2 — Institutional swarm** | Peered institutions pooling datacentre/workstation GPUs; pipeline-parallel serving of models no single member can host | Mid-latency inference of large open models | mTLS + node certificates + **redundant cross-check**; enclaves so hosts can't read model memory |
| **C3 — Civic agent grid** | Volunteer idle compute (citizens, small orgs); quantized local models via llama.cpp behind a secure job queue | **Latency-tolerant, parallelisable agentic/batch** work on **public data** (e.g. open fact-checking, source verification, dataset embedding) | **Redundant execution + consensus** across ≥3 nodes; no PII; sandboxed worker |

The C2 pipeline-parallel pattern was pioneered by **Petals** (BigScience) — a useful proof-of-concept but effectively dormant (last release 2023); adopt the *pattern* with maintained tooling, not the project. C3 is "Folding@Home for public-interest AI agents": it fits exactly the latency-tolerant, embarrassingly-parallel work volunteer compute does well, and is the most direct route to **citizen participation** in public AI.

### Reference implementation stack

| Layer | Starting point |
|---|---|
| Gateway / routing | Envoy AI Gateway or a LiteLLM-style model gateway; keep OpenAI-compatible endpoints |
| Inference runtime | vLLM or SGLang; KServe or Ray Serve LLM for orchestration; Triton/TensorRT-LLM where already in use |
| Batch scheduling | Kueue/MultiKueue (quotas, multi-cluster dispatch); Volcano for HPC-style batch |
| HPC integration | Slurm adapter first; Slurm federation where clusters already coordinate |
| Identity | Node-level **PKI/CA with signed SLAs** for institutional peers; OIDC/eduGAIN-style federation and Keycloak for users; SPIFFE/SPIRE for service identity |
| Policy | Open Policy Agent-style checks; keep public-AI policies readable and versioned |
| Observability | OpenTelemetry, Prometheus, GPU + token/cost accounting, privacy-minimised event records |
| Evidence registry | Signed Markdown/JSON cards in Git for v0; append-only registry with public exports later |

Build the **broker, evidence schema, governance rules, and adapters** — not a new runtime, scheduler, marketplace, or identity system.

## 4. Governance & anti-capture

What makes "no single power can switch off or capture" defensible rather than a slogan.

### Why it is necessary — documented, not hypothetical

- **Switch-off by one state:** US GPU export controls are toggled as policy (H100→H20→**H200 cleared for China, Dec 2025**, [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/us-eases-nvidia-export-restrictions-h200-cleared-for-china-under-tight-controls)).
- **Cut-off by sanctions:** AWS/Microsoft/Google suspended Russian cloud (2022) and forced firms off in 2024 ([TechCrunch](https://techcrunch.com/2022/03/10/amazon-microsoft-and-google-have-suspended-cloud-sales-in-russia/)).
- **Weaponised dependency:** after US sanctions on the ICC prosecutor, his Microsoft email was reportedly cut; the ICC moved to open-source by Oct 2025 ([The Register](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/)).
- **No sovereignty on a US stack:** Microsoft France told the French Senate under oath (June 2025) it **could not guarantee** data against the US CLOUD Act ([databalance.eu](https://www.databalance.eu/en/microsoft-cloud-sovereignty-2026/)).
- **Concentration (2025, re-verify):** the three US hyperscalers (AWS, Azure, GCP) hold roughly two-thirds of the global **cloud-infrastructure-services** market by revenue ([Statista, 2025](https://www.statista.com/chart/18819/worldwide-market-share-of-leading-cloud-infrastructure-service-providers/)); NVIDIA holds an estimated **~80–90%+ of data-centre AI accelerators** ([carboncredits.com, 2025](https://carboncredits.com/nvidia-controls-92-of-the-gpu-market-in-2025-and-reveals-next-gen-ai-supercomputer/)), reinforced by CUDA lock-in. (Figures are vendor/analyst estimates on differing bases — revenue vs. shipment — so treat as orders of magnitude.)

### Precedents and what each teaches

| Precedent | Rule | Anti-capture lesson |
|---|---|---|
| **CERN** | One state, one vote; unweighted | Gold standard vs. *political* capture; open-access mandate |
| **SKA Observatory** | Treaty IGO, one-member-one-vote | Modern (2019) template; host-state ratification gate |
| **ITER / IAEA** | Majority for ops, **unanimity to amend** | Split the layers: act by majority, change the constitution by unanimity; autonomous inspectorate |
| **EUMETSAT** | GNI-proportional funding | Funding scales with economy **without** governance collapsing to it |
| **EuroHPC** | Commission holds 50% of votes | *Cautionary*: legal form alone did not stop EU-dominance or vendor lock-in ([Open Future, Feb 2026](https://openfuture.eu/blog/who-controls-europes-ai-future/)) |
| **ICAIN** | Aspiring independent association | The live Swiss nucleus — but the neutral legal entity is unbuilt |

Background: compute is uniquely governable (detectable, excludable, concentrated supply chain) — [Computing Power and the Governance of AI](https://arxiv.org/abs/2402.08797) (Feb 2024) — and the [CERN-for-AI blueprint](https://cfg.eu/building-cern-for-ai/) supplies concrete oversight mechanisms. "Sovereignty not autarky" has direct backing: [Chatham House (Feb 2026)](https://www.chathamhouse.org/2026/02/how-middle-powers-can-weather-us-and-chinese-ai-dominance) names "share sovereignty" and "hedge" as two of four middle-power strategies.

### Design rules (apply to any node, broker, or co-stewardship deal)

1. **Physical + jurisdictional distribution** — many sites, many legal regimes; no single off-switch.
2. **Split-layer voting** — majority for operations; supermajority/unanimity for budget, director, admissions, and cost-share.
3. **Funding decoupled from control** — contribution buys access, not the rules.
4. **Neutral host** — Switzerland's actual comparative advantage (rule of law, IGO-hosting).
5. **Open, multi-vendor stack** — break the NVIDIA/CUDA + hyperscaler chokepoint (LUMI's AMD/ROCm path is the existing hedge).
6. **Autonomous verification** — evaluation/inspection outside any single member's hands.

**Residual risk to state honestly:** silicon. Every pool except China's runs on US accelerators under US licences. This is "sovereignty not autarky," truthfully — mitigate with multi-vendor procurement and jurisdictional spread; do not claim full-stack independence.

## 5. Trust & integrity layer

Capture-resistance and confidentiality come from boring, production-grade engineering — not exotic cryptography:

- **Portability on open standards** (open weights/formats, portable orchestration) — the single biggest anti-capture lever; the difference between "portable" and "captured."
- **Confidential computing (TEEs) + remote attestation** — run on infrastructure you don't own without the operator reading weights/data. <5–7% overhead for large-model inference on H100; near-zero on Blackwell ([benchmark](https://phala.com/posts/confidential-computing-on-nvidia-h100-gpu-a-performance-benchmark-study)). Fits C1–C2 institutional nodes. Caveats: no defence against physical access ([TEE.fail, Oct 2025](https://securityonline.info/tee-fail-researchers-break-intel-sgx-tdx-and-amd-sev-snp-with-sub-1000-ddr5-memory-bus-attack/)); attestation roots in the chip vendor — accept multiple roots and keep a non-TEE fallback.
- **Redundant execution + consensus** — the integrity mechanism for untrusted C3 volunteer nodes that lack server TEEs.
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

## 7. MVP for Geneva 2027

> A working **Public AI Compute & Evidence pilot**: one governed API, several public models, **at least two independently operated nodes/providers**, transparent quota rules, public model/node/evaluation cards, one constrained public-interest agent or evaluation use case, and a governance blueprint for expansion.

Minimum build: **(1)** one gateway exposing 2–4 public models; **(2)** broker for project identity, quota, data-class policy, accounting; **(3)** one inference/cloud node + one independent research/HPC node; **(4)** model/node/evaluation cards, an incident channel, a monthly usage summary; **(5)** a public-data evaluation or multilingual civic-information agent; **(6)** admission criteria, prohibited-use baseline, conflict-of-interest disclosure, appeal/redress path, anti-capture rule.

**Where to start.** Lead with the **inference + evaluation** MVP — lowest risk, and it builds directly on the proven public inference utility pattern. In parallel, prototype a small **civic agent grid** (C3) as the citizen-participation track: latency-tolerant public-interest agents such as open fact-checking and source verification — the pattern behind FactHarbor (the maintainer's alpha prototype). The grid is the more distinctive story but carries higher reliability/coordination risk, so it should ride alongside — not replace — the inference MVP.

Success is not global scale. Success is proving public compute can be shared under inspectable rules.

## 8. Development sequence

- **0–30 days — define & align:** adopt the definition above; map candidate nodes (Public AI Inference Utility, CSCS/Swiss AI/Apertus-adjacent, EuroHPC routes, ICAIN, Current AI, universities); choose one public-data use case; draft `ComputeNode v0`, `PublicAIWorkload v0`, and card templates.
- **31–90 days — prototype:** public models behind a governed API; project accounts, quotas, logging profiles; run one batch evaluation + one constrained agent task; publish evidence cards + a short lessons report.
- **3–6 months — federate:** add a second independently operated node via an adapter; test routing, failover, quota accounting, node disconnect, incident handling, public reporting; keep sensitive data out of scope.
- **6–12 months — institutionalise:** a small technical steering group + a separate public-interest governance group; admission rules for models/users/projects/nodes; contribution credits (compute, models, evaluations, datasets, translations, support); pilot-scale public/foundation funding tied to the evidence deliverable.

## 9. Risks & controls

| Risk | Control |
|---|---|
| **Overclaiming** a global training cluster | Frame as a federation; start with inference/eval/batch/agent/fine-tune |
| **Compute capture** (one state/funder/cloud/lab) | Publish allocation rules, routing logic, partner credits, conflicts of interest, accountability reports; apply the §4 design rules |
| **Jurisdiction confusion** | Data classes, jurisdiction constraints, sovereign-only routing, auditable operator profiles |
| **Node tampering / poisoning** | Node certificates (civic peering); redundant cross-check (C2) and redundant-execution consensus (C3) |
| **Agent abuse** | Tool allowlists, scoped permissions, sandboxing, budgets, human approval, full traces |
| **HPC usability gap** | Dual stack: HPC for training/batch, cloud-native for APIs/serving/agents |
| **Silicon / vendor lock-in** | Multi-vendor procurement, open formats, portability, weight escrow |
| **Sustainability blind spot** | Energy/carbon metadata in node profiles + scheduler policy |

## 10. Decisions to settle

| Decision | Default recommendation |
|---|---|
| Where to start the pilot? | Inference + evaluation MVP (proven, low-risk) as the lead; a small civic agent grid in parallel for the citizen-participation story |
| First two nodes/providers? | One inference utility/cloud node + one Swiss research/HPC node (CSCS-adjacent) |
| Who operates the first broker? | An existing Public AI utility or a Swiss/SNAI-adjacent neutral host; avoid a new institution claim |
| Identity scope for the pilot? | PKI/CA + signed SLAs for institutional nodes; Keycloak/OIDC for users now; eduGAIN-style federation later |
| Contribution credits across parties? | Banded GPU-credit accounting; design later, don't block the pilot |
| Commercial providers? | Allowed only with disclosure, portability, quota limits, and **no** control over governance or evaluation findings |
| Sensitive data? | Excluded from the first public pilot |

## 11. Anti-claims

Do **not** say: "we are building the global public compute pool"; "this solves sovereign AI"; "this is a certification"; "this replaces commercial AI"; "open models are safe by default."

Do say: "we are building a **federated public compute & evidence pilot**"; "the goal is **governed access** to public models, evaluations, and agent workflows"; "node control stays **local** while identity, quota, policy, evidence, and accountability are **shared**"; "the first deliverable is small — a working gateway, ≥2 nodes/providers, public evidence cards, and one constrained use case."

## Appendix — minimum schemas (v0)

```yaml
ComputeNode:
  operator: "named institution"        # public operator preferred
  jurisdiction: "CH"                    # legal regime of the node
  tier: "fast-core | institutional-swarm | civic-agent-grid"
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

The strongest architecture for the Public AI Network is a **federated public-compute broker with an evidence plane**, peered as **civic infrastructure** (known, accountable nodes — not a permissionless swarm), governed by **split-layer, funding-decoupled, multi-vendor, neutrally-hosted** rules, and made confidential by **portability + TEEs/attestation**. The runtime already exists. What is missing — and what the Charter can credibly contribute — is the public-interest control-and-evidence layer: who gets access, for what purpose, on which node, with what model, under which evidence obligations, with which redress path, and with what protections against capture.

## Sources

Operational anchors — [Public AI Inference Utility](https://publicai.co/) · [publicai.ch / SPIU](https://publicai.ch/) · [EuroHPC AI Factories](https://www.eurohpc-ju.europa.eu/ai-factories_en) · [CSCS Alps / Apertus (ETH, Sep 2025)](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html) · [ICAIN](https://icain.ch/) · [NAIRR](https://www.nsf.gov/focus-areas/ai/nairr) · [NSF ACCESS](https://access-ci.org/). Distributed training — [Decoupled DiLoCo (DeepMind, Apr 2026)](https://deepmind.google/blog/decoupled-diloco/) · [INTELLECT-3 reverted to centralised (Nov 2025)](https://www.implicator.ai/prime-intellects-intellect-3-open-source-ambition-meets-centralized-reality/) · [FlexOlmo (Ai2, Jul 2025)](https://allenai.org/blog/flexolmo) · [Project Tapestry](https://thealliance.ai/projects/tapestry) · [Epoch AI, Dec 2025](https://epoch.ai/gradient-updates/how-far-can-decentralized-training-over-the-internet-scale). Trust — [Confidential computing on H100 (benchmark)](https://phala.com/posts/confidential-computing-on-nvidia-h100-gpu-a-performance-benchmark-study) · [TEE.fail, Oct 2025](https://securityonline.info/tee-fail-researchers-break-intel-sgx-tdx-and-amd-sev-snp-with-sub-1000-ddr5-memory-bus-attack/). Governance & political economy — [Computing Power and the Governance of AI (Feb 2024)](https://arxiv.org/abs/2402.08797) · [Building CERN for AI](https://cfg.eu/building-cern-for-ai/) · [Who controls Europe's AI future? (Open Future, Feb 2026)](https://openfuture.eu/blog/who-controls-europes-ai-future/) · [Chatham House — middle powers (Feb 2026)](https://www.chathamhouse.org/2026/02/how-middle-powers-can-weather-us-and-chinese-ai-dominance). Capture precedents — [US H200-to-China (Dec 2025)](https://www.tomshardware.com/tech-industry/semiconductors/us-eases-nvidia-export-restrictions-h200-cleared-for-china-under-tight-controls) · [ICC moves off Microsoft (Oct 2025)](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/) · [Microsoft France / CLOUD Act (Jun 2025)](https://www.databalance.eu/en/microsoft-cloud-sovereignty-2026/).
