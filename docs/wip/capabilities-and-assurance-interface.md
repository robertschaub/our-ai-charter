> **Status: WORKING NOTES** — design sketch (2026-06-28), shaped by a GPT-5.5 / Gemini 3.1 exchange that corrected an earlier framing. **Phase-2/3 — not buildable now beyond the self-declared half.** A *profile of existing standards*, not a new interface. Companion to [charter-structure-and-views.md](charter-structure-and-views.md) — it is two of that note's plane-interfaces made machine-readable.

# A queryable Capabilities & Assurance Interface (CAI) — design direction

*A discoverable, machine-readable, signed surface a client — an agent, buyer, regulator, or another AI — can query to learn, for one deployed system + version: **what it is for** (capabilities) and **what has been assured** (assurance claim-state). The externally-queryable projection of the two planes — and **not a trust badge.***

## Lead with the danger

A machine-readable assurance surface propagates **false confidence as fast as true confidence.** Agents and procurement bots will read `assurance: valid` and auto-trust it — ignoring scope, depth, freshness, and exclusions. Concrete failure modes: **auto-trust** (proceed on a green light); **scope / depth / module laundering** (a narrow or shallow assessment read as broad approval); **stale claims** surviving a withdrawal or model swap; **fake or weak assessors** signing perfect wrappers; **split-view** (one CAI to the buyer, another to the regulator). So the CAI is worth building **only as a scoped, signed, freshness-checked claim-verification mechanism — never an "AI trust API" or badge.** "Queryable certification" is the phrase to avoid.

## Profile existing standards — don't invent

The *form* already exists; the Charter should **profile**, not reinvent:
- **IETF SCITT** — signed statements, assessor counter-signing, transparency log (the closest precedent).
- **in-toto** attestations (signed claim envelopes) + **CycloneDX ML-BOM** (the payload: model/dataset/dependency/compliance metadata).
- **VEX / CSAF** — the model for a status vocabulary (*valid · expired · suspended · withdrawn · superseded · under-review · not-assessed*).
- **Sigstore/Rekor or Certificate Transparency** (the public log); **W3C VC Status Lists / OCSP** (revocation); **`/.well-known/`** + security.txt, RFC 9116 (discovery).

The narrow, defensible novelty is only the **public-interest profile** binding these to the Charter's obligations and assurance-depth labels. *(This corrects an earlier claim that "only the form is new" — both the payload and the form largely exist.)*

## Two halves — decoupled, crypto-linked

Bundling capabilities and assurance in one blob implies the capabilities were assured. So **decouple physically, link cryptographically:**

| | **Capabilities** (runtime plane) | **Assurance** (assurance plane) |
|---|---|---|
| Signed by | provider — *self-declared* | assessor — *Phase-3+* |
| Content | purpose, prohibited uses, operating envelope, **config/version fingerprint**, model/data/tool summary, known limits | assessed-release ID, per-obligation **derived** status + depth, modules covered/not-assessed, legal-scope, **permitted public-claim text**, validity, withdrawal status, report-index link |

The assurance artifact **pins the config hash it covers**; a client compares it to the runtime's current fingerprint — **mismatch ⇒ `out_of_scope`** (interface #1, made mechanical — the silent-version-swap guard in crypto). Every field carries **provenance** (`self_declared` / `assessor_signed` / `runtime_observed` / `not_assessed`) — no whole-document "assurance aura," and **no `trusted` / `safe` / `compliant` / `score` booleans.**

## The safety keystone

A CAI claim is **invalid unless it carries proof of inclusion in a public append-only transparency log.** That one rule defeats the fake-assessor and split-view attacks — every claim becomes publicly scrutable. Paired with: **scoped claims only**; **clients fail to `indeterminate` / `out_of_scope`, never `valid`**; **no indefinite caching of "valid."** This is honesty-of-process (obligation 5) enforced cryptographically on the interface itself.

## The real dependency is the trust stack — not packaging

The JSON is trivial; what it presupposes is an **institutional build that does not exist yet**: an **accredited-assessor registry / trust anchors** (hybrid — a Charter registry plus national accreditation), signing profiles (COSE/JOSE, hardware-backed assessor keys), a revocation/status service, the transparency log, schema governance, relying-party rules, and **enforcement with teeth** (registry delisting, procurement exclusion, regulator notification — "penalties for false attestation" is empty without these). This is **Phase-3/4**, riding on a maturing certification scheme. *(This corrects an earlier claim that the CAI is "merely Phase-2 packaging.")*

## What is buildable now — the self-declared half only

No assessor or PKI exists yet, so the only honest v1 is the **capabilities half**:
- a **static signed `/.well-known/` descriptor** (profiling CycloneDX ML-BOM / in-toto) carrying provider-declared capabilities + the **config fingerprint** + a **link to the human-readable release risk assessment**;
- assured fields present but flagged **`not-machine-attested-yet`**;
- **no** assured booleans, **no** live API, **no** agent-authorization semantics.

It is safe precisely because it claims nothing it cannot back — it just makes the existing release risk assessment and model card discoverable and signed. The **assessor-signed assurance half + transparency log + revocation** is deferred to the trust-stack build above.

## Static vs live

Prefer **static signed artifacts** — a discovery descriptor plus an immutable, content-addressed release manifest — with a lightweight **freshness** mechanism (short-lived signatures, an OCSP-like signed status list, transparency-log inclusion). A live signed *status* endpoint (withdrawn / suspended / superseded) is a later refinement, not a v1 requirement. Never an indefinitely-cached "valid."

## What this is / is not

A design **direction**, not a spec or a standard; a **profile** of existing standards, not a new interface; explicitly **not** "queryable certification." Buildable now: the self-declared, provider-signed descriptor that links to the human assessment. Deferred: the assured layer, which waits on an assessor ecosystem and the trust stack — the same Phase-2/3 boundary as the rest of the certification work.
