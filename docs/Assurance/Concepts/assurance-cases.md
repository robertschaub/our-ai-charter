# Assurance cases — the five obligations as obligation→duty bridges

*Prototype crosswalks (2026-06-28), consolidated from five separate `wip/` notes. They validate the instrument in [charter-structure-and-views.md](charter-structure-and-views.md); per that note they should **graduate into a certification-model annex** once an obligation is piloted — this is working design, not settled normative text. Each routes to the [Charter Commitments](../Framework/charter-commitments.md)' eight duties and modules, inventing no new controls.*

Each obligation is a **Claims → Arguments → Evidence** view: the public **claim**, the **duties** that argue it, the **module/evidence** that proves it, and the remedy owed — with the obligation's status **derived** from those duty/module findings, never scored on its own. A **view over the duties**, not a new control layer. "Min. depth" is the minimum assurance depth for a **high-stakes** tier; lower tiers relax it.

## Obligation 1 — Purpose-bound

**Claim:** the system declares what it is for, what it must not be used for, who it may affect, and what is risky — and is used only within that declared, legitimate purpose. Triggered at the **authorize gate** (and on material scope change).

**Hard legitimacy gate (pass/fail, not graded):** before the crosswalk, the purpose must clear a binary gate — lawful basis; not a prohibited use; necessity and proportionality; affected groups identified; limits/residual risk stated. **Failing the gate bars the claim outright** — no depth elsewhere compensates. This is the structural difference from the rights-led case (obligation 2), whose rows degrade gracefully with assurance depth.

| Duty (argument) | Shows | Evidence / module | Min. depth |
|---|---|---|---|
| **D2 — purpose, scope, misuse** *(primary)* | intended + prohibited uses, foreseeable misuse, affected groups, limits, impact assessment | purpose/scope declaration + impact assessment | implementation-checked |
| **D1 — accountable ownership** | a named owner who stands behind the purpose; no capability overclaim | AI policy + responsibility map | implementation-checked |
| **D3 — risk, legal-scope map** | risk tier; markets/jurisdictions/intended-prohibited uses | legal-scope map + risk register | evidence-observed |
| **D4 — control** *(supporting)* | function-creep control; who may change purpose | change-control records | evidence-observed |
| **D7 — transparency** *(supporting)* | purpose publicly stated; capability not oversold | public purpose statement | evidence-observed |
| **D8 — re-authorization, withdrawal** *(supporting)* | purpose shift → re-authorize; beyond-purpose use → withdraw | material-change + withdrawal records | implementation-checked |

Remedy is mostly **narrowing or withdrawal**; individual harm from an out-of-purpose use routes to obligation 2. Duty-heavy — the module column is nearly empty.

## Obligation 2 — Answerable to people

**Claim:** a **named human institution answers** for the system, and people affected by consequential uses get **notice, meaningful review, a route to challenge, and remedy** — to the stated depth. Triggered on the **consequential-event lifecycle** (eligibility, ranking, screening, allocation, content removal, or a recommendation that drives such an outcome).

| Duty (argument) | Shows | Evidence / module | Min. depth |
|---|---|---|---|
| **D1 — accountable ownership** | a named institution that answers — never "the algorithm" | responsibility map | implementation-checked |
| **D6 — oversight, remedy** *(primary)* | human review/override; a reachable challenge route; remedy records | contestability module | **effectiveness-tested** |
| **D7 — transparency** | notice that AI is materially involved; an understandable explanation | notice + explanation artefacts | evidence-observed |
| **D8 — incidents, withdrawal** | incidents/appeals logged; escalation + withdrawal that work | incident + appeal records | implementation-checked |
| **D4 — control** *(supporting)* | who can restrict/recall/shut down — no hidden powers | restriction-transparency module | evidence-observed |

**Remedy splits individual vs collective:** individual — correct → reconsider under human review → reverse/compensate, with a published response time; **collective/systemic** — repeated failures, disparate error rates, or group-level harm trigger regulator- or representative-review (a person cannot appeal a *pattern*).

## Obligation 3 — Safe, secure, private, and resilient

**Claim:** the system protects people, data, infrastructure, and the continuity others rely on — against misuse, attack, privacy loss, and failure — to the stated depth. Bundles **four distinct properties** with different controls and evidence.

| Duty (argument) | Shows | Evidence / module | Min. depth |
|---|---|---|---|
| **D5 — safety, security, privacy** *(primary)* | hazard analysis; cyber + LLM threat model; prompt-injection & output-handling tests; tool/agent permission bounds; data minimisation, lawful basis, retention | app-security / prompt-injection · privacy/provenance | **effectiveness-tested** |
| **D4 — continuity, exit** *(resilience)* | critical-dependency map; fallback limits; continuity + exit plans | continuity / exit records | implementation-checked |
| **D3 — risk register** | safety/security/privacy hazards tiered + monitored | risk register | evidence-observed |
| **D8 — incidents, withdrawal** | incident response; rollback/withdrawal | incident records | implementation-checked |

Remedy: patch → rollback → withdraw; a breach → **notify affected people + regulator**. The most effectiveness-test-heavy obligation — it leans hardest on existing security/privacy standards and lightest on novel Charter machinery.

## Obligation 4 — Fair in practice

**Claim:** where the system may materially affect people, its performance is **tested and monitored for uneven or discriminatory outcomes** across groups, languages, regions, and contexts — and disparities are disclosed, mitigated, constrained, or withdrawn. **Conditional** (fires only where material impact is plausible) and inherently **collective** (assessed on aggregates, not a single output).

| Duty (argument) | Shows | Evidence / module | Min. depth |
|---|---|---|---|
| **D6 — fairness, inclusion** *(primary)* | affected-group identification; disparate failure/refusal/error testing across groups, languages, regions, accessibility; mitigation | fairness module | **effectiveness-tested** |
| **D3 — risk register** | disparate-impact risk registered + tiered | risk register | evidence-observed |
| **D7 — transparency** | known disparities + limits disclosed | public limitations statement | evidence-observed |
| **D8 — monitoring, drift** | ongoing disparity + drift monitoring | monitoring records | implementation-checked |

Remedy is **systemic** — mitigate / re-train / constrain / withdraw the affected scope, and disclose. Individual instances route to obligation 2; affected groups are declared under obligation 1. Where measurement is genuinely impossible, the **gap is disclosed, not waived**.

## Obligation 5 — Open to evidence & correction

**Claim:** material claims, decisions, and risk-relevant behaviour **leave a trail others can check** — sources shown where used; uncertainty and limits signalled; errors corrected and **not regenerated** — and the system's own public claims are **warranted**. **Honesty-of-process applies across all five obligations; it is enforced here,** and this is where the factual-output **grounding-faithfulness** module lives.

| Duty (argument) | Shows | Evidence / module | Min. depth |
|---|---|---|---|
| **D7 — transparency, claim-integrity** *(primary)* | claim↔source traceability; uncertainty/limits; AI-involvement notice; generated-content marking; unsupported claims corrected | grounding-faithfulness module | **effectiveness-tested** (factual systems) |
| **D5 — data provenance** | training/retrieval/data-source provenance retained | privacy/provenance module | evidence-observed |
| **D8 — correction, incidents** | correction records; paraphrase-regression; drift/currentness; withdrawal of false claims | correction records | implementation-checked |
| **D3 — residual-risk disclosure** | unresolved risks + limits disclosed | release risk assessment | evidence-observed |

Remedy: correct → re-verify (paraphrase-regression) → **withdraw the claim** if it cannot be corrected. This is the remedy the other cases borrow when they say "withdraw on false evidence."

## Cross-case findings (what the five prototypes established)

1. **The instrument needs a hard pass/fail gate, not only depth-graded rows** — a legitimacy-led obligation (1) has a binary "should this exist?" precondition that the rights-led one (2) lacks.
2. **Obligations differ in where their weight sits** — *Purpose-bound* is **duty-heavy** (module column nearly empty); *Open to evidence* is **module-heavy** (leans on grounding-faithfulness). The one crosswalk handles both, so its module column is legitimately sometimes empty.
3. **Obligations interlock** — remedies cross-reference (individual redress in obligation 2; affected groups in obligation 1; systemic remedy in 4 and 5), so the annex needs obligation→obligation references, not just obligation→duty.
4. **One obligation can bundle several properties** — obligation 3 spans safe/secure/private/resilient across different duties (D5 vs D4); it may render as sub-cards.
5. **Obligation 5 is partly meta** — it governs the *integrity of the other cases' own claims*; the "say only what the assurance depth supports" claim-discipline rule that recurs in every case **is obligation 5 operating reflexively** on the Charter's own outputs.

**Conclusion:** the Claims→Arguments→Evidence instrument generalizes cleanly across all five obligations without inventing new controls — the evidence that it is a *view over the duties*, ready to graduate into a certification-model annex once an obligation is piloted.

## Provenance

Consolidates five `wip/` prototypes (2026-06-28), shaped by GPT-5.5 / Gemini 3.1 exchanges; the assurance-depth vocabulary is shared with the [Charter Commitments](../Framework/charter-commitments.md) and the certification model. The superseded standalone files remain in git history.
