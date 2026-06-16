> **Status: WIP / DISCUSSION** — working reasoning, not an adopted position.

# From Manifesto to Mechanism — deep dives

_Companion to the published article **"Trustworthy AI, Accountable to People"** (2026-06-14). It takes the sections readers find most abstract — **how you'd know it's real**, **who could drive it**, and **the world has already declared what AI must respect** — and turns each into specific, plain-language solutions a solo founder could actually start._

_Draft synthesis, 2026-06-14, for public discussion. It records reasoning and candidate directions, not adopted policy. Claims, figures, and legal-status wording should be checked against direct sources before citation._

---

## The through-line (read this first)

All five analyses converged on the same spine. If you remember nothing else:

1. **Don't build an authority. Build a test.** The credibility comes from *separation of roles*, not from anyone's say-so. Borrow the machinery that already protects your coffee, timber, and the padlock in your browser bar.
2. **Start with "shows its work," not "tells the truth."** The first auditable module is **grounding-faithfulness** — *is each checkable claim actually supported by the source the system itself cited?* — plus calibration and correction. That sidesteps the "Ministry of Truth" trap and is genuinely measurable, but it is only one module.
3. **Audit evidence and procedure, not perfect outcomes.** You don't certify that an AI never errs — you check whether it has the basics: defined scope, disclosure, sources, review routes, correction records, risk evidence, and withdrawal triggers.
4. **Start narrow and cheap; the founder convenes, never rules.** One 2–3 page audit rubric → one pilot → 3–5 named co-signers → a public report webpage → taken into *one* existing working group. Not a new institution.
5. **Demand is the engine.** A badge consumers ignore becomes a badge vendors chase the moment a *buyer* writes "must meet this evidence baseline" into a contract.

---

## 1 · HOW YOU'D KNOW IT'S REAL — the verification mechanism

**In one sentence:** a pilot report is only useful if the evidence can be checked and the status can be withdrawn; a future trust mark is only as good as the machinery that can *take it away*. Split the job into separate hands so no one marks their own homework, and check measurable things (does the cited source support the claim? is there a real correction log? can an objection actually stick?).

### A. The four separated roles — with people who already do exactly this

| Role | What they do | Who really does this today | Why the split matters |
|---|---|---|---|
| **1 · Standard-setter** | Writes the rules, owns the badge. Audits *no one*. | **FSC** writes forestry rules and owns the tree-tick logo but issues zero certificates; **Fairtrade International** sets standards and owns the mark. | If the rule-writer also judged compliance, "passing" would just mean "the author likes you." |
| **2 · Assessor (certification body)** | Independently audits an applicant; decides pass/fail. | **FLOCERT** (spun off from Fairtrade in 2003 precisely to break the link); **IFCN's** external assessors check fact-checkers against 31 criteria. | The judge must have no stake in the verdict. |
| **3 · Accreditor** | Licenses and polices the assessors; can suspend a bad one. | **ASI** audits FSC's certifiers; **IOAS** accredits ~77 organic certifiers; national bodies (UKAS, ANAB) accredit against **ISO/IEC 17065**. | Watches the watchmen — a captured assessor gets caught here, not by the public. |
| **4 · Peer body** | Keeps accreditors honest by peer-reviewing each other internationally. | **IAF** peer-evaluates national accreditors against **ISO/IEC 17011**, so a mark earned in one country is trusted in another. | Stops any single accreditor — or government — becoming the sole gatekeeper. No central throne. |

Read top to bottom: **someone writes the standard → an independent assessor audits against it → an accreditor licenses and polices the assessors → a peer body keeps the accreditors honest.** Same chain behind ISO, organic/forestry labels, Fairtrade, and journalism's trust badges.

### B. What an audit *actually checks* (concrete, not hand-wavy)

**Obligation 1 — Purpose-bound**
- **Defined scope:** the operator names the assessed release, version, use-case, intended uses, prohibited uses, affected groups, known limits, risk tier, and reassessment triggers.
- **Misuse and impact boundaries:** foreseeable misuse, residual risks, and stakeholder impacts are documented before any public claim.

**Obligation 2 — Answerable to people**
- **Documented authority:** a public statement of *who* is accountable, who can restrict/recall/shut down, and on *what lawful basis*.
- **Working objection channel — tested live:** the assessor *files a test objection* and confirms it reaches a responsible decision-maker, with a written outcome and an appeal path. (This is the difference between a real mechanism and theatre.)
- **Control-intervention log:** restrictions, recalls, shutdowns, or external orders are recorded with date, scope, basis, decision-maker, and review route where disclosure is lawful; where disclosure is restricted, evidence is retained for confidential oversight where legally possible. If neither public disclosure nor confidential independent review is possible, the affected scope cannot keep a pilot listing or future mark claim.

**Obligation 3 — Safe, secure, private, and resilient**
- **Safety and security controls:** hazard analysis where relevant, cyber/LLM threat models, prompt-injection checks, tool/agent permission boundaries, output handling, and incident response are documented.
- **Privacy and provenance:** personal-data use, minimisation, consent or lawful basis where required, access/deletion routes, and data/model provenance are retained for review.
- **Continuity and exit path:** the operator documents critical providers, models, data sources, cloud/compute dependencies, and what happens if a critical provider withdraws; where exit is constrained, that limit is disclosed up front rather than discovered at failure.

**Obligation 4 — Fair in practice**
- **Disparate performance evidence:** affected groups, languages, regions, contexts, and accessibility needs are identified; relevant error/refusal/failure patterns are monitored; limits and disparities are recorded.
- **Escalation and remedy:** discriminatory or uneven harms have a route for human review, correction, escalation, or remedy.

**Obligation 5 — Open to evidence and correction**
- **Grounding-faithfulness:** draw a fresh, pre-registered claim/citation sample sized for the use-case, clustering, and risk tier; for each, check *does the cited source actually support the claim?* Score the failure *types*: no source cited · source doesn't say that · source says the opposite · misquoted · real-but-irrelevant · exaggerated beyond the source.
- **Calibration and uncertainty:** bucket the sample by the system's stated confidence; "high confidence" should be supported more often than "low confidence"; uncertainty and abstention should be measured, not guessed.
- **Lifecycle evidence:** material-change logs, drift/currentness checks, incident records, release risk assessments, correction records, re-checks, and withdrawal triggers remain available for independent review.

> **Worked example:** an AI says *"the minister was convicted of fraud in 2021,"* citing a court document. The document says the minister was *investigated*, not convicted. → **Fails grounding-faithfulness.** The audit never decides guilt or innocence — only whether the cited source supports the claim. It doesn't.

### C. Worked example — "Lab X volunteers for a pilot report" (8 steps)

1. **Volunteer** for an independent pilot evaluation, naming the exact product + version ("ClarityAssistant v4.2"); pay a flat fee if pilots are not grant-funded.
2. **Evidence pack:** legal-scope map, responsibility map, scope and risk boundaries (Obl 1); accountable owner + objection-channel design (Obl 2); provider/dependency/security/privacy evidence (Obl 3); fairness limits where relevant (Obl 4); query access, existing correction log, risk register, and privacy-preserving release risk assessment (Obl 5).
3. **Independent sampling:** the *assessor* (not Lab X) draws a fresh, pre-registered claim/citation sample sized for the use-case, clustering, and risk tier, scores faithfulness, calibration, correction — and **files one test objection** to see if it sticks.
4. **Findings & remediation:** say faithfulness lands below the proposed bar — findings issued, fixed window to remediate, re-sampled. The report records the result; no certificate or mark is issued in Phase 1.
5. **The pilot report card** (what's actually published):
   > **Pilot evaluation report — ClarityAssistant v4.2**
   > Scope: English Q&A with cited sources · Evaluated 2026-09-01
   > Evaluator: [independent body/person] · Method: [draft version]
   > **Reports:** grounding-faithfulness rate on independent sample; correction process; tested objection mechanism.
   > **Does NOT claim:** certification, truth, legal compliance, other languages, versions, use-cases, or modules not assessed.
6. **Public report entry** (free): product + version, scope, dates, evaluator, method version, link to a redacted evaluation summary. Any future mark would need a registry; the current phase needs a public report index.
7. **Surveillance:** annual re-sampling at minimum (IFCN re-checks yearly), plus spot-checks on complaints, material incidents, and assessor-reviewable material updates — and *more often* for systems that ship weekly updates.
8. **Withdrawal triggers** (report index says *withdrawn, with reason*): re-check drops below reported bar · correction log found falsified · objection channel shown to be theatre · material control intervention cannot be independently reviewed · evaluated version silently swapped · release risk assessment materially false or over-redacted · report marketed beyond its stated scope.

### D. Anti-gaming guards — each tied to a real failure

1. **No self-certification — independent sampling only.** *ENERGY STAR* was largely self-certified until 2010, when investigators got the label onto a fake "air cleaner" (a space heater with a feather duster and fly strips taped on) — 15 bogus products in all. Fix: required third-party testing. Our audit samples real outputs the applicant can't pre-select.
2. **Break the fee-capture loop.** Where a scheme depends heavily on logo royalties or per-product fees, it creates structural pressure to over-certify big payers. So: assessors are paid a **flat fee regardless of outcome**, and the standard-setter doesn't live off per-product royalties from the labs it judges.
3. **Police the assessors, with graduated sanctions.** ASI can suspend a drifting FSC certifier; Ostrom's commons research shows enforcement works best **graduated** (warning → fine → expulsion). Audit-shopping dies when the accreditor catches and suspends the soft assessor.
4. **Beat citation-theatre / provenance-theatre at the measurement layer.** Browsers didn't argue with bad certificate authorities — when *DigiNotar* was breached and *Symantec* mis-issued, Mozilla/Google/Apple simply removed them from the trusted list. A system that cites lots of sources that don't support its claims *fails the faithfulness sample*; a fake correction log *fails the re-run test*; the ultimate sanction is removal from the registry.
5. **Audit *procedure*, not *outcome*.** GDPR doesn't demand perfect algorithmic decisions; it demands the *plumbing* for accountability — human intervention, the right to express a view and contest. Certify that the steering wheel and brakes exist, not that the car never crashes. (Same instinct as JTI's "process, not content" standard.)
6. **Design for pluralism, publish dissent.** Run it like IETF/W3C: public drafts, public comments, visible objections, version history; non-Western reviewers from day one. The guard against "a self-appointed Western club governing global AI speech" is *visible* openness, cheaply.

### E. The demand engine — why this isn't just a nice badge

Consumers largely ignore trust badges and privacy labels. **Enterprises don't** — they adopt standards to manage liability (see **SOC 2**, **FedRAMP**). So aim first at **B2B procurement**: get a public broadcaster, a library consortium, or a government digital-service buyer to write *"must meet this evidence baseline"* into contracts. Later, if a mark exists, buyers can require the mark. Demand — not marketing — funds the whole chain (it's also what lets Phase 1 grow into Phase 2).

### F. Phase 1 vs Phase 2 — start light, ride existing rails

- **Phase 1 (now, run by a few people):** **five public obligations + operational duties → independent pilot evaluators → public evaluation reports → visible withdrawal if the report is misused, the evaluated system changes materially, or a material control intervention cannot be independently reviewed**. No mark, no certificate, no accredited assessor yet. **Call it a *pilot evaluation* or *pre-standard test*, not "certification," until it's earned**.
- **Phase 2 (only at scale):** formalise the chain — assessors accredited to **ISO/IEC 17065**, a national accreditation body as accreditor, **IAF peer review under ISO/IEC 17011** across borders. The path organic and Fairtrade already walked.

**Honest hard parts (not solved by structure alone):** (1) setting the faithfulness threshold + sample size so they're *affordable for a pilot yet statistically meaningful*; (2) auditing fast-changing models — v4.2 passes, a silent update breaks it — which is why every report is pinned to an exact version and frequent updates require re-checks.

---

## 2 · WHO COULD DRIVE IT

**In one sentence:** trust schemes are *convened* by a credible initiator and *hosted* inside an existing neutral body — almost none are built by the people who run the audits — so a solo founder's job is to **write one sharp criterion and walk it into a room that already exists**, not to found an institution.

### A. The three founding patterns (with real examples)

- **NGO stewards a standard, a standards body publishes it.** *Journalism Trust Initiative* — RSF convened ~130 experts (2018); AFNOR/DIN facilitated; **CEN published it as CWA 17493 (Dec 2019)**. RSF never had to become an auditor. *IFCN Code of Principles* — Poynter (a respected neutral nonprofit) launched it (2015–16); assessment is delegated to independent assessors, not run by Poynter staff.
- **Neutral technical host owns the venue; anyone joins the working group.** *OpenSSF* (Linux Foundation, 2020). *Coalition for Secure AI (CoSAI)* — an **OASIS** Open Project (2024) giving Google/IBM/Microsoft/NVIDIA/Anthropic/OpenAI a neutral shell so no one "owns" it.
- **A coalition governs the rules collectively.** *CA/Browser Forum* (2005) — the parties who *enforce* the rules (browsers) sat with those who must *meet* them (CAs). *AI Alliance* (IBM/Meta, Dec 2023) — open-membership, already produces substance (its Trust & Safety WG has 230+ participants) — but industry-led, which matters below.

**The recurring lesson:** convene a coalition, host inside an existing body, anchor to groups already doing the work. *No one built the host themselves.*

### B. Candidate hosts for an *information-integrity* standard — ranked

1. **A journalism-trust body — EFCSN or RSF/JTI (top pick for legitimacy).** Closest existing thing to "does the source show its work," with a working assessor model. *Risk:* built for *human* fact-checkers and Europe-centric — an AI-honesty annex is a genuine extension.
2. **A neutral tech host — OASIS or Linux Foundation (strong second for the venue).** Ready-made neutral governance, IP rules, a working-group venue tomorrow (CoSAI already lives at OASIS). *Risk:* optimises for engineering interop, not editorial/honesty norms — substance must come from elsewhere. **IEEE SA** — the IEEE 7000 / CertifAIEd track — is another possible tech-host option.
3. **MLCommons — measurement anchor, not host.** Its AILuminate benchmark shows it can run rigorous multi-stakeholder evaluation. Treat it as the *evaluation partner*.
4. **Digital Public Goods Alliance — Global-South legitimacy + a registry pattern.** *Risk:* its standard is open-source eligibility, not output honesty — adjacent, not aligned.
5. **AI Alliance Trust & Safety WG / Current AI — traction + money.** Both lean industry/foundation: great as members and funders, weaker as the *neutral face*.

> **Opinionated verdict:** *split the roles* — anchor **methodology + legitimacy** in the fact-checking world (EFCSN/RSF), host the **technical standard + registry** at a neutral tech body (OASIS / Linux Foundation), bring in **MLCommons** as the measurement partner. **Don't build a new organisation.** No single existing body covers both "honesty methodology" and "neutral technical governance," which is exactly why it's a split.

### C. The founding coalition — 6–10 seats, chosen by *role* not prestige

Each seat answers one question:

| Seat | Answers the question |
|---|---|
| A standards / neutral-host body (OASIS or Linux Foundation) | *Who hosts it?* |
| A fact-checking / journalism-trust body (EFCSN or RSF) | *Who proves it's honest?* |
| An open-model lab (an AI-Alliance / Hugging-Face-type participant) | *Who proves it's buildable?* |
| An academic evaluation lab (a university group already in MLCommons) | *Who measures it independently?* |
| A Global-South partner (a fact-checking org / DPGA member outside EU-US) | *Who isn't European?* |
| A procurement / buyer voice (public broadcaster, library consortium, gov digital-service buyer) | *Who will actually buy it?* — without this it's a press release |
| *Optional:* a consumer-protection NGO; **one** mainstream AI vendor (one, not a bloc) | keeps substance honest without ceding control |

### D. The solo-founder 90-day plan — one person, ~70% time, tiny budget

The highest-leverage move is **not to found anything** — it's to write one sharp criterion and walk it into a room that already exists. (Exactly how **Global Privacy Control** began in 2020: a tiny group published a one-page signal, took it to the W3C, browsers adopted it.)

- **Days 1–30 — write the artefact.** A 2–3 page **"Grounding-Faithfulness & Contestability Evaluation Protocol v0.1"**: scope (factual AI systems that cite sources) · what the report does/doesn't mean · sampling method · claim↔source scoring rubric · correction-log + contestability requirements · conflict-of-interest rule · a one-page sample evaluation report. Publish it openly, versioned.
- **Days 31–60 — find the first door.** Take it to **one** existing working group. **Most likely first door: the AI Alliance Trust & Safety WG** (open membership, low barrier, already cataloguing evaluation tooling). Second door: **EFCSN** (fact-checking-native home). Third: an **OASIS** discussion group.
- **Days 61–90 — co-signers + a report index.** Secure **3–5 named allies** to co-sign, and stand up a one-page public **report index** (a GitHub page listing pilot reports + links to evidence). Cheap — but it makes the method *real*. **Run a pilot evaluation on 1–2 real systems** (one open-weight, one proprietary) and publish the anonymised result as proof-of-concept.

> **Outreach sequence — ask each for the *smallest possible yes*:**
> 1. **First:** a named contact in the **AI Alliance Trust & Safety WG** — *"May I bring a 2-page honesty-criterion contribution to your next call?"* (not membership, not money).
> 2. **Second:** an **EFCSN / RSF-JTI** methodology lead — *"Would you review this against your transparency criteria and lend your name as a reviewer?"* (borrows legitimacy, costs them nothing).
> 3. **Third:** one **academic eval lab** already in MLCommons — *"Would you co-sign and help define one testable check?"* (turns opinion into measurement).

You are collecting **signatures and a venue**, not running an audit.

### E. Failure modes and the cheapest guard against each

| Failure mode | Real precedent | Cheapest guard |
|---|---|---|
| **Founder / big-tech capture** | GPAI struggled because control "rested with the two founders" | Host inside a neutral body from day one; write a **sunset clause** on the founder's role |
| **Closed-club dynamics** | Frontier Model Forum's compute thresholds read as an incumbent moat | Make the criterion **size-neutral** & open-membership — a tiny tool complies as easily as a frontier lab |
| **Ethics-washing / pay-to-belong** | Partnership on AI funded by Apple/Amazon/Meta/Google/IBM/Microsoft | Publish all funding; **cap any single funder's share**; keep certification delegated to independent assessors (IFCN model) |
| **Starting a new silo** | New standards orgs are the most common slow death | **Refuse to incorporate** — the artefact is a contribution to an existing body; the report index is a webpage |
| **Standards proliferation** ("now there are 15 competing standards") | NIST AI RMF, ISO/IEC 42001, OECD already exist | Build a **plug-in, not a silo**: position it as the *Grounding & Contestability module* that snaps into **NIST AI RMF** / **ISO/IEC 42001** — "they tell you *how* to manage AI risk; we provide the specific test for honesty and contestability" |

**The honest summary:** a solo fact-checker can credibly **convene** a trustworthy-AI honesty standard — by writing one criterion, borrowing one host, recruiting five names — but cannot and must not try to **run** it.

---

## 3 · THE WORLD HAS ALREADY DECLARED WHAT AI MUST RESPECT

**In one sentence:** three real, authoritative instruments already say what AI must respect — but a declaration is a *promise, not a test*; the mark's job is to convert their principles into concrete, checkable audit criteria a deployer can be held to and can *lose the mark* for failing.

### A. The three instruments, exactly as they stand

- **Universal Declaration of Human Rights (UDHR, 1948)** — foundational, **non-binding** declaration; the bedrock of later treaties. Most AI-relevant articles: **Art. 1** (dignity & equality), **Art. 2** (non-discrimination), **Art. 8** (effective remedy), **Art. 12** (privacy, honour, reputation), **Art. 19** (freedom of opinion/expression, incl. the right "to seek, receive and impart information"), **Art. 27** (share in scientific advancement).
- **UNESCO Recommendation on the Ethics of AI (Nov 2021)** — first global AI-ethics standard, adopted by all 193 member states; **non-binding (soft law)** but the most widely endorsed statement there is. Ten named **principles**: *proportionality & do-no-harm; safety & security; fairness & non-discrimination; sustainability; right to privacy & data protection; human oversight & determination; transparency & explainability; responsibility & accountability; awareness & literacy; multi-stakeholder & adaptive governance.* Plus two concrete tools: the **Ethical Impact Assessment (EIA)** and the **Readiness Assessment Methodology (RAM)**.
- **Council of Europe Framework Convention on AI (adopted 17 May 2024; opened for signature 5 Sep 2024)** — the **first legally binding** international AI treaty. *Scope nuance:* it directly covers AI used by public authorities (and private actors acting for them), leaving each party to decide how to handle the wider private sector. Core principles (Ch. III, by article): **human dignity & autonomy (Art. 7); transparency & oversight (Art. 8); accountability & responsibility (Art. 9); equality & non-discrimination (Art. 10); privacy & data protection (Art. 11); reliability (Art. 12); safe innovation (Art. 13).** Ch. IV adds unusually concrete procedural rights: **remedies (Art. 14)** and **procedural safeguards (Art. 15)** — incl. *being told when you're interacting with an AI* and *being able to contest* an AI-based decision.

### B. The crosswalk — declaration → testable audit criterion

Each row maps one named principle to a concrete test, and to the obligation it reinforces: **(1) Purpose-bound · (2) Answerable to people · (3) Safe, secure, private, and resilient · (4) Fair in practice · (5) Open to evidence and correction.**

| # | Principle (source) | Concrete, testable audit criterion | Obl |
|---|---|---|---|
| 1 | Transparency & explainability (UNESCO); transparency/oversight, Art. 8 (CoE) | User is clearly told, at first contact, they're interacting with an AI — not a human. | 5 |
| 2 | Transparency (UNESCO); right to *receive information*, Art. 19 (UDHR) | Every factual claim is traceable to its sources; the user can view them. | 5 |
| 3 | Human oversight & determination (UNESCO); oversight, Art. 8 (CoE) | A named human can review/override/halt consequential outputs; the path is documented and reachable. | 2 |
| 4 | Procedural safeguards / right to contest, Art. 15 (CoE) | Anyone affected by an AI decision has an accessible, documented way to challenge it and get human review. | 2 |
| 5 | Remedies, Art. 14 (CoE); Art. 8 (UDHR) | A working complaint channel with a published response time; complaints logged and auditable. | 2 |
| 6 | Accountability & responsibility (UNESCO); Art. 9 (CoE) | A specific, named legal entity is accountable for outputs and harms — not "the algorithm." | 2 |
| 7 | Fairness & non-discrimination (UNESCO); Art. 10 (CoE); Art. 2 (UDHR) | Tested for disparate error/refusal rates across protected groups, languages, regions; results on record. | 4 |
| 8 | Privacy & data protection (UNESCO); Art. 11 (CoE); Art. 12 (UDHR) | Personal-data use documented, minimised, lawful; users can see what's held and request deletion. | 3 |
| 9 | Proportionality & do-no-harm (UNESCO) | A pre-deployment impact assessment (UNESCO-style EIA) completed and available to the auditor. | 1 |
| 10 | Safety & security (UNESCO); reliability, Art. 12 (CoE) | Accuracy/failure rates measured and published; known failure modes disclosed, not hidden. | 3, 5 |
| 11 | Human dignity & autonomy, Art. 7 (CoE); Art. 1 (UDHR) | No covert manipulation; persuasive/behavioural techniques are disclosed. | 1, 2, 5 |
| 12 | Awareness & literacy (UNESCO) | Users get plain-language info on the system's limits and how to read its outputs. | 5 |
| 13 | Multi-stakeholder & adaptive governance (UNESCO); safe innovation, Art. 13 (CoE) | Not single-vendor-locked: the audit record remains independently reviewable. | 3, 5 |
| 14 | Share in scientific advancement, Art. 27 (UDHR); sustainability (UNESCO) | Audit methods and results are openly published so benefits and risks are public knowledge. | 3, 5 |

### C. A complementary practical tool — the "Developer's Translation Matrix"

Engineers can't code toward "human dignity"; they code toward constraints. So pair the crosswalk above (for *policy* readers) with a one-page builder-facing table (for *product* teams):

| Treaty right | UX requirement | Backend requirement |
|---|---|---|
| Right to remedy (UDHR Art. 8; CoE Art. 14) | An "Appeal" button in the interface | Log every false-positive filter block; track appeals filed / granted |
| Notice you're dealing with AI (CoE Art. 8/15) | A persistent "AI" disclosure at first contact | — |
| Transparency / receive information (UNESCO; UDHR Art. 19) | Clickable citation behind each factual claim | Store the claim↔source mapping for audit |
| Explainability / over-reliance (UNESCO) | Show a confidence/uncertainty signal | Compute and expose per-claim confidence |

This is itself a strong **90-day artefact** — publishable on GitHub/LinkedIn, it proves the founder understands *both* the law and the software.

### D. What the mark adds that the declarations don't

The declarations **declare**; the mark makes them **insistable**. Even the binding CoE treaty binds *states*, leaves the wider private sector to national discretion, and gives an individual buyer no lever to pull on a Tuesday afternoon. The mark closes that gap with four things a declaration can't provide: an **independent audit** against the criteria above; a **public registry** so anyone can check a badge; **revocation** when a system stops meeting the bar; and **procurement teeth** so buyers can require it by contract. In particular it turns the CoE treaty's procedural rights — notice (Art. 8/15), contestability (Art. 15), remedy (Art. 14) — plus UNESCO's transparency/oversight principles, from text in a treaty into conditions a deployer is *checked against and can lose the mark for failing*.

### E. One honest caveat (and the language to use)

A voluntary trust mark **is not law**. It cannot enforce a treaty, levy a fine, or compel a non-participant; it does **not** replace the EU AI Act or the CoE Convention. Its role is narrower and complementary: a usable, checkable signal **now**, ahead of and alongside binding regulation. So use careful wording: **"aligned with"** the instruments, not "compliant with"; **"testable indicators inspired by,"** not "legal certification." Jurisdiction-specific legal claims need counsel. (The model here is the **UN Guiding Principles on Business & Human Rights**: identify, prevent, mitigate, remedy — without pretending a private audit replaces courts or regulators.)

---

## Consolidated 90-day plan (one coherent sprint for one person)

Merging the three topic-specific plans into a single path:

1. **Write the v0.1 artefact** (≤ 3 pages): the *Grounding-Faithfulness & Contestability Audit Protocol* + the *Developer's Translation Matrix* on the back page. Scope it to **one** use-case (e.g. news/Q&A with cited sources). Versioned, openly published.
2. **Run one pilot audit** on 1–2 real systems (one open-weight, one proprietary), by hand, with one fellow fact-checker. Publish the anonymised "nutrition label." **Call it a pilot, not certification.**
3. **Walk it into one existing room** — first door the **AI Alliance Trust & Safety WG**; ask only for *"may I bring a 2-page contribution to your next call?"*
4. **Collect 3–5 named co-signers** (one fact-checking/JTI reviewer, one academic eval lab, one open-model dev, ideally one non-Western reviewer) and stand up a **public registry webpage**.
5. **Find one buyer** willing to say *"we'd require this"* — the demand seed that makes everything after it real.

Total cost: a few hundred francs and the founder's time. Builds nothing that must be funded.

---

## Where the five analyses agreed — and diverged

**Unanimous:** separation of roles; grounding-faithfulness (not truth); audit procedure-not-outcome; start narrow & cheap; convene-don't-rule; plug into existing bodies rather than found a new one; "aligned with" not "compliant with."

**Divergences / unresolved choices:**
- **Host choice.** One option is a *3-way split* (EFCSN/RSF + OASIS/LF + MLCommons); another is pitching the work first inside AI Alliance, MLCommons, or IEEE SA. Reconciled direction: legitimacy from fact-checking, venue from a neutral tech host, measurement from MLCommons; first practical door = AI Alliance T&S WG.
- **B2B vs B2C demand.** Consumers often ignore badges; enterprise and public procurement may be the engine (SOC 2 / FedRAMP analogy). Elevated to §1E.
- **Procedure-not-outcome framing.** The strongest version tests the steering wheel and brakes — complaint routes, correction logs, review powers — without claiming the system never crashes.
- **Naming discipline.** Early work should be called *pilot evaluation* or *pre-standard testing*, not certification, and should publish dissent for pluralism.

## Open / honest hard parts (carry into any next draft)

- Faithfulness **threshold + sample size**: affordable for a solo assessor *and* statistically meaningful — genuinely unsolved, needs a statistician.
- **Fast-changing models**: version-pinning + continuous surveillance and controlled updates, not annual-only.
- **Goodhart risk**: a behavioural floor could breed citation-theatre and reflexive hedging — guard is measuring *support* (not citation count) and re-running logged errors, but it needs live testing.
- **Legitimacy optics**: avoid "a Western fact-checking club governing global AI speech" — non-Western reviewers and public dissent from day one.

---

## Sources (selected; verify before citation)

**Certification machinery:** ISO/IEC 17065 (iso.org/standard/46568.html); ISO/IEC 17011 (blog.ansi.org/anab/overview-of-iso-iec-17011); IAF/ILAC mutual recognition (wto.org); FSC certification system (connect.fsc.org); ASI as FSC accreditor (fsc.org); FLOCERT history (flocert.net); IOAS (ioas.org); IFCN application + US$350 fee (ifcncodeofprinciples.poynter.org/application-process).
**Anti-gaming precedents:** ENERGY STAR GAO-10-470 (gao.gov/products/gao-10-470); MSC logo-fee criticism (en.wikipedia.org/wiki/Marine_Stewardship_Council); Ostrom design principles (wiki.p2pfoundation.net); Mozilla DigiNotar removal (blog.mozilla.org/security/2011/09/02); Symantec distrust (wiki.mozilla.org/CA:Symantec_Issues); GDPR Art. 22.
**Drivers/hosts:** RSF/JTI + CEN CWA 17493 (rsf.org; jti-app.com/footer/cwa); IFCN (ifcncodeofprinciples.poynter.org); EFCSN code (efcsn.com/code-of-standards); OpenSSF (openssf.org/about); CoSAI/OASIS (oasis-open.org/2024/07/18/introducing-cosai); CA/Browser Forum (cabforum.org); AI Alliance (thealliance.ai/blog/our-first-year); MLCommons AILuminate (github.com/mlcommons/ailuminate); Current AI (philanthropynewsdigest.org); Global Privacy Control + W3C (globalprivacycontrol.org; w3.org/TR/gpc); GPAI/Brookings (brookings.edu); Partnership on AI (en.wikipedia.org/wiki/Partnership_on_AI); NIST AI RMF; ISO/IEC 42001; IEEE 7000 / CertifAIEd.
**Declarations:** UDHR (un.org/en/about-us/universal-declaration-of-human-rights); UNESCO AI Ethics Recommendation (unesco.org/en/artificial-intelligence/recommendation-ethics; full text OHCHR PDF); CoE Framework Convention on AI, CETS 225 (coe.int; analysis: fpf.org; state.gov).

_Provenance note: this is a public discussion synthesis from earlier research notes and model-assisted review. Treat it as a reasoning aid, not as authority; verify direct sources before public citation._
