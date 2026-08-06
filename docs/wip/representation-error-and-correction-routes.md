> **Status: WORKING NOTES** — one reading pass (2026-08-06) over a public LinkedIn thread on decision governance, set against the Charter's existing correction duties to isolate what is genuinely not yet covered. Attribution is deliberately exact and the source's own caveat is carried through; the proposals in the last section are not adopted Charter text. Re-verify before relying on anything here.

# Representation error and the correction route

*The question.* The Charter's **Rely** gate lets an affected person challenge a determination and have reliance on it reopened, corrected, or withdrawn. But what happens when the determination was reached correctly and what is wrong is the picture the rules encode — the categories, the process rules, the operating envelope the mandate was written against? A publicly published account of exactly this failure appeared in late July 2026. This note checks it against what the Charter already says and keeps only what is new.

**Short answer.** Most of it the Charter already covers, and in one place more completely than the source does. Three things it does not name: **representation error** as a failure class, the case that **fits no category**, and the **second reading of an exception pattern**.

## Source

Wojciech Zygmunt Kaleta ([linkedin.com/in/wkaleta](https://www.linkedin.com/in/wkaleta/)) publishes a line of work he calls *Decision Engineering*, centred on what he terms *False Situational Awareness* — confidence remaining high while the accuracy of the situational picture is already falling. Two posts carry the material relevant here. LinkedIn shows relative timestamps only, so the dates below are derived from a 2026-08-06 read and are approximate to the day.

| Post | Read as | Content used here |
|---|---|---|
| [*Public Field Case*](https://www.linkedin.com/feed/update/urn:li:activity:7488525809452867585/) (10-page attachment) | ≈2026-07-30 ("1w", edited) | model/representation distinction; the correction chain; the category and exception questions |
| [*A decision can remain in force…*](https://www.linkedin.com/feed/update/urn:li:activity:7489956905885446144/) | ≈2026-08-03 ("3d") | inherited authority; revalidation triggers |

He states the failure as a chain that must remain unbroken: *"contradiction → preserved unresolved case → evidence about the representation → institutional standing → competent authority → binding reassessment → changed representation, authority or execution."* Two of his framings are load-bearing for what follows: a complaint channel is *"not necessarily a correction mechanism"*, and an exception log is *"not necessarily a reopening mechanism"*.

He labels the artifact *"a conceptual stress-test, not as a validated governance framework"*, credits thirteen named contributors on it, and states that attribution there recognises contribution without implying co-authorship or endorsement. That caveat travels with the material: nothing below should be read as a validated result of his, and no affiliation, endorsement, or joint work is claimed by this repository.

The Charter's own question in reply — who performs the reassessment when the body that would revalidate the authority is the body relying on it — was put publicly under the second post on 2026-08-06. Kaleta answered the same day with a distinction this note adopts: **institutional standing is not epistemic standing.** An organisation may hold the formal authority to reassess its own picture and still lack independence from the assumptions, incentives, and evidence chain that produced it. His test is therefore not who is authorised to review, but what gives a review *"the capacity to genuinely disconfirm"* the picture the institution still relies on; a reassessment that cannot reduce, suspend, or reopen the prior decision's authority is, in his phrase, *"procedurally valid while remaining epistemically captive"*.

## What the Charter already covers

Recorded so the overlapping parts are not re-imported as if new.

- **Rule-level correction and lineage.** [Charter Commitments](../Assurance/Framework/charter-commitments.md), duty 8, already reaches past the individual decision: where a material change to *an authority source, policy, rule set, evidence corpus, or verification logic* could alter outcomes, its effects are assessed before deployment against prior cases; and where evidence, a source, or a rule is corrected or withdrawn, lineage identifies the affected decisions so reliance can be reopened, corrected, or withdrawn rather than left standing. This is a superset of the chain's final step, and it adds a lineage stage the chain does not have.
- **Authority that expires.** Consequential-action baseline 3: the action mandate is specific, purpose-bound, time-limited, and revocable.
- **Self-approval barred at the model layer.** Consequential-action baseline 4: the admissibility check runs in a component that does not rely on the acting model to approve its own request.
- **Exceptions that do not harden.** [Runtime gates POC](runtime-gates-poc-spec.md) §5: an exception is a visible state transition scoped to one action, tool, or turn, expiring back to baseline — never silent standing authority.
- **Pattern as a trigger.** Same section: per-mandate cumulative counters and an escalation-pattern counter; crossing a ceiling escalates even where each action was individually admissible, and a recurring escalation or override pattern narrows the operating envelope pending re-authorization.

## What it does not name

**1. Representation error as a failure class.** The phrase does not occur anywhere in this repository. Duty 8 treats rules as things that *get changed* and then requires the consequences to be traced; it never names the state in which the system is performing exactly as specified and the specification itself has stopped describing the world. The distinction is between a model that is wrong and an organisational picture — data, categories, process rules — that has gone stale while every component still passes its own checks. Nothing in the Charter is inconsistent with this, which is the problem: it is implied everywhere and owned nowhere, so no duty attaches to detecting it.

**2. The case that fits no category.** The Charter's runtime verdicts are allow, deny, or escalate, and its risk register carries *unresolved findings*. Neither is the same as preserving a case **because no available category represents it adequately**, and treating that preservation as evidence about the category set. Escalate routes an individual case to a human, who resolves it and closes it; the anomaly is consumed rather than retained. A category set that fails repeatedly generates a stream of individually-resolved escalations and no signal at all.

**3. The second reading of an exception pattern.** The POC's escalation-pattern counter reads a run of overrides one way — the actor is pressing against its envelope — and responds by narrowing the envelope pending re-authorization. The same run supports a second reading: the envelope is drawn in the wrong place, and the overrides are evidence about the rule rather than about the actor. The Charter currently implements only the first. Where the second reading is correct, narrowing the envelope is the exactly wrong response, and it will look like successful governance while making the mismatch worse.

## What would follow

Not adopted text. Recorded as candidate work, in ascending order of cost.

- **Name the failure class.** Add representation error to the Charter's vocabulary as a distinct thing from model error, and state that duty 8's re-check triggers include evidence that the rule set has stopped describing the assessed reality — not only that it changed.
- **Give the no-fit case somewhere to go.** A verdict or record state for *no category applies*, distinct from escalate, that is retained and countable rather than closed on resolution. The cheapest version is a required field on an escalation disposition: whether the case was resolved *within* the category set or *despite* it.
- **Split the pattern counter.** Where a pattern trigger fires, record which reading it supports before acting on it. Narrowing the envelope and reopening the rule are different responses to the same signal, and the POC currently cannot express the second.
- **Answer the standing question.** All of the above still routes correction through the institution operating the system. The Charter's distinctive claim is that this is insufficient — [*Runtime AI Governance Gets When Right. The Harder Question Is Who Gets to Check?*](../Published/when-vs-who-ai-governance.md) (published 2026-07-23) — and the POC records the same gap honestly: independent reviewer and remedy decider are the two roles it cannot simulate, and its challenge beat populates a routing obligation rather than a remedy. Naming representation error sharpens that gap rather than closing it, because the party best placed to notice a stale representation is often the party relying on it.

  **A criterion for epistemic standing.** Capacity to disconfirm has to be structural, or it reduces to the reviewer's virtue. Three conditions, proposed in the exchange above and consistent with the Charter's existing [independence rule](../Assurance/Framework/charter-commitments.md): the reviewer can obtain evidence the institution would not volunteer; the finding changes the permission state rather than producing a report; and the reviewer does not depend on the reviewed party for appointment, funding, or renewal. The third is usually decisive — a reviewer who needs the relationship to continue can afford every finding except the disconfirming one. The Charter already states the economic half of this: the party that writes the method does not evaluate anyone, the assessor is paid a flat fee regardless of outcome, and the method-steward takes no per-product royalties from the systems it judges. What it does not yet state is the access half — what a reviewer may reach without the reviewed party's cooperation — which is where the [split-custody design](split-custody-per-action-records.md) becomes load-bearing rather than optional.

## Open questions

- Is representation error a distinct duty, or a trigger condition inside duty 8? Adding a duty is expensive and the Charter's duty set is deliberately short.
- Can a *no category applies* state be made countable without becoming a dumping ground for hard cases?
- Who has standing to submit evidence about a representation, as opposed to evidence about their own case? The affected person usually sees one instance; the pattern is visible only to the operator, which is the party the evidence is about.
- Does any existing regime already carry a representation-error duty under another name — regulatory model validation, safety-case revalidation, clinical-guideline review? Not checked.
