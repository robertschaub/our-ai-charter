> **Status: WORKING NOTES** — draft article for publication (LinkedIn, then mirror to `Published/` once live). Engages the runtime-governance argument with one representative public source named. Public-safe; source-checked through 2026-07-22.

# Everyone's Asking *When* AI Governance Should Happen. The Real Question Is *Who Gets to Check?*

*A security briefing redlined by 250 CISOs says the window between a flaw's disclosure and its exploitation has collapsed from years to hours. "Govern at runtime" is part of the answer. But a technical gate is not the same thing as public accountability.*

A striking security paper has been making the rounds since spring, and it earns the attention. *[The AI Vulnerability Storm](https://cloudsecurityalliance.org/artifacts/the-ai-vulnerability-storm-building-a-mythos-ready-security-program)* — a strategy briefing from SANS, the Cloud Security Alliance, the OWASP GenAI Security Project, and [un]prompted, reviewed by more than 250 CISOs — reports, citing the Zero Day Clock, that time to exploitation has fallen below a day in 2026. The tracker's own [reproducibility table](https://zerodayclock.com/audit) is more precise: among CVEs with confirmed in-the-wild exploitation, the median fell from 771 days in its 2018 cohort (273 cases) to 0.0 days in its still-small 2026 cohort (44 cases at the May audit).

Sit with that. What that collapse breaks is specific: the idea that a deployment can remain safe on the strength of an earlier assessment while ordinary patch cycles catch up. That is one more reason "certify once, deploy forever" fails. On that much, the alarm is earned.

The briefing itself cautions that faster exploitation has not yet meant proportionally worse damage — recent headline incidents still ran on credential abuse, social engineering, and supply chains. The tracker also covers only CVEs with confirmed exploitation, and the small recent cohort has had far less time to reveal a slow exploit. This is a leading indicator, not a loss report: read the endpoint as provisional and the direction as the warning.

That's one pressure: speed. A second, different in kind, is composition — and here one response is to govern at *runtime*, checking each action as the system composes it, on the argument that an agentic system assembles its behaviour on the fly and can exceed what you described in advance.

That argument has a true core. A static, one-time certificate genuinely cannot bound a system that recombines its own capabilities at run time. A pre-declared description was never going to be a defence on its own.

One detailed recent formulation is Stuart-Mueller & Woodward's *The Wrong Layer* (July 2026, [DOI: 10.5281/zenodo.21397661](https://doi.org/10.5281/zenodo.21397661)). The authors conclude from their framework survey that none requires a record proving a particular machine action was authorized, admissible, and bounded when it occurred. They also explicitly call for independent custody, separation of powers, appeal, and contestability. So the question here is not whether serious runtime proposals can name *who* should hold and check the record. It is whether those principles become institutions that independently assess the evidence and hear challenges from the people affected.

The paper is right that certifying a system as a class does not prove that each later action was admissible. But runtime *versus* assurance is still a false choice. For high-risk systems, the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) pairs pre-market conformity assessment with post-market monitoring and serious-incident reporting. [NIST's AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) makes risk management continuous and iterative across the lifecycle, including testing in operation, independent assessors where appropriate, and appeal processes for affected communities. Runtime monitoring — and enforcement where the risk warrants it — belongs inside that lifecycle. The per-action record supplies a missing evidence object; it does not replace independent assessment, incident reporting, or redress.

Which leads to the deeper point. **A gate is only as trustworthy as whoever holds it.**

A technical gate can answer a substantial question: *may this action proceed under the configured policy?* With a sound record behind it, the gate can later show what authority and evidence it applied. That is more than raw capability. But no gate can establish its own public legitimacy. Who sets the policy, who assesses the quality of the evidence, and who hears a challenge are institutional judgments, not cryptographic ones.

Where the same operator composes the action, sets the policy, and controls the evidence, it is still marking its own homework faster. Split custody and external integrity witnesses reduce that risk. Independent review of the decision and a real path to challenge it complete the loop.

The public-interest version asks for three things a runtime gate alone cannot provide:

- **Evidence others can actually inspect** — not merely a tamper-evident log, but a record whose relevance and sufficiency an independent party can assess: what the system claimed, the sources it used and where it used them, its uncertainty, its known limits, and — honestly — what was not recorded and why.
- **Decisions the affected can contest** — notice, review, challenge, and remedy for the people a system acts on, adjudicated by someone sitting outside any single operator.
- **Duties that don't evaporate at deployment** — a named human institution that answers for the system's claims, harms, and consequential decisions across its whole life, not just at launch.

None of that requires a new central authority. It requires the oldest trick in trustworthy institutions: separate the roles so no one certifies their own work. A standard-setter writes the test; independent certification bodies do the checking; an accreditation body formally recognizes the checkers' competence. [ISO certification](https://www.iso.org/certification.html) already runs on this split — ISO writes standards and certifies no one; external certification bodies assess, and accreditation can independently confirm their competence. [Fairtrade](https://www.flocert.net/flocert-history-with-fairtrade/) separates Fairtrade International's standard-setting from FLOCERT's inspections and certification. Journalism's [Journalism Trust Initiative](https://rsf.org/en/journalism-trust-initiative) likewise offers certification through external, independent auditors. Build the test, borrow the machinery.

And none of this means slowing every action to a crawl. Routine, rules-based checks can run in-band; ambiguous, out-of-bounds, or irreversible actions should escalate. The durable record then supports independent review and, when needed, adjudication. Check now, preserve the record, and make challenge possible. A collapsing exploit window is a reason to preserve better evidence and distribute trust, not to keep the only copy of the check inside the house.

One honest limit, because it cuts against my side too. No certificate can guarantee that every future AI output will be *true*. But we can evaluate whether a system *shows its work*: whether it grounds its material claims, signals its doubt, and corrects itself. Honesty-of-process is testable even when the truth of every answer is not. And the same discipline should bind the humans and institutions deploying these systems, not only the models — evidence before reliance, for people as much as for machines.

So by all means move governance closer to the moment of action. But *when* is the easy half. The hard half is *who*: moving the check out of the sole hands of whoever runs the system — into evidence independent parties can assess and decisions the affected can challenge.

This is a working draft from a small, unfunded effort — intent, not influence — model-plural and meant to dock onto the open-model work already happening, not to replace it. I'd genuinely like it torn into: where does it break? What's missing?

When AI is the thing we all think with, *who gets to check it* isn't a technical footnote. It's the whole question.

**Built by many. Accountable to all.**

`#AI #TrustworthyAI #AIGovernance #PublicAI #AgenticAI`

*Working draft. Source and work in progress: [robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter).*
