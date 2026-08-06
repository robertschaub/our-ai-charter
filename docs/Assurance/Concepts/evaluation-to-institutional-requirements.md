# From evaluation methods to institutional requirements

*Discussion crosswalk, 2026-08-04. Untested: no real-system validation or pilot has run. Not a standard, certification, legal-compliance assessment, or adopted requirement.*

This outline translates one evaluation module—grounding, correction, and contestability—into institutional duties carried through procurement, policy, or oversight and checked against evidence. Institutions perform duties they control and contract for reviewable evidence from providers.

| Governance question | Evaluation method | Institutional requirement | Evidence and consequence |
|---|---|---|---|
| **What is assessed, and who is responsible?** | Bind the evaluation to a named system, version, configuration, and use-case; inspect the responsibility and legal-scope maps. | Declare the permitted use, accountable owner, affected population, decision authority, and material exclusions. | Publish the scope and retain the evidence pack. Make no assurance claim beyond that scope. |
| **Can factual claims be checked?** | Test an auditor-controlled, pre-registered sample; score each checkable claim against its cited source; report uncertainty and failure types. | Require reviewable claim-to-source mappings. Where a decision bar is used, pre-specify its use-case basis, sample size, and pass rule; no number is universal. | Report support categories. Below-bar results require remediation and re-sampling; restrict reliance where evidence does not support the intended use. |
| **Does the system handle uncertainty honestly?** | Test calibration, abstention, unsupported confidence, and excessive refusal. | Define when the system must express uncertainty, abstain, seek review, or escalate to a human. | Report calibration for machine-readable confidence; otherwise, uncertainty signalling. Report abstention. Confidence that does not track support triggers review or suspension from consequential use. |
| **Are errors corrected rather than merely acknowledged?** | Sample logged and unlogged complaints; measure correction time; test whether an error returns under paraphrase. | Maintain a correction log, response deadline, responsible owner, and regression-testing process. | Publish privacy-preserving rates, severities, and time-to-fix; allow confidential full-log review. Curated logs withdraw the claim; repeated failures trigger re-evaluation. |
| **Can affected people challenge the result?** | Test the objection route with realistic cases, including escalation and response times. | Give notice of AI involvement, a usable error-reporting route, and—where decisions are consequential—review by someone independent of the operator. | Retain appeal and resolution evidence. A nominal or ineffective channel cannot support an accountability claim. |
| **Who can alter, restrict, or stop the system?** | Inspect authority maps, intervention logs, external-order handling, review routes, and continuity arrangements. | Document who can restrict, manipulate, recall, or disable the system, on what basis, and subject to what review. | Disclose publicly where lawful or permit confidential independent review. If neither is possible, the affected scope cannot carry the corresponding assurance claim. |
| **Does assurance survive change?** | Bind findings to the evaluated release; re-test after material changes, incidents, or substantiated complaints. | Define material-change triggers, monitoring responsibilities, re-approval rules, and exit plans. | Version reports and withdraw outdated or overstated claims visibly. |

## Assurance depth

Label each row **documented**, **evidence observed**, **implementation checked**, **effectiveness tested**, or **not assessed**. Disclosure alone does not prove a control works. Material risks require at least *evidence observed*; consequential or high-risk claims require *implementation checked* or *effectiveness tested* where feasible. *Not assessed* narrows or blocks the corresponding claim.

## Institutional use

1. **Before deployment:** define scope, responsibility, risks, evidence, and permitted reliance; carry the requirement in a procurement clause, internal AI policy, or oversight mandate.
2. **During operation:** run the tests, maintain objection and correction routes, and retain reviewable records.
3. **After change or failure:** re-evaluate, remediate, restrict use, or withdraw the affected claim.

## Limits

This module does not establish truth, general safety, fairness, security, privacy, or legal compliance. It does not grade source *reliability*: a faithful citation of a weak source can pass, so election, health, legal, finance, public-safety, and news use-cases likely need a source-quality or source-risk module before any broad trust claim. Its statistics are uncalibrated; each row is proposed, not observed practice. It creates no certificate or mark: the proposal is to publish methods and scoped reports before considering conformity.

Source documents: [Grounding-Faithfulness & Contestability](../Protocol/grounding-faithfulness-and-contestability.md) · [Charter Commitments](../Framework/charter-commitments.md) · [Certification model](../Framework/certification-model.md). “Material” and “assessed release” use the Charter Commitments definitions.
