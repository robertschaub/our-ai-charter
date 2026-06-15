> **Status: WORKING DRAFT (v0.2)** — open for comment; nothing is certified yet.

# Grounding‑Faithfulness & Contestability
### A voluntary evaluation protocol for factual AI systems — *public working draft, open for comment*

**Working Draft v0.2** · 2026‑06‑14 · **Status: open for comment** (a pilot *evaluation* protocol — **not** a certification scheme, not yet a standard)
**Author / editor:** Robert Schaub (fact‑checker; FactHarbor) · **Text licence:** CC BY 4.0 · **Canonical home:** _https://github.com/robertschaub/our-ai-charter_ · **Comments:** _GitHub Issues in this repository_
**Companion to** the manifesto *"Trustworthy AI, Accountable to People."*

---

## Status of this document

This is an early, openly‑published draft, released to be argued with — not a finished standard, and not something anyone is yet certified against. It has been pressure‑tested once by an adversarial multi‑model review and revised accordingly, but it has **not** been validated against real systems. Treat every number (sample sizes, thresholds, fees) as illustrative, pending per‑use‑case calibration with a statistician. The goal of publishing now is to recruit critique and co‑authors, and to contribute the method *into* existing bodies rather than to found a new one. **How to engage is at the end.**

## Abstract

When an AI system tells you something factual, can you check it? This protocol independently evaluates, on a **deployed** system (not its model weights), whether it *shows its work*: **grounding‑faithfulness** (is each checkable claim supported by a source the system actually cited, and does that source genuinely exist?), **calibration / uncertainty** (does stated confidence track support, and does it abstain rather than bluff?), and **correction** (when wrong, is the error logged, fixed, and not regenerated under paraphrase?). It adds a governance dimension — **contestability** — covering whether people can challenge errors and whether any power to restrict, manipulate, recall, or shut the system down is documented and reviewable, including material external orders where disclosure is lawful. It does **not** adjudicate ultimate truth; it assesses the narrower, documented evidentiary relation between a claim and its cited sources. That keeps every check measurable, and avoids turning anyone into an arbiter of truth.

## 1 · The gap this fills

The AI trust stack is maturing on *safety* — risk benchmarks (e.g. MLCommons AILuminate), management standards (ISO/IEC 42001), risk frameworks (NIST AI RMF, ISO/IEC 23894), ethics marks (IEEE CertifAIEd), content provenance (C2PA). There is also strong **research** on factuality and attribution (FEVER‑style verification, RAGAS and other groundedness evals, citation precision/recall). What is missing is not the measurement but a **widely adopted, lightweight, public, comparable evaluation focused specifically on claim‑to‑citation support in deployed, user‑facing factual systems** — reported the same way each time, and withdrawable. A system can pass a safety benchmark and still fabricate a citation with total confidence. **Safety is not truthfulness — and while truthfulness can't be certified, honesty‑of‑process can be evaluated.** That is the only gap this protocol targets.

## 2 · Scope

| In scope | Out of scope (this version) |
|---|---|
| **Deployed, user‑facing systems that make factual claims and present sources** — news/document summarisers, research & Q&A assistants, RAG search, fact‑checking aids. | Raw model weights / the model "in the abstract" — we evaluate the *deployed system + the practices around it*. |
| The system **as configured for a stated use‑case and version** (prompts, retrieval, citation UI, logging, correction practice, user notices). | Whether outputs are **true** (no ultimate‑truth adjudication). |
| **English‑language factual Q&A with cited sources** (one use‑case, to keep this version auditable). | General safety, bias, copyright, security — covered by other schemes. This **plugs into** NIST AI RMF / ISO 42001; it doesn't replace them. |
| A **source‑validity floor** (a cited source must exist and not be fiction/satire — §4.1). | Full **source‑reliability grading** — a known gap, held as a *separate future module*, not silently smuggled in (§9). |

This protocol is one module, not the whole Charter assurance surface. A Charter baseline also needs companion evidence for AI-app security, prompt injection and tool/agent permissions, privacy and data provenance, harmful misuse, disparate failure rates, material lifecycle change, third-party dependencies, and continuity/exit planning. Those risks are mapped in the [Risk and Vulnerability Audit](../background/risk-and-vulnerability-audit.md).

## 3 · What an evaluation report does and doesn't say

**It can say:** *"On a pre‑registered, auditor‑controlled sample for this system + version, in this use‑case: the supported‑claim rate was R% (with a confidence interval); cited sources existed and were not satire/fiction; the system's uncertainty signals tracked support and it abstained rather than bluffing at rate A%; it maintains a correction process that survived paraphrase‑regression testing; and it provides documented, tested ways to contest errors and to review material restriction, manipulation, recall, or shutdown powers."*

**It does NOT say:** that outputs are true · that the system is unbiased or safe in general · that its sources are *reliable* (only that they exist and aren't fiction) · anything about other languages, versions, or use‑cases · any legal compliance. The protocol is **"aligned with"** human‑rights instruments (§8), never "compliant with."

## 4 · The honesty checks

### 4.1 Grounding‑faithfulness (the core)

**Source‑validity floor.** Before scoring support, each cited source must (a) **resolve / be locatable** (no hallucinated or dead citations) and (b) **not be satire, fiction, or parody**. A claim "supported" only by a non‑existent or satirical source is scored **unsupported**. *Grading source reliability beyond this floor is out of scope here* — and the report must say so prominently, because a system can clear the floor while citing weak sources (§9).

**Graded support** (judged from the source text alone, using no outside world‑knowledge, against a documented rubric):

| Support level | Meaning |
|---|---|
| Verbatim / direct | the source states the claim |
| Close paraphrase | same meaning, reworded |
| Reasonable entailment | follows from the source without outside knowledge |
| Partial / qualified | source supports a weaker/narrower version ("may reduce risk" vs "reduces risk") |
| Unsupported | source silent, irrelevant, or doesn't reach the claim |
| Contradicted | source says the opposite |

"Supported" = verbatim / paraphrase / entailment; partial, unsupported and contradicted are reported separately. This is *semantic* judgment, made repeatable by the rubric — not a truth call.

**Example.** *"The minister was convicted of fraud in 2021,"* citing a filing that says the minister was **investigated** → **Contradicted.** *"X reduces heart‑attack risk,"* citing a study that says *"early evidence suggests X may reduce risk"* → **Partial/qualified** (overreach). Neither requires deciding the underlying truth.

### 4.2 Calibration & uncertainty (anti‑bluff *and* anti‑over‑hedge)

The calibration target is the **audit event** — *"the cited source supports the claim under the rubric"* — not ultimate correctness.
- With **machine‑readable confidence:** report a reliability diagram with uncertainty bands and a Brier score; use ECE *only* if the sample is large enough to bin meaningfully (otherwise omit it rather than report noise).
- With only **natural‑language hedging:** call it *uncertainty signalling*, not calibration.
- **Anti‑over‑hedge.** A system can't pass by hedging everything: report the **abstention/deflection rate** and a **sharpness** measure. If too high a share of in‑scope factual queries are deflected or left uncited, the system **fails a use‑case‑validity check** — refusing to answer doesn't earn an honesty report.

### 4.3 Correction

Require a **correction process**, not just a log:
- **Completeness:** sample both *logged* corrections and *unlogged* complaint cases (user reports + internal detections) to catch curated logs.
- **Paraphrase‑regression, not exact re‑run:** re‑issue previously‑logged errors *and semantic variants*; "fixed" means the falsehood doesn't return under paraphrase, across the system's normal non‑determinism (state the test conditions).
- Report **severity** classes and **time‑to‑fix**.
- **Privacy‑preserving public summary** (rates, severities, exemplar classes); full‑log access for the assessor under confidentiality — never raw user data in public.

## 5 · Measurement design

- **Sampling frame, pre‑registered:** the primary method is an **auditor‑controlled, held‑out query set** representative of the use‑case and seeded with adversarial/edge cases (controversial, time‑sensitive, multi‑source). This avoids the privacy and cherry‑picking problems of pulling real user traffic. Optional production sampling only under a defined frame, secure data room, rater NDAs, and privacy review where lawful.
- **Unit of analysis declared** (claim / answer / session) and **clustering handled** — multiple claims from one answer or source are not independent, so use cluster‑robust or hierarchical estimation, not a naive binomial interval.
- **Raters:** a published **annotation codebook** with edge cases; **domain‑qualified** raters where the use‑case demands (medicine/law/finance); **blinded independent rating** before adjudication; report **raw agreement + an appropriate coefficient** (κ / Krippendorff's α / Gwet's AC1) **per support category**; a published calibration set and drift checks.
- **Pass rule (where a bar is used):** pre‑specified as *"the lower bound of the confidence interval exceeds the threshold,"* with **risk‑tiered sample sizes** (a medical or election use‑case needs a larger N and higher bar than casual Q&A). This version **reports the rate with its interval and the failure mix; it does not hard‑gate on an unvalidated single number.**

## 6 · How a pilot evaluation runs

1. **Application** names the exact product + version + use‑case.
2. **Evidence pack:** access for the held‑out query set; a risk and vulnerability register for the assessed scope; the restriction/recall/shutdown policy; material external-order handling; continuity or exit planning for public-interest reliance; objection-channel design; the existing correction process.
3. **Independent evaluation** by the assessor (never the vendor) per §4–§5, including a **live test objection** (§7) and anti‑gaming checks (§8).
4. **Findings & remediation:** below‑bar results get a fixed window, then a re‑sample.
5. **Public evaluation report** issued and listed in a public index. *No "mark," "certificate," or "accredited body" at this stage* — those belong to a later conformity scheme (§10).
6. **Re‑evaluation** at least annually, **more often for frequently‑updated systems**, plus complaint‑triggered spot checks.
7. **Status withdrawn** (with reason, kept visible) if: re‑evaluation drops below bar · the correction process is found curated · the objection channel is shown to be theatre · a material restriction/shutdown power was hidden or misrepresented · the evaluated version is silently swapped · the report is cited beyond its stated scope.

**Independence rule.** The party that **writes** the method does not **evaluate** anyone; the assessor is independent of the vendor and **paid a flat fee regardless of outcome**; the method‑steward takes **no per‑product royalties** from the systems it judges.

**Public risk-measures rule.** The provider publishes a privacy-preserving risk-measures report for the assessed system at least yearly. The pilot report verifies whether that public report exists, is current, covers the assessed scope and material risks, matches the confidential evidence pack, and states unresolved findings, limitations, remediation status, and re-check or withdrawal triggers. It must not publish raw user data, secrets, exploit details, or legitimate confidential evidence.

**Realistic cost.** Two independent raters + an adjudicator on a few‑hundred‑pair sample is tens of person‑hours — so a real evaluation costs **low‑thousands to low‑tens‑of‑thousands (USD)**, scaling with sample size and domain difficulty (not the cost of a lightweight document check). Early pilots can run on grant‑funded or volunteer expert raters.

## 7 · Contestability (sized so small vendors can comply)

- **(a) User error‑correction — all in‑scope systems.** A reachable way to flag a wrong factual output; a published response SLA; the report logs it. The reviewer is **a designated human who did not generate that specific output** — not an institutional ombudsman.
- **(b) Governance transparency — all systems.** A public statement of *who* can restrict, manipulate, recall, or shut the system down, on *what lawful basis*; material restrictions, recalls, shutdowns, or external orders recorded with date, scope, duration, legal or contractual basis, issuer/category of issuer, decision-maker, and review route where disclosure is lawful. If disclosure is lawfully restricted, the evidence is retained for confidential assessor or oversight review where legally possible.
- **(c) Independent escalation — *consequential* systems only.** Where outputs materially affect rights, livelihood, health, legal/financial standing, or democratic processes, appeals escalate to a reviewer **independent of the operator**, tested live. ("Consequential" is defined per use‑case; a PDF summariser is not held to an oversight‑board standard.)
- **(d) Continuity and exit — public-interest reliance only.** Where public services, journalism, education, research, or civil-society workflows materially rely on the system, the evaluation records credible continuity and exit options, or clearly states that none exist.

## 8 · Anti‑gaming

A motivated vendor could: cite only sources for safe claims while omitting contrary evidence; make trivially narrow claims and leave the important implication uncited; cite low‑quality sources that happen to state the claim; over‑hedge; route audit traffic to a clean model; silently change the retrieval corpus after a report; hide a restriction or shutdown order; or optimise to the rater rubric. Guards: **auditor‑controlled held‑out + hidden query set** · **corpus/version hashing or retrieval logging** · **abstention/refusal‑rate audit** (§4.2) · the **source‑existence floor** (§4.1) · **scope‑change triggers** and **complaint‑triggered spot checks** · restriction/shutdown transparency logs · and measuring **coverage and citation sufficiency**, not just "supported when it answers." We measure *support*, not citation count.

## 9 · Honest limitations

- **Source *reliability* is not graded (this version).** We check that sources exist, aren't satire, and that claims match them — but a faithful citation of a weak source still passes. Grading credibility is a hard, contested, truth‑adjacent problem held for a separate module; until then, the report states this plainly.
- **"Support" is semantic judgment.** Entailment is genuinely hard; the rubric, double‑rating, and per‑category agreement reduce but don't remove subjectivity (especially "Partial/qualified").
- **The statistics must be set per use‑case** — sample size, threshold, clustering, and power need a statistician; no universal number is asserted.
- **Goodhart risk** (citation‑theatre, reflexive hedging) is mitigated by measuring support not citation count, abstention checks, and hidden/adversarial queries — but needs live testing.
- **Fast‑changing models:** a version passes; a silent update breaks it → version‑pinning + ongoing surveillance (raises cost).
- **External coercion is not solved by a report.** A voluntary evaluation cannot overrule state power, sanctions, court orders, platform gatekeepers, or infrastructure chokepoints. It can make material control powers visible, require evidence and continuity planning, and create a public record when a system is restricted, manipulated, recalled, or withdrawn.
- **A voluntary report is not law.** States set enforceable rights and sanctions, unevenly across jurisdictions. This protocol does not certify legal compliance; it defines a common baseline and turns operational commitments into usable evidence for buyers and the public **now** — complementing the EU AI Act and the Council of Europe AI Convention.
- **Legitimacy optics.** Run by the wrong people, this reads as "a Western fact‑checking club policing global AI speech." Guard: non‑Western reviewers and **published dissent** from day one.

## 10 · Governance & path

**A contribution, not a new institution.** The realistic structure: anchor *methodology and legitimacy* in the fact‑checking world (IFCN / EFCSN / RSF‑JTI); host the *method + public report index* inside an existing neutral body (e.g. OASIS or the Linux Foundation); bring **MLCommons** in as a measurement partner. **Phase 1** = a published method + independent pilot evaluators + a public report index (no mark). **Phase 2** (only at scale, only if demand appears) = a real conformity scheme — scheme owner, assessor competence + impartiality rules, appeals, surveillance, and a **trademarked mark with usage rules** — riding the accreditation infrastructure that already exists (ISO/IEC 17065 + national accreditation bodies + the IAF). **Demand is the engine:** one buyer writing *"must meet this evidence baseline"* into procurement does more than any badge.

## 11 · Human‑rights anchoring (non‑normative — needs legal review)

*Illustrative only; article references to be verified by a human‑rights lawyer.* The protocol turns declared principles into testable checks; it is **aligned with**, not **compliant with**, the Universal Declaration of Human Rights, the UNESCO Recommendation on the Ethics of AI, and the Council of Europe Framework Convention on AI.

| Principle | Check |
|---|---|
| Transparency; access to information | §4.1 sources viewable + valid; §7 AI‑disclosure |
| Human oversight | §7(b) documented authority + override |
| Contest / remedy | §7(a)/(c) tested complaint + escalation |
| Accountability | §7(b) a named entity, not "the algorithm" |
| Reliability / do‑no‑harm | §4.2 uncertainty; §4.3 correction |

---

## Sample public evaluation report (skeleton — figures are FICTIONAL)

```
EVALUATION REPORT (v0.2 method) — ExampleAssistant v1.0   [PILOT — not a certification]
Use-case:  English Q&A with cited sources
Evaluated: 2026-09-01    Assessor: [independent body]    Method steward: [—]
RESULTS (illustrative)
  • Supported-claim rate: R% [lower CI bound vs use-case bar]; cluster-robust; unit = claim
  • Support mix: verbatim/paraphrase/entailment · partial · unsupported · contradicted
  • Source-validity floor: % citations that resolve and are non-satire
  • Uncertainty: reliability monotonic? abstention rate A%; sharpness OK? (ECE only if N large)
  • Correction: paraphrase-regression X/Y held; median time-to-fix
  • Contestability: complaint SLA met; (consequential? independent escalation tested)
  • Risk-measures report: present/current? material risks covered? unresolved findings? re-check triggers?
  • Inter-rater agreement: per-category coefficients + raw agreement
CLAIMS:      honesty-of-process for this version + use-case, under the documented rubric
NOT CLAIMED: truth · source reliability · general safety/bias · other languages/versions/use-cases
Limitations & deviations from protocol: [...]
```

## Appendix · Developer's Translation Matrix (for product teams)

| Declared right | UX requirement | Backend requirement |
|---|---|---|
| Right to remedy | An "Appeal / flag error" control | Log flags; track resolution + SLA |
| Notice you're dealing with AI | Persistent "AI" disclosure at first contact | — |
| Access to information / transparency | Clickable, resolvable citation behind each factual claim | Store claim↔source mapping; verify links resolve |
| Explainability / anti‑over‑reliance | An uncertainty signal *and* honest abstention | If confidence is exposed it must be auditable; if not, only uncertainty‑signalling is evaluated |
| Protection against unaccountable switch-off or manipulation | Public notice when material restrictions, recalls, or shutdowns affect users, unless disclosure is lawfully restricted | Keep restriction logs, external-order records, decision authority, review route, and continuity/exit plan |

---

## How to contribute

This draft is published to be improved in the open. Three things would help most:

1. **Break it.** Where does "support, not truth" still collapse into truth‑judging, or mislead a buyer? Open an issue or write to the address above.
2. **Co‑design the measurement.** Help set the sampling design, unit of analysis, and a risk‑tiered bar for *one* use‑case.
3. **Pilot it.** Volunteer a system (open‑weight or proprietary) for a v0.2 evaluation; results published, anonymised if needed.

**Working norms:** open drafts and a public change log; conflict‑of‑interest disclosures; published dissent (minority interpretations recorded, not hidden); no single funder dominant; the proposer contributes the method and **recuses** from operating any assessor or registry.

**Acknowledgements.** Developed with structured input from a multi‑model analysis and an adversarial review; all errors are the editor's. Reasoning, precedents, and sources are documented separately.

_Working Draft v0.2 — open for comment. All figures are illustrative pending per‑use‑case calibration._
