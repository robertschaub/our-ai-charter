> **Status: WORKING NOTES** — Evidence-Gated Agents user needs and requirements v0.1 draft; no implementation baseline adopted from this draft.

# Evidence-Gated Agents — user needs and requirements

These proposed needs connect people accountable for AI-influenced decisions with people affected by them. Their suitability across companies, public bodies, newsrooms and civil society remains to be evaluated. Prototype coverage and possible development appear under the same needs.

<a id="stages-and-authority"></a>
## 1. Stages and authority

- **Exists:** demonstrated implementation in a named component/version with checkable evidence.
- **Prototype:** proposed, if-funded scope; activation and selected delivery scope require a recorded decision.
- **Later extension:** specified or sketched continuation outside that scope.
- **Aspiration:** research intent whose adequacy or generality remains unestablished.

A Prototype requirement may already Exist in a component. Labels alone create no obligation. Obligations require an adopted baseline naming applicable clauses and compatible, immutable versions of requirements, specification and inherited runtime constraints.

An EGA baseline governs only its explicitly adopted EGA scope. Existing runtime assignments retain their recorded immutable sources, accepted ADRs and acceptance criteria. Publication, EGA adoption and stage/version changes do not retarget that work or add an EGA adoption prerequisite. A runtime target change requires a separate runtime decision and impact review naming the affected task or milestone; the [specification's authority section](evidence-gated-agents-spec.md#status-applicability-and-authority) records the source boundary.

Later extensions carry no present delivery commitment. Retained, reviewed acceptance constraints remain the basis for later implementation unless explicitly superseded by a reviewed decision; sketches remain proposals. Each extension needs its own scope, estimate, activation decision and evidence. Changing applicability or retained acceptance constraints requires substantive review, a recorded decision and a major version change.

<a id="applicability"></a>

| Proposed applicability | Requirements | Adoption |
|---|---|---|
| Prototype | REQ-1–6, REQ-8, REQ-10 | Pending |
| Later extension | REQ-7, REQ-9 | No present delivery commitment |
| Aspiration | REQ-11 | Research evaluation required |

Acceptance references below identify required evaluation; they assert no completed evidence.

## 2. Needs and requirements

### N-1. Decide whether an exact answer may be released

An accountable operator needs to establish authority and evidence before an answer influences someone’s decision.

- <a id="req-1"></a> **REQ-1 — Prototype:** release requires current authority and a current, sufficient declared evidence basis. Failed checks stop release; missing, stale or corrupt evidence must not pass. [Acceptance: release-blocking tests, SPEC-1](evidence-gated-agents-spec.md#spec-1).
- <a id="req-2"></a> **REQ-2 — Prototype:** narrowed or revised answers rerun the checks; released text matches approved text. [Acceptance: revision and text comparisons, SPEC-1](evidence-gated-agents-spec.md#spec-1).

The prototype covers one governed real effect type: answer delivery, potentially across multiple attempts, revisions and releases. Broader action coverage needs separate adoption and evidence.

### N-2. Understand and preserve the evidence boundary

Operators and recipients need to know which assessments support an answer and where counter-evidence, uncertainty or language differences limit it.

- <a id="req-3"></a> **REQ-3 — Prototype:** prepare fixed German/English claim assessments from public sources, preserving verdicts and evidence for and against. Export/import a redacted evidence bundle and detect changes. [Acceptance: bundle integrity and admission checks, SPEC-2](evidence-gated-agents-spec.md#spec-2).
- <a id="req-4"></a> **REQ-4 — Prototype:** evaluate answers against declared evidence and report unsupported or undeclared claims and German/English differences. [Acceptance: dependency coverage, SPEC-3](evidence-gated-agents-spec.md#spec-3), and [language evaluation, SPEC-5](evidence-gated-agents-spec.md#spec-5).

Live evidence search is a Later extension. Reporting undeclared claims does not establish that the gate detects every undeclared assertion.

### N-3. Inspect and challenge a released answer

An affected recipient needs to understand why an answer was released and how to question it.

- <a id="req-5"></a> **REQ-5 — Prototype:** provide a receipt linking answer, authority, evidence basis, decision and outcome. A challenged view links the contested entry, reliance state, route and resolution status. Fix the authorised resolution owner and terminal remedy states before PF-M3 acceptance. [Acceptance: receipt, reliance and bounded challenge behaviour, SPEC-4](evidence-gated-agents-spec.md#spec-4).
- <a id="req-6"></a> **REQ-6 — Prototype:** invite practitioner feedback on recorded, consented and redacted receipts: are basis and decision clear, and is the challenge route findable? [Acceptance: formative feedback and revisions, SPEC-5](evidence-gated-agents-spec.md#spec-5).
- <a id="req-7"></a> **REQ-7 — Later extension:** complete independent remedy would require deployment-specific authority, correction and review rules. [Acceptance: separately scoped institution-owned remedy, SPEC-4](evidence-gated-agents-spec.md#spec-4).

Bounded prototype challenge and correction targets remain Prototype scope. Practitioner feedback does not establish independent validation or complete independent remedy.

### N-4. Reproduce a bounded evaluation

Maintainers and reviewers need an identifiable configuration and action path to interpret outcomes.

- <a id="req-8"></a> **REQ-8 — Prototype:** provide reproducible installation, recorded rules/settings and a guided German/English path from authorisation to real answer delivery and its receipt. Keep other actions simulated. [Acceptance: configuration records and end-to-end demonstration, SPEC-1](evidence-gated-agents-spec.md#spec-1).

### N-5. Adapt governance to organisational responsibilities

Organisations considering integration need to establish who may act, what evidence may be used and how errors will be addressed.

- <a id="req-9"></a> **REQ-9 — Later extension:** organisations could integrate authority/evidence checks into existing workflows. Organisation-specific policies, contracts and records require permission; every deployment needs authority, evidence, correction and review rules. [Acceptance: deployment and source boundaries, SPEC-1](evidence-gated-agents-spec.md#spec-1), [SPEC-2](evidence-gated-agents-spec.md#spec-2) and [SPEC-4](evidence-gated-agents-spec.md#spec-4).

The bounded prototype does not establish suitability for these wider deployments.

### N-6. Judge what evaluation establishes

Reviewers need observable outcomes and limitations without mistaking enforcement for semantic adequacy.

- <a id="req-10"></a> **REQ-10 — Prototype:** pre-set pass/fail rules; publish protocol, aggregate findings, failures and limitations, covering release checks, unsupported claims, language differences and receipt clarity. [Acceptance: evaluation record, SPEC-5](evidence-gated-agents-spec.md#spec-5).
- <a id="req-11"></a> **REQ-11 — Aspiration:** evaluate evidence-requirement adequacy through a separate review step. AI-derived requirements and reliable application across unfamiliar tasks remain research questions. [Acceptance: separate research evaluation, SPEC-5](evidence-gated-agents-spec.md#spec-5).

## 3. Traceability and claim limits

Adoption must complete the trace from need to requirement to [specification](evidence-gated-agents-spec.md) to acceptance evidence.

This work claims no operating network, certification scheme, trust mark or institutional mandate. FactHarbor remains Alpha; the runtime proof of concept uses simulated institutions; Our AI Charter remains a public draft. Gate enforcement alone does not establish adequate evidence requirements, independent adequacy review or suitability across intended uses.
