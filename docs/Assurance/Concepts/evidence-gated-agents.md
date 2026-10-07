# Evidence-Gated Agents

<a id="project-overview"></a>
<a id="evidence-gated-agents-aspiration-and-test"></a>

**Before we rely on an AI recommendation, does the evidence justify it—for this purpose?**

[Read the short introduction](../../Published/evidence-gated-agents-before-we-rely.md), or explore the foundations, next milestone and design below.

An AI assistant recommends a supplier, citing satisfied customers and strong average performance. Neither establishes the contractual response-time guarantee your organisation needs. A useful answer identifies that gap; a consequential recommendation should not pass simply because it sounds convincing.

**Evidence-Gated Agents (EGA) connects active evidence examination with controls outside the acting AI.** The design searches for supporting and contradicting evidence, checks authority and governs release of consequential AI output: a claim, decision or action instruction. The broader aim includes authorised actions, inspectable records and routes to challenge and correct decisions.

## Foundations and the selected next step

| What exists | What it contributes |
|---|---|
| **[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor)** | Searches and analyses supporting and opposing evidence, with sources and uncertainty visible. It remains an [invite-gated Alpha with documented quality limitations](https://github.com/robertschaub/FactHarbor/blob/main/CONTRIBUTING.md#known-limits). |
| **[Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first)** | A runnable proof of concept demonstrates controls outside the acting model, using synthetic scenarios and local test effects. It does not yet call FactHarbor. |
| **[Our AI Charter](../Framework/charter-commitments.md)** | The principles connecting authority, evidence, privacy, independent oversight and remedy. |

**The next milestone is to integrate and evaluate these foundations in one bounded recommendation workflow.** EGA analyses the exact proposed decision using retrieved material; separate controls apply human-defined evidence rules and check permission to release it. FactHarbor provides existing retrieval and analytical capabilities for this integration. This integration remains to be built. Releasing a recommendation does not authorise or execute the resulting action.

The selected prototype routes consequential decisions and instructions into evidence examination. Ordinary answers retain authority and disclosure checks and a minimal routing record, without full consequential-output evidence examination or an EGA receipt. Automatically deriving adequate evidence requirements for unfamiliar decisions is [wider research](evidence-requirements-research.md), not an established capability of this first integration.

**The cooperation opportunity:** bring a workflow, contribute engineering or evaluation expertise, or support the integration and its assessment. [See the milestone and how to contribute](#where-to-contribute).

[![Wider EGA design: Working AI plans and prepares within existing permission. Repeated EGA checks govern each protected transition using its applicable requirements. Both illustrated checks can request evidence, including evidence of permission and authority. Proceed remains within checked scope; Do not proceed records the reason and next permitted route, with human judgement where needed. Records, data protection and five oversight roles support accountability.](evidence-gated-agents-release-workflow.png)](evidence-gated-agents-release-workflow.png)

*Wider EGA design. The same EGA check pattern recurs for new inputs, processors, recipients and effects. Working AI plans and prepares within existing permission before the first illustrated check. Every check may request evidence, including evidence of permission and authority. Proceed and Do not proceed describe the gate decision; the reason determines the permitted next route, without automatically reopening a stopped attempt. Human judgement is requested where needed, within the person’s authority. [Lifecycle governance](../../Published/when-should-runtime-ai-governance-interrupt.md#the-when-has-two-clocks) surrounds this path. The first integration remains recommendation release only; integration, confidential-source handling and wider governance remain to be implemented and evaluated.*

## How the design works

[![Output-release instance of the EGA check: a retrieval-only evidence service is available to every check, including authority and permission checks. EGA analyses the claim, decision or action instruction and applies evidence, authority and disclosure requirements. The decision branches are Proceed within checked scope or Do not proceed with a reason, next permitted route and human judgement where needed. Decision-record access is restricted and data protection applies throughout the system.](../../Published/evidence-gated-agents-before-we-rely.png)](../../Published/evidence-gated-agents-before-we-rely.png)

*The output-release design. The first integration targets consequential recommendations and instructions, without executing resulting actions. Integration and confidential-source handling remain to be built.*

The output being gated is a **claim, decision or action instruction**. Releasing an instruction makes it available to an authorised recipient; it does not authorise or execute the resulting action. The first prototype retains the consequential-decision/instruction trigger described above.

The design repeats an **EGA check** outside the acting AI whenever a proposed step crosses a relevant boundary: **may this step proceed under its applicable requirements?** Trusted rules select the checks for that transition, such as authority, input integrity, evidence adequacy and data protection. Before-use and before-release/action checks are instances of this pattern, not the only two points at which it runs. This preserves the [operational gates](user-workflow-governance.md#five-steps) and their distinct responsibilities; the acting AI cannot select an easier check or authorise itself.

Any EGA check may request evidence through the evidence service, including material establishing permission, authority or delegation. Retrieval itself requires an already-permitted access and processing route; it cannot retroactively authorise its own disclosure. The service returns found material with sources and search coverage; EGA assesses what it establishes, including validity, support, contradiction and gaps. Its analytical verdict and reasons inform the applicable gate controls. Evidence supporting a recommendation and evidence establishing authority answer different questions; neither substitutes for the other. If the supplier guarantee is unsupported, the recommendation does not proceed. A qualified alternative needs its own check.

The evidence-service interface can have a general public-source implementation and specialised implementations for company/private sources. Query-relevance ranking and faithful extraction are permitted, with traceable sources and visible selection limits; the service does not judge support or contradiction. Permission to retrieve remains distinct from permission to send material to a retrieval, extraction or analysis processor and to disclose it to a recipient.

Routine checks run automatically within agreed limits. Human judgment is called for when the stakes justify interruption, someone with the necessary authority can make a difference, and the issue cannot be resolved within existing authority. The request identifies the unresolved decision. Human approval cannot replace missing evidence or authority, or reopen a stopped attempt.

<a id="protecting-evidence-and-accountability"></a>

### Data protection and accountability

Data protection applies throughout the system, including every outgoing request, search result, released output and record view. Permission to consult a confidential record does not automatically permit sending it to an external AI service or revealing it in an answer. **Access, processing and disclosure are separate permissions.** The [privacy commitments](../Framework/charter-commitments.md) call for using only the information needed for the permitted purpose. Decision records also need limited content, access and retention; accountability must not become an unrestricted copy of confidential evidence.

The [governance design](../../Published/when-vs-who-ai-governance.md) separates rulemaking, operation, record custody, independent review and remedy, so the operator does not control the whole chain. These are continuing responsibilities, not five approvals for every answer. A custodian preserves a sealed record without unilateral access; binding remedies require legal or contractual authority. Records support scrutiny, but do not themselves establish truth, legitimate authority or effective remedy.

## The next development milestone

**Does the combined approach reduce unsupported recommendations while retaining useful answers?** A bounded integration and evaluation would deliver:

- A working path demonstrating when a consequential recommendation is released or stopped.
- An assessment of unsupported releases, unnecessary stops, useful qualified answers, missed decision components, cost and delay.
- Evidence for deciding whether to continue, revise or stop that line of work.

The cooperation agreement would define the workflow, comparison, acceptance criteria and how successes and failures are reported, with confidentiality and publication arrangements suited to the cooperation. Those arrangements do not replace the wider research's [evaluation commitments](evidence-requirements-research.md#evaluation-commitments), including a published protocol before held-out testing and preservation of failed attempts.

## Where to contribute

Workflow owners and domain specialists can define a useful recommendation and the evidence it needs. Engineers can connect the foundations. Researchers can shape and critically assess the evaluation. Funding enables focused development and assessment of this milestone.

**Start with a brief workflow description or your area of contribution.** Contact [Robert Schaub on LinkedIn](https://www.linkedin.com/in/robertschaub/) or [info@factharbor.ch](mailto:info@factharbor.ch). A first conversation can use synthetic examples; no confidential records are needed. Work with private organisational evidence requires separately agreed access, handling and evaluation.

The work is stewarded by the FactHarbor association under its public [funding and independence commitments](../../About.md#stewardship-and-governance). Its purpose is to help people and organisations make and justify decisions while retaining control over AI and correcting errors: technology serving a free and fair society, democracy and justice.

## Who it is for and what it could become

The intended users include people preparing or reviewing decisions, organisations responsible for AI-supported work, and developers integrating controls into their systems. People receiving or affected by the resulting answers and actions also need to understand their basis and have a route to question them.

Two possible development paths are being considered:

- **Applications and services** that organisations could use directly and configure for their needs and working environments.
- **Reusable architecture and components** that software providers or internal development teams could adapt and integrate into existing applications.

Both paths would need evidence of practical usefulness and suitability in their intended settings.

## What the project aims to make possible

### Design responsibilities and consequential content in summaries

The central rule is: **before AI gives a consequential answer or takes a consequential action, it must have permission and enough evidence to justify it.**

The intended approach connects five responsibilities:

1. **Establish and verify authority.** Accountable people define and document who may authorise what, on which basis and through which delegation. Examine evidence that the issuer has the relevant authority and that the mandate covers the exact proposal, purpose, data, tools and limits. Check whether permission has expired, changed or been revoked. The authority basis itself must remain reviewable.
2. **Use permitted information and examine the evidence.** Check both whether a source may be used and what it can establish. Make material claims, assumptions, supporting evidence, counterevidence and uncertainty visible. Assess whether that evidence is current and sufficient for the particular proposed use.
3. **Control what proceeds.** Checks outside the acting model govern whether the exact proposal may be released or executed. Before acting, the executing service requests a fresh verification of the approval and checks that the intended action matches it.
4. **Make the outcome inspectable.** Provide an accessible record connecting the answer or action, authority, evidence, decision and actual outcome, with access appropriate to the people involved.
5. **Support challenge and correction.** Let affected people question the basis, route disputes to responsible reviewers, and revisit decisions when evidence or authority changes.

Authority checks are evidence checks too. Evidence supporting a proposal and evidence establishing permission to release or execute it answer different questions; neither can substitute for the other. The acting AI cannot authorise itself. Software can enforce recorded rules and decisions, while evidence adequacy and legitimate authority require accountable judgment. Human involvement should focus on decisions where a person can make a meaningful difference; an approval click cannot supply missing evidence.

Consequential decisions and instructions can also appear inside summaries or other apparently descriptive outputs. The intended checks would examine whether an output preserves the source’s meaning, including conditions, material risks, dissent and unresolved questions. A recommendation must not silently become an approved decision, or a forecast an established fact.

Faithfulness to a source and support for its factual claims require separate examination. Accurately reporting what someone stated or agreed does not establish that the underlying claims are true. Permission to release the report also does not establish authority for the decision it describes. Where essential judgment or approval is missing, a request for human review should identify the specific unresolved issue.

### View 1 — EGA target model: evidence and authority before release or action

<details markdown="1">
<summary>Open the wider design flow and current foundation</summary>

**Purpose:** show a consequential output/action path within the wider EGA design, not every possible route or current end-to-end functionality. Applicable requirements determine whether full output examination is needed; View 2 also shows ordinary routing. The drawn retrieval connection illustrates output examination; every check may request permitted material, including authority evidence. The overview uses Proceed / Do not proceed; this technical flow retains stage-specific stops, commitment states and uncertain outcomes. The evidence service retrieves material through a defined interface. EGA analysis interprets support, contradiction, uncertainty and gaps and produces the analytical verdict/report. Release controls apply evidence, authority and disclosure rules. FactHarbor offers existing retrieval and analysis capabilities; their integration behind these logical boundaries remains to be specified and implemented.

<div class="ega-flow" role="region" aria-label="Detailed EGA control flow" tabindex="0" markdown="1">

```mermaid
%%{init: {"flowchart": {"curve": "linear", "nodeSpacing": 50, "rankSpacing": 55, "padding": 12, "wrappingWidth": 285}, "htmlLabels": false}}%%
flowchart TD
    U(["Request + permitted context"]) --> P["Working AI plans and prepares<br/>Within existing permission"]
    P --> IN{{"EGA check · next step + inputs<br/>Authority + input checks<br/>Permitted processing?"}}
    IN -->|Yes| A["Working AI carries out permitted work<br/>and proposes output or action<br/>Withheld pending checks"]
    IN -->|No / unresolved| S1["Stop before proposed use<br/>Scoped record"]
    A --> PRE{{"EGA check · admission + examination:<br/>current authority and processor permissions?"}}
    PRE -->|Yes| EA["EGA analysis<br/>Support, contradiction and gaps"]
    PRE -->|No / unresolved| S2["Stop + scoped record"]
    EA <-->|Permitted requests / found material| ES["Evidence service · retrieval only<br/>Available to every EGA check<br/>Sources and search coverage"]
    EA -->|Submission acceptance unknown| JX["Stop; reconcile examination job<br/>No speculative resubmission"]
    EA -->|Assessment / evaluation deadline| G{{"EGA check · release / action rule satisfied?<br/>Evidence + authority + disclosure"}}
    G -->|Yes| C{{"Fresh verification + commitment<br/>Exact effect and recipient bound?"}}
    G -->|No / unresolved| S3["Do not proceed<br/>Reason recorded; revised content rechecked"]
    C -->|Not bound| S4["Stop before effect"]
    C -->|Bound| E["Executor validates one-use binding<br/>Release output OR perform authorised action"]
    C -->|Binding uncertain| BX["Binding uncertain<br/>Record; reconcile; no blind retry"]
    E -->|Outcome established| O["Record actual outcome<br/>Success, no effect or known failure"]
    E -->|Outcome uncertain| X["Record uncertainty<br/>Reconcile; no blind retry"]
    O --> R(["Inspect · Challenge · Correct<br/>Review ongoing reliance"])
    X -.-> R
    BX -.-> R
    classDef process fill:#f0f5fc,stroke:#7895ba,color:#17344c,stroke-width:1.5px
    classDef control fill:#fff4d9,stroke:#bf8a32,color:#573b14,stroke-width:1.5px
    classDef evidence fill:#e6f5f2,stroke:#459389,color:#154e48,stroke-width:1.5px
    classDef stop fill:#fff0eb,stroke:#c67b65,color:#803e2c,stroke-width:1.5px
    classDef result fill:#eaf4e5,stroke:#739266,color:#31572e,stroke-width:1.5px
    classDef uncertain fill:#f4effa,stroke:#9a81b5,color:#5d427b,stroke-width:1.5px
    class U,P,A,E process
    class IN,PRE,G,C control
    class EA,ES evidence
    class S1,S2,S3,S4,JX stop
    class O,R result
    class X,BX uncertain
```

</div>

Every stop has a scoped reason and inspection route. Human judgement is conditional at any stage where an authorised person can resolve a specific issue; it neither bypasses missing evidence or authority nor reopens a stopped attempt. Uncertain job acceptance, commitment and effects require their own reconciliation.

<a id="existing-runtime-foundation"></a>
<a id="view-1-existing-runtime-control-of-one-proposed-action"></a>
**Current foundation:** FactHarbor Alpha already performs evidence search and analysis and produces an inspectable verdict and report. Separately, the unfinished Runtime demonstrates gates and receipts outside the acting model using simulated scenarios and a local test action. It does not implement the complete View 1 path or call FactHarbor. See the [Runtime's documented limits](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first).

</details>

<a id="selected-prototype-dynamic-decision-examination"></a>
### View 2 — Selected EGA prototype: FactHarbor check before decision release

**Scope and limits:** one clear decision, human-defined evidence rules, recommendation release only. The integration is unimplemented. Model-assisted evidence analysis may miss consequential components; release is not proof of truth or completeness.

<details markdown="1">
<summary>Open the selected prototype flow and release rules</summary>

**Purpose:** show the planned bounded integration: EGA analysis examines an exact proposed decision using retrieved material, then reusable Runtime controls apply the evidence rule and check release permission. FactHarbor is a foundation for retrieval and analysis, but its complete analysis API is not the retrieval-only service. Component separation or a transitional analytical adapter remains an implementation investigation. Unlike View 1, this path does not execute a resulting action.

This prototype flow starts at admission to a new acting-model call. Earlier Working AI planning, shown in View 1, must already be permitted; it does not bypass the checks for new inputs or processing. Authority uses synthetic mandates here; broader evidence retrieval for authority checks is not an additional prototype prerequisite.

The controlled evaluation selects requests expected to yield one clear, non-complex decision. Free requests remain available for exploration. A decision may contain related components, but the prototype does not test several independent decision and effect paths.

A preset trigger rule selects full consequential-output evidence examination for a response containing a consequential decision or an instruction to act. An ordinary answer retains authority and disclosure checks, bypasses consequential-output evidence examination and leaves a minimal routing record — trigger decision, rule version, request and response fingerprints, timestamp and attempt ID — without retaining the request or response content. This routing record is not a receipt. Making the trigger judgment itself evidence-based and reviewable is a later extension.

<div class="ega-flow" role="region" aria-label="Detailed EGA control flow" tabindex="0" markdown="1">

```mermaid
%%{init: {"flowchart": {"curve": "linear", "nodeSpacing": 50, "rankSpacing": 55, "padding": 12, "wrappingWidth": 285}, "htmlLabels": false}}%%
flowchart TD
    U(["Request + permitted context"]) --> IN{{"EGA check · before model use<br/>Purpose, provider and data permitted?"}}
    IN -->|Yes| A["Working AI plans, prepares<br/>and proposes exact response<br/>Withheld from recipient"]
    IN -->|No / unresolved| S1["Stop before disclosure<br/>Scoped record"]
    A --> AD{{"EGA check · output admission<br/>Approval still current?"}}
    AD -->|No / unresolved| S2["Stop + scoped explanation<br/>Revised request starts a new attempt"]
    AD -->|Yes| T{{"Trusted preset routing"}}
    T -->|Ambiguous| S2
    T -->|Ordinary| OC{{"EGA check · ordinary delivery<br/>Current authority + disclosure pass?"}}
    OC -->|Yes| O["Ordinary answer + routing record"]
    OC -->|No / unresolved| S2
    T -->|Consequential decision / instruction| PRE{{"EGA check · examination permission<br/>Authority + processor permissions<br/>Examination permitted?"}}
    PRE -->|Yes| EA["EGA analysis · one examination<br/>Approved checklist + exact decision<br/>Assess each requirement; find gaps"]
    PRE -->|No / unresolved| S3["Stop + scoped record"]
    EA <-->|Permitted requests / found material| ES["Evidence service · retrieval only<br/>Sources and search coverage"]
    EA -->|Submission acceptance unknown| JX["Stop; reconcile examination job<br/>No speculative resubmission"]
    EA -->|Assessment / evaluation deadline| V{{"EGA check · evidence rule<br/>Complete, bound assessment<br/>Evidence rule satisfied?"}}
    V -->|Yes| C{{"Fresh verification + commitment<br/>Exact release bound?"}}
    V -->|No / pending / error| S4["Stop this attempt<br/>Late results cannot revive it"]
    C -->|Not bound| S5["Stop before release"]
    C -->|Bound| E["Validate one-use binding<br/>Attempt exact recipient-view release"]
    C -->|Binding uncertain| BX["Binding uncertain<br/>Record; reconcile; no blind retry"]
    E -->|Outcome established| R["Record release, no effect<br/>or known failure"]
    E -->|Outcome uncertain| X["Record uncertainty<br/>Reconcile; no blind resend"]
    R --> I(["Restricted receipt<br/>Inspect · Challenge · Correct"])
    X -.-> I
    BX -.-> I
    classDef process fill:#f0f5fc,stroke:#7895ba,color:#17344c,stroke-width:1.5px
    classDef control fill:#fff4d9,stroke:#bf8a32,color:#573b14,stroke-width:1.5px
    classDef evidence fill:#e6f5f2,stroke:#459389,color:#154e48,stroke-width:1.5px
    classDef stop fill:#fff0eb,stroke:#c67b65,color:#803e2c,stroke-width:1.5px
    classDef result fill:#eaf4e5,stroke:#739266,color:#31572e,stroke-width:1.5px
    classDef uncertain fill:#f4effa,stroke:#9a81b5,color:#5d427b,stroke-width:1.5px
    class U,A,O,E process
    class IN,AD,T,OC,PRE,V,C control
    class EA,ES evidence
    class S1,S2,S3,S4,S5,JX stop
    class R,I result
    class X,BX uncertain
```

</div>

All stop branches retain the same scoped explanation and inspection route described in View 1. Human judgement is conditional, and revised proposals start a new attempt; no stop automatically becomes a human approval request.

*Selected design, not an implemented integration. Semantic responsibilities are defined; exact trigger fixtures, interface schemas, evidence criteria, timing and Runtime compatibility remain preparation work. See [where the work stands](../../index.md#where-the-work-stands).*

If only a temporary gate ruling expires during analysis, fresh verification may occur within the same still-open attempt under unchanged, valid authority and bindings. This never extends a deadline, renews an expired mandate or revives a stopped attempt. No protected step may rely on the expired ruling; exact timing and compatibility remain to be specified.

EGA analysis does not need to reproduce the agent's wording and does not authorise release. A predefined EGA evidence rule evaluates its bound verdict and component assessments through an explicitly reviewed mapping. The controls infer no new semantic conclusion; missing or uninterpretable required fields stop release. A pass proceeds to Commit; a pending job, material unresolved contradiction, insufficient evidence, ambiguous output or technical error stops the attempt. Counterevidence can coexist with a supported, already qualified exact decision when its significance is addressed under the rule; a report caveat cannot repair an unsupported assertion. Passing this rule does not replace authority or disclosure checks, establish the legitimacy of the mandate, or authorise a resulting action. Completion never causes an automatic later release: a retry is a new attempt through all checks.

**Why Commit?** The service rechecks the bound request, decision, recipient and evidence result immediately before release. A changed or narrower decision cannot reuse an earlier approval; it must start a new attempt through every check.

The gated path's real effect is releasing the checked decision. It does not execute a resulting action or check authority for that action. Each later action needs fresh verification of its applicable authority and evidence; an existing mandate may cover it without another human approval.

**Known limit:** FactHarbor's decomposition is model-assisted and may miss a consequential component. The evaluation compares the complete decision with the components FactHarbor identified and reports omissions, language differences and selected repeat-run variation. A release is not proof that the decision is true or complete.

</details>

### What an inspectable receipt could show

<details markdown="1">
<summary>Open fictional receipt examples</summary>

![An illustrative record links proposal, evidence, authority and outcome, with inspection, challenge and correction.](evidence-gated-agents-inspectable-record.png)

**Fictional, shortened display examples, not generated receipts.** All identifiers, times and outcomes below are invented. These examples illustrate visible outcomes; they are not a complete receipt schema.

**Example 01, attempt 1: decision released**

| Visible item | Example |
|---|---|
| Decision and authority | “Method A is recommended for the described test; this does not apply to other conditions.” Demo mandate M1 permits release to the test recipient. |
| Evidence examination | FactHarbor job FH-1 found supporting evidence and a limitation on transfer to other conditions; sources and uncertainty are visible. |
| Checks | Authority, disclosure and the simple evidence rule pass at 10:15. Commit binds the exact decision and recipient. |
| Release | The checked decision was released to the specified recipient and the outcome was recorded. |
| Inspect or challenge | Inspect the request, decision fingerprint, evidence result, gate decisions and recorded outcome. A linked view shows how to question it. |

**Example 02, attempt 1: evidence still pending**

| Visible item | Example |
|---|---|
| Decision | Verify stops release at 10:15. |
| Reason | FactHarbor job FH-2 has not reached a terminal result (`evidence-pending`). |
| Effect | No decision was released. A later FactHarbor result does not trigger automatic release. |
| Inspect | The receipt links the request, exact decision, job state and stop reason. A new attempt must pass every check again. |

Links and fingerprints support checking the bound versions and recorded steps. They do not prove the answer true, the authority legitimate, the oversight independent or the answer read by its recipient. Complete independent review and remedy require more than a receipt.

</details>

## Longer-term development and open research

Later work could extend the same approach to permitted organisational sources and further agent, tool and action workflows. Each extension would need suitable authority, privacy controls, evidence requirements and evaluation. Checking private records and organisational evidence would require authorised access and additional checking processes, still to be defined and tested. Effective independent review and remedy would also require institutions with the power to act.

One research strand asks whether AI can identify adequate evidence requirements for unfamiliar questions, discover overlooked assumptions and have those requirements critically reviewed, without people writing a separate checklist for every question. This could broaden reuse; its reliability remains to be demonstrated.

Success means useful, supported answers and actions with fewer unjustified releases, understandable records and workable correction routes. Testing must also expose unnecessary blocking, missed claims, cost and practical limitations. Enforcing a gate does not establish that an answer is true, and agreement between AI reviewers does not establish that their judgment is adequate.

## Research detail

- <a id="aspiration-mostly-generic-evidence-gated-agents"></a> [AI-derived evidence requirements](evidence-requirements-research.md#aspiration-mostly-generic-evidence-gated-agents)
- <a id="test-of-the-aspiration"></a> [Research questions and evaluation](evidence-requirements-research.md#test-of-the-aspiration)
- <a id="path-from-the-prototype-to-wider-use"></a> [What the first prototype can tell us](evidence-requirements-research.md#path-from-the-prototype-to-wider-use)

For related context: [when runtime governance should interrupt](../../Published/when-should-runtime-ai-governance-interrupt.md), [who provides independent oversight](../../Published/when-vs-who-ai-governance.md), and [what the runtime layer adds](../Background/what-the-runtime-layer-adds.md).
