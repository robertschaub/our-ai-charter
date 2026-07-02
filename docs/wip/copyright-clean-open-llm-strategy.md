> **Status: WORKING NOTES** - grounded strategy note, prepared 2026-07-02 from web research plus three parallel assistant reviews. Re-verify legal, model-performance, and initiative-status claims before external use.

# Copyright-clean open/public LLMs - competitiveness strategy

*Working notes - 2026-07-02. Public-safe. Related: [Apertus fit & engagement plan](apertus-fit-and-engagement-plan.md), [public-interest control & evidence layer](../Infrastructure/control-and-evidence-layer.md), [initiation strategy](../Strategy/initiation-strategy.md), [actors & landscape](../Evidence/actors-and-landscape.md).*

## In one line

Copyright-clean open/public LLMs will not become frontier-competitive through clean training data alone. The credible route is a **rights-clean public frontier flywheel**: lawful data, pooled compute, open model-flow releases, strong post-training, public inference, domain adoption, and one legally usable feedback loop.

## Reality check

The first-pass answer - a public data trust plus provenance - is necessary but probably insufficient. Closed frontier labs have advantages that a clean corpus does not neutralize: proprietary product telemetry, private post-training data, larger compute budgets, faster iteration, integrated distribution, and the ability to absorb legal uncertainty.

The stronger answer is therefore not "out-scrape closed labs." It is: **out-institutionalize them where trust, sovereignty, auditability, local language quality, and procurement legitimacy matter.** Open/public LLMs do not need to beat the best closed model on every general benchmark to matter. They need to become the default trusted layer for public administration, research, education, cultural and language infrastructure, regulated workflows, and SMEs that need portability.

Stanford's 2026 AI Index is the best current reality check: as of March 2026, the top closed model led the top open model by 3.3%, up from 0.5% in August 2024 - the gap reopened in 2025 after briefly closing in 2024; it also notes that leading model performance is clustering and that competition is shifting toward cost, reliability, and domain performance ([Stanford AI Index 2026](https://hai.stanford.edu/ai-index/2026-ai-index-report/technical-performance)).

## Strongest objections

Three counter-theses this strategy must answer rather than assume away:

- **US fair-use asymmetry.** If US courts keep permitting model training on copyrighted data as fair use (unsettled, but the direction of several 2025 rulings), closed labs can train on everything while rights-clean public models accept opt-out friction. "Copyright-clean" is then a deliberate trade of capability ceiling for trust, legitimacy, and EU-market access, not a free win, and it pays off only where that trade is the buyer's binding constraint.
- **Open weights get distilled.** Rights-clean purity also forecloses distillation from frontier outputs, one of the most effective open catch-up levers. The constraint cuts both ways.
- **No durable funding model.** Pooled public compute and a public inference utility have no proven long-run funding path; treat this as a counter-thesis, not only a risk line.

## Source anchors

| Source / initiative | What it contributes | What it does not solve |
|---|---|---|
| [COMMUNIA copyright study](https://communia-association.org/2026/06/30/new-study-copyright-challenges-in-open-source-ai-development-in-the-european-union/) | Strongest legal diagnosis found for open-source AI in the EU: TDM uncertainty, opt-out friction, safe-harbor/public-corpus need. | Capability, compute, product, and adoption gaps. |
| [EU GPAI Code of Practice](https://digital-strategy.ec.europa.eu/en/policies/contents-code-gpai) and [training-content template FAQ](https://digital-strategy.ec.europa.eu/en/faqs/template-general-purpose-ai-model-providers-summarise-their-training-content) | Practical EU compliance baseline: copyright policy, transparency, training-content summaries, opt-out handling. | Compliance does not create frontier capability. |
| [DSM Copyright Directive](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019L0790) | Legal foundation for EU text and data mining exceptions, especially Articles 3 and 4. | Article 4 depends on fragmented rights reservations; Article 3 is narrow. |
| [Apertus](https://apertvs.ai/) / [ETH release](https://ethz.ch/en/news-and-events/eth-news/news/2025/09/press-release-apertus-a-fully-open-transparent-multilingual-language-model.html) | Strong proof point for public, fully open, multilingual, opt-out-aware model development and deployment. | Strong but not a general frontier leader across all tasks. |
| [Public AI: "If open source is to win, it must go public"](https://openreview.net/forum?id=zN7zY1UVru) (latest formal version, ICML 2026) | Strong diagnosis of the activation gap: open weights need compute, inference, post-training, deployment, and oversight. | Needs a harder commercial and institutional execution path. |
| [Current AI Gap Map](https://map.currentai.org/) | Maps open-source AI stack gaps; notably shows training/synthetic data and product adoption as weak points. | A map, not an operating model. |
| [OpenEuroLLM](https://openeurollm.eu/) | European route for transparent, compliant, multilingual foundation models for public and commercial services. | Still early; needs model releases, adoption, and feedback loops. |
| [OSI Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) | Helps distinguish real openness from open-weight marketing by requiring enough data information, code, and parameters to modify/recreate. | Does not itself clear copyright or fund compute. |
| [Common Corpus](https://huggingface.co/blog/Pclanglais/two-trillion-tokens-open) and [Common Pile](https://arxiv.org/abs/2506.05209) | Show that large public-domain/open-license corpora are possible and can train competitive smaller models. | Scale and breadth remain below frontier private data and telemetry loops. |

## Strategy comparison

Scores use 1-5: **maturity** = usable now; **potential** = ability to close the practical frontier gap under copyright constraints.

| Strategy | Maturity | Potential | Comments | Main risks |
|---|---:|---:|---|---|
| Public-domain / permissive corpus only | 4 | 3 | Cleanest legal base; Common Corpus/Common Pile prove feasibility. | Not enough for broad frontier performance by itself. |
| Lawful TDM plus opt-out pipeline | 3 | 4 | Required for scale in Europe; aligns with EU AI Act and DSM Article 4. | Opt-out standards remain fragmented; rightsholder disputes persist. |
| Collective licensing / data compacts | 2 | 5 | Could unlock books, media, education, legal, science, and culture at scale. | Slow, politically contested, expensive, sector-specific. |
| Public data trust / corpus institution | 2 | 5 | Creates a durable public data moat and shared provenance infrastructure. | Governance-heavy; needs funding, rights process, quality control. |
| Open model factory: Apertus/OLMo/OpenEuroLLM pattern | 3 | 4 | Data, code, recipes, checkpoints, evals, and model cards build trust and scientific leverage. | One-off model releases decay quickly without recurring compute. |
| Synthetic data and permitted distillation | 4 | 4 | Critical for instruction following, reasoning, domain scarcity, and smaller model quality. | Teacher-license constraints, inherited bias, quality collapse. |
| Reasoning RL and test-time compute | 4 | 5 | Best current lever for math, code, STEM, and verification-heavy workflows. | Less useful for factual breadth and subjective judgment. |
| Sparse MoE and efficient scaling | 4 | 4 | Needed to compete on cost/capacity; common among leading open-weight systems. | Hard training and serving engineering. |
| Public inference utility | 3 | 5 | Turns open weights into usable services and creates a lawful feedback channel. | Needs long-term operational funding and reliability. |
| Domain-specialized models plus RAG/tools | 5 | 4 | Best near-term wedge; can beat frontier models in bounded workflows. | Does not create general frontier capability. |
| Procurement-driven public market | 2 | 5 | Demand-side lever: public buyers can reward transparency, portability, and lawful provenance. | Public procurement is slow unless packaged as concrete service offers. |
| **Rights-clean public frontier flywheel** | **2** | **4** | Combines lawful data, compute, open model factory, post-training, inference utility, domain adoption, and a feedback loop. | Hard institution-building; failure mode is becoming only a policy slogan. |

## Persona and market assessment

The main market mistake is to position copyright-clean open/public LLMs as a generic replacement for the best frontier model. The strongest wedges are buyers whose binding constraint is not raw benchmark rank but **control, auditability, lawful data, procurement legitimacy, cost, language fit, or avoidance of vendor lock-in**.

| Segment / persona | Why they might choose open/public | Capability threshold | Best-fit strategy | Maturity / potential |
|---|---|---|---|---|
| Public-sector CIO | Sovereignty, auditability, lawful provenance, data control. | Reliable "good enough" service, hosted or on-prem, with documentation and support. | Public inference + domain RAG + procurement clauses. | 3 / 5 |
| Public procurement officer | Avoid opaque lock-in and supplier concentration. | Clear license, training summary, switching rights, inspection rights. | Procurement framework and evidence package. | 2 / 5 |
| Education ministry / university | Student privacy, local curriculum, public accountability. | Safe tutoring, teacher support, local-language quality. | Local model + curriculum data + safeguards. | 3 / 5 |
| Research lab | Reproducibility, inspectability, open science. | Open weights, code, data information, checkpoints. | Apertus/OLMo-style model flow. | 4 / 5 |
| Cultural or language institution | Minority languages, archives, dialects, cultural legitimacy. | Must outperform generic frontier models on local language/culture. | Data trust + community consent + multilingual model. | 3 / 5 |
| SME / startup CTO | Cost, portability, no API lock-in, customization. | Easy hosted API, deployment templates, predictable pricing. | Managed public inference + fine-tuning templates. | 3 / 4 |
| Regulated enterprise | Audit logs, privacy, liability chain, local deployment. | High reliability in narrow workflows. | VPC/on-prem domain models + evaluations. | 3 / 4 |
| Publisher / media organization | Rights, attribution, archive tools, licensing revenue. | Provenance, retrieval-first design, no unlicensed memorization. | Licensing pool + rights-aware model/service. | 2 / 5 |
| Developer / civic technologist | Hackability, local control, permissive reuse. | Docs, APIs, quantized models, eval harnesses. | Open model factory + inference stack. | 4 / 4 |
| Civil-society watchdog | Auditability, independent evaluation, public-interest governance. | Low-cost access and transparent artifacts. | Public inference + open evals + governance participation. | 2 / 4 |

## Recommended strategy

Build the **rights-clean public frontier flywheel** - an *ecosystem* agenda, not a to-do list for one actor. This initiative contributes one part of it: the rights, governance, evidence, procurement, and accountability layer (see [control & evidence layer](../Infrastructure/control-and-evidence-layer.md)); the compute, model-factory, and inference-utility layers belong to partners:

1. **Data layer:** combine public-domain/open corpora, lawful TDM with opt-out compliance, public-sector data, cultural archives, and negotiated licensing pools.
2. **Rights layer:** maintain crawler logs, provenance metadata, opt-out registries, takedown/update workflows, model training summaries, and source-domain reporting.
3. **Compute layer:** pool national/public compute through Swiss AI, EuroHPC, AI Factories, universities, and trusted commercial partners.
4. **Model factory:** release reproducible model flows: data recipes, training code, checkpoints, post-training data, evals, safety tests, and deployment configs.
5. **Post-training layer:** invest heavily in reasoning RL, permitted distillation, synthetic data, tool use, domain fine-tuning, long-context document work, and multilingual balancing.
6. **Inference utility:** provide public APIs and deployable hosted/on-prem packages so users do not need to become infrastructure teams.
7. **Market wedge:** win first in public administration, education, research, cultural/language infrastructure, regulated workflows, and SMEs.
8. **Feedback loop:** collect opt-in institutional feedback, eval traces, domain corrections, and task-specific telemetry under lawful governance; feed that back into post-training and benchmarks.

## What this means for Our AI Charter

This is directly relevant to the Public AI Network track. The network should not be framed as "another model" or a general claim that open models will automatically win. The more credible contribution is the **governance, evidence, rights, procurement, and accountability layer** that makes a public model ecosystem adoptable by real institutions.

Near-term artifacts that would fit this strategy:

- A rights/provenance checklist for public/open model builders.
- A procurement clause pack for public buyers: transparency, switching rights, lawful data, audit evidence, and feedback-data governance.
- A compact "public inference utility governance" note: how public deployment can gather feedback without becoming extractive telemetry.
- A worked evaluation case on an open/public model deployment, linked to the [evaluation proof-of-concept](evaluation-poc-scope.md).

## Open questions

- Can public institutions create feedback loops fast enough to match private product telemetry?
- Which rightsholders would join a licensing/data compact if the buyer were a public model utility rather than a private lab?
- Is the first proof point a model, an inference service, a procurement package, or a domain evaluation?
- How much compute is required for a public/open model to be "frontier-competitive enough" in the target segments?
- Should this be positioned under the Public AI Network name, or under a narrower functional label such as "public-AI rights and evidence layer"?
