# Federated public-compute — pilot & rollout

*The **strategy** for standing up the [federated public-compute architecture](../Architecture/federated-public-compute-architecture.md): the Geneva-2027 pilot, the development sequence, the decisions still open, and the messaging discipline. A forward plan — **proposed, not yet built.** Section references (§2, §3, …) point to the architecture doc.*

## The Geneva-2027 MVP

> A working **Public AI Compute & Evidence pilot**: one governed API, several public models, **at least two independently operated nodes/providers**, transparent quota rules, public model/node/evaluation cards, one constrained public-interest agent or evaluation use case, and a governance blueprint for expansion.

Minimum build: **(1)** one gateway exposing 2–4 public models; **(2)** broker for project identity, quota, data-class policy, accounting; **(3)** one inference/cloud node + one independent research/HPC node; **(4)** model/node/evaluation cards, an incident channel, a monthly usage summary; **(5)** a public-data evaluation or multilingual civic-information agent; **(6)** admission criteria, prohibited-use baseline, conflict-of-interest disclosure, appeal/redress path, anti-capture rule.

**Where to start.** Lead with an **Apertus/PublicAI-backed inference + evaluation** MVP — lowest risk, and it builds directly on the nearest live pattern. The first pilot is Apertus-anchored simply because that is where the live, fully-open assets sit today, not as a Swiss-leadership claim; the federation's rules stay model-plural (§3). Use Apertus as the flagship model family and PublicAI's chat/API pattern as the access precedent; add the missing broker/evidence controls around it, then federate a second independently operated node/provider — ideally a second model family. In parallel, prototype a small **civic agent grid** (C3) as the citizen-participation track: latency-tolerant public-interest agents such as open fact-checking and source verification — the pattern behind FactHarbor (the maintainer's alpha prototype). The grid is the more distinctive story but carries higher reliability/coordination risk, so it should ride alongside — not replace — the inference MVP.

Success is not global scale. Success is proving public compute can be shared under inspectable rules.

## Development sequence

- **0–30 days — define & align:** adopt the federation's working definition (architecture §2); treat Apertus/PublicAI as the reference implementation to learn from; map candidate nodes (Public AI Inference Utility, CSCS/Swiss AI/Apertus-adjacent, EuroHPC routes, ICAIN, Current AI, universities); choose one public-data use case; draft `ComputeNode v0`, `PublicAIWorkload v0`, and card templates.
- **31–90 days — prototype:** an Apertus-compatible governed API pattern; project accounts, quotas, logging profiles; run one batch evaluation + one constrained agent task; publish model/node/evaluation cards + a short lessons report.
- **3–6 months — federate:** add a second independently operated node via an adapter; test routing, failover, quota accounting, node disconnect, incident handling, public reporting; keep sensitive data out of scope.
- **6–12 months — institutionalise:** a small technical steering group + a separate public-interest governance group; admission rules for models/users/projects/nodes; contribution credits (compute, models, evaluations, datasets, translations, support); pilot-scale public/foundation funding tied to the evidence deliverable.

## Decisions to settle

| Decision | Default recommendation |
|---|---|
| Where to start the pilot? | Apertus/PublicAI-backed inference + evaluation MVP (proven, low-risk) as the lead; a small civic agent grid in parallel for the citizen-participation story |
| First two nodes/providers? | One Apertus/PublicAI-style inference utility node + one Swiss research/HPC or sovereign-cloud node (CSCS/SNAI-adjacent where possible) |
| Who operates the first broker? | PublicAI/SPIU-adjacent or a Swiss/SNAI-adjacent neutral host; avoid a new institution claim |
| Identity scope for the pilot? | PKI/CA + signed SLAs for institutional nodes; Keycloak/OIDC for users now; eduGAIN-style federation later |
| Contribution credits across parties? | Banded GPU-credit accounting; design later, don't block the pilot |
| Commercial providers? | Allowed only with disclosure, portability, quota limits, and **no** control over governance or evaluation findings |
| Sensitive data? | Excluded from the first public pilot |

## Anti-claims — what to say, what not to say

Do **not** say: "we are building the global public compute pool"; "this solves sovereign AI"; "this is a certification"; "this replaces commercial AI"; "this replaces Apertus/PublicAI"; "open models are safe by default."

Do say: "we are building a **federated public compute & evidence pilot**"; "Apertus/PublicAI is the nearest live anchor, and the Charter adds the public-interest broker/evidence layer"; "the goal is **governed access** to public models, evaluations, and agent workflows"; "node control stays **local** while identity, quota, policy, evidence, and accountability are **shared**"; "the first deliverable is small — a working gateway, ≥2 nodes/providers, public evidence cards, and one constrained use case."
