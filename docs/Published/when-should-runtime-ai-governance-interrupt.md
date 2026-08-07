> **Status: PUBLISHED 2026-07-30** — mirror of the LinkedIn article *When Should Runtime AI Governance Interrupt?*, published 30 July 2026. The accompanying feed post, cover, and related public discussion are mirrored here.
> Canonical article: [https://www.linkedin.com/pulse/when-should-runtime-ai-governance-interrupt-robert-schaub-mc2sc](https://www.linkedin.com/pulse/when-should-runtime-ai-governance-interrupt-robert-schaub-mc2sc)

## Accompanying feed post

𝗪𝗵𝗲𝗻 𝗦𝗵𝗼𝘂𝗹𝗱 𝗥𝘂𝗻𝘁𝗶𝗺𝗲 𝗔𝗜 𝗚𝗼𝘃𝗲𝗿𝗻𝗮𝗻𝗰𝗲 𝗜𝗻𝘁𝗲𝗿𝗿𝘂𝗽𝘁?

Ask a person to approve every step and the system trains them to stop reading. Approve nothing after launch and a live agent can move beyond what anyone assessed.

My last article asked who gets to check the runtime gate. This one asks when it should interrupt.

The better rule:

𝗚𝗼𝘃𝗲𝗿𝗻 𝗲𝘃𝗲𝗿𝘆 𝗮𝘂𝘁𝗵𝗼𝗿𝗶𝘁𝘆-𝗯𝗲𝗮𝗿𝗶𝗻𝗴 𝘁𝗿𝗮𝗻𝘀𝗶𝘁𝗶𝗼𝗻 — 𝗻𝗼𝘁 𝗲𝘃𝗲𝗿𝘆 𝗶𝗻𝗳𝗲𝗿𝗲𝗻𝗰𝗲 𝗼𝗿 𝗺𝗲𝗰𝗵𝗮𝗻𝗶𝗰𝗮𝗹 𝘀𝘁𝗲𝗽.

Runtime governance has two clocks:

1. the life of the system — design, deployment, operation, incident, and remedy;
2. the life of each action — from planning and preparation through evidence checks, decision, and review.

For each action, the Our AI Charter model asks:

𝗔𝘂𝘁𝗵𝗼𝗿𝗶𝘇𝗲 → 𝗦𝘂𝗯𝗺𝗶𝘁 → 𝗩𝗲𝗿𝗶𝗳𝘆 → 𝗖𝗼𝗺𝗺𝗶𝘁 → 𝗥𝗲𝗹𝘆

Two boundaries matter most. Before inference, an entry gate checks whether new data, instructions, and tool output may enter the path. Before external effect, a commitment gate verifies the exact action, current authority, and policy again.

The acting model does not approve itself. An independent component returns allow, deny, or escalate; the user sees only what needs attention. Missing or expired authority fails closed. A human may choose among valid options, but cannot create a basis that is absent.

That does not mean endless prompts. Preserve human attention for consequential boundaries: when evidence becomes a decision basis, authority expands, data crosses a trust boundary, a proposal becomes an external effect, or the system leaves its approved conditions.

The practical test:

Which transition must not occur without which evidence, whose authority, and what action-scoped, tamper-evident record?

Full article below ↓

#AI #TrustworthyAI #AIGovernance #AgenticAI #PublicAI #AIAccountability

_[Original feed post on LinkedIn](https://www.linkedin.com/posts/robertschaub_ai-trustworthyai-aigovernance-activity-7488606064989360129-JukJ)._

---

![Two connected AI-governance clocks explicitly labeled System Lifecycle and Action Path: the outer lifecycle runs Design, Deploy, Operate, Incident, and Remedy; the inner path visually separates each navy activity from its orange-capsule gate—Plan/Authorize, Prepare/Submit, Check/Verify, Decide/Commit, and Review/Rely—with machine-enforced entry and commitment gates outside the acting model, a loop from Verify back to Entry for new inputs, a human branch only on escalation, and a sealed action record feeding review and remedy](when-should-runtime-ai-governance-interrupt.png)

# When Should Runtime AI Governance Interrupt?

*Companion to [Runtime AI Governance Gets When Right. The Harder Question Is Who Gets to Check?](when-vs-who-ai-governance.md). That article argued for independent institutions around the runtime gate. This one opens the gate itself.*

Ask a person to approve every step and the system trains them to stop reading. Approve nothing after launch and the live system can move beyond what anyone assessed. Both are failures of timing.

“Govern at runtime” sounds precise until someone has to decide when an agent should proceed, warn, or stop — especially if it acts a thousand times an hour.

The better rule is:

> **Govern every authority-bearing transition — not every inference or mechanical step.**

Intervene when evidence becomes a decision basis, authority expands, data crosses a trust boundary, a proposal becomes an external effect, or a live system leaves the conditions under which it was approved. Those are changes in control, reliance, or consequence — not merely internal model-state changes.

Three roles must not blur: the model proposes; a component outside the model decides under current policy and authority; the service producing the effect verifies that decision again.

[Stuart-Mueller and Woodward's *The Wrong Layer*](https://doi.org/10.5281/zenodo.21397661) supplies an important premise: governance needs per-action evidence that a consequential machine action was authorized, admissible, and bounded when it occurred. The Charter model developed here adds a two-clock timing structure, five public-facing gates, and the institutional route from record to independent review and remedy.

## The “when” has two clocks

Runtime governance does not replace lifecycle governance. It gives the lifecycle an action-level control point.

The first clock is the life of the system:

**design → deploy → operate → incident → remedy**

Before deployment, the provider and deployer define purpose, risk, limits, evidence, responsibilities, and exit conditions. During operation, they monitor performance, drift, complaints, and material changes. Failure triggers investigation, constraint, rollback, withdrawal, or remedy.

The [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) similarly treats risk management as continuous. The [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) pairs human oversight (Article 14) with post-market monitoring (Article 72) and serious-incident reporting (Article 73). [Regulation (EU) 2026/1744, the Digital Omnibus on AI](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng), moved the application of Chapter III's high-risk-system duties to 2 December 2027 for systems covered by Article 6(2) and Annex III, and 2 August 2028 for systems covered by Article 6(1) and Annex I. Agentic systems are shipping now.

The second clock is the life of one AI-supported action:

**plan → prepare → check → decide → review**

The [Our AI Charter runtime reference model](../Assurance/Concepts/user-workflow-governance.md) turns those five moments into five gates:

1. **Plan → Authorize.** Is AI — and this system — appropriate here, and are the person and system allowed, able, and accountable within defined limits?
2. **Prepare → Submit.** May these data, sources, and instructions enter this system under the relevant privacy, rights, and confidentiality rules?
3. **Check → Verify.** Is the material evidence sound enough for this use, with uncertainty and disagreement carried forward?
4. **Decide → Commit.** May this exact action, for this purpose, target, cost, and consequence, become externally effective?
5. **Review → Rely.** Does the decision remain supportable, monitored, correctable, challengeable, and reversible or withdrawable where possible?

Two enforceable boundaries anchor the path:

- **Entry boundary — before reliance or inference.** May these instructions, data, resource identifiers, tool structures, and outputs enter this action path? Their origin, integrity, rights, policy fit, and trust status are checked before the acting model may rely on them.
- **Commitment boundary — before external effect.** May this exact proposal become a tool call, message, payment, filing, deployment, decision, or other effect under the current mandate and policy? The executing service checks again rather than trusting the model's claim that approval occurred.

Every model, tool, or agent hop re-arms **Submit** and **Verify**. Machine controls can establish provenance, signatures, required fields, policy version, and source admissibility; they cannot deterministically establish that disputed evidence is true, sufficient, or fair. Those judgments need an accountable route, with uncertainty preserved.

When nobody is in the seat, the gates do not disappear; they change enforcer. **Authorize** moves up to a bounded mandate granted in advance, external components enforce the entry and commitment rules, and only a valid escalation route can interrupt a person. A gate must not vanish because no one was there to click it.

The first clock asks whether the system should remain in service. The second asks whether this action should advance. They must be wired together: rising denials, escalations, overrides, or uneven outcomes can constrain or withdraw a release; a lifecycle suspension or policy change must invalidate affected authority already issued and in flight.

## The gate decides before the interface interrupts

For each consequential transition, a component independent of the acting model returns **allow, deny, or escalate** against the current mandate and policy. Missing, ambiguous, expired, revoked, broadened, substituted, or replayed authority fails closed. A human approval cannot create a missing legal, policy, evidentiary, or institutional basis.

Only then does the user experience vary:

- **Silent** — record an allowed, routine, reversible action inside the authorized envelope without prompting.
- **Flag** — surface a concern without blocking where a valid basis already exists.
- **Stop** — block for a decision when proceeding would cross a consequential boundary without adequate evidence or authority.

A denial may never interrupt a person if a safe fallback exists. An escalation produces a Stop. An allow may carry a Flag, but not where the concern undermines the basis for a consequential transition.

A Stop is required when an action would be irreversible, external, regulated, or person-affecting without the declared basis; when it creates a legal or financial obligation; when protected data would leave a trust boundary; when the agent seeks a new tool, privilege, recipient, or purpose; when evidence conflicts on a load-bearing point; or when manipulation, injected instructions, or corrupted context may have redirected the task.

Human escalation is justified when three conditions hold together:

1. a human or independent reviewer can still change the outcome;
2. the stakes justify interruption; and
3. the system cannot responsibly resolve the issue inside its existing authority.

The escalation names the rule, decision, eligible role, evidence, response bound, valid options, safe default, and record consequences. The person may allow within existing authority, deny, narrow, seek review, cancel, reverse, or route to remedy. Silence may select only a declared reversible fallback; it cannot grant authority.

## Autonomy needs bounded authority, not endless prompts

High-frequency and autonomous systems cannot ask for fresh approval at every mechanical step. Nor should they receive a standing permission to do whatever becomes convenient.

The workable middle is a **bounded operating envelope**. Its baseline identifies the principal, purpose, action class, tools, data, recipients, budget and volume ceilings, affected population, duration, risk level, and delegation limits. It has an expiry, revocation path, monitoring, rollback, and safe stop.

An exception is a visible state transition, not new standing authority. It applies to a defined action, tool, turn, or scope; expires; and returns the path to its baseline. Context may persist. Permission must not persist silently with it.

Aggregate limits matter as much as per-action limits. A thousand individually admissible actions can compose an effect nobody authorized, so the gate needs cumulative counters and aggregate escalation triggers, not only a per-request test.

The draft [Charter Commitments](../Assurance/Framework/charter-commitments.md) and [agentic-control working note](../wip/ambient-agentic-ai-control.md#7-a-compliant-technical-control-plane) specify the implementation: freeze the proposal; bind it to a current, purpose-limited, time-limited, revocable mandate and policy; gate it outside the acting model; declare the intervention contract for any escalation; re-verify it at the executing service; and seal the decision before effect in an action-scoped, tamper-evident record. Delegation cannot broaden authority. Stale or unavailable authority fails closed, and interrupted workflows need a recovery owner.

Existing building blocks include fine-grained authorization in [OAuth Rich Authorization Requests](https://datatracker.ietf.org/doc/html/rfc9396); the February 2026 [NCCoE draft concept paper on software and AI agent identity and authorization](https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf), which asks how an agent proves authority for a specific action, conveys intent, delegates authority, and binds actions back to human authorization; and OWASP guidance on [prompt injection](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) and [excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/). They do not yet form a complete accountability system.

## Consider one public decision

Imagine an AI assistant supporting a public grant decision.

At **Plan**, the agency authorizes the system to retrieve permitted material, compare it with published criteria, draft an assessment, and identify uncertainty — but not invent criteria or make the award.

At **Prepare**, applicant data may enter only the approved system for the declared purpose. An unapproved model or tool stops at the entry boundary.

At **Check**, machine controls confirm source and integrity; an accountable reviewer judges disputed meaning or sufficiency. Missing eligibility evidence, conflicting records, or corrupted context stops the path before the output becomes a decision basis. That transition maps to an observable event: filing the draft, presenting it in the decision interface, or feeding it to the next stage.

At **Decide**, the commit gate binds the applicant, rule, amount, evidence, disclosed data, decision-maker, and policy version. An official chooses only among valid dispositions; the executing service verifies the gate decision rather than trusting a model claim or bare approval click.

At **Review**, the applicant receives a scoped extract of the determination and a receipt showing that the full record was lodged. The agency monitors errors and uneven outcomes, and corrects, reopens, or withdraws reliance when the basis no longer holds.

The point is not to automate public judgment. It is to prevent automation from quietly crossing the line between assisting a judgment and exercising power.

## A record is part of the control

Runtime governance fails if it produces only a green light.

Every gate decision and consequential action is recorded. The record is sealed before effect and bound to what the service did. It preserves the proposal, material evidence and uncertainty, authority, policy and system version, gate decision, effect, intervention, and challenge route.

Accountability must not become ambient surveillance. The record's subject is the action and its authority, not every token or the whole conversation. Access is role-scoped and logged. The Charter's [split-custody proposal](../wip/split-custody-per-action-records.md) separates content, integrity, survivability, and access.

One limit belongs in the open. These mechanisms protect a record that was created; they cannot expose a determination that was never recorded or was false when created. That gap is institutional, not cryptographic: it needs a duty to lodge, an affected person's right to discover that a decision was made about them, and independent oversight able to notice when an expected record is missing.

## What “when” does not solve

Identity does not establish permission. A signed mandate does not establish fairness. A compliant gate does not establish legitimacy.

Runtime timing cannot decide whether the rule itself is lawful or fair, whether the reviewer is independent, whether an affected person can reach the evidence, or whether anyone can bind a remedy. Those are the institutional questions in the [earlier article](when-vs-who-ai-governance.md): split rulemaking, operation, record custody, independent review, and remedy.

Assurance of a release, authorization of an action, and accountability for its consequence are three different units. None substitutes for the other two.

This is how the Charter's five public obligations reach runtime: actions stay purpose-bound; answerable to people; safe, secure, private, and resilient; fair in practice; and open to evidence and correction. Fairness cannot be established by a single gate. Per-action checks screen for unjustified treatment, while aggregate outcome monitoring reveals patterns individual checks cannot.

## The practical test

The useful question is not simply, “Is there a human in the loop?”

Ask instead:

> **Which transition must not occur without which evidence, whose authority, and what action-scoped, tamper-evident record?**

If the system cannot answer, it should not cross that boundary.

Runtime governance gets *when* right when it governs the handoffs:

- from design to deployment only after the release’s purpose, limits, risks, and responsibilities are reviewable;
- from information to a decision basis only after material evidence and uncertainty have been checked;
- from proposal to effect only under exact, current, independently enforced authority;
- from ordinary operation to escalation when the action leaves its approved envelope;
- from incident to correction, withdrawal, and remedy while the evidence still survives.

Govern every authority-bearing transition. Preserve the action-scoped record. Keep the power answerable to the people who bear its consequences.

**Built by many. Accountable to all.**

`#AI #AIGovernance #AgenticAI #PublicAI #TrustworthyAI #AIAccountability`

*Source and further work: [Our AI Charter](https://robertschaub.github.io/our-ai-charter/).*

---

## Related public discussion

**Robert Schaub — reply in Valerie (Val) Fraser's *The Cost of Not Seeing* discussion** (posted 2026-08-03)

_Published on [Fraser's LinkedIn post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7487804966309466113/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287489986109435789314%2Curn%3Ali%3AugcPost%3A7487804966309466113%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287490017573451857920%2Curn%3Ali%3AugcPost%3A7487804966309466113%29). Fraser had moved the question upstream: to conditions that make concerns unsafe or futile to voice, and to AI-generated meeting notes that can make a qualified or dissenting discussion appear more settled than it was._

You're right about the ordering: nothing downstream can recover a concern that was never voiced, or restore doubt that the record no longer shows.

The person responsible for the meeting should circulate AI-generated notes as a draft, clearly separating what was decided from what remained contested or unresolved.

Participants should be able to correct the draft or ensure unresolved disagreement remains visible before it is relied on.

Where a summary may shape a consequential decision, a named reviewer should verify its key claims against the available evidence; fluency is not evidence.

These controls cannot replace a safe route to raise concerns outside the reporting line.

They should be proportionate—strongest where decisions have real consequences, without turning every meeting into surveillance.

**Valerie (Val) Fraser — follow-up (summary)** (posted 2026-08-03)

_In a [follow-up reply](https://www.linkedin.com/feed/update/urn:li:ugcPost:7487804966309466113/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287489986109435789314%2Curn%3Ali%3AugcPost%3A7487804966309466113%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287490023768011198464%2Curn%3Ali%3AugcPost%3A7487804966309466113%29), Fraser argued that even an accurate decision record can flatten adjacent risks, tensions, and the conditions that made a concern meaningful. If such a record later becomes learning material for AI, future outputs may inherit the simplified account as though it were the whole truth._

**Robert Schaub — follow-up** (posted 2026-08-03)

_[Published in response](https://www.linkedin.com/feed/update/urn:li:ugcPost:7487804966309466113/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287489986109435789314%2Curn%3Ali%3AugcPost%3A7487804966309466113%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287490035897443373056%2Curn%3Ali%3AugcPost%3A7487804966309466113%29)._

I agree—the key is to distinguish the purpose of the record from any later use. A decision summary can accurately document what was decided and still be incomplete as an account of everything that informed it.

The practical safeguard is to label what the summary is for, preserve the uncertainty and unresolved context that were material to the decision, and not reuse it as training or decision input without first checking that it contains the context needed for that new purpose. The aim is not to record everything, but to prevent a concise record from later being treated as the whole truth.

**Robert Schaub — comment on Lara Stuart-Mueller's EU AI Act post** (edited; verified 2026-08-07)

_[Published on Stuart-Mueller's LinkedIn post](https://www.linkedin.com/posts/lara-stuart-mueller-bab1172ab_the-eu-ai-act-is-a-gigantic-regulatory-band-aid-share-7489860271662919680-xNnf)._

The design point lands, but the dates complicate it.

For high-risk systems, the Act contains technical design and lifecycle requirements, not just paperwork:
Risk management, pre-market testing, event logging, and human oversight.
Those duties do not begin applying until December 2027 or August 2028.

The narrower gap is that the Act does not establish a general action-time check showing that each consequential action is authorised and within limits.
Who performs that check is an institutional question, not only an engineering one!

**Robert Schaub — comment on B. Setyadi's *AI Governance Series Vol. 1*** (posted 2026-08-04)

_[Published on Setyadi's LinkedIn post](https://www.linkedin.com/feed/update/urn:li:ugcPost:7489956885828128768/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287490278578509725697%2Curn%3Ali%3AugcPost%3A7489956885828128768%29). Setyadi's visual paper proposes **Observe → Understand → Model → Validate → Infer → Respond** as a reasoning-preservation flow. The comment connects that flow to the Charter's distinction between testimony, inference, confirmation, permission, and action-time authorization._

[B. Setyadi](https://www.linkedin.com/in/bsetyadi/) Your Observe → Understand → Model → Validate → Infer → Respond flow names an important design rule.

I would add one governance boundary: preserve not only a reasoning trace, but the status of each element—what the person actually said, what the system inferred and with what uncertainty, what the person confirmed, and what it has revocable permission to use or remember.

An interpretation must never silently become a fact.

Where a conclusion may lead to consequential action, faithfully modelled intent is still not authorization.

Observation, inference, recommendation, preparation, authorization, commitment and effect should remain distinct, with the final check outside the generative model and a record that supports challenge, correction and remedy.

Preserve the reasoning—and preserve the person’s authority over what follows from it.
