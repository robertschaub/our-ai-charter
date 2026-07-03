> **Status: WORKING NOTES** — draft article for publication (LinkedIn, then mirror to `Published/` once live). Engages the runtime-governance argument at the level of the idea, not any named author. Public-safe.

# Everyone's Asking *When* AI Governance Should Happen. The Real Question Is *Who Gets to Check.*

*A 250-CISO paper says the window to catch AI failures has collapsed from years to hours. The popular fix — "govern at runtime" — is half right, and it stops exactly where the hard part begins.*

A striking security paper is making the rounds, and it earns the attention. *[The AI Vulnerability Storm](https://cloudsecurityalliance.org/artifacts/the-ai-vulnerability-storm)* — a strategy briefing from SANS, the Cloud Security Alliance, OWASP's GenAI Security Project and [un]prompted, reviewed by more than 250 CISOs — reports, citing Zero Day Clock, that the mean time from a vulnerability being disclosed to confirmed exploitation has fallen from about 2.3 years in 2019 to less than a day in 2026.

Sit with that. The assumption under most of our governance — that we can describe a system's behaviour up front, certify the description, and patch faster than anyone can abuse the gap — no longer holds. "Certify once, deploy forever" is dead. On that, the alarm is earned.

So a fix is gaining traction: stop governing *before* deployment and govern at *runtime* — check each action as the system composes it, because an agentic system assembles its behaviour on the fly and will always exceed whatever you described in advance.

That argument has a true core. A static, one-time certificate genuinely cannot bound a system that recombines its own capabilities at run time. A pre-declared description was never going to be a defence on its own.

But it smuggles in a false choice — runtime *versus* certification — and then stops one question short of the one that matters.

Take the false choice first. Certification done properly was never a single gate. For high-risk systems, the EU AI Act pairs up-front conformity assessment with post-market monitoring and serious-incident reporting. NIST's AI Risk Management Framework is built as a continuous, iterative practice — governance running through the mapping, measuring, and managing of risk — not a one-time stamp. Runtime enforcement isn't the *alternative* to assurance; it's a phase mature assurance already requires. Framing it as a replacement quietly discards the parts — recorded evidence, independent audit, redress — that make a runtime check worth anything.

Which leads to the deeper point. **A gate is only as trustworthy as whoever holds it.**

Here's the distinction I keep coming back to. Every runtime, scheduler and gateway we have is very good at one question: *can this run — fast, at scale?* That's **capability**. None of them answers, in a public, portable, contestable way, a different question: *may it run — for whom, for what purpose, accountably, and can the people it affects contest it?* That's **legitimacy**. The runtime-governance debate is a sophisticated argument about *when* and *whether* a system *can* act. It barely touches whether it *may* — and who gets to check.

And "govern at runtime" gives a comfortable answer to the wrong question, because in many deployed versions of it the party that *composes* the action also *owns the gate that checks it* — and even where the gate is a separate service, it is rarely one the affected public can inspect or contest. That isn't *accountable* governance; at best it's the operator marking its own homework, faster. A checkpoint the public can't see or challenge concentrates exactly the power we should be worried about — a captured checkpoint is a captured market.

The public-interest version asks for three things a runtime gate alone cannot provide:

- **Evidence others can actually inspect** — checkable at the point of deployment, not merely asserted in a policy page: what the system claimed, the sources where it used them, its uncertainty, its known limits, and — honestly — what wasn't recorded and why.
- **Decisions the affected can contest** — notice, review, challenge, and remedy for the people a system acts on, adjudicated by someone sitting outside any single operator. No secret kill-switches, in either direction.
- **Duties that don't evaporate at deployment** — a named human institution that answers for the system's claims, harms, and consequential decisions across its whole life, not just at launch.

None of that requires a new central authority — nobody should hold that power. It requires the oldest trick in trustworthy institutions: separate the roles so no one certifies their own work. Someone writes the test; independent assessors check against it; an accreditor licenses and polices the assessors. It's how ISO marks, Fairtrade, and journalism's own trust badges already work. Build the test, borrow the machinery.

And none of this means slowing the system to a crawl. The in-band check and the durable record are different things: the gate can fire in milliseconds, while the evidence it leaves is reviewed — and, when contested, adjudicated — afterward, by someone outside the operator. Record now, contest later. A collapsing exploit window is a reason to log more and check independently, not a reason to keep the only copy of the check inside the house.

One honest limit, because it cuts my way too. We cannot certify that an AI's output is *true* — truth isn't certifiable. But we can evaluate whether a system *shows its work*: whether it grounds its material claims, signals its doubt, and corrects itself. Honesty-of-process is testable even when truth is not. And the same discipline should bind the humans and institutions deploying these systems, not only the models — evidence before reliance, for people as much as for machines.

So by all means move governance closer to the moment of action. But moving it *earlier in time* is the easy half. The hard half is moving it *out of the sole hands of whoever runs the system* — into evidence the public can weigh and decisions they can challenge.

This is a working draft from a small, founder-led, unfunded effort — intent, not influence. It's model-plural by design, meant to dock onto the open-AI work already happening rather than replace it, and I'd genuinely like it torn into. Where does it break? What's missing?

When AI is the thing we all think with, *who gets to check it* isn't a technical footnote. It's the whole question.

**Built by many. Accountable to all.**

`#AI #TrustworthyAI #AIGovernance #PublicAI #AgenticAI`

*Working draft. Source and work in progress: [robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter).*
