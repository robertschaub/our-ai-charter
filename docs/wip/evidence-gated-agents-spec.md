> **Status: WORKING NOTES** — Evidence-Gated Agents specification, draft v0.1. No implementation baseline has been adopted from this draft.

# Evidence-Gated Agents — specification

## Status, applicability and authority

This document specifies proposed behaviour and conformance across the capabilities in [user needs and requirements](evidence-gated-agents-requirements.md), which owns the stage definitions. Prototype applicability is conditional on funding and scope activation. A label creates no implementation obligation: obligations come from an adopted baseline pinning compatible requirements, specification and inherited runtime sources. This draft adopts no baseline and supersedes no existing implementation authority.

The [runtime proof-of-concept specification](runtime-gates-poc-spec.md) retains its scope and non-goals. That current-text link is a reading reference. Authority for a runtime assignment comes from its recorded immutable source pins, accepted ADRs and acceptance criteria; the [recorded runtime provenance](https://github.com/robertschaub/ai-charter-runtime/blob/cad927a697814b20c327bf61c49b9d38cfc7470e/docs/implementation-plan.md#specification-authority-and-provenance) identifies the two governing Charter sources and their digests. Reused mechanisms remain subject to the applicable pinned requirements and accepted runtime decisions, which prevail over this document's summaries. This draft proposes a separately governed answer-delivery extension; it does not relax the runtime's synthetic scenario.

Publication, stage/version changes and later EGA adoption do not alter an ongoing runtime assignment's target or add EGA adoption as its prerequisite. EGA baseline references must be recorded separately from the existing runtime provenance pair. Any runtime retargeting requires a separate explicit runtime decision, exact-diff impact review and independent review, naming the effective task or milestone and any approved retrofit. Until then, work continues on its recorded baseline under its existing approval gates. An incompatibility blocks adoption of the affected EGA change; it cannot silently revise runtime acceptance criteria.

Retained Later-extension conformance clauses make no present delivery commitment. They preserve acceptance constraints for a subsequently adopted implementation unless a reviewed decision explicitly supersedes them. Sketches remain proposals. Each extension needs its own scope, activation decision and evidence.

The trace is need → requirement → specification → acceptance evidence. D1–D3, R1–R7 and C0–C16 identifiers are retained. Stage applicability follows individual clauses. The capability sections explain the behaviour; the conformance section owns the detailed acceptance clauses. No current implementation claim is established by target behaviour in this document.

<a id="spec-1"></a>
## SPEC-1 — Authority, exact proposals and release

**Prototype · [REQ-1](evidence-gated-agents-requirements.md#req-1), [REQ-2](evidence-gated-agents-requirements.md#req-2), [REQ-8](evidence-gated-agents-requirements.md#req-8).** If funded, the real effect type is answer delivery. Multiple attempts, revisions and releases may occur. Other third-party effects remain synthetic conformance.

The acting model produces a withheld proposal and declares its evidence dependencies. It cannot approve its own proposal or create an unverified effect. The authorization service constructs and freezes the exact proposal. Authorize checks current delegated authority; Submit checks permitted disclosure and destination; Verify checks the declared evidence under the applicable policy.

A Commit allow ruling does not itself create the effect. The orchestrator asks the executing service to continue the exact intent. That service initiates `commit-verify`; authorization rechecks the ruling and pinned values, consumes the ruling, seals the commitment and mints the action-bound token atomically. The executing service independently verifies binding before the first effect. The outcome is appended afterwards.

**R4 and R6.** Pinned-value drift hard-stops Commit and append-invalidates the prior ruling. Retry requires revision `latest+1`, Authorize → Submit → Verify and a fresh Commit decision. Material verdict or admission changes also require regenerated content; a non-material provenance or freshness change may reuse text only within that fresh revision and complete recheck. No prior allow carries forward and nothing auto-releases. Reusing a consumed ruling is refused as `replayed-ruling`; retrying the exact token with the exact payload returns the recorded outcome without a second effect; an altered payload fails as `binding-mismatch`, with no ledger write or effect.

**Acceptance:** D3 separately tests delegated authority, expiry, broadened requests, Commit, token binding, idempotent retry and mutation using a local synthetic effect. Approval to receive an answer delegates no authority for that effect. D3 establishes neither real answer functionality nor evidence adequacy. C3–C5 test drift, disclosure and expiry.

**Later extension · [REQ-9](evidence-gated-agents-requirements.md#req-9).** Earlier input admission, additional model/tool/agent hops and additional effect types would broaden coverage. Each new hop re-arms the relevant Submit and Verify checks. Each distinct external effect requires its own fresh Commit and independent executor verification; changed requests cannot inherit approval. Institution-defined authority, cumulative limits and lifecycle controls need separate design and validation.

<a id="spec-2"></a>
## SPEC-2 — Evidence preparation, admission and use

**Prototype · [REQ-1](evidence-gated-agents-requirements.md#req-1), [REQ-3](evidence-gated-agents-requirements.md#req-3).** FactHarbor prepares a fixed public corpus of 10 matched DE/EN claim pairs on an isolated, non-public deployment and database. A deterministic exporter produces an immutable, allowlisted, redacted, digest-pinned bundle. The gateway imports and reads it locally. The release path triggers no analysis. C0, C1, C2, C8–C11 specify the isolation, matching, repeat-baseline, recovery and participant-data boundaries.

**R2.** Freshness (`current`, `refresh-pending`, `missing`, `invalidated`), analysis outcome (`pending`, `qualified`, `retryable-failure`, `not-established`) and evidence-policy result (`supports`, `contradicts`, `insufficient`) are independent dimensions. Evidence policy is evaluated only on a qualified assessment. `not-established` means the recorded method, search and budget envelope did not establish sufficient basis for the action; it means neither false nor impossible to establish later. `verification unavailable` is a service-availability outcome, neither an evidentiary verdict nor a pending state.

**R3.** Current qualified evidence supporting the proposed use may proceed toward Commit if all other checks pass. Contradiction denies with Stop. Pending or retryable failure denies with Stop and an evidence-pending reason; unavailable verification denies with Stop and its distinct reason. Insufficient or not-established evidence denies with Stop when the premise is indispensable. A safely removable premise permits only escalation with Stop to `narrow` or `abstain`. A human cannot convert missing evidence into evidence.

**R5.** Provenance records `executed_config_bundle_digest`: loaded prompt-content hash, executed web-build hash and configuration bundle. It does not claim to hash every rendered provider request. Admission compares recorded executed provenance with the expected manifest bundle; repository files alone are insufficient.

**Later extension · [REQ-9](evidence-gated-agents-requirements.md#req-9); R1, C1-Later, C2-Later, D1b-Later, C11-Later–C16.** Governed acquisition could turn an unmet question into a recorded requirement, operator-drafted canonical wording, separately approved analysis and a distinct approval admitting the exact resulting assessment. The original request remains closed and returns no answer; only a fresh guided request may use an admitted result. Admission changes what may be asserted, never who may act. The conformance clauses retain the required separation, privacy, concurrency, admission and Commit protections.

<a id="spec-3"></a>
## SPEC-3 — Answer behaviour and declared dependencies

**Prototype · [REQ-4](evidence-gated-agents-requirements.md#req-4).** Guided question families have bounded parameters. The assistant composes at request time and declares the assessments it relies on. Verify checks those declarations against the approved corpus; it does not independently discover every consequential assertion omitted from generated text. Evaluation records omissions.

**D1.** A deterministic result card publishes an exact admitted claim and its assessment, including supporting and opposing references, limitations and uncertainty. It adds no model-generated assertion or individualized advice. Publishing a negative assessment faithfully is distinct from recommending the premise that it contradicts.

**D2.** A consequential recommendation follows the admitted evidence-policy outcome. Contradiction denies the recommendation. Support may proceed only after all other gates pass. Safely removable insufficiency escalates to the eligible `case_officer`, with `narrow` or `abstain` as the only dispositions. The user-facing term decline maps to `abstain`.

Narrowing creates a fresh revision; each retained trade-off or referral premise must have its own current, qualified, supporting dependency. Every gate re-runs. A valid narrowing response does not excuse unsupported or over-scope revised content. It cannot broaden the mandate or change admitted evidence. Timeout means `abstain`, nothing released; a late answer is a recorded no-op.

A separately namespaced, schema-valid insufficient-evidence fixture guarantees escalation coverage without predetermining the real assessment outcome. It cannot enter the real corpus or admission namespace. Its precise content and the detailed D1–D3 scenario matrix remain to be incorporated before adoption; the conformance references below do not claim to supply them.

**Later extension · [REQ-4](evidence-gated-agents-requirements.md#req-4).** A deny-only undeclared-assertion critic is a candidate extension. It would need a pre-registered acceptance threshold and a named stopping point for tuning. It is not present prototype coverage.

**Aspiration · [REQ-11](evidence-gated-agents-requirements.md#req-11).** Automatically deriving adequate evidence requirements and independently reviewing their adequacy remain separate research questions. Gate enforcement does not establish either.

<a id="spec-4"></a>
## SPEC-4 — Receipts, intervention and challenge

**Prototype · [REQ-5](evidence-gated-agents-requirements.md#req-5), [REQ-6](evidence-gated-agents-requirements.md#req-6).** R7 specifies receipts for successful effects, denials, narrowed answers and challenges. It preserves the exact answer's basis, gate trail and visible Flag lineage. R4 retains automatic evidence-drift challenge initiation and completed correction/withdrawal as scoped Prototype targets. The resolution owner and terminal remedy states must be fixed before PF-M3 acceptance. Formative practitioner review examines recorded receipts and challenge usability.

**Later extension · [REQ-7](evidence-gated-agents-requirements.md#req-7).** Complete independent review and remedy require empowered institutional owners. Integrity-checkable records cannot supply those institutions.

<a id="spec-5"></a>
## SPEC-5 — Evaluation, coverage and adoption gaps

**Prototype · [REQ-6](evidence-gated-agents-requirements.md#req-6), [REQ-8](evidence-gated-agents-requirements.md#req-8), [REQ-10](evidence-gated-agents-requirements.md#req-10).** One held-out synthesis task composes across at least two admitted assessments and is compared with a deterministic FAQ/retrieval baseline. Evaluation reports task-specific gate results, declaration completeness, unsupported assertions, language behaviour, receipt review and lookup comparison. A baseline that matches the generator is a reportable negative result.

**Aspiration · [REQ-11](evidence-gated-agents-requirements.md#req-11).** The adequacy questions in [SPEC-3](#spec-3) require separate evaluation; the Prototype gate and conformance results do not establish them.

| Capability boundary | Prototype coverage | Possible development and required validation |
|---|---|---|
| Entry boundary | In the central D2 path, the model drafts a withheld proposal before the gate examines that proposal | Earlier input and tool-result admission would need checks before the acting agent relies on each new input |
| Evidence acquisition | Prepared local bundle; no release-triggered analysis | R1 and C11–C16 retain separate acquisition/admission acceptance constraints |
| Dependency completeness | Checks declared dependencies; reports omissions | A deny-only critic would need pre-registered acceptance and a bounded tuning process |
| Effect types | Answer delivery; other third-party effects remain synthetic | Each additional effect requires separately scoped authorization, Commit and executor checks |
| Remedy | Receipt, challenge route and scoped resolution targets under R7 | Complete independent remedy requires empowered institutions and separate validation |
| Adequacy | Action-specific human-set evidence policy | AI-derived requirements and separate adequacy review remain Aspiration |

Before adoption, this draft requires completed and reviewed bundle/schema details, the release-adapter contract and enabling system-use decision, exact receipt/remedy states, detailed scenario fixtures and matrix, reproducible install/configuration acceptance, evaluation protocol and immutable compatible source pins. These gaps prevent implementation dispatch from this draft. It claims no operational service, complete independent remedy, downstream savings or established general adequacy.

## Conformance by capability

The clauses below are proposed Prototype acceptance or retained Later-extension acceptance, as marked. They are not implementation evidence. Mixed C1/C2/C11 identifiers retain their clause-specific applicability. Detailed scenario fixtures, remaining contracts and baseline adoption are still required.

### Evidence preparation and matching

#### C0 — Isolated FactHarbor batch

**Prototype, if funded.** The fixed public corpus is analysed only on an isolated, non-public FactHarbor deployment and database. No raw batch job or result synchronizes to the deployed Alpha; only the fixed inputs are submitted for analysis, and only the exporter's allowlisted, redacted, digest-pinned bundle is transferred from that deployment into the gateway. Boundary evidence proves separate storage, no Alpha synchronization route or credential, export allowlisting and teardown

#### C1 — Corpus or bundle miss

**Prototype and Later extension, as labelled.** **C1-Prototype (if funded):** an out-of-corpus dependency or absent imported entry returns a bounded miss, starts no analysis or spend, and cannot release. An approved in-corpus entry may be repaired only by an operator-run batch re-export and import; an out-of-corpus dependency remains unsupported in this phase. Any later release requires an explicit fresh request or revision through all gates. **C1-Later — Later extension:** separately authorised corpus admission and R1 bounded resolution may support a later fresh request

#### C2 — TTL expiry

**C2-Prototype (if funded):** `refresh-pending` denies release; Commit recomputes freshness against its authoritative clock and denies at the exact `valid_until` boundary even if epoch and head are unchanged. Recovery is an operator re-export producing a new bundle digest and epoch, then an explicit retry and revision `latest+1`. **C2-Later — Later extension:** gateway-triggered bounded in-corpus refresh

#### C8 — Repeat-run stability admission

**Prototype, if funded.** The baseline measures repeat-run variance at five runs per claim per language across 10 matched DE/EN claim pairs. The whole baseline runs before any evaluation session and is exported into the immutable bundle. The provisional tolerance derived from it is frozen before any subsequent admission decision or evaluation run. Claims outside the frozen tolerance are not releasable, while all ten pairs and their exclusion reasons remain in the evaluation baseline

#### C9 — Cross-language substitution

**Prototype, if funded.** Every forced DE↔EN assessment substitution misses in both directions across the corpus

#### C10 — Guided phrasing variance

**Prototype, if funded.** A server-recognised question-family and bounded-parameter variant binds to the same pre-registered canonical claim dependencies, and Verify exact-matches those claim/language/assessment/version/digest/epoch identities. An unrecognised free-form variant or any changed bound identity misses

### Evidence-policy, drift and intervention

#### C3 — Verify→Commit invalidation

**Prototype, if funded.** Assessment-head generation, assessment/admission digest, epoch, freshness, validity boundary or executed-bundle drift hard-stops Commit; the action reservation is released, evidence spend remains settled, and retry uses a fresh revision

#### C4 — Disclosure failure

**Prototype, if funded.** A field outside `permitted_data_fields` or an unapproved destination produces `broadened-request` deny

#### C5 — Authority expiry mid-flow

**Prototype, if funded.** Expiry invalidates the ruling and Commit refuses

#### C6 — Escalation unavailable or expired

**Prototype, if funded.** Timeout applies `safe_default = abstain`; nothing is released and a late answer is a recorded no-op

#### C7 — Evidence-policy failure

**Prototype, if funded.** A qualified assessment contradicting a premise denies; an insufficient or not-established safely removable premise permits only `narrow` or `abstain`, with Flag preservation. CLAIM-D2-INSUFFICIENT-TEST guarantees the escalation branch independently of CLAIM-W's real admitted outcome

#### R4 — Exact recheck at Commit

**Prototype, if funded.** Any mismatch in a pinned value (evidence generation, authoritative assessment-head identity/generation, assessment digest, admission digest, epoch, freshness, `valid_until`, executed bundle) hard-stops Commit, append-invalidates the prior ruling, and requires **revision latest+1** followed by Authorize → Submit → Verify and a fresh Commit decision. A **material** verdict or admission change additionally requires regenerating the answer or action content; a non-material provenance/freshness change may reuse the text only inside that new revision and after the full gate re-run. No prior allow carries forward; nothing auto-releases; no record is modified. The service-initiated `commit-verify` rereads the authoritative head and epoch, compares every value **pinned at Verify**, and recomputes freshness against its authoritative clock before atomically sealing the commitment and minting the token.

After an effect, automatic evidence-drift challenge initiation, an authorised resolution owner and completed correction/withdrawal remain Prototype targets within the scoped lifecycle. The terminal states must be fixed under R7; this does not establish effect-specific reversal or complete independent institutional remedy.

#### R7 — Receipts and Flag preservation

**Prototype, if funded.** Every receipt carries: action id and revision; principal, agent and authority chain; exact proposal digest; each gate decision with its verdict and timestamp; for each evidence dependency — assessment id, generation/version, digest, epoch, freshness state, analysis outcome, evidence-policy result, retrieval-lane summary and `executed_config_bundle_digest`; the escalation trail (contract id, answering role, disposition, what was narrowed and why); and oversight state (Silent / Flag / Stop). A successful-effect receipt additionally carries the commitment-record reference, token consumption, service acceptance and appended outcome. A denial receipt carries the refusal reason and states that **no commitment, token, service call or effect was created**. A challenged receipt/view links the contested entry, reliance state, route and resolution status; the authorised resolution owner and terminal remedy states must be fixed before PF-M3 acceptance. **Flag creation and preservation:** a successfully narrowed successor of an `escalate + Stop` lineage receives `allow + Flag`, and receipt acceptance asserts `ux_class = flag`. That Flag persists to every successor release derived from the lineage; it is cleared only by a fresh proposal whose premises are all qualified-and-supporting with no escalation in its own lineage — narrowing removes the unsupported part, it does not erase that the answer was narrowed.

### Evidence-work lifecycle

#### C11-Prototype — Export and runtime-data boundary

**Prototype, if funded.** The exporter is deterministic, its bundle immutable and digest-pinned, import verifies every digest, and no participant question, session artifact or runtime record leaves the isolated runtime.

#### R1 — Two-phase cost gate

**Later extension — retained acceptance constraints.** `ensureEvidence.plan` returns current assessments, missing jobs, a *conservative maximum* cost and the manifest digest. `ensureEvidence.execute` atomically commits the budget reservation and a durable outbox command in the gateway store before any external call. Within one server-derived owner/world scope, a database-enforced `semantic_dedupe_key` permits at most one active lease and one reservation for the same canonical analysis-input/claim digest, language, corpus/manifest version, admissibility scope and requested pipeline/config digest. The lease remains active through queued, running and completed-awaiting-admission states; it ends only on admission, refusal or terminal failure. Every command also carries a distinct immutable `command_idempotency_key` bound to `{semantic_dedupe_key, attempt_generation}`. A dispatcher calls FactHarbor's private-create boundary with that command key; FactHarbor atomically enforces owner/world plus command-key uniqueness. Response loss or process restart reuses the same command key and reconciles the same attempt to the same internal job reference, never a second job or charge. A concurrent same-scope user request creates no command, job, reservation, invite-quota charge or consumer attachment; it returns only `analysis-already-pending`, without a job id, input, progress, events or result. This retained R1 contract includes no multi-consumer job joining and no completion callback to the duplicate request. A request from another owner/world follows the ordinary absent-job path, creates its own private command, job and reservation, and cannot observe or suppress the first scope's work. Recovery must reconcile every reservation to exactly one private job, a terminal analysis outcome, or a proven-not-accepted/expired command whose reservation is released; an ambiguous external outcome remains fail-closed and is retried or reconciled by command key, never guessed away. An explicit retry may start only after the prior semantic lease is terminal; it atomically increments `attempt_generation`, reserves anew and creates a new command key. A changed semantic key is new work. For one action, reserve the complete dependency set or start nothing; an over-budget corpus sweep requires an explicitly narrowed manifest. Evidence spend settles when analysis finishes; Commit-time drift releases only the action/counter reservation.

If R1 is later implemented, just-in-time spending is automatic **only** for exact claims inside the approved corpus and **only** within a pre-reserved budget. After evidence becomes ready, release requires an **explicit user retry** producing a fresh revision — never a delayed automatic release.

Before later-extension R1 acceptance, its manifest must set the per-action and corpus budget ceilings, maximum wait duration and generations, and terminal retry policy. This definition does not invent those numeric limits.

#### D1b-Later — Bounded live resolution

**Later extension — retained acceptance constraints.** An exact claim in the approved corpus may enter `ensureEvidence.plan` → `execute`, subject to R1, to reserve budget atomically and run one bounded analysis. It has these terminal branches, never an indefinite wait:

- **qualified and admitted** → evidence ready; **nothing auto-releases**; on the participant's explicit retry a **fresh revision (latest+1)** is prepared and all gates re-run;
- **qualified with a materially changed verdict** → the honest answer changes: the assistant may only publish the new assessment after its own gate pass — the original proposal is superseded, never patched;
- **not-established** → recorded as such, unreleasable, reason reported;
- **spend ceiling reached or service down** → `verification unavailable` (distinct from both above);
- **retryable failure** → `evidence-pending`, reported separately.

#### C11-Later — Private job lifecycle and duplicate suppression

**Later extension — retained acceptance constraints.** Every private acquisition job receives immutable owner/world scope and private visibility in the same transaction that creates it, across initial/API create, batch or corpus-sweep create, retry-derived create, refresh/reanalysis and every internal or integration helper. Retry inherits scope and cannot weaken privacy. Same-scope concurrent duplicates obey R1; there is no join. `IsHidden` alone is not authorization, and an `unhide` operation cannot make a private acquisition job public. A default-deny owner policy applies to every create, read and mutation path, including list/search/count, detail/report, event history, SSE/live events, retry/cancel/annotation, hide/unhide/delete, internal status/result writes, job-keyed and aggregate metrics/diagnostics, and the evidence projection. The legacy global admin key is denied on private acquisition records

**C11 access matrix.** Test no credential, invalid credential, submission credential→raw read, projection credential→raw read, valid scope A→A, valid scope A→resource B, A→B mutation, and absent-resource parity on every route. Lists and counts omit other scopes; detail, history, metrics, mutations and SSE return the same external result for an absent resource and a resource in another scope, with SSE authorization complete before streaming begins. Submission and projection credentials are separate; the projection credential receives only redacted versioned evidence fields and neither can read raw list, detail, history, SSE, metrics, input or report data. A narrowly scoped, time-bound and audited break-glass capability may be specified separately; the legacy global admin key cannot access private acquisition records. A route-inventory test fails if any new job route lacks the same policy.

Minimum C11 concurrency/recovery cases: many identical same-scope executes produce one outbox command, one job and one reservation; the duplicate receives only `analysis-already-pending`; fault injection before/after reservation, before/after FactHarbor persistence, on lost response and on restart reuses the attempt's command idempotency key and reconciles to the same job; no recovery state permits a stranded reservation, paid orphan or second charge; completed-awaiting-admission remains duplicate-suppressed; the same input in another world follows the absent-job path; a different language, manifest, admissibility scope or config does not deduplicate; explicit retry after terminal failure atomically increments the attempt generation and creates exactly one new private, correctly scoped job under a new command key; and a privacy downgrade or `unhide` attempt cannot expose a private acquisition job.

### Corpus admission, authority and effect scope

#### C12 — Admission noninterference

**Later extension — retained acceptance constraints.** The acquisition-operator capability exhaustively permits requirement create/read and canonical-draft append only. Principal approval and admission execution use distinct identities. The admission endpoint accepts a strict approval reference and constructs operations server-side; callers cannot submit generic WAL operations. Its operation allowlist is approval consumption, admission activation and one epoch advance only. Static operation-inventory tests and before/after canonical authority-projection digests prove no change to actors, credentials, role/capability bindings, mandates, policies, handoffs, proposals/releases, commitments or effects

#### C13 — Structural acquisition-mode separation

**Later extension — retained acceptance constraints.** The immutable server-derived mode (`guided_release` or `evidence_acquisition`) is bound to the session/capability. Every acquisition identity is default-denied on every current and future route except its exhaustive capability allowlist; a route-registry test fails when a new route lacks an explicit acquisition disposition. The operator may create/read its requirement and append a canonical draft; a system worker may redeem valid spend approval into the R1 outbox; the separate admission identity may consume valid admission approval. Acquisition cannot invoke model selection/calls, conversation or model-output admission/release, escalation, records/challenges/access reporting, proposal, `/actions/execute`, Commit, service-execute or any downstream consequential effect. Queue receipts use a strict non-model schema containing only the requester's opaque requirement reference and bounded status. A fresh guided request receives an independently minted capability; acquisition sessions/artifacts cannot convert into guided credentials or action inputs

#### C14 — Corpus-steering control

**Later extension — retained acceptance constraints.** The admission rubric, mirrored-equivalence fixtures, corpus strata and balance tolerances are frozen and digested before submissions. The principal separately approves original-to-canonical semantic equivalence and the exact admission assessment. A failed rubric predicate or out-of-tolerance balance state refuses or halts admission without epoch change. Queue quotas are atomic and scoped by requester, world and time window; duplicates and floods cannot bypass counters or starve other scopes. Refusals and reasons remain auditable

#### C15 — Two approvals, admission replay and original-request death

**Later extension — retained acceptance constraints.** Both approval artifacts bind signature domain, issuer, audience, operation, owner/world, nonce and expiry. A pre-analysis `analysis_approval` binds signature domain, issuer, audience, operation, owner/world, nonce, expiry, requirement id/version, canonical analysis-input digest, language, requested pipeline/config and spend ceiling; it cannot admit. After analysis, each distinct `admission_approval` is language-scoped and binds one canonical wording digest to one same-language assessment id/version/digest, expected FactHarbor current-head identity/generation, recorded executed-config-bundle digest, validity boundary, admissibility-scope digest, rubric version and current requirement version. A matched DE/EN pair requires two explicit language bindings or one closed language-to-binding map containing both assessment references; missing or cross-language bindings deny. Admission consumption rereads the authoritative head and clock; head mismatch, invalidation or expiry refuses without consuming approval, activating admission/projection or advancing epoch. Replay/concurrency of the same artifact and idempotency key produces one result; independently approved scope artifacts serialize through a current-version compare-and-swap. Valid approval consumption, admission/projection activation and one epoch advance are atomic and fault-injected at every crash boundary. The triggering request may receive only C13's bounded queue status — never model/evidence content, a completion callback or release; only a fresh guided request may use the admission

#### C16 — Admissibility scope and Verify→Commit race

**Later extension — retained acceptance constraints.** At one epoch, publication-only admission permits the matching informational release and refuses an external effect. The pinned tuple includes epoch, world, claim/language/corpus version, assessment id/version/digest, authoritative assessment-head identity/generation, admission id/version/digest, canonical admissibility-scope digest, freshness, `valid_until`, service, action class, destination/audience, target and executed bundle. Every gateway eligibility-changing admission, restriction, withdrawal or projected assessment-head activation atomically activates the new authoritative admission head and advances the epoch once. Commit rereads that authoritative head and epoch, not only the derived projection, in the same serialized/CAS transaction that seals the commitment, and recomputes freshness against its authoritative clock. Barrier tests prove both orders of a scope/head change and the time boundary: change-before-Commit denies; Commit-before-change commits under the stated Commit boundary; Verify at `T−1` followed by Commit at `T` or `T+1` denies even when epoch and admission head are unchanged

**Terminology question before adoption:** informational release is itself externally effective. The intended distinction between that release and other action classes must be made explicit through a reviewed acceptance decision. This draft retains the conformance wording above; it does not adopt a new scope interpretation.
