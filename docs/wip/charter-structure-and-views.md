> **Status: WORKING NOTES** — design synthesis (2026-06-28), shaped by two GPT-5.5 reviews and a GPT-5.5 / Gemini 3.1 cross-model exchange. Settles how the Charter organizes its perspectives. Companion to the [user-workflow](user-workflow-governance.md) and [control-and-evidence](public-compute-control-evidence-layer.md) notes; the obligations and duties it points to live in the [Founding Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md).

# Structuring the Charter: obligations as spine, views as lenses

*There are many ways to slice "responsible / trustworthy / honest / resilient AI" — by who is looking, which property, which layer, when in the lifecycle. This note settles which one is the **spine** and which are **lenses onto it**, so new material has a home and the pieces cohere. It is a **map**, not the assurance spec itself — the binding detail lives in the Accord's obligations and operational duties.*

## The resolution

The spine is the Charter's **five public obligations**. Every other cut — who is accountable, when in the lifecycle, which layer, what risk tier — is a **navigation lens** onto that spine, or a **module**.

**Honesty-of-process** sits *across* the spine, not inside one obligation: it is the discipline of **warranted public claims** — every checkable claim (about safety, fairness, provenance, oversight, "we consulted stakeholders," as much as about facts) must be traceable, scoped, dated, versioned, uncertainty-qualified, and withdrawn when unsupported. **Grounding-faithfulness** is one *module* of it — the instance for factual system outputs. Obligation 5 ("open to evidence & correction") is where the discipline is *enforced*, not a synonym for it.

Why obligations, not "stakeholder seat": a perspective-led structure fragments one obligation across many seats and conflates four kinds of actor. An obligation-led structure keeps the Charter what it already is, is shaped toward an assurance framework (**claims → controls → evidence**) rather than a tour of viewpoints, and keeps honesty *evidentiary* rather than rhetorical.

## The spine — and the obligation→duty bridge

The five obligations are the spine — but they are **public claims, not assessable units.** The **eight operational duties (plus modules) stay the single source of audit truth**; an obligation's status is **derived** from the duty/module findings that support it, never scored on its own. This is the rule that stops a readable per-obligation summary from becoming a "legitimacy wrapper" — easier to pass than the assurance beneath it — and a GPT-5.5 / Gemini 3.1 exchange converged hard on it.

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

## The lenses — a small, fixed set

Read the card through these; they do not replace it. **Each lens renders a usable artifact** (see *How it's used*) — the lenses are how the obligation-spine becomes navigable for real readers.

1. **Actor-kind** — assigned *by role in a given context, not by fixed identity*; one entity can hold several at once (a hospital is deployer, data supplier, and affected institution; a worker is user, duty-holder, and rights-holder). The kinds: **rights/interest-holders** (whom an obligation protects) · **duty-holders** (who must act) · **oversight actors** (auditor/regulator/court/ombuds — public accountability runs *through* them, but reporting and cooperation duties also run *to* them) · **meta-governance** (the Charter steward/certifier — its own independence and capture duties).
2. **Two lifecycles** — the slow **system lifecycle** (conceive → assess → procure → authorize → deploy → monitor → incident → update → retire) and the fast **consequential-event lifecycle** for an action *involving* AI (purpose/authority/notice → AI processing/recommendation/**action** → effectuation within an authorised envelope → explanation → challenge → remedy → systemic learning). Both open with a **legitimacy gate** — *is this lawful, necessary, proportionate, within the authorised envelope?* — **before** any controls or evidence. Before/during/after belongs *here*, as one lens, not as the spine.
3. **Layer** — data/knowledge/**provenance** · model/component · application/system · compute/infrastructure · then the *levels of analysis*: human workflow · institution/governance · ecosystem/society. Data/provenance is first-class, and is **legal as well as technical** (consent, licensing, source authority, chain of custody, version lineage); honesty depends on it.
4. **Risk / context calibrator** — sets *assurance intensity* (assessment depth, oversight, independence, disclosure, re-check cadence) from severity, likelihood, reversibility, scale, autonomy, dependency, vulnerability, domain, and essential-service status.
5. **Collective ↔ individual impact** — individual → group → community → polity → commons → environment. Sets *remedy route and evidence type*: individual challenge at one end; aggregate monitoring, disparity testing, and regulator/representative routes at the other. **This axis joins the two workstreams** — the Assurance layer's *affected person* and the Public AI Network's *sovereignty / anti-capture* concern are its two ends.

## Modules — activated, not optional

Labour/worker, environment/resource, creator/copyright, sovereignty/Global-South, and capture/political-economy are **public-interest modules with activation triggers**, not a flat "where material" escape hatch: every system gets a baseline screen, and deeper duties switch on when the trigger is met (labour → algorithmic management or human-fallback roles; environment → foundation-scale compute; copyright → training/retrieval/generation). **Capture is always-on for the Charter's own meta-governance** — it governs a body that will itself certify, fund, and audit. **Worker is the one to watch:** a worker compelled to use a tool is not the free "able + accountable" human the [user-workflow note](user-workflow-governance.md) assumes.

## How it's used — lenses render artifacts

The spine is the architecture; the lenses are how it becomes usable. Each renders a navigable artifact: **role cards** (actor-kind), **lifecycle checklists** (the two lifecycles), **risk-tier profiles** (calibrator), a **remedy map** (impact). The [user-workflow note](user-workflow-governance.md) is the first of these — the *user role-card on the consequential-event lifecycle*. Working the four-block view per obligation (as a **CAE / obligation×duty crosswalk**) is the next step; it graduates into a **certification-model annex**, not the Accord body. The first two are prototyped — a rights-led obligation in [answerable-to-people-assurance-case.md](answerable-to-people-assurance-case.md) and a legitimacy-led one in [purpose-bound-assurance-case.md](purpose-bound-assurance-case.md) (which showed the view also needs a hard pass/fail legitimacy gate alongside the depth-graded rows).

## Where the existing pieces sit

- [Founding Accord](../AI%20Assurance%20and%20Certification/Framework/founding-accord.md) — the spine itself (obligations + operational duties; owner, legal-scope, assurance-depth, and withdrawal all live here).
- [Grounding-Faithfulness & Contestability](../AI%20Assurance%20and%20Certification/Protocol/grounding-faithfulness-and-contestability.md) — the factual-output honesty module, at the data + deployed-system layers.
- [Control-and-evidence layer](public-compute-control-evidence-layer.md) — duty-holder + oversight view at the compute layer, on the system lifecycle.
- [User-workflow governance](user-workflow-governance.md) — the user role-card, on the consequential-event lifecycle.

## What this is / is not

A structural **map**, reasoned through and cross-model reviewed — not normative text, and not yet the assurance spec (no thresholds or RACI; the per-obligation CAE views graduate into a certification-model annex, not the Accord). The one change from the first sketch: the spine is **obligations**, not stakeholder seats — and "seat" splits into four role-based actor-kinds that become one lens among several.
