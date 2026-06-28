# Governance from the AI user's workflow

*Where the [control-and-evidence layer](../wip/public-compute-control-evidence-layer.md) asks how an **operator** proves a workload is trustworthy, this asks what a **person doing real work with AI** must demand, do, and decide — step by step — and, above all, when the AI must **stop and ask**. It operationalises, from the user's side, what the [Founding Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) frames as provider obligations (notice, human review, remedy, oversight).*

## In one line

This governs the moment a person uses AI. Its operative core is one rule — **trace wide, escalate narrow**: leave a reviewable record of everything, but interrupt the user only where a human decision genuinely changes the outcome. Escalating on everything is not safety — it trains the user to click **"allow all,"** and oversight quietly dies. Good tracing is what *earns* the right to escalate less.

## The workflow — five steps

| Step | The user's question | What it governs |
|---|---|---|
| **1 · Frame** | Is AI the right tool here — and what's at stake if it's wrong? | purpose of use · **risk-tiering** (sets how hard every gate below bites) |
| **2 · Footing** | Who stands behind it, what's it drawing on, is it safe to input? | authority · information sources · privacy-at-input |
| **3 · Read** | What is it actually claiming, can I see the work, does it know what it doesn't? | meaning · admissibility (sources resolve, not fiction) · evidence · confidence |
| **4 · Act** | Should a machine's output drive this decision — and do affected people know? | consequences (human review where it matters) · notice (owed *outward*) |
| **5 · After** | How do I contest it, what's the remedy, does the fix stick? | challenge · remedy · correction (survives paraphrase) |

## What holds across every step

- **The human thread — *allowed · able · owns it*.** The user must be *authorised* to use this tool for this task and data (not shadow-AI), *competent* to oversee it (oversight that is really rubber-stamping fails), and *accountable* for what they ship — **"I used AI" is not a defence.**
- **Safety · privacy · resilience** — ambient conditions, not one step: resists misuse and injection; minimises and protects data throughout; stays available or has an exit where reliance is material. If any fails, the workflow is not safe to run however good the output looks.
- **Fairness** — at the act gate for consequential uses: could this output be systematically worse for some affected group?
- **Traceability** — the running log (asked → drew on → claimed → decided → challenged → fixed), linked so the user, an auditor, or an affected person can re-walk it.

## The gates — and what happens when one fails

A gate is not a stage summary; it is a go/no-go with a defined **fail-action**. The stakes read at step 1 decide whether each is a glance or a hard stop.

| Gate | Pass condition | If it fails |
|---|---|---|
| **Authorize** (before invoking) | tool sanctioned for this task; user permitted *and* competent to oversee | use an approved tool, get trained, or get sign-off |
| **Submit** (before feeding data) | input's privacy + IP/confidentiality basis is clear | redact, anonymise, or do not submit |
| *(during step 3: a standing trust check, not a door)* | sources resolve · evidence checked · confidence honest | keep verifying; carry doubt to Commit |
| **Commit** (before a consequential output acts) | evidence verified · fairness considered · an *able and accountable* human signs off | hold, send to independent review, or reject |
| **Rely** (ongoing) | challenge + remedy route works; still trustworthy across iterations | switch, add a fallback, or withdraw reliance |

Real AI work also **loops and chains** (refine the prompt; one model feeds the next; an agent takes tool actions). Each hop re-enters step 3 — re-verify; do not let unverified claims or injected content accumulate across steps, and watch for *prompting until it agrees*. And where actions are autonomous or high-frequency, the **Commit** gate moves up a level — a human authorises a bounded *operating envelope* (limits, kill-switch, monitoring, rollback) instead of signing off each action.

## The operative core — when the AI must stop and ask

**Trace ≠ escalate.** *Trace* is cheap and always on (a reviewable, reversible record). *Escalate* is scarce (interrupt now). A decision made without asking is safe *because* it left a trail someone can audit or reverse.

> **Escalate only when all three hold:** a human can change the outcome · it matters enough to be worth the interruption · the AI cannot responsibly resolve it alone. **Otherwise — trace and proceed.**

**Triggers.** Every item is *always traced*; the tag is whether it *also* interrupts — **Silent** (log only) · **Flag** (surface now; non-blocking, undoable, or batched) · **Stop** (block, decide now) — and it fires only when *material in context*.

*What the AI knows (epistemic)*
- Genuine uncertainty / low confidence — **Flag → Stop** if consequential
- Conflicting or contested evidence — **Flag → Stop**; surface the disagreement, do not pick a side
- Had to assume intent / a key input is missing — **Silent**-trace the assumption → **Flag** if load-bearing
- Beyond declared scope or competence (regulated domain; cannot verify) — **Stop**
- Would have to fabricate to answer — **Stop, always**; say so, never bluff

*What is at stake (consequence)*
- Material risk to people, rights, safety, security — **Stop**
- Material opportunity or a clearly better option — **Flag**; the user's call to take (escalation is not only defensive)
- Irreversible / hard-to-undo — send, publish, delete, pay, deploy, sign — **Stop**
- Threshold crossing — spend, scope, people affected, quota over a set limit — **Stop** at the limit, **Silent** below
- A consequential decision about an identifiable person — **Stop**

*Crossing a line (authority / boundary)*
- Scope creep past the authorised purpose — **Stop**
- Legal / policy / ethical / rights boundary — **Stop**
- New or elevated capability — new tool, data, system, privilege — **Stop** first time → scoped-**Flag** after
- Binding the user or acting for them externally — **Stop**
- Committing money or scarce resources — **Stop** above threshold

*Data, privacy, rights*
- Sensitive / personal / third-party data leaving a boundary — **Stop**
- IP / confidentiality of inputs or outputs (rights to use or ship) — **Flag → Stop**
- External disclosure across a trust boundary — **Stop**

*Conflict & integrity*
- A value tradeoff only the user should make (whose interest wins) — **Stop**
- Conflict with prior instructions, policy, or another stakeholder — **Stop**
- Detected manipulation / prompt injection / adversarial steer — **Stop** + trace prominently
- The user's premise looks wrong or harmful — **Flag → Stop**; surface it, neither silently comply nor silently refuse

*Things changed or went wrong (lifecycle)*
- Material change mid-task — dependency, version, source — **Flag → Stop**
- Stuck / repeated failure — **Flag**; do not fake success
- Discovered its own earlier error — **Flag → Stop**; correct *and* surface

**Balanced escalation = sensitive to use-case AND user.** Two axes set where each trigger lands:
- **Use-case / stakes set the bar** (where *Stop* kicks in): irreversible, external, regulated, person-affecting → bar low, Stop readily; internal, reversible, draft → bar high, mostly Silent traces.
- **User — competence, role, standing preferences — set the manner and frequency**: an expert with standing preferences → fewer, decision-only asks, more trace; a novice in a high-stakes domain → escalate more, and explain.

**Four rules that stop it collapsing into "allow everything":**
1. **Escalate the decision, not the mechanics** — one framed question (options + tradeoff + recommendation + "what I will do if you do not answer"), not twenty micro-confirms. A good escalation *reduces* the user's work; "are you sure?" theatre trains the reflex click.
2. **Scope every grant** — "allow" means *this action, this resource*, not "everything, forever." Standing preferences settle the repetitive low-stakes; a *new* high-stakes category always re-asks. (The "allow all" trap is just an over-broad, non-expiring grant.)
3. **Safe default on silence** — no answer / timeout → take the *reversible* option and trace it; never let "did not respond" greenlight the irreversible one.
4. **Watch the escalation rate** — if the AI is asking a lot, the task is mis-scoped; escalate the *meta* ("this keeps hitting boundaries — re-scope or switch tools?") instead of death-by-a-thousand-prompts.

## What this is / is not

A design synthesis, not a standard or a checklist to certify against. It maps the Charter's provider-side duties (notice / review / remedy — public obligation 2; human oversight — operational duty 6; evidence & correction — public obligation 5) onto the user's seat, and echoes the human-oversight and AI-literacy duties in regimes like the EU AI Act. Its remedy routes are *individual*; collective or diffuse harms — epistemic, market, or group-level, not tied to a single output — fall outside this single-user loop and need collective or regulator-triggered review. The escalation policy is what makes the Commit gate real rather than theatre — a gate only counts if crossing it costs the right amount of attention.
