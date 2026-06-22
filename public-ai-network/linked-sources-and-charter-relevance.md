> **Status: WORKING DRAFT** — reference compilation of the sources cited in the published *Public AI Network* article, 22 June 2026.

# Linked sources in the "Public AI Network" article — essence + relevance to *Our AI Charter*

**Source article:** [The Public AI Network: Building Sovereignty, Resilience, and Free Society Infrastructure](https://www.linkedin.com/pulse/public-ai-network-building-sovereignty-resilience-free-robert-schaub-ggpne) (Robert Schaub, LinkedIn).
**Compiled:** 2026-06-22.

**What "Our AI Charter" is (the yardstick used below):** a public-interest governance framework to keep advanced AI trustworthy, accountable, and answerable to people — treating AI as *public infrastructure* rather than purely proprietary systems. It defines **five public obligations**, and uses a three-layer assurance model (legal scope → common baseline → public-interest modules) plus independent pilot evaluations. Repo: [github.com/robertschaub/our-ai-charter](https://github.com/robertschaub/our-ai-charter).

| # | Obligation | Short form |
|---|------------|-----------|
| 1 | **Purpose-bound** | Declare intended/prohibited uses, affected populations, known risks |
| 2 | **Answerable to people** | Named institutions responsible; notice, review, challenge, remedy |
| 3 | **Safe, secure, private, resilient** | Protect people, data, infrastructure, continuity |
| 4 | **Fair in practice** | Test and disclose performance disparities; mitigate harms |
| 5 | **Open to evidence and correction** | Auditable trails for claims, sources, limits, incidents |

> The three LinkedIn legal links in the article (Cookie Policy, User Agreement, Privacy Policy) are platform boilerplate and are excluded. Each entry below states the site's essence and which charter obligation(s) it most directly serves.

---

## 1 · The public-AI movement & coordination

### Public AI Network (PAINT) — https://publicai.network/
**Essence:** A coalition advancing "AI as public infrastructure" — provisioned like electricity, water, or libraries — on three principles: public accessibility, public accountability, and creation of permanent public goods. It runs a cross-sector community, coordinates ML research, supports policymakers, and maintains open tooling and regional initiatives (e.g., Public AI Switzerland), with operational support from Metagov, Mozilla, the Internet Archive, and Harvard's Berkman Klein Center.
**Relevance to our AI charter:** Its "AI as public infrastructure" thesis and public-accountability principle directly mirror the charter's framing and obligation (2) answerable to people.

### Metagov — https://metagov.org/
**Essence:** A 501(c)3 nonprofit "laboratory for digital governance" (founded 2019) that builds tools, practices, and communities for digital self-governance, spanning governance infrastructure, digital constitutions, and deliberative tools. It incubates the Public AI project alongside DAOstar and Interoperable Deliberative Tools.
**Relevance to our AI charter:** Its governance-infrastructure and deliberative tooling support the charter's accountability layer — named-institution responsibility with notice/review/challenge/remedy (2) — and its open, experimental ethos aligns with (5) openness to evidence.

### Current AI — https://www.currentai.org
**Essence:** A global public-private-philanthropic partnership building public-interest, open-source AI as a viable alternative to proprietary systems — funding grantees, building an open AI stack, and bridging aligned organizations and governments. It has secured $400M+ (targeting $2.5B over five years) with state and foundation backing.
**Relevance to our AI charter:** Its mission to build open AI serving the public interest embodies the charter's core goal of AI as trustworthy public infrastructure, and its transparent, community-owned development supports obligation (5).

### AI Alliance — Project Tapestry — https://thealliance.ai/projects/tapestry
**Essence:** An open-source platform (under the 200+ member AI Alliance, with Yann LeCun as Chief Science Advisor) for globally *federated* training of a shared frontier model: partners contribute compute and data while retaining data sovereignty and full ownership of derivatives — only weight updates leave each node. Phased rollout mid-2026 through 2027+.
**Relevance to our AI charter:** Its data-sovereignty / local-control architecture advances obligation (3) safe, secure, private, resilient and keeps institutions answerable for their own AI (2) rather than dependent on proprietary providers.

---

## 2 · Public / sovereign open models

### OLMo (Allen Institute for AI / Ai2) — https://allenai.org/olmo
**Essence:** A fully open LLM family (Olmo 3 spans 7B and 32B with base, instruction-tuned, and reasoning variants) from US non-profit Ai2. Exceptionally open across every dimension — weights, complete pretraining and post-training datasets, training framework (OlmoCore), post-training pipeline (Open Instruct), evaluation tools, training logs, and intermediate checkpoints are all public.
**Relevance to our AI charter:** Releasing the entire "model flow" — not just the endpoint — makes OLMo a near-complete embodiment of obligation (5) auditable trails, and its full data/code disclosure supports (1) purpose-bound and (4) reproducible fairness testing.

### LLM-jp (Japan) — https://huggingface.co/llm-jp
**Essence:** A large open collaboration (1,000+ academic and industry participants) building open Japanese-proficient LLMs under Japan's National Institute of Informatics (NII). It releases models (8B, 32B), training datasets via public GitLab, code/tooling, and an open Japanese-LLM leaderboard, governed for cross-organizational knowledge-sharing rather than proprietary control.
**Relevance to our AI charter:** A named institutional steward (NII) speaks to obligation (2), while open datasets and a public benchmark advance (4) disclosed performance and (5) openness.

### Apertus (Switzerland / Swiss AI) — https://www.swiss-ai.org/apertus
**Essence:** A fully open, sovereign-compute foundation model (8B and 70B, multilingual across 1000+ languages) from the Swiss AI Initiative — EPFL, ETH Zurich, and national supercomputing centre CSCS, with Swisscom as strategic partner. It releases weights, code, training data, methods, and alignment principles as documented and reproducible, built for EU AI Act compliance (PII removal, memorization prevention).
**Relevance to our AI charter:** A publicly-governed sovereign open model with documented data/methods advances (2) and (5); its explicit PII / memorization safeguards map to (3) safe, secure, private and (1) purpose-bound risk declaration.
> **Note — Apertus domain:** `apertvs.ai` (stylized **APERTVS**, classical-Latin *V*-for-*U*) is the **official** Apertus site of the Swiss AI Initiative; `swiss-ai.org/apertus` issues an official 301 redirect to it, and the facts above are corroborated by the official `huggingface.co/swiss-ai` org page (leads Martin Jaggi, Antoine Bosselut). It is **not** a typosquat. A separate `apertus.ai` (with a "u") is an unaffiliated third-party hosting platform — not the official model site.

### EuroLLM — https://eurollm.io/
**Essence:** A fully open multilingual model covering all 24 official EU languages (flagship EuroLLM-22B, plus 9B and 1.7B; 35 training languages), built by a consortium of eight European institutions and publicly funded via Horizon Europe, the ERC, and EuroHPC on MareNostrum 5. Base and instruction-tuned models are free on Hugging Face for European researchers, organizations, and citizens.
**Relevance to our AI charter:** A publicly-funded, multi-institution effort with declared beneficiaries supports (1) affected-population declaration and (2) answerability; open releases plus technical reports serve (5).

### ALIA (Spain) — https://alia.gob.es/
**Essence:** A Spanish public-infrastructure initiative providing open language and multimodal models for Spanish, Catalan, Valencian, Basque, and Galician, coordinated by the Barcelona Supercomputing Center under Spain's State Secretariat for Digitalization and AI (2024 National AI Strategy), funded with public resources on MareNostrum 5. Models are verified by Spain's AI Supervision Agency (AESIA) to EU AI Act transparency standards.
**Relevance to our AI charter:** State stewardship with independent verification by a named regulator (AESIA) directly embodies obligation (2) with review; EU-AI-Act transparency and universal access map to (3) and (5).

### Sarvam (India) — https://www.sarvam.ai/
**Essence:** India's "full-stack sovereign AI" platform (conversational agents, document digitization, workflow automation), built by Bangalore-based Axonwise (valued ~$1.5B). Supports 11–12 Indic languages (~23 for translation) and is *partially* open — it has announced open-sourcing its 30B and 105B models while keeping the broader platform proprietary.
**Relevance to our AI charter:** Its "sovereign by design" stance and in-India data control speak to (1) and (3); the partial openness only weakly supports (5).

### BLOOM (BigScience) — https://huggingface.co/bigscience/bloom
**Essence:** A 176B-parameter multilingual model (46 natural + 13 programming languages) from the BigScience Workshop — a volunteer open-science collaboration funded by the French government and Hugging Face. Released under the Responsible AI License (RAIL v1.0): open weights with use-restrictions against harms like disinformation and unconsented surveillance.
**Relevance to our AI charter:** Open weights and a public research mandate serve (5) and (4) (multilingual reach); RAIL use-restrictions operationalize (1) purpose-bound deployment. A 2022 precedent for the whole movement.

### SEA-LION (Southeast Asia) — https://sea-lion.ai/
**Essence:** A family of efficient multilingual/multimodal open models for Southeast Asia from AI Singapore (a national program under the National Research Foundation, hosted at NUS). Supports 11+ SEA languages with explicit focus on under-resourced communities; fully open on Hugging Face, Ollama, and major hyperscalers under permissive licensing.
**Relevance to our AI charter:** Its stated Open / Responsible / Inclusive principles map almost one-to-one onto (5) auditability, (3) safety, and (4) disparity disclosure, with a named accountable institution satisfying (2).

### LatamGPT — https://www.latamgpt.org/
**Essence:** A regional language-model initiative "made in Latin America, for Latin America," coordinated through Chile's CENIA, with active GitHub and Hugging Face presences suggesting open-weights components (homepage does not spell out licensing).
**Relevance to our AI charter:** Regional, locally-built sovereignty supports (1) and (4) for under-served Latin American languages; a named coordinating institution (CENIA) underpins (2).

### Masakhane (African languages) — https://www.masakhane.io/
**Essence:** A grassroots, community-driven NLP movement for African languages — "for Africans, by Africans" ("we build together" in isiZulu) — coordinated by the Data Science for Social Impact lab at the University of Pretoria, with 1,000+ participants across 30+ countries. Firmly open-science: public code and datasets on GitHub; explicitly opposes paywalling African data.
**Relevance to our AI charter:** Data sovereignty, reproducibility, and community participation embody (5) and (4) for under-represented languages; its by/for-community model exemplifies (2).

---

## 3 · Evaluation & benchmarking

### AI Verify (Singapore) — https://aiverifyfoundation.sg
**Essence:** A Singapore not-for-profit (under IMDA) developing open-source AI-governance testing tools. Its AI Verify framework offers process checks and technical tests against recognized AI-ethics principles; Project Moonshot is one of the first open-source LLM evaluation toolkits, combining 100+ benchmark datasets with manual and automated red-teaming, integrable into CI/CD with shareable reports.
**Relevance to our AI charter:** A concrete, runnable toolkit for obligation (4) fairness testing and (3) safety, and a model for the charter's pilot evaluations and auditable evidence trails (5).

### MLCommons AILuminate — https://mlcommons.org/ailuminate/
**Essence:** A family of safety/security benchmarks from nonprofit MLCommons (via its 100+-org AI Risk & Reliability working group), assessing generative AI across 12 hazard categories — multilingual text-to-text safety, jailbreak/multimodal attacks, agentic reliability — using ~60,000 prompts to produce comparative safety *grades* (not certification).
**Relevance to our AI charter:** A standardized independent benchmark supporting (3) safety and (4) disclosed performance; a candidate measurement instrument for the charter's common-baseline layer.

---

## 4 · Governance, regulation & openness standards

### EU AI Act — https://artificialintelligenceact.eu
**Essence:** The first comprehensive, risk-based AI regulation by a major jurisdiction, sorting systems into prohibited, high-risk (strict design/testing/documentation/monitoring duties), and lower-risk tiers, plus transparency rules (Art. 50) and general-purpose-AI provisions. Enforced via the European Commission's AI Office, member-state sandboxes, and conformity assessment, with extraterritorial reach.
**Relevance to our AI charter:** The binding **legal-scope layer** the charter's three-layer model defers to; a regulatory anchor for (1) purpose/risk declaration, (2) accountable institutions, and (5) documentation/conformity evidence.

### Council of Europe Framework Convention on AI — https://www.coe.int/en/web/artificial-intelligence/the-framework-convention-on-artificial-intelligence
**Essence:** The first international legally binding treaty on AI (adopted 17 May 2024; opened for signature 5 Sept 2024), requiring AI to respect human rights, democracy, and the rule of law across its lifecycle via a risk-based approach. Core principles: human dignity, equality/non-discrimination, transparency, accountability, safe innovation. Early signatories include the EU, US, UK; designed to be compatible with the EU AI Act.
**Relevance to our AI charter:** A human-rights treaty backbone for (2) answerability (notice/review/challenge/remedy) and (4) fairness/non-discrimination, reinforcing the legal-scope layer.

### OSI Open Source AI Definition — https://opensource.org/ai
**Essence:** The Open Source Initiative's OSAID 1.0 adapts open-source's four freedoms — use, study, modify, share for any purpose — to AI. Achieving them requires the "preferred form for modification": not just code and weights but data *information*, parameters, and documentation needed to genuinely rebuild the system — explicitly to combat "openwashing."
**Relevance to our AI charter:** Defines what "open" credibly means for obligation (5), and informs the openness criteria of the charter's public-interest modules and auditable-trail expectations.

### Model Openness Framework — https://isitopen.ai/
**Essence:** The MOF, maintained by the Generative AI Commons at the LF AI & Data Foundation, classifies and *rates* how complete and open a model's released components and licenses are across the lifecycle. Its Model Openness Tool scores a model on a three-tier scale via 16 structured questions about which artifacts are public and under what licenses.
**Relevance to our AI charter:** A graded, evidence-based openness metric operationalizing obligation (5); a ready scoring instrument for the charter's openness definitions and module assessments.

---

## 5 · International standards bodies

### ISO/IEC JTC 1/SC 42 (Artificial Intelligence) — https://www.iso.org/committee/6794475.html
**Essence:** The joint ISO/IEC committee that is the focal point for international AI standardization across the full lifecycle (data, training, design, testing, evaluation, use). Its program spans foundational standards, data quality, trustworthiness, governance, system testing, and ethical/societal concerns; secretariat held by ANSI.
**Relevance to our AI charter:** Its trustworthiness/testing/governance standards operationalize (3) and (5), giving the charter externally recognized benchmarks to align "auditable trails" and risk controls against.

### OECD AI Policy Observatory (OECD.AI) — https://oecd.ai/
**Essence:** An intergovernmental platform promoting trustworthy, human-centric AI through policy data, analysis, and the OECD AI Principles (the first intergovernmental AI standard). Practical tools include the AI Policy Toolkit, the Catalogue of Tools & Metrics, and the AI Incidents Monitor (AIM).
**Relevance to our AI charter:** Incident monitoring and accountability/human-oversight principles support (2) answerability and (5) incident/limit disclosure; its tools/metrics catalogue offers concrete instruments for testing the other obligations.

### UNESCO Recommendation on the Ethics of AI — https://www.unesco.org/en/artificial-intelligence/recommendation-ethics
**Essence:** Adopted by all 193 Member States in November 2021 — the first global standard on AI ethics, grounded in human rights and dignity. Sets four core values and ten principles (proportionality, safety, privacy, transparency, human oversight, fairness, accountability, sustainability, etc.) plus policy actions across 11 areas.
**Relevance to our AI charter:** Its principles map almost one-to-one onto the charter — fairness→(4), accountability/oversight→(2), privacy/safety→(3), transparency→(5) — anchoring it in a near-universal, human-rights mandate.

---

## 6 · Open training-data commons & provenance

### Common Corpus (PleIAs) — https://huggingface.co/datasets/PleIAs/common_corpus
**Essence:** The largest openly-licensed text dataset (2.27 trillion tokens, 30+ languages), built by Pleias with partners including the AI Alliance and the Wikimedia Foundation. Every document is uncopyrighted or freely licensed and carries document-level provenance and licensing metadata across six themed collections.
**Relevance to our AI charter:** Document-level provenance/licensing trails are a working model of obligation (5) — showing training-data sourcing can be transparent and traceable at scale rather than opaque.

### Common Pile v0.1 (EleutherAI) — https://blog.eleuther.ai/common-pile/
**Essence:** An 8 TB corpus (June 2025) from 30 sources, containing only openly licensed and public-domain text vetted against the Open Knowledge Foundation's Open License Definition. EleutherAI trained the 7B Comma v0.1 models on it to show openly licensed data can match models trained on unlicensed text; contributors include Hugging Face, Ai2, and the Vector Institute.
**Relevance to our AI charter:** Proving competitive models can be built from auditable, openly licensed data advances (5) and undercuts the claim that trustworthiness must trade off against capability.

### Data Provenance Initiative — https://www.dataprovenance.org/
**Essence:** A multidisciplinary legal/ML effort (originating at MIT) that has audited and traced the lineage — source, creators, licenses, downstream use — of 1,800+ AI text datasets, finding license-omission rates >70% and error rates >50% on popular hosting sites. Publishes the Data Provenance Explorer for filtering datasets by license and origin.
**Relevance to our AI charter:** A direct instantiation of obligation (5) — auditable trails for sources and limits — exposing the misattribution crisis in training data and providing tooling to verify provenance claims rather than take them on trust.

---

## 7 · Public compute & infrastructure

### Public AI Inference Utility — https://publicai.co/
**Essence:** A Switzerland-based nonprofit building infrastructure for public and sovereign AI models worldwide. Its flagship Inference Utility (launched Sept 2025) is a shared, decentralized public access point for running open models from public institutions — powered by models/compute from the Swiss National Supercomputing Centre, AWS, and Intel — and it released Apertus.
**Relevance to our AI charter:** A direct, operating instance of the "AI as public infrastructure" thesis — a public-interest inference utility offering open models as a shared commons, supporting (1) and (5) via its open-source codebase.

### EuroHPC AI Factories — https://www.eurohpc-ju.europa.eu/ai-factories_en
**Essence:** Public computing ecosystems built around AI-optimized supercomputers, run by the European High Performance Computing Joint Undertaking (EU + member states + private partners). They provide free, customized compute and support for developing large AI models, prioritizing European SMEs and startups; currently 19 AI Factories plus 13 Antennas.
**Relevance to our AI charter:** Publicly governed compute that democratizes AI-development capacity — embodying the public-infrastructure model and obligation (4) by widening access beyond incumbents.

---

## 8 · Public-interest AI organizations

### Mozilla.ai — https://www.mozilla.ai/
**Essence:** Builds AI infrastructure and products premised on AI being "trustworthy, transparent, and controllable" and aligned with users' values. Ships products (Octonous agent platform, Otari LLM control plane) and open-source tools (any-agent, any-llm, any-guardrail, llamafile, Blueprints) emphasizing model choice, user control, local deployment, and guardrails.
**Relevance to our AI charter:** Transparency, controllability, and guardrail tooling map onto (2) answerability, (3) safety/privacy, and (5) openness; its open-source stance reinforces the public-infrastructure thesis.

### Open Future — https://openfuture.eu/
**Essence:** A European foundation working to preserve and strengthen open digital ecosystems, framing digital commons as collectively created resources prioritized for public access over private commodification. Advances "Public Digital Infrastructure" / a "Digital Public Space," works with EU institutions on openness policy, and researches equitable data licensing.
**Relevance to our AI charter:** Its digital-commons and public-digital-infrastructure agenda is the policy backbone of the charter's "AI as public infrastructure" thesis; its equitable-data work supports (4) and (5).

### HIIG Public-Interest AI project — https://www.hiig.de/en/project/public-interest-ai/
**Essence:** At Berlin's Humboldt Institute for Internet and Society, led by Dr. Theresa Züger (Oct 2020–Sep 2024, funded by Germany's Federal Ministry of Education and Research), researching AI focused on benefiting society rather than profit maximization. Develops principles/criteria for public-interest AI, a global dataset of initiatives, and an interactive Public Interest AI Interface with prototypes.
**Relevance to our AI charter:** Supplies the academic definition, criteria, and evidence base underpinning the charter's (1) purpose-bound obligation and its commitment to auditable, evidence-grounded standards.

### Digital Public Goods Alliance (DPGA) — https://www.digitalpublicgoods.net/
**Essence:** A multi-stakeholder coalition (governments, international orgs, nonprofit/for-profit members) advancing "digital public goods" — open-source software, open data, open AI systems, open content that meet applicable laws/best practices and serve humanitarian ends. Maintains a verified DPG registry (242 listed) governed by the DPG Standard; recognized in the UN Global Digital Compact.
**Relevance to our AI charter:** Its DPG Standard and open-AI-systems criteria operationalize obligation (5) and reinforce (3) by requiring open, vetted, lawful systems as a precondition for trust.

---

## 9 · UN & multilateral governance

### UN Global Digital Compact — https://www.un.org/global-digital-compact/en
**Essence:** A comprehensive global framework for digital cooperation and AI governance negotiated by all 193 UN Member States, opened for endorsement at the September 2024 Summit of the Future (rollout Q1 2025; high-level review Q3 2027). Its AI/data-governance pillar created the international scientific panel on AI and the global AI policy dialogue.
**Relevance to our AI charter:** The multilateral instrument establishing named global AI institutions and a public review tracker — embodying (2) answerability and (1) purpose-bound governance achieved through international coordination.

### UN Independent International Scientific Panel on AI — https://www.un.org/independent-international-scientific-panel-ai/en
**Essence:** Established by UN GA Resolution A/RES/79/325 (26 Aug 2025) — the first global scientific body dedicated to AI, with 40 experts delivering independent, evidence-based assessments to inform international policy. Non-regulatory: an authoritative source of scientific insight rather than an enforcement body; a direct GDC commitment (inaugural meeting 2026).
**Relevance to our AI charter:** The institutional embodiment of obligation (5) open to evidence and correction, ensuring international AI deliberations rest on the best available independent science.

### UN Global Dialogue on AI Governance — https://www.un.org/global-dialogue-ai-governance/en
**Essence:** A universal UN platform (committed in the GDC, established by A/RES/79/325) convening all governments and stakeholders for open, inclusive discussion of AI governance. First session: Geneva, 6–7 July 2026 (alongside the ITU AI for Good Summit); second: May 2027 in New York; co-chaired by El Salvador and Estonia.
**Relevance to our AI charter:** The standing multilateral forum for converging on compatible AI governance — the charter's core method of international coordination — and supports (4) by amplifying less-resourced nations' priorities.

### 2027 Geneva AI Summit (Digital Watch) — https://dig.watch/processes/2027-geneva-ai-summit
**Essence:** A 2027 Geneva summit organized by Switzerland with the Geneva Internet Platform / DiploFoundation, framed as a global learning-and-policy journey across four pillars: social/economic impacts, safety and security, human rights, and ethics. Builds on prior convenings (e.g., the Feb 2026 India AI Impact Summit) and connects to UN working groups and the IGF.
**Relevance to our AI charter:** Its human-rights and safety pillars map to (2), (3), and (4); its multistakeholder, standards-oriented mission reflects the charter's commitment to international coordination. The article proposes it as a deadline for a cooperation package.

---

## 10 · The charter itself

### Our AI Charter — https://github.com/robertschaub/our-ai-charter
**Essence:** The author's own working paper and open-source collaboration project: a public-interest governance framework defining the five obligations tabled above, a three-layer assurance model (legal scope → common baseline → public-interest modules), and an initial evaluation protocol for factual grounding and contestability. Currently a Phase-1 working draft, open for public comment and pilot participation — not yet a certification standard.
**Relevance to our AI charter:** This *is* the charter — the destination all the above initiatives feed into. The models supply what to assess, the openness definitions and benchmarks supply how to assess it, the regulation/treaties supply the binding legal floor, and the UN venues supply the coordination path.

---

## Notes on method
- Summaries are distilled from each site's own pages (fetched 2026-06-22). Two sites — **AI Verify** and the **Council of Europe** page — bot-block automated fetching (HTTP 403); their entries were grounded against official primary sources via web search.
- **Apertus link (verified 2026-06-22):** `swiss-ai.org/apertus` issues an official 301 redirect to the **official** `apertvs.ai` (stylized APERTVS) — the article link is correct; no repoint needed. Do not confuse it with the unaffiliated third-party `apertus.ai` (with a "u").
