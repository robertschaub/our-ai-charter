# The Public AI Network — what it is, how it works, how to join

*A plain-language front door. For the full design see the [federated public-compute architecture](Strategy/federated-public-compute-architecture.md); for the trust layer, the [AI Assurance & Certification](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) workstream; for the strategy and current asks, the [briefing](briefing.md).*

## What it is

The **Public AI Network** is an international, co-stewarded effort for **public AI that free societies can trust, inspect, and rely on** — open and plural, accountable to the people who depend on it, and **resistant to capture** by any single state, company, or funder. *A network, not a fortress.*

It rests on four pillars:

1. **Open, plural models** — no single model or vendor privileged.
2. **A data & knowledge commons** — lawful, rights-respecting, well-documented data and provenance.
3. **Shared assurance & evaluation** — common, public, checkable standards for whether a system shows its work and answers for it (the [Charter / assurance](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) layer). **This is the network's distinctive contribution — the trust layer.**
4. **Federated public compute** — capacity from many independent operators under common rules — **the first buildable substrate.**

Holding them together: **accountable, anti-capture governance**, plus the **demand** (public institutions, procurement) and **capacity-building** (so small and Global-South operators can take part) that make it durable.

> **A note on names.** *"Public AI"* is a broad movement — AI provisioned as public-interest infrastructure. *"PublicAI" / SPIU* is a specific inference utility we draw on as a partner and precedent. **The Public AI Network** is this distinct, co-stewarded initiative — not the movement, and not the PublicAI utility.

"The network" is the **umbrella**. Its concrete buildable system is the **federated public-compute layer** (a policy broker + an evidence plane); we call that by its name, not "the network," to keep the two clear. And **"capture-resistant" is a design commitment and a governance obligation, not a guaranteed property** — a voluntary, early-stage network *can* be captured; the design works to make that hard and visible.

## A short glossary

- **Federated public-compute layer** — the buildable system: many independently-run **nodes**, reachable through one public front door, governed by a **policy broker** (decides who/what/where may run, and what evidence is kept) and leaving an **evidence plane** (public, checkable records). [Full design.](Strategy/federated-public-compute-architecture.md)
- **Node** — a unit of compute capacity in the federation. **Operator** — the accountable entity running it. **Provider** — any contributor of compute, models, data, or tools. *(Every node has an operator; not every provider runs a node.)*
- **The tiers** — three different things, each classifying *one* dimension (not a single prestige ladder): **compute tiers** = the trust level of the hardware; **access tiers** = who the user is and how sensitive the data; **assurance depth** = how well a claim is evidenced.
- **Member roles** — see *How to join*.

## How it's used

Through one public front door, different people reach trustworthy public models for different work:

- a **citizen or journalist** — public Q&A with sources they can check;
- a **researcher** — evaluation, red-teaming, model adaptation;
- a **public institution** — a service it can inspect, contest, and rely on, rather than a black box it cannot govern;
- a **developer / civic app** — building on open models under clear terms;
- a **constrained agent** — a bounded public-interest task (e.g. source verification).

Access is tiered by *who you are* and *how sensitive the data is* — not by hardware — and work runs in lanes (inference, evaluation, adaptation, later co-training, agents). [Access model.](Strategy/federated-public-compute-architecture.md)

## How it's built

Federated and phased, not one system switched on at once:

- **Define & align → prototype** (one governed front door, a few public models) **→ federate** (add a second, independent node) **→ institutionalise** (neutral host, published rules).
- **The MVP:** one governed API, several public models, **≥ 2 independently-operated nodes**, transparent quota rules, public model/node/evaluation cards, one public-interest use case, and a governance blueprint. [Architecture §8.](Strategy/federated-public-compute-architecture.md)
- **Who builds what:** the Charter brings the **assurance + governance rules** and the evidence schema; **operators** bring compute; **model providers** bring open models; a **neutral host** convenes — and none of them controls the rules.
- The near-term vehicle is the **Geneva 2027** window. [Routes & sequence.](Strategy/initiation-strategy.md)

## How to join

Joining is **role-specific**, and **joining is not endorsement or certification** — a *participation status* states the role you hold and what has (and has not) been verified.

**Roles** (kept distinct because they carry different power and accountability):

- **Operator / node** — runs compute under a signed participation agreement.
- **Model / data / tooling contributor** — supplies models, datasets, or evaluations, each with its own provenance and rights duties.
- **Deployer** — builds a public-facing service on the network and **remains accountable for that use** — where the network meets the Charter's *[answerable to people](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md)*.
- **Steward** — helps set the rules, under conflict-of-interest constraints.
- **Assessor** / **adjudicator** — evaluate, and resolve disputes, **independently** of those they assess.
- **Supporter** — endorses the effort; no operational role.

**The terms an operator / provider accepts** — qualification is gated on the *public-interest terms accepted, not tax status* (so cooperative, academic, nonprofit, mission-aligned commercial, and sovereign-cloud operators can all take part):

- capability + dependency **disclosure**; **portability** (open weights / formats); a declared purpose + **prohibited-use** baseline; **quota** limits; conflict-of-interest disclosure; a redress path + named incident contact; submission to attestation / audit-sampling.
- **No participant controls** the rules, admissions, enforcement, or the evaluation findings **about itself**: operators have a *structured voice* in governance, not control, and contributing compute or money does not buy governance control.

**How admission works (concept-level)** — four powers kept apart, so admission cannot become a chokepoint:

1. **eligibility rules** — published, by role, set by the steward body;
2. the **admission decision** — rules-based (not invitation-based) and appealable;
3. **verification** of claims — honestly, **early on this is signed commitments + disclosure + provisional self-attestation**, with independent review and audit-sampling added as the assurance layer matures;
4. **appeal / dispute** — to the independent adjudicator.

Status is **not binary**: *applicant → provisional → verified → restricted/suspended → former*, on a public register that shows the role and the verification level.

**What keeps joining fair and capture-resistant:** rules published, not invitation-only; obligations **proportionate to risk and scale** (so small and Global-South operators are not burdened out); no pay-to-rank; revocable for cause; and **membership is not a trust badge** — only what is verified may be claimed.

## What this is / is not

A plain-language front door, not the spec. The deep design lives in the [federated public-compute architecture](Strategy/federated-public-compute-architecture.md) and the [Charter / assurance](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) workstream; the join model is **concept-level** (no certificate or API mechanics) and **early-stage and voluntary** — its assurance and admission machinery is a deliberate build, not a claim that it already exists.
