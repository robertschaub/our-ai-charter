# Our AI Charter and Hugging Face — overlap and cooperation options

*Assessment as of 2026-07-22. Re-verify platform features, provider availability, and prices before relying on them.*

## Conclusion

Hugging Face is a strong prospective **distribution, metadata, evaluation, and developer-access partner** for the proposed public-AI network. Our AI Charter contributes the layer Hugging Face does not supply: public-interest admission and routing rules, independent assurance, redress, evidence custody, and protection against capture.

The useful relationship is therefore complementary:

> **Hugging Face can be an interoperable discovery and evidence surface, but should not become the network's sole host, governor, or source of truth.**

This maps closely to the network's [find → check → use](../network-overview.md#how-it-would-work) path. The Hub helps people find models and datasets; cards and evaluations help them check documented claims; Inference Providers and Spaces help them use models. The Charter's [control-and-evidence layer](../Infrastructure/control-and-evidence-layer.md) adds the missing public-interest decisions and accountabilities around those functions.

## Where the fit is strongest

| Network need | Hugging Face capability | Cooperation option | What remains missing |
|---|---|---|---|
| **Open, plural models** | Hub repositories, search, organisations, Collections, model cards, and downloadable revisions | Curate a Public AI Network collection linking participating models, datasets, evaluations, papers, and services | Rules for inclusion, neutral ordering, conflicts, appeals, and continuity outside one platform |
| **Data and provenance commons** | Dataset repositories and cards recording fields such as licence, language, size, and intended use | Publish rights-cleared datasets, provenance manifests, evaluation sets, opt-out information, and reusable documentation | Independent verification of rights, consent, provenance gaps, and correction or withdrawal routes |
| **Shared evaluation** | Benchmark datasets, structured evaluation results, community submissions, source links, and verified evaluation runs | Publish Charter evaluation modules as open benchmark datasets and results linked to exact model revisions | Method validity, assessor independence, deployment context, consequences, redress, and durable custody |
| **Federated model access** | One client and API across multiple inference providers | Use the existing router for an early multi-model pilot while the Charter broker is still being specified | Purpose-, jurisdiction-, data-class-, evidence-, and public-allocation-aware routing |
| **Public front door** | Model pages, widgets, organisations, Collections, and open Spaces | Demonstrate the network's find → check → use experience without first building a new catalogue | Capture-resistant governance, public-service continuity, and a provider-independent canonical record |
| **International participation** | Large multilingual and open-science communities; the BigScience/BLOOM precedent | Learn from participatory research, ethical-charter, data-host, and multilingual-governance experience | A present commitment by Hugging Face to the Charter or to co-govern the proposed network |

The connection is already operational rather than hypothetical. The nonprofit **Public AI Inference Utility became a supported Hugging Face Inference Provider in September 2025**, so public and sovereign models such as Apertus can be found on the Hub and served through Public AI using Hugging Face's common interface ([Hugging Face announcement](https://huggingface.co/blog/inference-providers-publicai); [current provider documentation](https://huggingface.co/docs/inference-providers/en/providers/publicai)). The emerging stack is:

> public and sovereign models → Hugging Face discovery and tooling → Public AI inference → Charter control and evidence

## Best first cooperation: a deployment-evidence pilot

The strongest bounded project is the existing [evaluation proof-of-concept](../wip/evaluation-poc-scope.md), implemented on an Apertus/PublicAI-backed cited-source deployment and published through Hugging Face as well as this repository.

1. Build or identify a minimal Apertus-based cited-source Q&A deployment. Evaluate the **deployment**, not the weights.
2. Publish its held-out evaluation set as a Hub benchmark dataset with a pinned revision and an `eval.yaml` definition.
3. Run the open evaluation with Inspect against an exact model revision and named inference provider.
4. Publish structured results, method version, configuration, source traces, and limitations. Keep any public result labelled **PILOT, not certification**.
5. Add a Charter deployment-evidence record covering provider, runtime, responsible operator, jurisdiction where disclosable, declared purpose, data class, retention, assessed and unassessed duties, assessor independence, incidents, correction, and appeal.
6. Present the result through a small open Space or collection following find → check → use, while mirroring the canonical evidence independently.

Hugging Face's own evaluation guide makes the deployment distinction material: it notes that the same model can perform differently across providers because inference implementations, hardware, batching, and nondeterminism vary ([Inspect evaluation guide](https://huggingface.co/docs/inference-providers/en/guides/evaluation-inspect-ai)). A model-only score is therefore not enough; evidence should bind the model revision to the provider and material deployment configuration.

The Hub's evaluation system is useful substrate. Benchmark datasets can aggregate results from model repositories; results can link to sources and community submissions; and a verification token can show that an evaluation ran through Hugging Face Jobs with Inspect ([Evaluation Results](https://huggingface.co/docs/hub/eval-results)). But that verification proves an execution path, not independent assurance, social validity, legal compliance, or Charter alignment.

## Reusable contribution: a Charter Evidence Profile

A compact **Charter Evidence Profile** could extend existing Hub conventions without requiring Hugging Face to adopt the Charter. It should remain an open, provider-neutral specification that can also be stored outside the Hub.

The profile would bind:

- model, dataset, benchmark, and method revisions;
- inference provider, runtime, and material generation or retrieval settings;
- responsible operator and node or jurisdiction where appropriate;
- declared purpose, data class, retention, and prohibited-use baseline;
- evaluation result, source traces, and what was not logged or assessed;
- evaluator identity, independence, conflicts, and adjudication status;
- incident, correction, withdrawal, and appeal routes; and
- a signature or receipt plus an independent mirror for survivability.

Hugging Face model and dataset cards already provide valuable author-facing documentation and structured metadata ([Model Cards](https://huggingface.co/docs/hub/en/model-cards); [Dataset Cards](https://huggingface.co/docs/hub/main/datasets-cards)). The Charter profile should complement them rather than relabel self-documentation as assurance.

## Boundaries and risks

1. **Common platform does not mean neutral governor.** Hugging Face is a company-operated platform and proxy. Non-Team and non-Enterprise repositories are stored in the US; paid organisations can select an EU region ([Storage Regions](https://huggingface.co/docs/hub/main/storage-regions)). That is useful infrastructure, not the Charter's required institutional neutrality.
2. **Do not create a single point of dependency.** Exact repository revisions can be downloaded and cached locally ([Hub download guide](https://huggingface.co/docs/huggingface_hub/guides/download)). The network should mirror permitted artifacts and evidence across independent hosts and retain a provider-independent catalogue.
3. **A verified run is not an independently verified claim.** A reproducible benchmark execution may still use a weak task, omit relevant risks, or be submitted by an interested party. Charter reporting must keep `documented`, `implementation-checked`, `effectiveness-tested`, and `independently assessed` distinct.
4. **Cards are not proof of provenance or compliance.** Publisher-authored documentation is evidence to inspect, not a substitute for rights verification, audit, or redress.
5. **Commercial routing goals differ from public-interest routing.** Hugging Face supports provider selection for speed, price, or user preference. The Charter broker must additionally consider purpose, eligibility, jurisdiction, data sensitivity, quota, evidence duties, and accountability ([Inference Providers](https://huggingface.co/docs/inference-providers/en/index)).
6. **No affiliation claim.** Existing technical compatibility and the Public AI integration do not imply that Hugging Face endorses or participates in Our AI Charter.

## Engagement path

The initiative should bring a working artifact before proposing a broad partnership.

**First:** run the bounded deployment-evidence pilot through the existing PublicAI/Hugging Face path and publish the result openly.

**Then ask Hugging Face for three concrete forms of cooperation:**

1. review or allow-list the benchmark dataset and its result format;
2. discuss a portable provider/node/deployment evidence schema compatible with Hub cards and Community Evals; and
3. explore how independently submitted evidence can remain visible, contestable, and durable without becoming a misleading certification badge.

The relevant counterparts are the teams responsible for **Community Evals, Inference Providers, and ML & Society**. BigScience is a useful precedent for participatory and multilingual open research, including its ethical charter and data-provider/host work ([BigScience organisation](https://huggingface.co/bigscience); [ML & Society retrospective](https://huggingface.co/blog/yjernite/ml-society-at-3)). It is experience to learn from, not evidence of present institutional agreement.

## Recommendation

Treat Hugging Face as a **high-priority technical and community collaborator**, reached first through a concrete PublicAI/Apertus evaluation artifact. Do not ask it to own the Charter, operate the assurance authority, or hold the only registry. The partnership is strongest when Hugging Face supplies reach and interoperability while the Charter supplies public-interest governance and independently checkable evidence.
