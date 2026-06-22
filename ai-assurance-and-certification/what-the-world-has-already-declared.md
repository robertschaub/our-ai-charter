> **Status: WIP / DISCUSSION** — the summaries of the instruments are factual reference; the mapping to the five public obligations is a proposed reading, open for comment.

# What the world has already declared (and what's still missing)

_Reference companion to the manifesto line: "The world has already declared what AI must respect — the Universal Declaration of Human Rights, UNESCO's AI ethics recommendation, the Council of Europe's AI treaty. This is the part that turns those declarations into something you can insist on."_

_Three instruments already say what AI must respect. They differ in force — one is foundational, one is a global consensus, one is binding law — and none of them, on its own, makes those promises checkable. This page captures their essence and maps them to the charter's five public obligations. Current mechanism details are split across the [Founding Accord](founding-accord.md), [certification model](certification-model.md), and [protocol](grounding-faithfulness-and-contestability.md)._

---

## 1. Universal Declaration of Human Rights (UDHR, 1948)

**Status:** foundational, **non-binding** declaration; the moral bedrock under most later human-rights law.

Articles most relevant to AI:
- **Art. 1** — dignity and equality
- **Art. 2** — non-discrimination
- **Art. 8** — the right to an effective remedy
- **Art. 12** — privacy, honour, and reputation
- **Art. 19** — freedom of opinion and expression, including the right to seek, receive, and impart information
- **Art. 27** — the right to share in scientific advancement and its benefits

## 2. UNESCO Recommendation on the Ethics of AI (2021)

**Status:** adopted by **all 193 member states** (Nov 2021); the first global AI-ethics standard, but **non-binding (soft law)**.

**4 values:** human rights & dignity · a flourishing environment and ecosystems · diversity & inclusiveness · peaceful, just, interconnected societies.

**10 principles:** (1) proportionality & do-no-harm · (2) safety & security · (3) fairness & non-discrimination · (4) sustainability · (5) right to privacy & data protection · (6) human oversight & determination · (7) transparency & explainability · (8) responsibility & accountability · (9) awareness & literacy · (10) multi-stakeholder & adaptive governance.

**What makes it more than a list — implementation tools:** the **Ethical Impact Assessment (EIA)** (a structured pre-deployment review) and the **Readiness Assessment Methodology (RAM)** (a state's capacity self-assessment), plus ~11 policy action areas (data, education, labour/economy, health, gender, culture, communication & information, environment…).

## 3. Council of Europe Framework Convention on AI (2024)

**Status:** the **first legally binding international treaty on AI** (CETS No. 225) — adopted 17 May 2024, opened for signature 5 Sept 2024. Frame: AI and **human rights, democracy, and the rule of law**.

**Core principles (Ch. III):** Art. 7 human dignity & autonomy · Art. 8 transparency & oversight · Art. 9 accountability & responsibility · Art. 10 equality & non-discrimination · Art. 11 privacy & data protection · Art. 12 reliability · Art. 13 safe innovation.

**Unusually concrete procedural rights (Ch. IV):** **Art. 14 — remedies** for rights violations; **Art. 15 — procedural safeguards**, including the right to be **told you're interacting with an AI** and the ability to **contest** an AI-based decision. **Art. 16** adds a risk- and impact-management duty (with the option to ban/pause incompatible systems).

**Honest caveats:** binding, but with a **scope gap** — it directly covers AI used by **public authorities** (and private actors acting for them), and leaves the **wider private sector** to each party's discretion. And it is a *framework*: high-level obligations implemented through national law.

---

## 4. At a glance: declarations -> obligations

The instruments do not create the charter's five public obligations. They give each obligation public-law and public-ethics roots. The charter's move is to make those roots inspectable for a deployed system. These mappings are interpretive, not authoritative readings of the instruments.

| Charter obligation | UDHR anchor | UNESCO anchor | CoE AI treaty anchor | What a check can look for |
|---|---|---|---|---|
| **1. Purpose-bound** | Art. 1: dignity; Art. 27: benefits of scientific advancement | Proportionality and do-no-harm; impact assessment | Art. 16: risk and impact management | Assessed release, intended/prohibited uses, affected groups, impact assessment, known limits, misuse boundaries |
| **2. Answerable to people** | Art. 8: effective remedy | Human oversight; responsibility and accountability | Arts. 14-15: remedies and procedural safeguards | Named accountable entity; reachable complaint route; human review; logged restriction, recall, shutdown, external-order, or significant-change decisions |
| **3. Safe, secure, private, and resilient** | Art. 12: privacy; Art. 27: share in scientific advancement | Safety and security; privacy and data protection; sustainability | Arts. 11-13: privacy, reliability, safe innovation | Security/privacy controls; dependency map; continuity and exit paths; incident response; no single-vendor lock on the standard or evidence |
| **4. Fair in practice** | Art. 2: non-discrimination | Fairness and non-discrimination; diversity and inclusiveness | Art. 10: equality and non-discrimination | Disparate error/refusal monitoring, affected-group analysis, published limitations, escalation and remedy |
| **5. Open to evidence and correction** | Art. 19: seek, receive, and impart information; Art. 12: reputation | Transparency and explainability; adaptive governance | Arts. 8-12: transparency, accountability, reliability | AI disclosure; claim-to-source support; uncertainty signals; correction, incident, change, and withdrawal records |

---

## 5. Crosswalk — declared principle → testable check → obligation

Obligations: **(1) Purpose-bound · (2) Answerable to people · (3) Safe, secure, private, and resilient · (4) Fair in practice · (5) Open to evidence and correction.**

| Declared principle (source) | A concrete, testable check | Obl. |
|---|---|---|
| Transparency / explainability (UNESCO P7; CoE Art. 8); receive information (UDHR 19) | User is told it's AI; the sources behind a factual claim are viewable | 5 |
| Human oversight (UNESCO P6; CoE Art. 8) | A named human can review, override, or halt consequential outputs; the path is documented | 2 |
| Right to contest (CoE Art. 15) | Anyone affected by an AI decision can challenge it and get human review | 2 |
| Remedy (CoE Art. 14; UDHR 8) | A working complaint channel with a published response time; complaints logged | 2 |
| Accountability (UNESCO P8; CoE Art. 9) | A specific named entity is accountable, not "the algorithm" | 2 |
| Protection against unaccountable shutdown or manipulation (derived from accountability, remedy, transparency, and safe innovation) | Material restriction, recall, shutdown, or external-order handling is scoped, logged, reviewable, and paired with continuity/exit planning where public reliance is material | 2, 3 |
| Fairness / non-discrimination (UNESCO P3; CoE Art. 10; UDHR 2) | Tested for disparate error/refusal rates across groups; results on record | 4 |
| Privacy & data protection (UNESCO P5; CoE Art. 11; UDHR 12) | Data use documented, minimised, lawful; deletion available | 3 |
| Proportionality / do-no-harm (UNESCO P1) | A pre-deployment impact assessment (UNESCO-style EIA) was done and is available | 1 |
| Safety/security & reliability (UNESCO P2; CoE Art. 12) | Accuracy and failure rates measured and published; known failure modes disclosed | 3, 5 |
| Human dignity & autonomy (CoE Art. 7; UDHR 1) | No covert manipulation; persuasive/behavioural techniques disclosed | 1, 2, 5 |
| Multi-stakeholder & adaptive governance (UNESCO P10); safe innovation (CoE Art. 13) | Not single-vendor-locked; the audit record remains independently reviewable | 3, 5 |
| Share in scientific advancement (UDHR 27); sustainability (UNESCO P4) | Audit methods and results openly published | 3, 5 |

---

## 6. What's still missing — and what the charter adds

The declarations **declare**; none of them makes the promise **checkable** for a given system, or gives a buyer a lever today:
- **UDHR** — a value, not a mechanism.
- **UNESCO** — a global consensus, but *soft law*; it commits states politically, not legally.
- **CoE treaty** — *binding*, and uniquely concrete on contestability and remedy, but it binds **states/public bodies** and leaves the wider private sector to national discretion.

The charter's contribution is the operational layer the declarations lack: first, **pilot evaluation reports** against criteria like those above; later, if justified, a **public registry**, **revocation**, and **procurement teeth** — so the principles become something a deployer is *checked against and can lose public status for failing.* It especially translates the CoE treaty's procedural rights (notice, contest, remedy) and UNESCO's transparency/oversight principles into testable indicators.

**Caveat (non-negotiable framing):** a voluntary evaluation report or future mark **is not law**. It cannot enforce a treaty or compel a non-participant. It is **"aligned with"** these instruments, never "compliant with," and it **complements** the EU AI Act / CoE Convention by giving buyers and the public usable, checkable evidence **now** — for the systems and the private deployers the declarations don't yet reach.

---

_Sources: UDHR (un.org); UNESCO Recommendation on the Ethics of AI, 2021 (unesco.org); Council of Europe Framework Convention on AI, CETS No. 225, 2024 (coe.int). Article references verified against the instruments; the obligation-mapping is this project's proposed reading._
