# Evidence-Gated Agents

*Project overview and development direction. EGA is at an early stage; this page explains its goals and does not define implementation obligations.*

<a id="evidence-gated-agents-aspiration-and-test"></a>

Evidence-Gated Agents (EGA) aims to develop AI-assisted decision-making applications and reusable components that keep consequential answers and actions authorised, grounded in evidence, and open to inspection and challenge.

Consequential answers and actions include those affecting people’s rights, access to services or significant resources.

The goal is to help people and organisations make and justify decisions while retaining control over what AI may do and how errors can be corrected. This work serves a broader aim: a free and fair society in which technology supports democracy, justice and well-grounded decisions.

## Who it is for and what it could become

The intended users include people preparing or reviewing decisions, organisations responsible for AI-supported work, and developers integrating controls into their systems. People receiving or affected by the resulting answers and actions also need to understand their basis and have a route to question them.

Two possible development paths are being considered:

- **Applications and services** that organisations could use directly and configure for their needs and working environments.
- **Reusable architecture and components** that software providers or internal development teams could adapt and integrate into existing applications.

Both paths would need evidence of practical usefulness and suitability in their intended settings.

## What the project aims to make possible

The central rule is: **before AI gives a consequential answer or takes a consequential action, it must have permission and enough evidence to justify it.**

The intended approach connects five responsibilities:

1. **Establish authority and limits.** Accountable people define who may do what, for which purpose, using which data and tools. The basis of that authority must itself be reviewable.
2. **Use permitted information and examine the evidence.** Check both whether a source may be used and what it can establish. Make material claims, assumptions, supporting evidence, counterevidence and uncertainty visible. Assess whether that evidence is current and sufficient for the particular proposed use.
3. **Control what proceeds.** Checks outside the acting model govern whether the exact proposal may be released or executed. Before acting, the executing service requests a fresh verification of the approval and checks that the intended action matches it.
4. **Make the outcome inspectable.** Provide an accessible record connecting the answer or action, authority, evidence, decision and actual outcome, with access appropriate to the people involved.
5. **Support challenge and correction.** Let affected people question the basis, route disputes to responsible reviewers, and revisit decisions when evidence or authority changes.

The acting AI cannot authorise itself. Software can enforce recorded rules and decisions, while evidence adequacy and legitimate authority require accountable judgment. Human involvement should focus on decisions where a person can make a meaningful difference; an approval click cannot supply missing evidence.

As an illustrative future use, a procurement team might review an AI-generated supplier recommendation. A claim about guaranteed performance would need evidence addressing that guarantee; a generally positive report would not settle it. If that premise remained unsupported, the recommendation should be held or narrowed and checked again. The record should show the evidence, who authorised the next step and what actually happened.

## Foundations and the selected next step

EGA draws on three related pieces of work:

- **[FactHarbor Alpha](https://github.com/robertschaub/FactHarbor#what-is-factharbor)** assesses claims using supporting and opposing evidence and makes sources and uncertainty inspectable.
- **[Our AI Charter Runtime](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first)** is a separate, unfinished proof of concept for controls outside the acting model. Its demonstrations use simulated scenarios and a local test action.
- **[Our AI Charter](../Framework/charter-commitments.md)** provides the broader principles for accountable AI use, including authority, evidence, oversight and remedy.

**Selected next step:** build a bounded prototype in which a normal AI agent proposes a decision and FactHarbor examines whether current evidence sufficiently supports that exact decision for the user’s request. The gate then releases the checked decision or stops it. This integration is not yet implemented.

### View 1 — EGA target model: evidence and authority before release or action

**Purpose:** show the complete intended EGA pattern, not current end-to-end functionality. A separate evidence service — FactHarbor in the selected prototype — searches and analyses evidence and returns a verdict and report. The EGA gate then applies authority, disclosure and evidence rules; the evidence service does not decide release or execution.

```mermaid
flowchart TD
    SET["Accountable setup:<br/>mandate + disclosure,<br/>evidence and release rules"]
    U["Request + permitted<br/>relevant context"] --> A["Normal AI agent proposes<br/>an exact decision or action"]
    A --> PRE["Authorize + Submit:<br/>mandate and disclosure checks"]
    SET -. Governs checks .-> PRE
    PRE --> P{"Pass?"}
    P -->|No| N1["Stop + receipt"]
    P -->|Yes| Q["Verification request:<br/>request + permitted context<br/>+ exact proposal"]
    subgraph ES["Evidence service"]
        SEA["Evidence search<br/>and analysis"] --> VR["Evidence verdict + report:<br/>support, counterevidence,<br/>limits, uncertainty"]
    end
    Q --> SEA
    VR --> POST["Verify + Commit:<br/>evidence and binding checks"]
    POST --> D{"Pass?"}
    D -->|No / unclear / changed| N2["Stop + receipt"]
    D -->|Yes| O["Release decision or execute<br/>the authorised action"]
    O --> R["Record outcome<br/>and issue receipt"]
    R --> Y["Rely, inspect, challenge<br/>and correct"]
```

<a id="existing-runtime-foundation"></a>
<a id="view-1-existing-runtime-control-of-one-proposed-action"></a>
**Current foundation:** FactHarbor Alpha already performs evidence search and analysis and produces an inspectable verdict and report. Separately, the unfinished Runtime demonstrates gates and receipts outside the acting model using simulated scenarios and a local test action. It does not implement the complete View 1 path or call FactHarbor. See the [Runtime's documented limits](https://github.com/robertschaub/ai-charter-runtime#honest-limits--read-this-first).

<a id="selected-prototype-dynamic-decision-examination"></a>
### View 2 — Selected EGA prototype: FactHarbor check before decision release

**Purpose:** show the planned bounded integration in which FactHarbor performs evidence search and analysis, returns its verdict and report, and reusable Runtime controls decide whether the exact agent decision may be released. Unlike View 1, this path does not execute a resulting action.

The controlled evaluation selects requests expected to yield one clear, non-complex decision. Free requests remain available for exploration. A decision may contain related components, but the prototype does not test several independent decision and effect paths.

A preset trigger rule routes only a response containing a consequential decision or an instruction to act into the gate. An ordinary answer bypasses the gate and leaves a minimal routing record — trigger decision, rule version, request and response fingerprints, timestamp and attempt ID — without retaining the request or response content. This routing record is not a receipt. Making the trigger judgment itself evidence-based and reviewable is a later extension.

```mermaid
flowchart TD
    U["Request + permitted<br/>relevant context"] --> A["Normal AI agent proposes<br/>one exact response"]
    A --> T["Apply preset trigger rule"]
    T --> R{"Route?"}
    R -->|No| OA["Release ordinary answer<br/>+ minimal routing record"]
    R -->|Yes| PRE["Authorize + Submit:<br/>authority and disclosure checks"]
    PRE --> P{"Pass?"}
    P -->|No| N1["Stop receipt"]
    P -->|Yes| Q["Verification request:<br/>request + permitted context<br/>+ exact decision"]
    subgraph ES["Evidence service"]
        subgraph FH["FactHarbor"]
            F["Evidence search<br/>and analysis"] --> FR["Verdict + report:<br/>support, counterevidence,<br/>limits, uncertainty"]
        end
    end
    Q --> F
    FR --> V["Verify:<br/>apply the EGA evidence rule"]
    V --> D{"Pass?"}
    D -->|No / unclear / error| N2["Stop receipt"]
    D -->|Yes| C["Commit binds the exact<br/>checked decision and recipient"]
    C --> O["Release decision"]
    O --> RR["Release receipt"]
```

*Status on 19 September 2026: this integration is not implemented. The trigger fixtures and routing-record schema, FactHarbor API contract, release rule and Runtime compatibility are open preparation work; the homepage's [where the work stands](../../index.md#where-the-work-stands) carries the current status.*

FactHarbor does not need to reproduce the agent's wording and does not decide the EGA release. It supplies the evidence record; the gate applies the release rule. A pending FactHarbor job, contradiction, insufficient evidence, ambiguous output or technical error stops the attempt. Completion never causes an automatic later release: a retry is a new attempt through all checks.

**Why Commit?** The service rechecks the bound request, decision, recipient and evidence result immediately before release. A changed or narrower decision cannot reuse an earlier approval; it must start a new attempt through every check.

The gated path's real effect is releasing the checked decision. It does not execute a resulting action or check authority for that action. A later EGA would need a new authorization and evidence check at every autonomous action boundary.

**Known limit:** FactHarbor's decomposition is model-assisted and may miss a consequential component. The evaluation compares the complete decision with the components FactHarbor identified and reports omissions, language differences and selected repeat-run variation. A release is not proof that the decision is true or complete.

### What an inspectable receipt could show

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

## Longer-term development and open research

Later work could extend the same approach to permitted organisational sources and further agent, tool and action workflows. Each extension would need suitable authority, privacy controls, evidence requirements and evaluation. Effective independent review and remedy would also require institutions with the power to act.

One research strand asks whether AI can identify adequate evidence requirements for unfamiliar questions, discover overlooked assumptions and have those requirements critically reviewed, without people writing a separate checklist for every question. This could broaden reuse; its reliability remains to be demonstrated.

Success means useful, supported answers and actions with fewer unjustified releases, understandable records and workable correction routes. Testing must also expose unnecessary blocking, missed claims, cost and practical limitations. Enforcing a gate does not establish that an answer is true, and agreement between AI reviewers does not establish that their judgment is adequate.

## Research detail

- <a id="aspiration-mostly-generic-evidence-gated-agents"></a> [AI-derived evidence requirements](evidence-requirements-research.md#aspiration-mostly-generic-evidence-gated-agents)
- <a id="test-of-the-aspiration"></a> [Research questions and evaluation](evidence-requirements-research.md#test-of-the-aspiration)
- <a id="path-from-the-prototype-to-wider-use"></a> [Prototype-to-research coverage](evidence-requirements-research.md#path-from-the-prototype-to-wider-use)
