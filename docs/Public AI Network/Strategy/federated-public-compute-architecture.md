# Federated public compute architecture for the Public AI Network

_Strategy note, 2026-06-27. Purpose: ground the compute pillar in existing federated/governed models, not a speculative global GPU pool._

## 1. The concept: governed capacity, not one big bucket

"Pooled compute" for the Public AI Network should be designed as **federated public compute capacity**, governed through a shared broker for identity, eligibility, quota, policy, routing, provenance, evaluation, and incident reporting, while each node keeps local operational and jurisdictional control.

It is not one global GPU bucket. It is a governed federation of accountable nodes.

## 2. Architecture: broker + evidence plane

```text
Users / civic apps / agents
  -> public access layer
  -> AI gateway + workload API
  -> policy broker: identity, eligibility, quota, routing, jurisdiction, trust tier
  -> independent nodes: inference utility, Kubernetes GPU cluster, Slurm/HPC centre, cloud/burst provider   
  -> evidence plane: model cards, node cards, evaluation records, usage reports, incidents, redress
```

## 3. The MVP: a compute-and-evidence pilot

By Geneva 2027, a credible deliverable is one governed API, several public models, at least two independently operated nodes or providers, transparent quota rules, public model/node/evaluation cards, one constrained public-interest agent or evaluation use case, and a governance blueprint for expansion.

We are designing a federated public compute and evidence pilot. The goal is governed access to public models, evaluations, and agent workflows. The architecture keeps node control local while sharing identity, quota, policy, evidence, and accountability.
