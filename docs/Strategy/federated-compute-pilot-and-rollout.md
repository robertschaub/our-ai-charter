# Federated public-compute — pilot & rollout

Strategy for standing up the [federated public-compute architecture](../Architecture/federated-public-compute-architecture.md): Geneva 2027 MVP, development sequence, open decisions, and messaging discipline. Proposed, not yet built.

## Geneva 2027 MVP

> A working **Public AI Compute & Evidence pilot**: one governed API, several public models, at least two independently operated nodes/providers, transparent quota rules, public model/node/evaluation cards, one constrained public-interest agent or evaluation use case, and a governance blueprint for expansion.

Minimum build:

1. one gateway exposing 2–4 public models;
2. broker for project identity, quota, data-class policy, and accounting;
3. one inference/cloud node plus one independent research/HPC node;
4. model, node, and evaluation cards; incident channel; monthly usage summary;
5. one public-data evaluation or multilingual civic-information agent;
6. admission criteria, prohibited-use baseline, conflict disclosure, appeal/redress path, and anti-capture rule.

Start with an **Apertus/PublicAI-backed inference + evaluation MVP** because it builds on the nearest live pattern. Apertus is the first anchor because the live open assets sit there today; the federation's rules remain model-plural. Add broker/evidence controls around the access layer, then federate a second independent node/provider, ideally with a second model family.

A small **civic agent grid** can run in parallel as the citizen-participation track, but it carries more reliability and coordination risk. It should not replace the inference MVP.

Success is not global scale. Success is proving that public compute can be shared under inspectable rules.

## Development sequence

- **0–30 days — define and align:** adopt working terms; treat Apertus/PublicAI as reference implementation; map candidate nodes; choose one public-data use case; draft `ComputeNode v0`, `PublicAIWorkload v0`, and card templates.
- **31–90 days — prototype:** governed API pattern; accounts, quotas, logging profiles; one batch evaluation plus one constrained agent task; public cards and a lessons report.
- **3–6 months — federate:** add a second independently operated node via adapter; test routing, failover, quota accounting, disconnect, incidents, and public reporting; keep sensitive data out of scope.
- **6–12 months — institutionalise:** technical steering group, separate public-interest governance group, admission rules, contribution credits, and pilot-scale funding tied to the evidence deliverable.

## Decisions to settle

| Decision | Default recommendation |
|---|---|
| First pilot | Apertus/PublicAI-backed inference + evaluation MVP; small civic agent grid in parallel |
| First nodes/providers | One PublicAI-style inference utility node + one Swiss research/HPC or sovereign-cloud node |
| First broker operator | PublicAI/SPIU-adjacent or Swiss/SNAI-adjacent neutral host; no new-institution claim |
| Identity scope | PKI/CA + signed SLAs for institutional nodes; Keycloak/OIDC for users; eduGAIN-style later |
| Contribution credits | Banded GPU-credit accounting later; do not block the pilot |
| Commercial providers | Allowed only with disclosure, portability, quota limits, and no control over governance or findings |
| Sensitive data | Excluded from the first public pilot |

## Anti-claims

Do **not** say: "global public compute pool"; "this solves sovereign AI"; "this is certification"; "this replaces commercial AI"; "this replaces Apertus/PublicAI"; "open models are safe by default."

Do say: "federated public compute and evidence pilot"; "Apertus/PublicAI is the nearest live anchor"; "the Charter adds broker/evidence controls"; "node control stays local while identity, quota, policy, evidence, and accountability are shared"; "the first deliverable is small and testable."
