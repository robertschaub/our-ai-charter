# Governance from the AI user's workflow

*Runtime reference model. Where the [control-and-evidence layer](../../wip/public-compute-control-evidence-layer.md) asks what an operator must prove, this asks what a person using AI must decide, trace, and escalate.*

## Core rule

**Trace wide, escalate narrow.** Keep a reviewable record of the workflow, but interrupt the user only when a human decision can materially change the outcome. Escalating everything trains people to click "allow all"; good tracing is what earns the right to escalate less.

> **Escalate only when all three hold:** a human can change the outcome, the stakes justify interruption, and the AI cannot responsibly resolve it alone. Otherwise: trace and proceed.

## Five steps

| Step | User question | Governs |
|---|---|---|
| **1. Frame** | Is AI the right tool, and what is at stake? | purpose, authority, risk tier |
| **2. Footing** | Who stands behind it, what sources does it use, and is input safe? | provider, sources, privacy, IP/confidentiality |
| **3. Read** | What is it claiming, and can I see the work? | evidence, source validity, uncertainty |
| **4. Act** | Should this output affect a decision or external action? | consequence, fairness, notice, human sign-off |
| **5. After** | How is it challenged, corrected, and learned from? | complaint, remedy, correction, reliance |

## Conditions across every step

- **Allowed, able, accountable:** the user is authorised to use the tool, competent to oversee it, and responsible for what they ship.
- **Safety, privacy, resilience:** misuse resistance, data protection, and fallback/exit where reliance is material.
- **Fairness:** for consequential uses, ask whether the output may be systematically worse for some affected group.
- **Traceability:** record what was asked, used, claimed, decided, challenged, and fixed.

## Gates and fail actions

| Gate | Pass condition | If it fails |
|---|---|---|
| **Authorize** | tool sanctioned; user permitted and competent | use approved tool, get trained, or get sign-off |
| **Submit** | privacy/IP/confidentiality basis is clear | redact, anonymise, or do not submit |
| **Verify** | sources resolve, evidence checked, uncertainty carried forward | keep verifying; do not convert doubt into certainty |
| **Commit** | evidence and fairness considered; accountable human signs off where needed | hold, seek independent review, or reject |
| **Rely** | challenge/remedy route works and remains current | switch, add fallback, or withdraw reliance |

Loops and chains re-enter **Verify**: each model/tool hop can add unverified claims, injected content, or drift. For autonomous or high-frequency actions, **Commit** moves up a level: a human authorises a bounded operating envelope with limits, monitoring, rollback, and kill-switch.

## Escalation triggers

Every trigger is traced. It interrupts only when material in context: **Silent** (log), **Flag** (surface non-blocking), or **Stop** (block for decision).

Calibration runs on two axes. The **use case and stakes** set where Stop kicks in: irreversible, external, regulated, or person-affecting → Stop readily; internal, reversible, or draft → mostly Silent trace. The **user** — competence, role, standing preferences — sets the manner and frequency: an expert with standing preferences → fewer, decision-only asks; a novice in a high-stakes domain → escalate more, and explain.

**What the AI knows**
- Low confidence or genuine uncertainty — **Flag → Stop** if consequential.
- Conflicting evidence — **Flag → Stop**; surface the disagreement.
- Missing load-bearing input or assumed intent — trace; **Flag** if important.
- Beyond declared scope or would need fabrication — **Stop**.

**What is at stake**
- Risk to people, rights, safety, or security — **Stop**.
- Material opportunity or clearly better option — **Flag**.
- Irreversible action — send, publish, delete, pay, deploy, sign — **Stop**.
- Threshold crossing — spend, scope, people affected, quota — **Stop** at threshold.
- Consequential decision about an identifiable person — **Stop**.

**Authority and boundaries**
- Scope creep, legal/policy/rights boundary, new privilege/tool/data, external action on the user's behalf, or money/resource commitment above threshold — **Stop**.

**Data, privacy, and rights**
- Sensitive/personal/third-party data leaving a boundary — **Stop**.
- Input/output IP or confidentiality uncertainty — **Flag → Stop**.
- External disclosure across a trust boundary — **Stop**.

**Conflict and integrity**
- Value tradeoff, stakeholder conflict, prompt injection, manipulation, or harmful false premise — **Flag → Stop**.

**Lifecycle**
- Material dependency/source/version change — **Flag → Stop**.
- Repeated failure — **Flag**.
- Earlier error discovered — **Flag → Stop**; correct and surface.

## Preventing "allow all"

1. **Escalate decisions, not mechanics.** Ask one framed question with options, tradeoff, recommendation, and default.
2. **Scope every grant.** Permission is for this action and resource, not everything forever.
3. **Use safe defaults on silence.** Timeout selects the reversible option; silence never authorises irreversible action.
4. **Watch escalation rate.** If the system asks too often, re-scope the task or tool.

## What this is

A design synthesis, not a certifiable checklist. It maps provider-side Charter duties — notice, review, remedy, evidence, correction — onto the user's seat. Collective or diffuse harms need representative, regulator, or system-level review outside this single-user loop.
