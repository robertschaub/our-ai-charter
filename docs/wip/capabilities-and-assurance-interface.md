> **Status: WORKING NOTES** — design sketch (2026-06-28), shaped by a GPT-5.5 / Gemini 3.1 exchange. **Concepts and principles, not interfaces** — mechanisms are deliberately out of scope at this stage. Phase-2/3. Companion to [charter-structure-and-views.md](../Assurance/Concepts/charter-structure-and-views.md): the demand side's *check* surface.

# A queryable Capabilities & Assurance Interface (CAI) — design direction

*A way for a person or their agent to ask, of one deployed system: **what is it for** (capabilities) and **what has been assured** (assurance claim-state). The "check" step of the demand side — and **not a trust badge.***

## Lead with the danger

A machine-readable assurance surface propagates **false confidence as fast as true confidence.** Agents and procurement systems will read a green light and act on it, ignoring scope, depth, and freshness. So the CAI is worth having **only as a scoped, honest, freshness-checked claim surface — never an "AI trust API" or badge.** "Queryable certification" is the phrase to avoid.

## The principles

- **Profile, don't invent.** The form already exists in supply-chain-attestation and transparency practice; the Charter contributes only the *public-interest profile* — binding it to the obligations and assurance-depth labels — not a new standard.
- **Decouple capabilities from assurance.** Self-declared capabilities must not borrow assurance's credibility: keep **self-declared** and **independently-assured** fields visibly distinct, each carrying its own provenance. Bind every assured claim to the **exact assessed version**, so a changed system falls **out of scope** rather than silently inheriting the old claim.
- **Public scrutiny by default.** An assurance claim must be **publicly checkable**, not privately asserted — that is what defeats the fake-assessor and the "one story to the buyer, another to the regulator" failures.
- **Scoped and fail-safe.** No global "trusted / safe / compliant" verdict; every claim carries its **scope, depth, and currentness**. When status cannot be confirmed, the honest answer is **"unknown," never "valid"** — and a stale "valid" must expire, not linger.
- **The trust stack is the real dependency.** The hard part is not the format; it is the **institutional trust infrastructure** — accredited assessors, revocation, and enforcement with teeth (delisting, procurement exclusion). That is why the **assured half** is **Phase-3** — riding on a maturing certification scheme — not mere packaging of existing content.

## Buildable now vs deferred

- **Now — the self-declared half only:** a provider publishes its **capabilities** (purpose, prohibited uses, operating envelope, version, limits) plus a **link to the human-readable release risk assessment**, with assured fields marked **not-yet-independently-attested**. Safe, because it claims nothing it cannot back.
- **Deferred — the assured half:** independently-signed obligation statuses, public-scrutiny records, and revocation — which wait on the assessor ecosystem and trust stack above.

## What this is / is not

A design **direction** and a **profile**, not a spec, a standard, or "queryable certification." It is the demand side's *check* surface — read alongside *find* (discovery) and *watch* (runtime inspection) in the [structure map](../Assurance/Concepts/charter-structure-and-views.md). Mechanisms (schemas, signing, logs) are intentionally left out at this stage.
