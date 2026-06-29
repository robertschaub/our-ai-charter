# The Public AI Network — what it is, how it works, how to join

*A plain-language front door. For the full design see the [federated public-compute architecture](Architecture/federated-public-compute-architecture.md); for the trust layer, the [AI Assurance & Certification](AI%20Assurance%20and%20Certification/Framework/charter-commitments.md) sub-stream; for the strategy and current asks, the [briefing](briefing.md).*

> **Where this stands today.** The Public AI Network is an **early-stage, voluntary** effort, and this page describes the **design and intent** — much of it **proposed, not yet built.** There is no live front door, no admission body, assessor, adjudicator, public register, or certification yet. *What exists now:* the design, the principles below, and prospective partners and use cases. *What "joining" means now:* registering interest — not endorsement, certification, or a trust badge.

## What it is

The **Public AI Network** is an international, co-stewarded effort for public AI that helps **build and strengthen free societies** — open and plural, accountable to the people who depend on it, inspectable and contestable, and **resistant to capture** by any single state, company, or funder. *A network, not a fortress.*

It rests on four pillars:
1. **Open, plural models** — no single model or vendor privileged.
2. **A data & knowledge commons** — lawful, rights-respecting, well-documented data and provenance.
3. **Shared assurance & evaluation** — common, public, checkable standards for whether a system shows its work and answers for it (the [Charter / assurance](AI%20Assurance%20and%20Certification/Framework/charter-commitments.md) layer). **This is the network's distinctive contribution — the trust layer.**
4. **Federated public compute** — capacity from many independent operators under common rules — **the first buildable substrate.**

Holding them together: **accountable, anti-capture governance**, plus the **demand** (public institutions, procurement) and **capacity-building** (so small and Global-South operators can take part) that make it durable.

> **A note on names.** *"Public AI"* is a broad movement — AI provisioned as public-interest infrastructure. *"PublicAI" / SPIU* is a specific inference utility we draw on as a partner and precedent. **The Public AI Network** is this distinct, co-stewarded initiative — not the movement, and not the PublicAI utility. This initiative is **Our AI Charter** — a **Public AI Network** initiative; its trust-and-evidence **sub-stream** is **AI Assurance & Certification**, whose normative core is the Charter Commitments.

"The network" is the **umbrella**. Its concrete buildable system is the **federated public-compute layer** (a policy broker + an evidence plane); we call that by its name, not "the network," to keep the two clear. And **"capture-resistant" is a design commitment and a governance obligation, not a guaranteed property** — a voluntary network *can* be captured; the design works to make that hard and visible.

## A short glossary

- **Federated public-compute layer** — the buildable system: many independently-run **nodes**, reachable through one public front door, governed by a **policy broker** (decides who/what/where may run, and what evidence is kept) and leaving an **evidence plane** (records **public where possible, protected-access where sensitive** — never raw personal data). [Full design.](Architecture/federated-public-compute-architecture.md)
- **Node** — a unit of compute capacity in the federation. **Operator** — the accountable entity running it. **Provider** — any contributor of compute, models, data, or tools. *(Every node has an operator; not every provider runs a node.)*
- **The tiers** — three different things, each classifying *one* dimension (not a single prestige ladder): **compute tiers** = the trust level of the hardware; **access tiers** = who the user is and how sensitive the data; **assurance depth** = how well a claim is evidenced.
- **Member roles** — see *How to join*.

## How it's used

*(This describes the **federated layer** — the system the network is building.)* Using the network is a short path — **find → check → use**:

- **Find / navigate** — discover the providers and models in the network and navigate to one that fits the need (purpose, capability, jurisdiction, language, openness), comparing on what each publishes. The directory is **plural and neutral — never a single gatekeeper** (whoever controls discovery controls the market).
- **Check** — query a provider's **capabilities** (what it is for, its limits) and its **assurance** (what has been independently checked — the [trust layer](AI%20Assurance%20and%20Certification/Framework/charter-commitments.md)), kept visibly distinct, and honest about what is *not* yet verified.
- **Use** — reach it through one public front door; access tiered by *who you are* and *how sensitive the data is* (not by hardware), with work in lanes — inference, evaluation, adaptation, later co-training, agents. [Access model.](Architecture/federated-public-compute-architecture.md)

Different people use it for different work:
- a **citizen or journalist** — public Q&A with sources they can check;
- a **researcher** — evaluation, red-teaming, model adaptation;
- a **public institution** — a service it can inspect, contest, and rely on, rather than a black box it cannot govern;
- a **developer / civic app** — building on open models under clear terms;
- a **constrained agent** — a bounded public-interest task (e.g. source verification).

## How it's built

Building the **federated layer** is federated and phased, not one system switched on at once — **define & align → prototype** (one governed front door, a few public models) **→ federate** (a second, independent node) **→ institutionalise** (neutral host, published rules). The near-term target is a **Geneva-2027 MVP**: one governed API, several public models, **≥ 2 independently-operated nodes**, public model/node/evaluation cards, and a governance blueprint.
- **Who builds what:** the Charter brings the **assurance + governance rules** and the evidence schema; **operators** bring compute; **model providers** bring open models; a **neutral host** convenes — and, by design, none of them controls the rules.
- **The build plan in full** — the MVP, the development sequence, the open decisions, and the messaging discipline — is the [pilot & rollout strategy](Strategy/federated-compute-pilot-and-rollout.md); the routes into the **Geneva AI Summit 2027** window are the [initiation strategy](Strategy/initiation-strategy.md).

## How to join

Ordinary **users** simply *use* the public front door once it exists; the roles below are for those who *join* as participants. Joining is **role-specific**, and **joining is not endorsement or certification** — a *participation status* states the role you hold and what has (and has not) been verified.

**Roles** (kept distinct because they carry different power and accountability):
- **Operator / node** — runs compute under a signed participation agreement.
- **Model / data / tooling contributor** — supplies models, datasets, or evaluations, each with its own provenance and rights duties.
- **Deployer** — builds a public-facing service on the network and **remains accountable for that use** — where the network meets the Charter's *[answerable to people](AI%20Assurance%20and%20Certification/Framework/charter-commitments.md)*.
- **Steward** — helps set the rules, under conflict-of-interest constraints.
- **Assessor** / **adjudicator** — evaluate, and resolve disputes, **independently** of those they assess.
- **Supporter** — endorses the effort; no operational role.

*If something goes wrong, accountability is role-specific:* the **deployer** answers to affected people for the service; the **operator** for the infrastructure and its participation terms; **contributors** for the claims and provenance they supply; **stewards** for the rules; and the **adjudicator** resolves disputes independently.

**The terms an operator / provider accepts** — qualification gated on the *public-interest terms accepted, not tax status* (so cooperative, academic, nonprofit, mission-aligned commercial, and sovereign-cloud operators can all take part):
- capability + dependency **disclosure**; **portability** (open weights / formats where applicable); a declared purpose + **prohibited-use** baseline; **quota** limits; conflict-of-interest disclosure; a redress path + named incident contact; submission to attestation / audit-sampling.
- **By design, no participant controls** the rules, admissions, enforcement, or the evaluation findings **about itself**: operators have a *structured voice* in governance, not control, and contributing compute or money does not buy governance control.

**How admission works, by design** — four powers kept apart, so admission cannot become a chokepoint:
1. **eligibility rules** — published, by role, set by the steward body;
2. the **admission decision** — rules-based (not invitation-based) and appealable;
3. **verification** of claims — early on, signed commitments + disclosure + provisional self-attestation, with independent review and audit-sampling added as the assurance layer matures;
4. **appeal / dispute** — to the independent adjudicator.

Status is **not binary**: *applicant → provisional → evidence-reviewed → restricted/suspended → former*, on a public register showing the role and the verification level.

**What keeps joining fair and capture-resistant:** rules published, not invitation-only; obligations **proportionate to risk and scale** (so small and Global-South operators are not burdened out); no pay-to-rank; revocable for cause; and **membership is not a trust badge** — only what is verified may be claimed.

## What this is / is not

A plain-language front door, not the spec, and an **early-stage, voluntary** design (see *Where this stands today*, above). The deep design lives in the [federated public-compute architecture](Architecture/federated-public-compute-architecture.md) and the [Charter / assurance](AI%20Assurance%20and%20Certification/Framework/charter-commitments.md) workstream; the join model is **concept-level** (no certificate or API mechanics) — its assurance and admission machinery is a deliberate build, not a claim that it already exists.
