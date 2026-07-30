> **Status: WORKING NOTES**

## Proposed accompanying feed post

𝗪𝗵𝗲𝗻 𝗦𝗵𝗼𝘂𝗹𝗱 𝗥𝘂𝗻𝘁𝗶𝗺𝗲 𝗔𝗜 𝗚𝗼𝘃𝗲𝗿𝗻𝗮𝗻𝗰𝗲 𝗜𝗻𝘁𝗲𝗿𝗿𝘂𝗽𝘁?

Ask a person to approve every step and the system trains them to stop reading. Approve nothing after launch and a live agent can move beyond what anyone assessed.

My last article asked who gets to check the runtime gate. This one asks when it should interrupt.

The better rule:

𝗚𝗼𝘃𝗲𝗿𝗻 𝘁𝗵𝗲 𝘁𝗿𝗮𝗻𝘀𝗶𝘁𝗶𝗼𝗻, 𝗻𝗼𝘁 𝗲𝘃𝗲𝗿𝘆 𝘀𝘁𝗲𝗽.

Runtime governance has two clocks:

1. the life of the system — design, deployment, operation, incident, and remedy;
2. the life of each action — from planning and preparation through evidence checks, decision, and review.

For each action, the Our AI Charter model asks:

𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲 → 𝗦𝘂𝗯𝗺𝗶𝘁 → 𝗩𝗲𝗿𝗶𝗳𝘆 → 𝗖𝗼𝗺𝗺𝗶𝘁 → 𝗥𝗲𝗹𝘆

Each time a model, tool, agent, or document contributes new material, the input and evidence checks re-open — fresh instructions and evidence must be screened, and drift reassessed. When nobody is in the seat, the checks do not disappear: a bounded mandate granted in advance replaces the click, and the service carrying out the action verifies that authority before anything becomes binding.

That does not mean endless approval prompts. Trace wide. Escalate narrow. Preserve human attention for consequential boundaries: when evidence becomes a decision basis, authority expands, data crosses a trust boundary, a proposal becomes an external effect, or the system leaves its approved conditions.

The practical test:

Which transition must not occur without which evidence, whose authority, and what recoverable record?

Full article below ↓

#AI #TrustworthyAI #AIGovernance #AgenticAI #PublicAI #AIAccountability

---

![Two connected AI-governance clocks: an outer system lifecycle running Design, Deploy, Operate, Incident, and Remedy surrounds an inner action path pairing Plan/Authorize, Prepare/Submit, Check/Verify, Decide/Commit, and Review/Rely; a diverse independent review group sits at the amber Decide/Commit boundary](article-runtime-ai-governance-when.png)

# When Should Runtime AI Governance Interrupt?

*Draft companion to [Runtime AI Governance Gets When Right. The Harder Question Is Who Gets to Check?](../Published/when-vs-who-ai-governance.md). That article argued for independent institutions around the runtime gate. This one opens the gate itself.*

Ask a person to approve every step and the system trains them to stop reading. Approve nothing after launch and the live system can move beyond what anyone assessed. Both are failures of timing.

“Govern at runtime” sounds precise until someone has to decide when an agent should proceed, warn, or stop — especially if it acts a thousand times an hour.

The better rule is:

> **Govern the transition, not every step.**

Intervene when evidence becomes a decision basis, when authority expands, when data crosses a trust boundary — where control or assurance changes — when a proposal becomes an external effect, or when a live system leaves the conditions under which it was approved. Trace the rest. Those are the transitions this article names.

That is what *when* should mean.

## The “when” has two clocks

Runtime governance does not replace lifecycle governance. It gives the lifecycle an action-level control point.

The first clock is the life of the system:

**design → deploy → operate → incident → remedy**

Before deployment, the provider and deployer define purpose, risk, limits, evidence, responsibilities, and exit conditions. During operation, they monitor performance, dependencies, misuse, drift, complaints, and material changes. When the system fails, they investigate, correct, constrain, roll back, or withdraw it. Afterwards, affected people still need a route to challenge the decision and obtain a remedy.

This is not a novel rejection of existing governance. The [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) treats risk management as continuous across the lifecycle and includes post-deployment monitoring, appeal, override, recovery, and decommissioning. For high-risk systems, the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) pairs human oversight (Article 14) with post-market monitoring (Article 72) and serious-incident reporting (Article 73). The July 2026 [Digital Omnibus on AI](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) (Regulation (EU) 2026/1744) moved the application of the Chapter III high-risk duties, including Article 14, to 2 December 2027 for Annex III systems and 2 August 2028 for product-based Annex I systems. Agentic systems are shipping now.

The second clock is the life of one AI-supported action:

**plan → prepare → check → decide → review**

The [Our AI Charter runtime reference model](../Assurance/Concepts/user-workflow-governance.md) turns those five moments into five gates:

1. **Plan → Authorize.** Is AI — and this system — appropriate here, and are the person and system allowed, able, and accountable within defined limits?
2. **Prepare → Submit.** May these data, sources, and instructions enter this system under the relevant privacy, rights, and confidentiality rules?
3. **Check → Verify.** Is the material evidence sound enough for this use, with uncertainty and disagreement carried forward?
4. **Decide → Commit.** May this exact action, for this purpose, target, cost, and consequence, become externally effective?
5. **Review → Rely.** Does the decision remain supportable, monitored, correctable, challengeable, and reversible or withdrawable where possible?

The gates are not a single pass. Every model, tool, or agent hop re-arms **Submit** and **Verify**: fresh material enters the system and fresh claims enter its reasoning. Untrusted web pages, documents, messages, and tool output are where injected instructions arrive, so Submit is a recurring boundary check, not a session-opening decision.

The model was written for a person in the seat. When the seat is empty, the gates do not disappear; they change enforcer. Authorize moves up to the bounded mandate a person or institution issued in advance; boundary controls, evidence checks, and policy components outside the acting model enforce Submit and Verify; and the service executing the action enforces Commit downstream. A gate must not quietly vanish because no one was there to pass it.

The first clock asks whether the system should remain in service. The second asks whether this action should move to its next state. They must be wired together. A rising rate of denials, escalations, overrides, or uneven outcomes on the action clock is a signal to constrain, reassess, or withdraw the release on the system clock. A suspension, policy change, or withdrawal on the system clock must invalidate affected authority already issued and still in flight.

## Stop where power changes hands

Not every transition deserves the same response. The runtime model’s core operating rule is **trace wide, escalate narrow**: preserve a reviewable path, but interrupt a person only when the interruption can materially improve a sufficiently important outcome.

Everything is traced. What varies is whether a person is interrupted:

- **Silent** — trace routine, reversible activity inside an authorized envelope and proceed.
- **Flag** — surface a material concern without blocking where proceeding preserves the user’s options.
- **Stop** — block for a decision when proceeding would cross a consequential boundary without adequate evidence or authority.

A stop should be ready when an action is irreversible, external, regulated, or person-affecting; when it creates a legal or financial obligation; when personal or protected data would leave a trust boundary; when the agent seeks a new tool, privilege, recipient, or purpose; when evidence conflicts on a load-bearing point; or when prompt injection, manipulation, or scope drift may have redirected the task.

The trigger alone is not enough. Human escalation is justified when three conditions hold together:

1. a human or independent reviewer can still change the outcome;
2. the stakes justify interruption; and
3. the system cannot responsibly resolve the issue inside its existing authority.

This is more concrete than “keep a human in the loop.” It says which decision the human must make, why it matters now, and what the system must do if no valid decision arrives. Silence may select a reversible default. It must never authorize an irreversible action. This preserves human attention for Stop gates that can still change a material outcome instead of spending it on routine, reversible approvals.

## Autonomy needs bounded authority, not endless prompts

High-frequency and autonomous systems cannot ask for fresh approval at every mechanical step. Nor should they receive a standing permission to do whatever becomes convenient.

The workable middle is a **bounded operating envelope**. A person or accountable institution authorizes a defined purpose, action class, tools, data, recipients, budget, rate and volume ceilings, number of people who may be affected, duration, geography, risk level, and limits on delegation. The envelope has an expiry, a revocation path, monitoring, rollback, and a safe stop. A material change reopens the decision.

Aggregate limits matter as much as per-action limits. A thousand individually admissible actions can compose an effect nobody authorized, so the gate needs cumulative counters and aggregate escalation triggers, not only a per-request test.

## What must be true at the gate

The five gates form a timeline: they say when and why governance should intervene. The Charter requirements form a control-and-evidence specification: they say what must be true — and what evidence must survive — for a consequential action to cross those boundaries. They do not map one-to-one: the structured proposal carries Submit and Verify into Commit, while the action-and-effect record connects the path through Rely.

The draft [Charter Commitments](../Assurance/Framework/charter-commitments.md) make this operational for consequential actions; the [agentic-control working note](ambient-agentic-ai-control.md#7-a-compliant-technical-control-plane) develops one implementation path:

1. separate observation, inference, recommendation, preparation, authorization, commitment, and external effect;
2. record the exact proposal before commitment;
3. bind the action to a specific, purpose-limited, time-limited, revocable mandate that is no broader than necessary, with a reviewable authority chain — the path from the person granting authority through every agent and service that acts — and a rule for overlapping or superseded mandates;
4. have a component independent of the acting model return **allow, deny, or escalate** against the current mandate and policy;
5. require the service producing the external effect to verify the exact authority and parameters again; and
6. join the proposal, authority, decision, effect, review, and remedy in a privacy-preserving, tamper-evident record that yields a receipt and routes for cancellation, reversal, compensation, challenge, and remedy.

The acting model must not approve its own request. Every consequential path must pass the gate, and each delegated agent must receive no more authority than its parent currently holds. Ambiguous, expired, revoked, broadened, substituted, or replayed authority fails closed: the action does not proceed.

Unavailable authority also fails closed by default. A signed mandate may support bounded offline verification only where its scope, short validity window, maximum allowed policy lag, revocation model, and residual risk were declared in advance; an indefinite cached *allow* is not a substitute for a current check. Revocation and narrowing must propagate through the delegation chain within a published bound. An action in flight when authority or policy changes is cancelled or, if already committed, routed to reversal and remedy. An interrupted multi-step workflow needs a named recovery owner responsible for cancellation, reversal, or compensation when partial commitment cannot be cleanly undone.

**Silent, Flag, and Stop** describe the user experience; **allow, deny, and escalate** are machine gate responses. They map to each other but are not synonyms: *escalate* produces a Stop, *deny* may never interrupt a person if a safe fallback exists, and *allow* may still carry a Flag.

The pieces are feasible even though the general system is unfinished. [OAuth Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396) already shows how fine-grained transaction details can be bound to an authorization request. The US National Cybersecurity Center of Excellence’s February 2026 [draft concept paper](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf) for a potential demonstration project explores agent identification, authorization, access delegation, intent, binding agent actions to human identity, verifiable auditing, and prompt-injection controls. That is a signal that standards work is starting, not that it is finished. The OWASP [LLM Prompt Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) recommends least-privilege tools and screening proposed actions against the user’s original intent; [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) adds downstream, user-context execution and approval for high-impact actions.

These are building blocks, not proof that runtime accountability is solved.

## Consider one public decision

Imagine an AI assistant supporting a public grant decision.

At **Plan**, the agency decides whether this system is suitable and what it may do: retrieve permitted material, compare an application with published criteria, draft an assessment, and identify uncertainty. It may not invent a criterion, change the programme’s purpose, or make the final award.

At **Prepare**, applicant data can enter only through the approved system and for the declared purpose. A request to send the file to an unapproved model or tool stops at the boundary.

At **Check**, the assistant links findings to the application and criteria. A minor ambiguity may be flagged. Missing evidence on an eligibility condition, conflicting records, or a suspected injected instruction stops the path before the output becomes a decision basis. A draft is only a draft while nothing relies on it; filing it in the case record or using it to frame the decision has already crossed that boundary.

At **Decide**, before an award, rejection, notification, or payment becomes effective, the commit gate binds the exact applicant, programme rule, amount, evidence, disclosed data, decision-maker, and current policy version. A properly authorized official reviews the consequential judgment, but review quality is not established by a click. Workload, time-on-task distributions, override and divergence rates, and sampled reasoning quality are monitored together, with the sampling done from outside the deciding unit. A reviewer who never disagrees is a finding, not a reassurance. The executing service verifies the mandate rather than trusting the model’s claim that approval occurred.

At **Review**, the applicant receives, as of right, a scoped extract of their own determination: the decision, its basis, the policy version, the authority chain, the human-review event, and the challenge route — plus a receipt showing that the full record was lodged. The agency preserves the decision basis, authority, review event, and outcome; monitors repeated errors and uneven outcomes; and corrects, reopens, or withdraws reliance when the evidence no longer holds.

The point is not to automate public judgment. It is to prevent automation from quietly crossing the line between assisting a judgment and exercising power.

## A record is part of the control

Runtime governance fails if it produces only a green light.

The decision record should be sufficient to reconstruct the proposal, material evidence and uncertainty, authority chain, policy and system version, admissibility decision, commitment, external effect, human-review event, and route to challenge or remedy. It should also say what was deliberately not captured and why.

But accountability must not become ambient surveillance. The record’s subject is the consequential action and its authority, not the whole conversation. Access should be role-scoped, sensitive content protected, and every deeper access itself logged. The Charter’s [split-custody proposal](split-custody-per-action-records.md) separates content, integrity, survivability, and access so neither the operator nor an evidence custodian quietly controls the whole record.

This is also why **Review** belongs inside the runtime model. A system is not governable merely because it paused at the right moment. It must preserve enough evidence for correction and challenge, learn from failures, and stop relying on conditions that have changed.

One limit belongs in the open. These mechanisms protect a record that was created; they cannot expose a determination that was never recorded or was false when created. That gap is institutional, not cryptographic: it needs a duty to lodge, an affected person’s right to discover that a decision was made about them, and independent custody or oversight able to notice when the expected record is missing.

## What “when” does not solve

Identity does not establish permission. A signed mandate does not establish fairness. A compliant gate does not establish legitimacy.

Runtime timing cannot decide whether the rule itself is lawful or fair, whether the reviewer is independent, whether an affected person can reach the evidence, or whether anyone can bind a remedy. Those are the institutional questions in the [earlier article](../Published/when-vs-who-ai-governance.md): split rulemaking, operation, record custody, independent review, and remedy.

Assurance of a release, authorization of an action, and accountability for its consequence are three different units. None substitutes for the other two.

## The practical test

The useful question is not simply, “Is there a human in the loop?”

Ask instead:

> **Which transition must not occur without which evidence, whose authority, and what recoverable record?**

If the system cannot answer, it should not cross that boundary.

This is how the Charter’s five public obligations reach runtime: not as labels, but as controls that keep actions purpose-bound; answerable to people; safe, secure, private, and resilient; fair in practice; and open to evidence and correction. Fairness cannot be established by a single gate. Per-action checks must screen for unjustified treatment, while aggregate outcome monitoring reveals patterns that individual checks cannot.

Runtime governance gets *when* right when it governs the handoffs:

- from design to deployment only after the release’s purpose, limits, risks, and responsibilities are reviewable;
- from information to a decision basis only after material evidence and uncertainty have been checked;
- from proposal to effect only under exact, current, independently enforced authority;
- from ordinary operation to escalation when the action leaves its approved envelope;
- from incident to correction, withdrawal, and remedy while the evidence still survives.

Govern the transition. Preserve the record. Keep the power answerable to the people who bear its consequences.

**Built by many. Accountable to all.**

`#AI #AIGovernance #AgenticAI #PublicAI #TrustworthyAI #AIAccountability`

*Source and further work: [Our AI Charter](https://robertschaub.github.io/our-ai-charter/).*
