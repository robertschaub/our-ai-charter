> **Status: WORKING NOTES** — session synthesis (primary sources, verified 2026-07-03); assessments labelled. The **visual + connection capstone** for the Public AI coalition mapping: it carries the people-connection findings and the maps, and points to where each detail already lives. Companions: [Apertus fit & engagement](apertus-fit-and-engagement-plan.md) (coalition roles, Bosselut, Ticino), [Metagov & Public AI landscape](metagov-public-ai-landscape.md) (Metagov org, assurance adjacency, Klein).

# Public AI — stakeholder & connection map (Swiss ecosystem)

*Who's who in the Public AI coalition — including the open [Public AI Fellow (Switzerland)](https://publicai.network/jobs/fellow-switzerland) role — and how the key people actually connect. Diagrams render on the site.*

## TL;DR

- **Joshua Tan is the coalition's connective node**, and the contact for the open Fellow (Switzerland) role (`josh@publicai.co`). That role is **operational** — grow Public AI Switzerland / SPIU, advance Apertus deployment, build Swiss relationships, prep the 2027 summit — so **independent assurance is a Charter differentiator, distinct from that remit**.
- **Alek Tarkowski is a peer of Tan's, not a gatekeeper.** They co-ran the Public AI Seminar's **Season 3 only**; Open Future is the coalition's **European-policy arm**. A credible bridge into Tan's orbit, but decisions route through Tan.
- **Samuel Klein** is the co-founder whose work (verification / provenance) sits **closest to the Charter's assurance building block**.

## 1. The coalition around the Swiss role — who's who (map)

```mermaid
flowchart TD
  TAN["<b>Joshua Tan</b><br/>Public AI lead · Fellow (CH) contact"]

  subgraph CORE["Swiss operational core (the role's remit)"]
    direction LR
    SPIU["Public AI Switzerland / SPIU<br/>the co-op it grows"]
    LAV["Oleg Lavrovsky · Datalets<br/>holds co-op dues"]
    NV["Nick Vincent<br/>co-research director"]
    BJ["Brandon Jackson<br/>product"]
  end
  TAN --> CORE

  subgraph REL["Swiss relationships to build"]
    direction LR
    APE["Bosselut · Schlag · Jaggi<br/>Apertus technical leads"]
    SAL["Marcel Salathé<br/>EPFL AI Center — bridge"]
    ICN["ICAIN · K. Frey<br/>co-stewarded public AI"]
  end

  subgraph WARM["Bridges and assurance allies"]
    direction LR
    ALEK["Alek Tarkowski<br/>Open Future · seminar S3"]
    CAV["B Cavello<br/>Aspen · Metagov board"]
    KLEIN["Samuel Klein<br/>verification-thesis ally"]:::lev
    MIY["Evan Miyazono · Atlas<br/>Metagov AI-gov RD"]:::lev
  end

  CHT["Charter — AI assurance and certification"]:::charter
  ALEK -.->|bridge into Tan's orbit| TAN
  KLEIN -.->|assurance affinity| CHT
  MIY -.->|assurance affinity| CHT

  classDef charter fill:#EEEDFE,stroke:#534AB7,stroke-width:2px,color:#26215C;
  classDef lev stroke:#534AB7,stroke-width:2px;
```

The role's detailed remit and the framing cautions live in the [Apertus note](apertus-fit-and-engagement-plan.md) (§5). Violet = the Charter's assurance angle; dashed = bridges / affinities.

## 2. How the key people actually connect (network)

```mermaid
flowchart LR
  TAN["<b>Joshua Tan</b><br/>Metagov co-founder · Public AI lead<br/>founding-paper author"]
  UTIL["Public AI utility<br/>+ Swiss co-op (SPIU)"]
  SEM(["Public AI Seminar"])
  TAN --> UTIL
  TAN --> SEM

  KLEIN["Samuel Klein<br/>co-founder · Underlay/Omnipedia"]
  ALEK["Alek Tarkowski / Open Future<br/>EU-policy arm"]
  CAV["B Cavello / Aspen"]

  KLEIN -->|S1 co-organiser| SEM
  CAV -->|S2 and S3| SEM
  ALEK -->|S3 co-organiser| SEM

  ALEK -.->|Open Future = coalition partner| TAN
  KLEIN -.->|co-founder, not a Metagov RD| TAN
```

- **Joshua Tan — the nucleus.** Metagov co-founder; co-author of the founding paper *[An Alternative to Regulation: The Case for Public AI](https://arxiv.org/abs/2311.11350)* (Vincent, Bau, Schwettmann, Tan; Nov 2023); leads product/strategy; ran the seminar **Seasons 1–3**; operates the inference utility.
- **Alek Tarkowski / Open Future — the EU-policy arm.** Co-organised the seminar **Season 3 only** (Apr–Jun 2025) with Tan; authored Open Future's [White Paper on Public AI](https://openfuture.eu/publication/white-paper-on-public-ai/) and the [Jan 2026 *European Public AI* brief](https://openfuture.eu/publication/european-public-ai-policy-brief/). **Not** a co-author of the founding paper — a well-placed peer, not Tan's principal.
- **Samuel Klein — co-founder, verification thesis.** Public AI Network co-founder; co-author of the *Infrastructure for the Common Good* whitepaper; seminar **Season 1** co-organiser; Berkman Klein affiliate, ex–Wikimedia Foundation trustee, works on Underlay / Omnipedia. Full profile in the [landscape note](metagov-public-ai-landscape.md).
- **B Cavello / Aspen Digital** — seminar Seasons 2–3; Metagov board — the convening backbone.

**Reading:** same movement, different lanes — Tan the intellectual/organisational core, Tarkowski the Brussels policy flank, Klein the verification/provenance founder. They intersect through the coalition and, for Tan × Tarkowski, through one seminar season. Treat these as professional peer ties, not proven close partnerships.

## 3. Apertus grounding confirmed this session

Both folded into the [Apertus note §1](apertus-fit-and-engagement-plan.md); recorded here so the people-map stays self-contained.

- **Antoine Bosselut co-leads Apertus *and* the Swiss AI Initiative** and sits on its Steering Committee (ETH + EPFL, equal voting power) — [swiss-ai.org](https://www.swiss-ai.org/team-3).
- **First government production use — canton Ticino** runs in-house document translation on a fine-tuned **Apertus-8B** (Artificialy-built; ~100 staff; in-canton data centre; no data leaves Swiss infrastructure) — [CSCS](https://www.cscs.ch/science/computer-science-hpc/2026/apertus-powers-in-house-ai-translation-for-ticino), [EPFL](https://actu.epfl.ch/news/apertus-powers-in-house-ai-translation-for-ticin-3/). *Sensitive-document translation in real government use is exactly where independent assurance would matter.*

## 4. Actor note — Marcel Salathé (bridge, not a role-holder)

*Public-source; re-verify before outreach. Salathé appears above as a "Swiss relationship to build," not a coalition member — this note is the guardrail against overclaiming him.*

- **What he is** — EPFL Associate Professor and **co-director / founder of the EPFL AI Center** ([EPFL](https://people.epfl.ch/marcel.salathe?lang=en), [AI Center](https://ai.epfl.ch/about/)); a visible public interpreter of **Apertus** (hosted the Inside AI episode with Bosselut / Jaggi / Schlag; argued ["AI sovereignty is a spectrum, not a switch"](https://engineeringprompts.substack.com/p/ai-sovereignty-is-a-spectrum-not)); close to **SNAI** / the Swiss AI Initiative; linked to democratic-legitimacy work (the EPFL [Citizens' Assembly on AI](https://ai.epfl.ch/innovation/citizens-assembly-on-ai/), the [Geneva AI Initiative](https://ai.epfl.ch/innovation/geneva-ai-initiative/), CH++, AMLD, AIcrowd, Swiss {ai} Weeks). A high-leverage EPFL / SNAI / Apertus **ecosystem bridge**.
- **What he is *not* (don't overclaim)** — not an Apertus *technical* lead (that is Schlag / Bosselut / Jaggi); not a verified **PublicAI / publicai.ch / SPIU / Metagov / Current AI** role-holder; no control over Apertus governance, SNAI decision rights, or the official Geneva 2027 process. Public posts and podcasts show interest and influence — not partnership or endorsement.
- **How to use him** — best as an **orientation / correction / framing** contact *once a concrete artifact exists*; weak as a first ask for adoption or governance ownership. Keep the Public AI / Metagov route (Tan, direct) separate. Natural ask: *"We're drafting a public governance-and-evidence layer for open public-AI deployments — Apertus as a motivating case, not a client. What is technically wrong, politically unhelpful, or duplicative from the EPFL / SNAI view?"* For technical detail, El-Assady / Schlag / Bosselut / Jaggi are better routes.
- **Name him as** — "Marcel Salathé, EPFL AI Center co-director and public Apertus/SNAI-adjacent voice." Avoid "Apertus lead," "Public AI / Metagov bridge," or "supporter / partner / endorser."

## Reading

- The role's decisions route through **Tan**; the Charter's distinct contribution is **independent assurance**, where **Klein** and **Miyazono / Atlas** are the nearest allies.
- The Swiss relationships the role builds run through **Salathé** (ecosystem bridge), the **Apertus leads** (Bosselut / Schlag / Jaggi), and **ICAIN / Frey** (co-stewarded angle).
- Tan, Tarkowski (Open Future / EU policy), Klein (verification), and Cavello (Aspen) are the coalition's connective figures — peers in one movement, not a hierarchy.

## Provenance

Built 2026-07-03 from primary sources: [Public AI Seminar](https://publicai.network/seminar.html), [The Case for Public AI (arXiv 2311.11350)](https://arxiv.org/abs/2311.11350), [Open Future](https://openfuture.eu/), [Berkman Klein — SJ Klein](https://cyber.harvard.edu/people/sklein), the [Fellow posting](https://publicai.network/jobs/fellow-switzerland), [swiss-ai.org team](https://www.swiss-ai.org/team-3), [CSCS](https://www.cscs.ch/science/computer-science-hpc/2026/apertus-powers-in-house-ai-translation-for-ticino) and [EPFL](https://actu.epfl.ch/news/apertus-powers-in-house-ai-translation-for-ticin-3/) on Ticino. Facts cited inline; assessments labelled. The Salathé actor note (§4) folds a former standalone profile; its public EPFL / AI Center / Apertus-commentary / citizens'-assembly sources are linked inline.
