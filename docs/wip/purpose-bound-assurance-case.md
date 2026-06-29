> **Status: WORKING NOTES** — prototype (2026-06-28). The **second** worked obligation→duty bridge, built to test whether the instrument in [charter-structure-and-views.md](../Concepts/charter-structure-and-views.md) generalizes from a rights-led obligation ([Answerable to people](answerable-to-people-assurance-case.md)) to a **legitimacy-led** one. Pointer-level: routes to the [Charter Commitments](../AI%20Assurance%20and%20Certification/Framework/charter-commitments.md)' duties, inventing no new controls.

# Assurance case — *Purpose-bound* (obligation 1)

*A Claims → Arguments → Evidence view of one obligation, with the obligation's status **derived** from duty/module findings, never scored on its own. A **view over the duties**, not a new control layer. This obligation also carries a **hard legitimacy gate** that the depth-graded rows do not — see below.*

## Claim

The system declares **what it is for, what it must not be used for, who it may affect, and what is known to be risky** — and is used **only within that declared, legitimate purpose.**

## Scope & trigger

Every system, at the **system-lifecycle authorize gate** — and re-triggered on any material purpose or scope change. This is the *first* question ("should this run, for this purpose, at all?"), so it sits earlier than the per-event machinery. Tier rises with intrusiveness, domain sensitivity, and the breadth of affected groups.

## The legitimacy gate (hard, pass/fail — not a graded row)

Before any of the crosswalk below, the declared purpose must clear a **binary gate**: a lawful basis; **not** a prohibited / no-go use; **necessity and proportionality** (least-intrusive means for the stated aim); affected groups identified; known limits and residual risks stated. **Failing the gate is not "low assurance" — it bars the claim outright.** No depth elsewhere compensates. This is the structural difference from the rights-led case, whose rows all degrade gracefully with assurance depth.

## Argument & evidence — the crosswalk

Each row routes the claim to an existing Charter Commitments duty (the *argument*) and the artifact that proves it (the *evidence*). Required depth is the minimum for a **high-stakes** tier.

| Duty (argument) | What it must show for purpose-binding | Evidence / module | Min. depth (high tier) |
|---|---|---|---|
| **D2 — purpose, scope, misuse** *(primary)* | intended + prohibited uses, foreseeable misuse, affected groups, known limits, impact assessment, residual risk | purpose/scope declaration + impact assessment | implementation-checked |
| **D1 — accountable ownership** | a named owner who declares and stands behind the purpose; AI policy; **no overstated capability/marketing claims** | AI policy + responsibility map | implementation-checked |
| **D3 — risk register, legal-scope map** | risk tier; legal-scope map (markets, jurisdictions, intended/prohibited uses, risk category) | legal-scope map + risk register | evidence-observed |
| **D4 — control, dependencies** *(supporting)* | function-creep control; who may change purpose/scope; secondary-use approvals | change-control records | evidence-observed |
| **D7 — transparency, claim-integrity** *(supporting)* | the purpose is publicly stated; capability is not oversold | public purpose statement | evidence-observed |
| **D8 — change, re-authorization, withdrawal** *(supporting)* | a purpose shift triggers re-authorization; use beyond purpose triggers withdrawal | material-change + withdrawal records | implementation-checked |
| **misuse monitoring** *(where exposed)* | a declaration is not a defence — abuse/misuse is actively watched | app-security / abuse-monitoring module | effectiveness-tested |

## Remedy & escalation (derived)

Purpose-bound's "remedy" is mostly **narrowing or withdrawal**, not individual redress: detected scope-creep or a prohibited use → constrain, re-authorize, or withdraw. Individuals harmed by an out-of-purpose use route through *[Answerable to people](answerable-to-people-assurance-case.md)* — the two obligations interlock.

## Failure / withdrawal triggers

The declared purpose **fails the legitimacy gate** (prohibited or disproportionate); the system is used materially **beyond** its declared purpose; a **silent** purpose/scope expansion; or a capability **overclaim**. Each bars or withdraws the claim. These resolve to duties 2 and 8.

## Derived status & claim discipline

Not graded directly. Public status = the *weakest primary row* (D1, D2) **and** a **passed legitimacy gate** as a hard precondition. Claims track the depth:
- *Allowed* (D2 implementation-checked): "intended and prohibited uses are declared and implementation-checked for this release."
- *Not allowed*: "the system cannot be misused" — you **monitor** misuse, you do not guarantee its absence.
- Any *not-assessed* row is shown, never hidden.

## What this does not prove

Not that the purpose is *wise*, nor that the system *works* — only that a **legitimate purpose is declared, bounded, disclosed, and monitored** to the stated depth.

## What this prototype tested (generalization findings)

Doing a second, different obligation surfaced what one could not:

1. **The instrument needs a hard pass/fail gate**, not only depth-graded rows. The rights-led case degraded smoothly; a legitimacy-led one has a binary precondition ("should this exist?"). The CAE template gains a *gate* element distinct from the crosswalk.
2. **Obligations differ in where their weight sits.** Purpose-bound is **duty-heavy** (realized almost entirely by duties; the "module" column is nearly empty); honesty was **module-heavy** (leans on grounding-faithfulness). The instrument handles both — and the crosswalk's module column is legitimately sometimes empty.
3. **Obligations interlock.** Purpose-bound's remedy is narrowing/withdrawal; individual redress lives in *Answerable*. So a future annex needs **obligation→obligation cross-references**, not just obligation→duty — otherwise the same remedy gets restated or dropped.
