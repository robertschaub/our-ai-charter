> **Status: DRAFT** — draft scan; re-verify before citing.

# Is the initiative obsolete, or should it join something? — landscape investigation

_Draft scan, 2026-06-14; key claims re-checked on the web 2026-06-25. For public discussion — not a sourced market report or an adopted position. Maturity scores and fast-moving third-party statuses still need direct source verification before citation._

**The wedge under test:** an *independent, audited, revocable* trust mark / evaluation for AI **information integrity** — does a deployed AI *show its work* (claims supported by the sources it cited = grounding-faithfulness, NOT "truth"; calibration; error-correction) — plus **contestability** (documented, challengeable power to restrict/recall/shut down) — run via separation of powers, hosted in existing bodies.

---

## Verdict in one line

**NOT obsolete. The wedge is genuinely OPEN — but do NOT build a new silo. Federate it: author the standard, host execution inside bodies that already run the machinery.** All six analyses agreed on both halves, and a mid-2026 web re-check confirms it: the 2026 wave of AI trust marks (ISO/IEC 42001 — now issued by the Big 4 — Nemko, TrustArc, aicerts) is governance and management-system assurance; none certifies that a deployed system's claims are supported by the sources it cited.

## Why it's not obsolete: nobody owns the *combined* proposition

The space is crowded with *adjacent* maturity, but the specific claim — *"this deployed AI's factual statements are supported by its cited sources; its uncertainty and corrections are auditable; certified by an independent assessor under a revocable, public-interest scheme"* — is unclaimed. Every mature player owns a neighbouring piece:

| Who | Maturity | Owns | Covers the wedge? |
|---|---|---|---|
| **ISO/IEC 42001** (BSI/SGS/TÜV/Schellman issuing certs) | 3 | AI *management-system* certification | No — process/governance, not output honesty |
| IEEE CertifAIEd · TÜV · Fraunhofer AIC4 | 2 | AI *ethics/process* properties (transparency, bias, privacy) | No |
| **Nemko AI Trust Mark · TrustArc Responsible AI Cert** | 2 | Real *independent, revocable* AI trust marks | No — **explicitly exclude** accuracy/grounding (proves the *form* works, confirms the *dimension* is empty) |
| Responsible AI Institute (RAISE) | 1–2 | Governance badges + registry | No |
| AI Verify Foundation (Singapore) · MLCommons AILuminate | 2 | GenAI *testing toolkits* / *safety-hazard* benchmarks | Partly (testing), not a faithfulness mark |
| **Vectara HHEM · Patronus Lynx · Galileo · RAGAS · DeepMind SAFE · HELM · ALCE · FActScore** | 2–3 | Grounding/faithfulness *measurement* | **Tools/benchmarks only** — vendor-internal or academic; never an independent attestation about a deployed system |
| **NewsGuard AI False-Claims Monitor** | 3 | *Independent* audits of AI *misinformation rates* | No — measures truth/falsity rate, proprietary, **issues no cert**; closest independent player |
| RSF / **Journalism Trust Initiative** | 3 | Audited, **revocable**, CEN-standardised trust mark — for *newsrooms* | No (yet) — the exact machinery, pointed at publishers not AI |
| IFCN · EFCSN | 2–3 | Codes for *human fact-checkers* | No — EFCSN now *funding* AI-model investigations (watch) |
| AI Alliance T&S · Public AI Network · Current AI · DPGA · Mozilla · LF AI · PAI · CoSAI | 2–3 | Open eval stacks, funding, coalitions | No honesty mark; several are ideal **hosts** |

**Two findings de-risk the idea:** (1) Nemko and TrustArc prove an *independent, revocable AI trust mark* is a viable business form — and both deliberately omit factual-grounding, confirming the dimension is unoccupied. (2) The grounding-*measurement* tech (HHEM, Lynx, SAFE, RAGAS) is commoditised → adopt it as substrate; **the moat is the conformity-scheme layer (independence + revocability + published methodology), not the detector.**

## Why not to build a silo (the other unanimous half)

Standing up an accreditation body — assessor training, recognition, registry, surveillance — takes a decade and tens of millions; a solo founder at 70% time would drown in overhead. **And there's a cautionary data point:** the **Digital Trust Label** (Swiss Digital Initiative) — a neutral-body Swiss trust label — was transferred to the commercial certifier SGS at Davos in January 2025, moving from a foundation-incubated concept to a vendor-run standard rather than sustaining as an independent foundation scheme. A Swiss solo founder should weigh how hard an independent, foundation-run label is to sustain.

## Where to JOIN — the "author the standard, federate execution" playbook

No single "join X and stop" target exists (nobody occupies the wedge), so the move is to assemble a federation around an authored standard. The roles, with the strongest candidate for each:

1. **Standard + mark machinery → RSF / Journalism Trust Initiative.** *The single highest-leverage move.* JTI already runs an independent, third-party-**audited, revocable, CEN-standardised** certification (130 criteria, Bureau Veritas auditors, 2,000+ outlets). The founder doesn't invent the trust-mark machinery — he proposes an **"AI Information Integrity" annex/module to the JTI standard**, bringing the source-fidelity/calibration/correction method as the technical core. (IFCN/EFCSN as standard-setter legitimacy + EU hedge.)
2. **Open venue to incubate now → AI Alliance Trust & Safety working group.** Open, no-invitation individual contributor path; already has the evaluation reference-stack that *needs* exactly this layer; a 501(c)(3) home. First move: join the WG, table the protocol as a project in `trust-safety-evals`.
3. **Measurement substrate → existing tools + Public AI Network's AI Evaluator Forum / MLCommons.** Don't reinvent detection; adopt HHEM/Lynx/RAGAS/SAFE and borrow evaluator credibility (METR/RAND-class) from the Evaluator Forum's "minimal standards for independent evaluation."
4. **Funding → Current AI** (its **Accountability** pillar — public-interest auditing and oversight — is the closest fit anywhere) — treat as funder, not home.
5. **Accreditation mechanics, later → ISO/IEC 17065 logic + AI Verify Foundation / RAII** once a pilot exists.
6. **Position relative to ISO 42001:** *complement layered inside/on top of it*, never against it — 42001 is becoming the default "AI trust cert" buyers ask for; the wedge must ride it, or be commoditised by it.

**Steward the canonical version and any mark; federate the execution.** The document text remains open under CC BY 4.0. What needs stewardship is the canonical standard process, version history, criteria governance, and any reserved name or trust mark — not exclusive control over the public text.

## Obsolescence watch list (monitor; none has done it yet)

1. **NewsGuard** — the #1 watch: it could formalise its at-scale AI-falsehood monitoring into a "model honesty" mark first, and in June 2026 it launched *NewsGuard AI* (a chatbot answering only from its rated sources) — a step deeper into AI output, though still a product, not a certification of others' systems. Counter: it stays proprietary and measures falsity-rate, not source-fidelity — position the Charter as the *open, auditable standard* its benchmarks could certify against.
2. **EFCSN** — its 2026 "Tech Accountability Call" funds members investigating platforms and "widely used AI models," and EFCSN won a separate €5M EU "FACTEUR" grant (2026) for European fact-checking; either could grow into the wedge. Engage early (doubles as early warning).
3. **MLCommons / AI Verify** — could standardise a faithfulness benchmark a notified body then certifies against.
4. **Nemko / TrustArc** — could add an accuracy/grounding module to an existing AI mark.
5. **ISO/IEC 42001** — positional, not substantive: risk that buyers treat it as "the" AI trust cert and dismiss a faithfulness mark as redundant. Counter by framing as a complement inside it.

---

_Sources named for follow-up verification (selected): ISO/IEC 42001 cert ecosystem (BSI/SGS/TÜV/Schellman); IEEE CertifAIEd; Nemko AI Trust Mark (digital.nemko.com/ai-trust-mark); TrustArc Responsible AI Cert; Responsible AI Institute (RAISE); AI Verify Foundation / Project Moonshot (IMDA); MLCommons AILuminate; Vectara HHEM + hallucination leaderboard; Patronus Lynx; Galileo; RAGAS; DeepMind SAFE/LongFact; Stanford HELM; ALCE; FActScore; NewsGuard AI False-Claims Monitor; AI Alliance Trust & Safety (thealliance.ai); Public AI Network AI Evaluator Forum; Current AI; DPGA; Mozilla; LF AI & Data; Partnership on AI; CoSAI; IFCN (Poynter); EFCSN (+ FACTEUR grant); RSF/JTI (CEN CWA 17493, Bureau Veritas, 2,000+ outlets); The Trust Project; Credibility Coalition/W3C; C2PA; Swiss Digital Trust Label (transferred to SGS, Jan 2025). This scan is not a substitute for direct source review._

_Re-checked on the web 2026-06-25: the independent grounding-faithfulness certification wedge remains **unoccupied**; NewsGuard launched its sources-grounded *NewsGuard AI* chatbot (June 2026); EFCSN's Tech Accountability Call and the €5M FACTEUR fund are active; Current AI's **Accountability** pillar funds public-interest auditing; ISO/IEC 42001 certification is now offered by the Big 4. Sources: [NewsGuard AI (CNN, 22 Jun 2026)](https://www.cnn.com/2026/06/22/media/newsguard-ai-chatbot-news-atlantic-publisher) · [EFCSN Tech Accountability Call](https://efcsn.com/funding-opportunities/tech-accountability-call/) · [EC €5M fact-checking grant](https://digital-strategy.ec.europa.eu/en/news/commission-boosts-independent-fact-checking-eu5-million-grant-under-european-democracy-shield) · [Current AI](https://www.currentai.org/)._
