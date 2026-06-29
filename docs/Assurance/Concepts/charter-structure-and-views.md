# Structuring the Charter: obligations as spine, views as lenses

*Map, not specification. The binding detail lives in the [Charter Commitments](../Framework/charter-commitments.md); this note explains where new material belongs and how the parts relate.*

## Resolution

The Charter's **five public obligations** are the spine. Everything else — actor roles, lifecycle, system layer, risk tier, impact type — is a **lens** over that spine or a **module** triggered by the assessed use.

The assessable truth remains the **eight operational duties plus modules**. An obligation summary is derived from duty/module findings; it is not scored on its own. Three rules prevent a readable summary from becoming a weak legitimacy wrapper:

- **Non-compensatory:** a strong module cannot offset a failed material duty.
- **Not assessed blocks material claims:** an omitted material module narrows or blocks the claim.
- **Honesty failures contaminate affected claims:** false, stale, or unsupported evidence invalidates the claim it supports, not only obligation 5.

**Honesty-of-process** cuts across the spine: public claims must be scoped, dated, versioned, evidence-backed, uncertainty-qualified, and withdrawn when unsupported. **Grounding-faithfulness** is one module of that discipline for factual system outputs.

## Obligation-to-duty bridge

Use a **Claims → Arguments → Evidence** view:

1. **Scope & trigger** — when the obligation applies and at what risk tier; links to legal-scope map, risk register, and duties 2–3.
2. **Accountability** — interests protected, accountable owner, duty-holders, and oversight route; links to duty 1.
3. **Controls & evidence** — what must be done and how it is proven, labelled by assurance depth; links to duty 3 and relevant modules.
4. **Remedy & escalation** — remedy owed, escalation route, and withdrawal triggers; links to duties 6 and 8.

This view is a crosswalk over existing duties, not a new control layer. The five working prototypes live in `docs/wip/`: [answerable](../../wip/answerable-to-people-assurance-case.md), [purpose-bound](../../wip/purpose-bound-assurance-case.md), [safe-secure-private-resilient](../../wip/safe-secure-private-resilient-assurance-case.md), [fair-in-practice](../../wip/fair-in-practice-assurance-case.md), and [open-to-evidence](../../wip/open-to-evidence-assurance-case.md).

## Two planes

**Assurance** and **runtime** are different planes:

- **Assurance plane:** periodic, outside the request path; produces warranted claims, evidence, depth labels, findings, and withdrawals.
- **Runtime plane:** inside the system; produces actions and traces under a governed operating envelope.

Runtime is the object of assurance, not a rival authority. Five interfaces bind the planes:

1. assured scope → runtime envelope;
2. runtime trace → assurance evidence;
3. runtime drift/incident → re-assurance or withdrawal;
4. shared risk tier → gate strength and evidence depth;
5. one honesty discipline across reports and live notices.

The [user-workflow governance](user-workflow-governance.md) note is the runtime reference model the assurance plane can assess.

## Lenses

Use a small fixed set of lenses when a reader needs a different view:

1. **Actor-kind** — rights/interest-holders, duty-holders, oversight actors, and meta-governance. Roles are contextual; one entity can hold several.
2. **Two lifecycles** — system lifecycle (conceive → assess → procure → deploy → monitor → incident → update → retire) and consequential-event lifecycle (purpose → AI processing/action → effect → explanation → challenge → remedy → learning). Both start with a legitimacy gate. Admissibility — may this purpose enter Charter space at all? — is separate from assurance depth: a well-documented purpose can still be inadmissible, and some uses sit below a non-negotiable floor that no evidence redeems.
3. **Layer** — data/knowledge/provenance, model/component, application/system, compute/infrastructure, human workflow, institution/governance, ecosystem/society.
4. **Risk/context calibrator** — severity, likelihood, reversibility, scale, autonomy, dependency, vulnerability, domain, and essential-service status.
5. **Collective to individual impact** — individual, group, community, polity, commons, environment; sets remedy route and evidence type.

## Modules

Modules are triggered, not optional decoration. Every assessed system gets a baseline screen; deeper duties activate when the trigger is met. Examples: labour/worker, environment/resource, creator/copyright, sovereignty/Global-South, and capture/political-economy. Capture is always-on for the Charter's own governance because the steward, assessor, funder, and registry roles can themselves be captured. **Worker** is the one to watch: someone compelled to use a tool is not the free, accountable user the [user-workflow note](user-workflow-governance.md) assumes.

## Demand side: find, check, watch

The outward surfaces are concepts, not interface specs:

- **Find** — discovery and navigation across providers and systems, based on scoped assurance depth rather than an "approved" badge. The directory must remain plural and neutral: the index is a chokepoint, and a captured registry is a captured market.
- **Check** — a [Capabilities & Assurance Interface](../../wip/capabilities-and-assurance-interface.md): what a system says it is for, what has been assured, and what is not verified.
- **Watch** — runtime inspection at least-exposure: each audience sees only its slice (own session, affected-person decision, assessor sample, regulator access, public aggregate). Inspection must be verifiable rather than self-reported, privacy-bounded (confirm behaviour without exposing content), and itself assessed — the assurance plane checks that inspection is adequate.

These surfaces steer discovery, procurement, and trust. They are governed public-power surfaces, not neutral plumbing.

## Accountability

Claims need consequences:

- **Standing:** users, affected people, and representatives for diffuse or collective harms can challenge.
- **Authority:** a named adjudicator outside any single member decides contested Charter claims under published standards.
- **Consequence:** unsupported, misleading, or out-of-scope claims are narrowed, reclassified, or withdrawn, and the record is public. Honesty applies reflexively — that consequence record is itself a warranted public claim.

Without this leg, the system only produces claims. With it, claims are answerable.

## Where pieces sit

- [Charter Commitments](../Framework/charter-commitments.md) — assurance plane: obligations, duties, scope, depth labels, withdrawal.
- [Grounding-Faithfulness & Contestability](../Protocol/grounding-faithfulness-and-contestability.md) — assurance plane: factual-output honesty module.
- Five `wip/` assurance cases — obligation-to-duty crosswalk prototypes.
- [Control-and-evidence layer](../../Compute/public-compute-control-evidence-layer.md) — policy broker plus evidence plane.
- [User-workflow governance](user-workflow-governance.md) — runtime reference model.
- [Capabilities & Assurance Interface](../../wip/capabilities-and-assurance-interface.md) — demand-side check surface.

## What this is

A structural map. It is not normative text, not an assurance spec, and not a threshold/RACI model. The obligation crosswalks should graduate into a certification-model annex, not into the body of the Charter Commitments.
