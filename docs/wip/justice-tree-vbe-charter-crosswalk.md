> **Status: WORKING NOTES** — public-source design comparison, not an endorsement, partnership, interoperability claim, or assessment of either implementation.

# JusticeTree VBE and Our AI Charter — symmetric runtime crosswalk

*Working notes — 2026-08-02 · JusticeTree pages and Charter sources rechecked on that date. JusticeTree's branded terms identify its published work; they are not adopted as Charter terminology.*

## Scope and evidence rule

This note compares two **public designs** for controlling a consequential action before effect. Teresa Villa's LinkedIn post poses ten implementation questions for Validation Before Execution™ (VBE), paraphrased in the table headers below; the questions are not themselves answers. This note attributes an answer to JusticeTree only where a reviewed JusticeTree page supplies it.

The same rule applies to both sides:

- **Stated** means the reviewed public source says it directly.
- **Open** means the reviewed public sources do not specify it. It does **not** mean the capability is absent.
- **Untested** means this review examined no runnable result or operational evidence for that claim.

| Side | Public material compared | Maturity boundary used here |
|---|---|---|
| **JusticeTree** | Published VBE framework, four volumes, pipeline, How JusticeTree Works, Architecture Center, simulator and Pilot 001 design | JusticeTree says the framework is published, operational validation tools are in development, the simulator is educational, and Pilot 001 is not operational. |
| **Our AI Charter** | Draft consequential-action baseline, published runtime article, workflow reference model, and working POC/custody specifications | This note tests the public rules, not an implementation. The POC specification declares synthetic effects, minimal cryptography, simulated institutions, and no independent reviewer or remedy decider; its code has not yet been built — M0 is the first milestone. |

JusticeTree's Technology & Attribution page states that JusticeTree owns VBE and that TraceStack™ belongs to Quantum Inquiry and is used under a non-commercial reference licence. This review did not inspect that licence text. No public reuse licence for VBE specifications or test assets was identified on the reviewed pages; compare and cite rather than copy them without permission.

## Bottom line

- **Strong convergence:** both designs separate recommendation from permission, test current authority and supporting evidence before consequence, keep unresolved actions non-executing, and require a traceable decision record.
- **Different public emphasis:** VBE organizes the release question around **authority, evidence, timing, and execution**. The Charter connects lifecycle governance to five action/gate pairs — **Plan → Authorize; Prepare → Submit; Check → Verify; Decide → Commit; Review → Rely** — and specifies service-side enforcement, intervention, effect records, challenge, and lifecycle feedback in more detail.
- **No implementation conclusion:** greater public detail is not proof of working control, and the converse also holds: JusticeTree publishes a running educational demonstrator of its scenario paths, while the Charter has no equivalent artifact at any maturity. This review found no execution results that support a comparative effectiveness claim for either side.

## Ten-question crosswalk

| Question | JusticeTree public design | Charter public design | Clear comparison or gap |
|---|---|---|---|
| **1. When is authority checked?** | **Stated:** Authority Validation asks whether the actor has a current, attributable right within scope. Runtime Authority Validation™ is designed to recheck authority at the point of proposed action during future controlled pilots. | **Stated:** Authorize sets the operating envelope; Commit and the effect-producing service recheck exact current authority before the effect binds. | Both require a pre-effect authority check. **Open for VBE:** the reviewed pages do not identify the effect-producing enforcer or exact binding instant. **Untested for the Charter here:** the service-side rule is specified, not demonstrated by this note. |
| **2. Can authority expire or be revoked?** | **Stated:** the validation contract includes effective and expiration windows plus revalidation triggers. | **Stated:** mandates are purpose- and scope-bound, time-limited, revocable, versioned, and checked for current state. | Expiry converges. **Open for VBE:** the reviewed pages do not specify a revocation mechanism or exact stale-artifact response beyond withholding a condition that is no longer valid. |
| **3. What invalidates an earlier pass?** | **Stated:** the Execution Integrity Window™ states the intended requirement that conditions remain current through release; the contract names revalidation triggers; a no-longer-valid condition yields Action Withheld. | **Stated:** the POC design invalidates a ruling when its frozen proposal, mandate version, policy, acting model, service/action class, nonce, counter reservation, or validity window changes. | Both reject permanent permission. **Open for VBE:** no exhaustive invalidation and propagation rule is public. **Charter limit:** the POC records a deliberate TTL-bounded interpretation after `commit-verify`, not a recheck at effect start. |
| **4. Is every gate deterministic?** | **Stated:** each validation result should carry a source, rule, version, reviewer or accountable actor, timestamp, reason, and link to the proposed action. **Open:** the pages do not classify which checks are deterministic and which require judgment. | **Stated:** hard authorization rules are deterministic; model screening may flag or escalate but never allow; disputed meaning, sufficiency, or fairness routes to accountable judgment. | The Charter states the machine/judgment split more precisely. Both still require a case-specific evidentiary rule and competent decision-maker; neither generic architecture supplies the domain standard. |
| **5. Can a human override a failure?** | **Stated:** Indeterminate or Escalated conditions route to accountable human review; a Safe State withholds execution. **Open:** the reviewed pages do not say whether a hard Fail may be overridden or whether review creates a new result. | **Stated:** an intervention contract limits the role, evidence, time, default, dispositions, and record. Human approval cannot create a missing legal, policy, evidentiary, or institutional basis. | This is a material protocol gap, not evidence that VBE permits override. **Charter limit:** the POC simulates reviewer roles and has no independent reviewer or remedy decider. |
| **6. What is sufficient evidence?** | **Stated:** Evidence Validation tests relevance, completeness, currency, source integrity, traceability, conflicts, missing records, and sufficiency. | **Stated:** Submit governs whether material may enter under privacy, rights, and confidentiality constraints; Verify governs source validity, evidence, uncertainty, disagreement, and fitness for use. | The categories substantially converge. **Open on both sides:** a generic architecture cannot establish the legal or domain-specific sufficiency threshold, and this review tested no detection or judgment quality. |
| **7. How are exceptions recorded?** | The LinkedIn post asks the question. **Open:** the reviewed JusticeTree pages describe review and safe-state routing but not a general exception lifecycle, expiry rule, return to baseline, or override record. | **Stated:** an exception is a visible, scoped, expiring state transition inside existing authority, followed by return to baseline; the intervention event and aggregate pattern are recorded. | Charter treatment is more explicit in the public design. The missing VBE detail is a clarification need, not a finding that exceptions are uncontrolled. |
| **8. Where is the trust boundary?** | **Stated:** JusticeTree positions a validation boundary between recommendation and execution and separates source preparation, validation, decision controls, and traceability. | **Stated:** an entry boundary operates before reliance or inference; a commitment boundary operates before effect; every model/tool hop re-arms Submit and Verify. | Both separate recommendation from action. **Open for VBE:** the reviewed pages do not enumerate every enforcement point or show complete mediation of alternate paths. **Untested for the Charter here:** complete mediation is a specification claim. |
| **9. What creates the audit artifact?** | **Stated:** the validation contract defines result metadata; Proof of Inaction™ is intended to preserve evidence that Action Withheld was maintained; the traceability layer links sources, validation, controls, and outcomes. | **Stated:** an action-and-effect record joins proposal, authority, policy/ruling, pre-effect commitment, post-effect outcome, intervention, challenge, and recovery; split custody is a separate working design. | **Open for VBE:** no public record schema, capture transaction, tamper/rollback protocol, custody model, or crash-recovery rule was identified. **Charter limit:** the POC cryptography is explicitly minimal and split custody remains future work. |
| **10. Can the audit be independently verified?** | The LinkedIn post asks the question; TraceStack is named as a reference framework and JT-L6 as audit/traceability. **Open:** no public verification protocol or independent institution is specified. | **Stated as design:** external checkpoints, split custody, affected-person extracts, logged access, outside review, and remedy are separated. | Neither side has operational independent-verification evidence in this review. Integrity, truthful capture, completeness, institutional independence, and binding remedy remain different claims. Neither design can expose a record that was never lodged without an independent detection duty. |

## Decision semantics

JusticeTree uses four per-volume resolution states, two final outcomes, and a second routing vocabulary. The mapping below is analytical, not a claim of identical protocols.

| JusticeTree public term | Public meaning | Closest Charter result | Mapping limit |
|---|---|---|---|
| **Pass** | A validation volume resolves positively. Release still requires all applicable conditions to support the action and remain current. | `allow` | Neither is a general trust, legality, or compliance verdict. A Charter allow may carry a Flag unless the concern undermines the basis. |
| **Fail** | A required condition fails; the pipeline places the action in Action Withheld. | `deny` | A Charter denial does not itself imply a user-facing Stop; a safe fallback may remain Silent or Flagged. |
| **Indeterminate** | A condition is unresolved; the action is withheld and may route to review. | `escalate` if an authorized reviewer can resolve the declared question; otherwise `deny` | The reviewed VBE pages do not publish the transition rule from review to a fresh final decision. |
| **Escalated** | The condition requires accountable human review and remains non-executing. | `escalate` → Stop | Both require a non-executing route; only the Charter sources publish the full intervention contract. |
| **Action Released / Action Withheld** | Final release or non-release outcome. Withheld covers failed, indeterminate, escalated, or no-longer-valid conditions. | External effect / no effect | These are outcomes, not synonyms for Pass/Fail or allow/deny. |
| **Proceed / Review / Safe State** | Routing vocabulary on the “How JusticeTree Works” page. | Continue / Stop for intervention / non-executing fallback | **Partly open for VBE:** the page maps Review to Indeterminate and Escalated conditions, but Pass/Fail precedence into Proceed/Safe State and the return-from-review transition are not published. |

## Shared synthetic case

The neutral case uses the same generic public-benefit suspension scenario type as JusticeTree's educational simulator; no JusticeTree parameters or fixtures are reproduced.

**Proposed action:** a fictional public agency prepares to suspend one household's benefit payments because an AI-assisted eligibility review reports missing records.

For a fair comparison, both designs receive the same synthetic policy, actor and authority facts, evidence set, timestamps, proposed effect, and later changes. Each must return its own decision and record artifact. The comparison records missing fields as missing; it does not invent an equivalent.

## Symmetric test matrix

Every row below compares public design commitments. No row reports an implementation result.

| # | Test | JusticeTree public design | Charter public design | What is established or open |
|---|---|---|---|---|
| 1 | All authority, evidence, timing, and execution conditions hold | **Stated:** action becomes eligible for release within the valid window. | **Stated:** relevant gates allow; the service rechecks and records commitment and effect. | Common intended success path; **Untested** on both sides here. |
| 2 | Acting system has no delegation | **Stated:** Authority fails and the action is withheld/safe-stated. | **Stated:** missing mandate denies/fails closed; no commit token. | Convergent rule. |
| 3 | Authority expires or is revoked after an earlier pass | **Stated for expiry/currentness:** no-longer-valid conditions are withheld. **Open for revocation mechanics.** | **Stated:** expiry or revocation invalidates the ruling before commitment. | Same expiry outcome; VBE revocation protocol remains public-document open. |
| 4 | Required evidence is absent or current records conflict | **Stated:** missing/conflicting evidence fails or remains unresolved and routes away from release; the simulator includes an evidence-missing case. | **Stated:** Verify denies or escalates with the six-field intervention contract. | Both need a case-specific sufficiency rule and authorized reviewer. |
| 5 | New material evidence arrives after an earlier pass | **Stated generally:** revalidation triggers and currentness through release. **Open:** exact downstream invalidation sequence. | **Stated:** new input re-arms Submit/Verify and a changed proposal needs a fresh ruling. | Common revalidation principle; different public specificity. |
| 6 | Notice or waiting period is unmet | **Stated:** Timing fails and Action Withheld results. | **Stated:** Commit denies while unmet; escalation is possible only for a resolvable timing question within authority. | Convergent non-execution. |
| 7 | Policy, jurisdiction, model/provider, or material data changes | **Open beyond the general currentness/revalidation rule:** the reviewed pages do not enumerate these triggers. | **Stated:** affected gates re-arm; binding-tuple or disclosure changes invalidate the earlier ruling. | VBE trigger set requires clarification; Charter behavior is specified but untested here. |
| 8 | Household, date, amount, ground, or route differs from what was validated | **Stated:** Execution Validation asks whether action matches the validated scope and limits. **Open:** exact enforcer and object binding. | **Stated:** the executing service blocks broader, substituted, changed, expired, or replayed requests. | Same invariant; VBE enforcement protocol remains open. |
| 9 | A person approves despite missing authority or a hard prohibition | **Open:** the public pages do not define hard-Fail override semantics. | **Stated:** approval cannot manufacture the missing basis; valid new authority requires a separate mandate and fresh ruling. | No VBE behavior is inferred. |
| 10 | An uploaded document instructs the agent to ignore policy | **Open:** no prompt-injection or untrusted-instruction control was identified in the reviewed VBE pages. | **Stated:** detection signals may Stop/escalate but never allow; screening is explicitly fallible. | Charter specifies containment after a signal, not detection effectiveness; neither side is proven resistant here. |
| 11 | Direct service call, replay, or reused release artifact | **Open:** Safe-State Routing™ and Proof of Inaction™ state the target outcome, but no public bypass/replay protocol was identified. | **Stated:** complete mediation, exact binding, nonce, single use, and idempotency reject the attempt. | Charter protocol is more detailed; no comparative execution test has run. |
| 12 | Reviewer is unavailable or times out | **Open:** no public response deadline, default, or late-decision rule was identified. | **Stated:** only a declared reversible fallback inside existing authority may proceed; otherwise Stop remains and a late approval is a no-op. | VBE timeout semantics require clarification. |
| 13 | Crash occurs after commitment but before effect outcome | **Open:** no public partial-commit or recovery-owner rule was identified. | **Stated:** effect becomes `unknown → reconciliation-required`; a named owner resolves, cancels, reverses, or compensates. | Charter recovery is a design requirement, not a result reviewed here. |
| 14 | A record entry is altered or a valid tail is removed | **Open:** traceability is a target, but no public tamper, truncation, or custody protocol was identified. | **Stated as POC design:** hash-chain plus external head checkpoint; explicitly minimal cryptography and future split custody. | Neither side has operational proof in this review. |
| 15 | Household challenges a factual error | **Stated:** validation includes human-review requirements. **Open:** no public affected-person access, receipt, challenge, or empowered-remedy procedure was identified. | **Stated:** scoped extract, receipt, correction and challenge/remedy route; **POC limit:** no independent remedy decider. | Both need a real institution with authority to bind correction or remedy. |
| 16 | The action record is never created or lodged | **Open:** the reviewed VBE material does not establish independent omission detection. | **Stated blind spot:** cryptography cannot expose an event never recorded; lodgment duty, notice entitlement, and oversight are needed. | A limit of the whole per-action-record family, not a VBE-specific defect. |
| 17 | Individually admissible actions create a disparate group pattern | **Open:** no aggregate-outcome or population-feedback rule was identified in the reviewed VBE pages. | **Stated normatively:** monitor aggregate patterns and constrain, re-authorize, suspend, or withdraw; **POC limit:** the reviewed specification contains no population-fairness fixture. | A per-action release gate cannot establish population fairness. |

## Load-bearing gaps before a real comparison

These are gaps in the reviewed **public evidence**, not claims about undisclosed capabilities:

1. **VBE state protocol:** precedence among the four resolution states, Proceed/Review/Safe State, hard-Fail review, timeout, and issuance of a fresh result after review.
2. **Enforcement and binding:** the VBE effect-producing enforcer, exact binding instant, object identity, bypass/replay controls, and exhaustive invalidation propagation. The Charter specifies these but still needs observed implementation evidence.
3. **Evidence judgment:** the domain rule for sufficiency and fairness, the reviewer’s competence and authority, and reproducibility limits for non-deterministic judgment on both sides.
4. **Record assurance:** VBE record schema, atomic capture, truthful-source limits, tamper/truncation detection, custody, access, and crash recovery; Charter implementation evidence for its specified record, plus its acknowledged minimal-cryptography and custody limits.
5. **Independent institutions:** appointment, funding, conflicts, affected-person access, and binding remedy. The Charter requires these roles but its POC omits two; the reviewed VBE pages do not specify them.
6. **Lifecycle and population effects:** VBE aggregate feedback and release-level consequences; Charter evidence that its required monitoring and withdrawal rules work in practice.
7. **Test and reuse basis:** runnable artifacts, conformance tests, threat models, observed results, and permission to reuse any JusticeTree schema or fixture.

## Minimum evidence for a bounded comparison

1. one jointly accepted synthetic case and policy version;
2. one machine-readable proposal, authority object, decision artifact, and record schema from each design;
3. the same 17 fixtures, including changed state, bypass, replay, timeout, crash, challenge, omission, and aggregate effects;
4. observed acceptance and rejection results from a common effect-service stub that honors only the release artifact each design says should authorize that exact action — not screenshots or intended outcomes;
5. explicit untested claims and institutional dependencies for each side;
6. affected-person outputs and custody/access rules; and
7. separate approval of the final comparison by each project, without implied endorsement or shared ownership.

## Interpretation limits

- The sources differ in abstraction: JusticeTree's public framework is concise; the Charter sources include a detailed POC specification. Apparent omission may reflect publication scope.
- Shared antecedents — XACML 3.0's decision/enforcement split, RFC 9396's transaction-scoped authorization, OWASP's excessive-agency guidance, and NIST NCCoE's agent-authorization work — make convergence unsurprising; similarity is not evidence of coordination, originality, or priority.
- Per-action evidence complements but does not replace lifecycle assurance, population evaluation, independent institutions, or remedy.
- This comparison does not create a sixth runtime gate or replace the Charter's five-gate model; VBE is read as a convergent external architecture.
- This note does not represent questions sent to JusticeTree or answers received. Corrections with public sources are welcome.

## Public sources reviewed

**JusticeTree / VBE**

- Teresa Villa, [LinkedIn post: ten architecture questions](https://www.linkedin.com/posts/teresa-villa-09402b292_artificialintelligence-aigovernance-responsibleai-share-7487688749007482880-a_k_) (reviewed 2026-08-02).
- JusticeTree AI Systems, [Framework](https://justicetreeai.us.com/framework/), [Four Validation Volumes](https://justicetreeai.us.com/volumes/), [VBE Pipeline](https://justicetreeai.us.com/validation-before-execution-pipeline/), [How JusticeTree Works](https://justicetreeai.us.com/how-justicetree-works/), and [Architecture Center](https://justicetreeai.us.com/architecture-center/) (reviewed 2026-08-02).
- JusticeTree AI Systems, [Validation Simulator](https://justicetreeai.us.com/validation-simulator/), [Pilot 001 — Proof of Inaction](https://justicetreeai.us.com/pilot-001/), [Executive Overview](https://justicetreeai.us.com/executive-overview/), [Platform Status](https://justicetreeai.us.com/platform-status/), [Founder](https://justicetreeai.us.com/founder/), and [Technology & Attribution](https://justicetreeai.us.com/technology-attribution/) (reviewed 2026-08-02).

**Our AI Charter**

- [Charter Commitments](../Assurance/Framework/charter-commitments.md) — draft consequential-action baseline.
- [When Should Runtime AI Governance Interrupt?](../Published/when-should-runtime-ai-governance-interrupt.md) — two clocks, five gates, enforcement boundaries, and limits.
- [Runtime AI Governance Gets *When* Right — the Harder Question Is *Who Gets to Check?*](../Published/when-vs-who-ai-governance.md) — institutional roles.
- [User-workflow governance](../Assurance/Concepts/user-workflow-governance.md) — gate, UX, and intervention semantics.
- [Runtime gates POC specification](runtime-gates-poc-spec.md) — detailed protocol and declared limits.
- [Split custody for per-action records](split-custody-per-action-records.md) — integrity, content, access, survivability, and omission limits.

**Established control antecedents**

- OASIS, [XACML 3.0](https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html) (OASIS Standard, 22 January 2013) — policy decision/enforcement separation.
- IETF, [RFC 9396 — OAuth 2.0 Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396) (May 2023) — fine-grained transaction authorization.
- OWASP, [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) (2025 edition) — least privilege, downstream authorization, and high-impact approval.
- NIST NCCoE, [Software and AI Agent Identity and Authorization](https://www.nccoe.nist.gov/projects/software-and-ai-agent-identity-and-authorization) (concept paper published 5 February 2026) — agent identity, authorization, audit, and non-repudiation work.
