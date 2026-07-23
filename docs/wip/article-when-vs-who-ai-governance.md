> **Status: WORKING NOTES** — draft article for publication (LinkedIn, then mirror to `Published/` once live). Engages the runtime-governance argument with one representative public source named. Public-safe; source-checked through 2026-07-22.

# Runtime AI Governance Gets *When* Right. The Harder Question Is *Who Gets to Check?*

*A [security briefing reviewed by more than 250 CISOs](https://www.sans.org/press/announcements/emergency-strategy-briefing-ai-driven-vulnerability-discovery-compresses-exploit-timelines) warns that AI-assisted vulnerability discovery is compressing exploit timelines. "Govern at runtime" is part of the answer. But a technical gate is not the same thing as public accountability.*

*[The AI Vulnerability Storm](https://cloudsecurityalliance.org/artifacts/the-ai-vulnerability-storm)* — a strategy briefing from SANS, the Cloud Security Alliance, the OWASP GenAI Security Project, and [un]prompted — warns that the window between vulnerability discovery and weaponization is collapsing from weeks to hours. The underlying Zero Day Clock [measures a narrower interval](https://zerodayclock.com/audit): among CVEs with confirmed in-the-wild exploitation, the median time from NVD publication to a confirmed exploit signal fell from 771 days across 273 cases in the 2018 cohort to 0.0 days — same-day or earlier under the tracker's definition — across 44 cases in its still-small 2026 cohort at the May audit.

For AI assurance, the implication is narrow but important: an earlier assessment cannot establish that a live deployment remains safe while vulnerabilities and attacks change faster than ordinary patch cycles. It is one more reason "assess once, deploy forever" fails.

But the briefing also cautions that faster exploitation has not yet meant proportionally worse damage; many consequential incidents still relied on credential abuse, social engineering, or supply-chain compromise. The tracker covers only CVEs with confirmed exploitation, and the small 2026 cohort has had little time to reveal a slow exploit. This is a leading indicator, not a loss report: the endpoint is provisional; the direction is the warning.

Speed is one pressure. Composition is another. One response is runtime governance: check each consequential action as an agent composes it, because the resulting behaviour can exceed what was described in advance.

That argument has a true core. A one-time assessment cannot establish that every later, dynamically composed action will be admissible. A pre-declared description cannot be the whole defence.

Stuart-Mueller & Woodward's preprint *The Wrong Layer* (July 2026, [DOI: 10.5281/zenodo.21397661](https://doi.org/10.5281/zenodo.21397661)) makes a detailed version of that case. After surveying current frameworks, the authors argue that none requires a record proving a particular machine action was authorized, admissible, and bounded when it occurred. The paper does not ignore *who*: it calls for structurally independent custody, separation of powers, appeal, and contestability. The unresolved question is how those principles become institutions that independently assess the evidence and hear challenges from affected people.

The paper is right that assessing a system as a class does not prove that each later action was admissible. But runtime *versus* assurance is still a false choice. For high-risk systems, the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng) pairs pre-market conformity assessment with post-market monitoring and serious-incident reporting. [NIST's AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) makes risk management continuous across the lifecycle, including post-deployment monitoring, independent assessment where appropriate, and appeal mechanisms for end users and affected communities. A per-action record adds missing evidence; it does not replace lifecycle assurance, incident reporting, or redress.

Which leads to the deeper point. **A gate is only as trustworthy as the institutions around it.**

A technical gate can answer a substantial question: *may this action proceed under the configured policy?* With a sound record behind it, the gate can later show what authority and evidence it applied. That is more than raw capability. But no gate can establish its own public legitimacy. Who sets the policy, who assesses the quality of the evidence, and who hears a challenge are institutional judgments, not cryptographic ones.

Where the same operator composes the action, sets the policy, and controls the evidence, it is still marking its own homework faster. Independent custody, outside review, and a real path to challenge the decision complete the loop.

The public-interest version asks for three things a runtime gate alone cannot provide:

- **Evidence others can actually inspect** — not merely a tamper-evident log, but a record whose relevance and sufficiency an independent party can assess: what the system claimed, the sources it used and where it used them, its uncertainty, its known limits, and — honestly — what was not recorded and why.
- **Decisions the affected can contest** — notice, review, challenge, and remedy for the people a system acts on, adjudicated by someone sitting outside any single operator.
- **Duties that don't evaporate at deployment** — a named human institution that answers for the system's claims, harms, and consequential decisions across its whole life, not just at launch.

None of that requires a new central authority. It requires role separation so no one certifies their own work. [ISO](https://www.iso.org/certification.html) writes standards, external certification bodies do the checking, and accreditation can independently confirm their competence. Journalism's [Journalism Trust Initiative](https://rsf.org/en/journalism-trust-initiative) similarly offers optional certification through external, independent auditors. Build the test, borrow the machinery.

And none of this means slowing every action to a crawl. Routine, rules-based checks can run in-band; ambiguous, out-of-bounds, or irreversible actions should escalate. The durable record then supports independent review and, when needed, adjudication. Check now, preserve the record, and make challenge possible. A collapsing exploit window is a reason to automate controls and preserve better evidence, not to collapse control, custody, and review into one operator.

One honest limit, because it cuts against my side too. No certificate can guarantee that every future AI output will be *true*. But we can evaluate whether a system *shows its work*: whether it grounds its material claims, signals its doubt, and corrects itself. Honesty-of-process is testable even when the truth of every answer is not. And the same discipline should bind the humans and institutions deploying these systems, not only the models — evidence before reliance, from people as much as from machines.

So move governance closer to the moment of action. But *when* is only half the question. The harder half is *who*: move the check out of the sole hands of whoever runs the system — into evidence independent parties can assess and decisions affected people can challenge.

This is a working proposal from a small, unfunded, model-plural effort, intended to contribute to open-model and public-interest work already under way. Where does it break? What's missing?

**Built by many. Accountable to all.**

`#AI #TrustworthyAI #AIGovernance #PublicAI #AgenticAI`

*Working draft. Source and work in progress: [robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter).*
