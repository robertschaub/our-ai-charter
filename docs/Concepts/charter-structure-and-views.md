# Structuring the Charter: obligations as spine, views as lenses

*There are many ways to slice "responsible / trustworthy / honest / resilient AI" — by who is looking, which property, which layer, when in the lifecycle. This note settles which one is the **spine** and which are **lenses onto it**, so new material has a home and the pieces cohere. It is a **map**, not the assurance spec itself — the binding detail lives in the Accord's obligations and operational duties.*

## The resolution

The spine is the Charter's **five public obligations**. Every other cut — who is accountable, when in the lifecycle, which layer, what risk tier — is a **navigation lens** onto that spine, or a **module**.

**Honesty-of-process** sits *across* the spine, not inside one obligation: it is the discipline of **warranted public claims** — every checkable claim (about safety, fairness, provenance, oversight, "we consulted stakeholders," as much as about facts) must be traceable, scoped, dated, versioned, uncertainty-qualified, and withdrawn when unsupported. **Grounding-faithfulness** is one *module* of it — the instance for factual system outputs. Obligation 5 ("open to evidence & correction") is where the discipline is *enforced*, not a synonym for it.

Why obligations, not "stakeholder seat": a perspective-led structure fragments one obligation across many seats and conflates four kinds of actor. An obligation-led structure keeps the Charter what it already is, is shaped toward an assurance framework (**claims → controls → evidence**) rather than a tour of viewpoints, and keeps honesty *evidentiary* rather than rhetorical.

## The spine — and the obligation→duty bridge

The five obligations are the spine — but they are **public claims, not assessable units.** The **eight operational duties (plus modules) stay the single source of audit truth**; an obligation's status is **derived** from the duty/module findings that support it, never scored on its own — under explicit **claim semantics**: findings are **non-compensatory** (a strong module cannot offset a failed one), a material module left **not-assessed *blocks*** the claim rather than merely qualifying it, and an **honesty failure invalidates the affected claims**, not only obligation 5. (Others will still distil this into crude scores; the discipline is that any status is derived, scoped, and uncertainty-qualified — not that no summary exists.) This is the rule that stops a readable per-obligation summary from becoming a "legitimacy wrapper" — easier to pass than the assurance beneath it — and a GPT-5.5 / Gemini 3.1 exchange converged hard on it.

The bridge is a **Claims → Arguments → Evidence** view: each obligation (claim) → the duties that *argue* it → the modules that *evidence* it, at a risk-tiered assurance depth. Rendered per obligation it has four blocks — **a view over the duties, not a new control layer** — each resolving to an existing Accord duty rather than restating it:

1. **Scope & trigger** — when the obligation applies and at what risk tier *(→ legal-scope map; risk register, duties 2–3)*.
2. **Accountability** — interests protected · the named accountable owner + supporting duty-holders · the oversight route *(→ duty 1)*.
3. **Controls & evidence** — what must be *done* (controls) and how it is *proven* (evidence + assurance depth: documented → … → effectiveness-tested) *(→ duty 3; the protocol)*.
4. **Remedy & escalation** — the remedy level owed and the failure/withdrawal triggers *(→ duties 6, 8)*.

**Worked example — *Open to evidence & correction*** (honesty-of-process enforced here; grounding-faithfulness as its factual-output module):
- *Scope & trigger:* any system making checkable public claims; tier up for consequential or high-reliance use.
- *Accountability:* interests = users, affected persons, the public, the knowledge commons; owner = the provider's named claim-owner; data/model suppliers carry inherited duties; oversight via an independent assessor.
- *Controls & evidence:* claim↔source mapping, source-validity floor, retrieval logging, version-locking, calibration/abstention — *proven* by an independent grounding-faithfulness rate (with sampling + uncertainty) and paraphrase-regression on corrections.
- *Remedy & escalation:* output-level (correct/withdraw the claim) → decision-level (re-do affected decisions) → system-level (rollback). **Withdrawal triggers:** curated correction logs, a silent version swap, or false evidence.

***Answerable to people*** fills the same four blocks but is rights-led, and exposes machinery the honesty example doesn't: *scope* = consequential decisions about people; *accountability* = a named human institution, never "the algorithm"; *controls/evidence* = notice, explanation, human review, preserved records; *remedy* = individual challenge **and**, for patterns, collective / regulator-triggered review. The other three obligations fill the same card; full text in the [Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md).

## Two planes — assurance and runtime

Cutting across the spine is the distinction the rest depends on: **assurance** (assessment-time) and **runtime** (operation-time) are different planes.

- **Assurance plane** — *about* the system: periodic, outside the request path, producing a **warranted claim + evidence + depth** (obligations → duties → modules). This is the "AI Assurance & Certification" work.
- **Runtime plane** — *in* the system: per-decision, in the request path, producing an **action + a trace** (purpose-admission, the gates, the trace-wide/escalate-narrow policy, the operating envelope, human-in-the-loop).

Runtime is the **object** of assurance, not a rival authority: the Charter *certifies*, it does not *run*. So the runtime model — the [user-workflow note](user-workflow-governance.md) — is the **reference model the assurance plane assesses**, sitting below the obligations as what-gets-checked. Five interfaces keep the planes bound so neither floats free:

1. **assured scope → runtime envelope** — the assessed release bounds what runtime may do; drift voids the claim (why a silent version swap is a withdrawal trigger).
2. **runtime trace → assurance evidence** — runtime produces the evidence plane; assurance consumes it.
3. **runtime drift/incident → re-assurance / withdrawal** (duty 8).
4. **shared risk calibrator** — the assessed tier sets how hard the runtime gates bite.
5. **honesty-of-process across both** — one claim-discipline governs the report *and* the live AI-notice/confidence.

(Analogues: control plane vs data plane; the EU AI Act's conformity assessment vs post-market monitoring.)

## The lenses — a small, fixed set

Read the card through these; they do not replace it. **Each lens renders a usable artifact** (see *How it's used*) — the lenses are how the obligation-spine becomes navigable for real readers.

1. **Actor-kind** — assigned *by role in a given context, not by fixed identity*; one entity can hold several at once (a hospital is deployer, data supplier, and affected institution; a worker is user, duty-holder, and rights-holder). The kinds: **rights/interest-holders** (whom an obligation protects) · **duty-holders** (who must act) · **oversight actors** (auditor/regulator/court/ombuds — public accountability runs *through* them, but reporting and cooperation duties also run *to* them) · **meta-governance** (the Charter steward/certifier — its own independence and capture duties).
2. **Two lifecycles** — the slow **system lifecycle** (conceive → assess → procure → authorize → deploy → monitor → incident → update → retire) and the fast **consequential-event lifecycle** for an action *involving* AI (purpose/authority/notice → AI processing/recommendation/**action** → effectuation within an authorised envelope → explanation → challenge → remedy → systemic learning). Both open with a **legitimacy gate** — *is this lawful, necessary, proportionate, within the authorised envelope?* — **before** any controls or evidence. **Admissibility** (may this purpose enter Charter space at all?) is a *separate dimension* from assurance depth (how well-evidenced the claims are): a well-documented purpose can still be inadmissible, and no depth of evidence rescues an illegitimate one — some uses sit below a **non-negotiable floor**. Before/during/after belongs *here*, as one lens, not as the spine. (These two are the **cadences of the two planes** above — system lifecycle = assurance, consequential-event = runtime.)
3. **Layer** — data/knowledge/**provenance** · model/component · application/system · compute/infrastructure · then the *levels of analysis*: human workflow · institution/governance · ecosystem/society. Data/provenance is first-class, and is **legal as well as technical** (consent, licensing, source authority, chain of custody, version lineage); honesty depends on it.
4. **Risk / context calibrator** — sets *assurance intensity* (assessment depth, oversight, independence, disclosure, re-check cadence) from severity, likelihood, reversibility, scale, autonomy, dependency, vulnerability, domain, and essential-service status.
5. **Collective ↔ individual impact** — individual → group → community → polity → commons → environment. Sets *remedy route and evidence type*: individual challenge at one end; aggregate monitoring, disparity testing, and regulator/representative routes at the other. **This axis joins the two workstreams** — the Assurance layer's *affected person* and the Public AI Network's *sovereignty / anti-capture* concern are its two ends.

## Modules — activated, not optional

Labour/worker, environment/resource, creator/copyright, sovereignty/Global-South, and capture/political-economy are **public-interest modules with activation triggers**, not a flat "where material" escape hatch: every system gets a baseline screen, and deeper duties switch on when the trigger is met (labour → algorithmic management or human-fallback roles; environment → foundation-scale compute; copyright → training/retrieval/generation). **Capture is always-on for the Charter's own meta-governance** — it governs a body that will itself certify, fund, and audit. **Worker is the one to watch:** a worker compelled to use a tool is not the free "able + accountable" human the [user-workflow note](user-workflow-governance.md) assumes.

## How it's used — lenses render artifacts

The spine is the architecture; the lenses are how it becomes usable. Each renders a navigable artifact: **role cards** (actor-kind), **lifecycle checklists** (the two lifecycles), **risk-tier profiles** (calibrator), a **remedy map** (impact). The [user-workflow note](user-workflow-governance.md) is the first of these — the *user role-card on the consequential-event lifecycle*. Working the four-block view per obligation (as a **CAE / obligation×duty crosswalk**) is the next step; it graduates into a **certification-model annex**, not the Accord body. All five obligations are now prototyped as `wip/` CAE views — [answerable](../wip/answerable-to-people-assurance-case.md) (rights-led), [purpose-bound](../wip/purpose-bound-assurance-case.md) (legitimacy-led, with a hard gate), [safe-secure-private-resilient](../wip/safe-secure-private-resilient-assurance-case.md) (technical, effectiveness-led), [fair-in-practice](../wip/fair-in-practice-assurance-case.md) (collective, measurement-led), and [open-to-evidence](../wip/open-to-evidence-assurance-case.md) (the honesty wedge, partly meta) — ready to migrate into a certification-model annex.

## The demand side — find, check, watch

Everything above is the *supply* side (how trust is produced) and its *operation*. The outward, consumer-facing side — how a person or their agent actually engages the network — is three surfaces, described here as **concepts and principles, not interfaces**:

- **Find — discovery & navigation.** Locate providers that match a need, and navigate the network. *Principles:* match on **scoped, depth-labelled assurance**, never an "approved/safe" badge; the directory must be **plural and neutral, never a single gatekeeper** (the index is a chokepoint — a captured registry is a captured market), extending the network's anti-capture ethos to its own front door; serve humans and agents alike.
- **Check — the [Capabilities & Assurance Interface](../wip/capabilities-and-assurance-interface.md).** Read, for a chosen system, what it is for and what has been assured — **self-declared and independently-assured kept distinct**, and publicly checkable.
- **Watch — runtime inspection.** See what the system is actually doing, live and after the fact. *Principles:* **differentiated, least-exposure access** (each audience sees only its appropriate slice — your own session, an affected person's decision, an assessor's sample, the public's aggregates); **verifiable, not self-reported**; **privacy-bounded** (confirm behaviour without exposing content); and **inspectability is itself assessed** (the assurance plane checks whether adequate inspection is afforded, and to what depth).

All three read capabilities (runtime) and assurance claims under the same honesty discipline — scoped, depth-labelled, never a guarantee. They are not *certification* authorities — but a directory, a claim-surface, and an inspection feed **bear real public power** (they steer discovery, procurement, and trust), so they are **governed surfaces** (plural, anti-capture, contestable, honest), not neutral plumbing.

*Cross-stream: **Find** (discovery/navigation) and the **capabilities** half of *Check* are also the Public AI Network's "how it's used" (see its [overview](../Public%20AI%20Network/network-overview.md)); the **assurance** half of Check and **Watch** (inspection) are this accountability side.*

## Accountability — standing, authority, consequence

For a charter that is *accountable to people*, producing, surfacing, and checking claims is not enough — it must also say **who may challenge a claim, who answers for it, who interprets the Charter when one is contested, and what follows when one is unsupported.** This is the third leg, alongside the two planes and the demand side, and it mostly **unifies pieces the Charter already has**:

- **Standing — who may challenge.** The user and the *affected person* (the answerable-to-people obligation in the [Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md)), and — for **diffuse or collective** harms with no individual complainant — whoever can speak for them (a regulator, a representative body, a watchdog). The standing counterpart to the collective↔individual lens.
- **Authority — who adjudicates.** A contested claim (a misreported finding, a misdeclared purpose, a stale or selectively-scoped claim) is decided by a **named adjudicator outside any single member** — the role already introduced in the [control-and-evidence layer](../wip/public-compute-control-evidence-layer.md) — with published standards and graduated sanctions. Interpreting the Charter is itself an accountable act, not a provider's to self-serve.
- **Consequence — what follows.** An unsupported, misleading, or out-of-scope claim is **narrowed, reclassified, or withdrawn**, and the loss of standing is **public** (the cards' withdrawal triggers, generalised). Honesty-of-process applies reflexively — the consequence record is itself a warranted public claim.

Without this leg the rest is a sophisticated *claim-production* system; with it, the claims are answerable.

## Where the existing pieces sit

- [Founding Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) — **assurance plane**: the spine (obligations + operational duties; owner, legal-scope, assurance-depth, withdrawal).
- [Grounding-Faithfulness & Contestability](../AI%20Assurance%20and%20Certification/Protocol/grounding-faithfulness-and-contestability.md) — **assurance plane**: the factual-output honesty module (data + deployed-system layers).
- The five obligation assurance-cases (e.g. [Answerable to people](../wip/answerable-to-people-assurance-case.md)) — **assurance plane**: the obligation→duty CAE views.
- [Control-and-evidence layer](../wip/public-compute-control-evidence-layer.md) — **the seam**: a policy broker (runtime) + an evidence plane (assurance).
- [User-workflow governance](user-workflow-governance.md) — **runtime plane**: the runtime reference model the assurance plane assesses.
- [Capabilities & Assurance Interface](../wip/capabilities-and-assurance-interface.md) — the demand side's **check** surface (design sketch): a system's capabilities + assurance claim-state, made discoverable, self-declared and assured kept distinct; Phase-2/3.

## What this is / is not

A structural **map**, reasoned through and cross-model reviewed — not normative text, and not yet the assurance spec (no thresholds or RACI; the per-obligation CAE views graduate into a certification-model annex, not the Accord). The one change from the first sketch: the spine is **obligations**, not stakeholder seats — and "seat" splits into four role-based actor-kinds that become one lens among several.
