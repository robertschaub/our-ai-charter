> **Status: WORKING NOTES** — prototype (2026-06-28). Third worked obligation→duty bridge, testing the instrument in [charter-structure-and-views.md](../Assurance/Concepts/charter-structure-and-views.md) on the **technical-assurance** obligation. Pointer-level; routes to the [Charter Commitments](../Assurance/Framework/charter-commitments.md)' duties, inventing no new controls.

# Assurance case — *Safe, secure, private, and resilient* (obligation 3)

*A Claims → Arguments → Evidence view; status **derived** from duty/module findings, never scored on its own. A view over the duties, not a new control layer.*

## Claim

The system **protects people, data, infrastructure, and the continuity others rely on** — against misuse, attack, privacy loss, and failure — to the assurance depth stated below.

## Scope & trigger

Every system; depth rises sharply with exposure — user-facing, tool/agent-enabled, processing personal or sensitive data, or carrying public-interest reliance. This obligation **bundles four distinct properties** (safe · secure · private · resilient) with different controls and evidence.

## Argument & evidence — the crosswalk

| Duty (argument) | What it must show | Evidence / module | Min. depth (high tier) |
|---|---|---|---|
| **D5 — safety, security, privacy, data governance** *(primary)* | hazard analysis; cyber + LLM threat model; prompt-injection & output-handling tests; tool/agent permission bounds; data minimisation, lawful basis, retention, access/deletion; provenance | app-security / prompt-injection module · privacy/provenance module | **effectiveness-tested** |
| **D4 — control, dependencies, continuity, exit** *(resilience)* | critical-dependency map; fallback limits; continuity + exit plans where reliance is material | continuity / exit records | implementation-checked |
| **D3 — risk register** | safety/security/privacy hazards registered, tiered, monitored; residual risk | risk register | evidence-observed |
| **D8 — incidents, withdrawal** | security/privacy/misuse incident response; rollback/withdrawal | incident records | implementation-checked |

## Remedy & escalation (derived)

System-level: patch → rollback → withdraw. Breach: **notify affected people + regulator**. Resilience failure: invoke fallback/continuity. Individual privacy redress (access/deletion) sits in D5; affected-person harm routes through *[Answerable](answerable-to-people-assurance-case.md)*.

## Failure / withdrawal triggers

Unmitigated critical vulnerability; sensitive-data leakage; a prompt-injection or tool-permission failure; no continuity plan where reliance is material; a hidden incident. → withdraw.

## Derived status & claim discipline

Weakest primary row (D5, D4). *Allowed*: "security and prompt-injection controls were effectiveness-tested for this release." *Not allowed*: "the system is secure / cannot be breached" — you test and monitor, you do not guarantee. *Not-assessed* rows shown.

## What this does not prove

Not invulnerability or zero-incident operation — only that the named controls were tested to the stated depth.

## What this prototype tested (finding)

**A single obligation can bundle several distinct properties.** Safe / secure / private / resilient carry different controls, evidence, and even different duties (D5 vs D4). The crosswalk absorbed this as per-concern rows — but the annex may want to render obligation 3 as **sub-cards**, since "one obligation" here maps to multiple module clusters. It is also the **most effectiveness-test-heavy** obligation, which is why both cross-model reviewers called it "the easy one": it leans hardest on existing security/privacy standards and lightest on novel Charter machinery.
