> **Status: WORKING NOTES** — Evidence-Gated Agents user needs and requirements v0.2 draft; no implementation baseline adopted from this draft.

# Evidence-Gated Agents — user needs and requirements

These requirements describe the selected first-prototype direction and distinguish it from later product development. They are public working notes, not evidence of completed implementation.

<a id="stages-and-authority"></a>
## 1. Stages and authority

- **Exists:** demonstrated in a named component and version.
- **Prototype:** selected target for the first integrated experiment.
- **Later extension:** outside that prototype and requiring its own decision and evidence.
- **Aspiration:** research intent whose reliability remains unestablished.

The Runtime and FactHarbor remain separate existing foundations. The prototype direction does not retarget current Runtime implementation work by itself; compatibility, API contracts and acceptance tests require recorded implementation decisions.

## 2. Prototype requirements

### N-1. Decide whether an exact decision may be released

An accountable operator needs to stop a consequential decision from being released when authority, disclosure or evidence conditions fail.

- <a id="req-1"></a> **REQ-1 — Prototype:** a normal AI agent accepts a freely worded request and proposes one exact decision. Release requires the configured authority and disclosure checks plus a completed evidence examination that satisfies the prototype's simple release rule. Any failed, pending, contradictory, insufficient, ambiguous or technically incomplete result stops release. [Acceptance: SPEC-1](evidence-gated-agents-spec.md#spec-1).
- <a id="req-2"></a> **REQ-2 — Prototype:** Commit binds release to the exact checked decision, recipient and evidence result. A changed or narrower decision is a new attempt through every check. [Acceptance: SPEC-1](evidence-gated-agents-spec.md#spec-1).

The prototype's only real external effect is releasing the checked decision. It neither executes a resulting action nor checks authority for that action.

### N-2. Examine evidence for the actual decision

Operators and recipients need to see whether the evidence supports the decision the agent actually proposed, not a separately prepared answer.

- <a id="req-3"></a> **REQ-3 — Prototype:** after authority and disclosure checks, EGA starts one FactHarbor examination for the request, exact decision and permitted relevant context. The result preserves supporting and opposing evidence, limitations and uncertainty. [Acceptance: SPEC-2](evidence-gated-agents-spec.md#spec-2).
- <a id="req-4"></a> **REQ-4 — Prototype:** a pre-set simple rule maps the completed FactHarbor result to release or stop. Evaluation compares the full decision with the components FactHarbor identified and reports missed consequential components, German/English differences and run-to-run variation. [Acceptance: SPEC-2 and SPEC-3](evidence-gated-agents-spec.md#spec-2).

FactHarbor's decomposition and assessment are model-assisted. The prototype does not claim that every consequential component or every relevant source will be found.

### N-3. Inspect release and stop outcomes

Recipients need a usable explanation of what was checked and why the decision was released or stopped.

- <a id="req-5"></a> **REQ-5 — Prototype:** every registered release and stop produces a receipt linking the request, exact decision, recipient, authority and disclosure rulings, FactHarbor job and result, release rule, Commit decision and outcome. [Acceptance: SPEC-4](evidence-gated-agents-spec.md#spec-4).
- <a id="req-6"></a> **REQ-6 — Prototype:** formative review tests whether recipients can understand the evidence basis, limitations, outcome and route to question it. This is usability feedback, not independent validation or complete remedy. [Acceptance: SPEC-5](evidence-gated-agents-spec.md#spec-5).

### N-4. Extend the same control to later actions

- <a id="req-7"></a> **REQ-7 — Later extension:** before an autonomous message, tool call, filing, payment or system change, check authority, evidence and limits again at that effect's execution boundary. A prior decision release does not authorize a later action.
- <a id="req-8"></a> **REQ-8 — Prototype:** provide a reproducible guided German/English path plus free-request play mode. Controlled tests select requests expected to yield a clear, non-complex decision. Multiple independent decision and effect paths are not tested. [Acceptance: SPEC-1 and SPEC-5](evidence-gated-agents-spec.md#spec-1).
- <a id="req-9"></a> **REQ-9 — Later extension:** connect organisational identity, delegation and authorization systems; support permitted private evidence and lifecycle controls for multiple independent decisions and effects.

### N-5. Learn from a bounded experiment

- <a id="req-10"></a> **REQ-10 — Prototype:** pre-set the test requests, release rule and pass/fail conditions. Publish aggregate findings, failures and limitations, including unsupported releases, unjustified stops, missed decision components, language differences, run variance, latency and receipt comprehension. [Acceptance: SPEC-5](evidence-gated-agents-spec.md#spec-5).
- <a id="req-11"></a> **REQ-11 — Aspiration:** investigate whether AI can derive and critically review adequate evidence requirements across unfamiliar tasks. The first prototype does not establish that capability.

## 3. Current boundary

The selected prototype dynamically examines the agent's decision through FactHarbor. A fixed corpus and imported evidence bundle are not part of the current direction. The exact API contract, privacy boundary, Runtime compatibility and replacement effort estimate remain implementation work; they do not reopen the architecture decision.

The [technical specification](evidence-gated-agents-spec.md) defines the corresponding behaviour. The [project overview](../Assurance/Concepts/evidence-gated-agents.md) explains the idea and its limits in less technical language.
