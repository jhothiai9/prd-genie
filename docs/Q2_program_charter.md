# Q2: Program Charter - PRD Genie

**Sponsor:** Head of Product, NeuronForge Technologies · **Program lead:** Sivanantha Jhothi (AI PM/TPM, Product and Innovation) · **Status:** Draft

## 1. Vision
Every product conversation becomes a consistent, traceable PRD and backlog within minutes. Nothing goes in that the stakeholders did not say, and nothing they said gets lost.

## 2. Objectives
1. Cut the time from meeting to first PRD draft from hours to under 15 minutes of PM review.
2. Standardise every PRD on the company template, so engineering can estimate from a common structure.
3. Make every requirement traceable to a source quote, with 100% groundedness on the evaluation set.
4. Surface ambiguities, conflicts and dependencies as explicit open questions before sprint planning.

## 3. Scope
**In scope (v1):** text ingestion of transcripts, product briefs and stakeholder notes (including Tamil/Tanglish text); requirement extraction; template-based PRD; epics and user stories with priority; gap analysis; T-shirt sizing; two PM review checkpoints; Markdown, Word and JSON export; tracing and an automated evaluation suite.
**Out of scope (v1):** live meeting-bot capture; direct Jira/Confluence writing (export only); approval workflows beyond the PM; fine-tuned models; version comparison (planned for v1.1).

## 4. Success criteria
| Metric | Target at pilot exit |
|---|---|
| Baseline test pass rate (T1-T12) | 12 / 12 |
| Groundedness: PRD items traceable to a source quote | 100% |
| Extraction completeness on detailed inputs | ≥ 95% |
| PM edit rate at checkpoint 1 | ≤ 20% of items, falling over the pilot |
| Time from transcript to approved PRD draft | ≤ 15 minutes |
| Cost per PM per day | < $0.50 |

## 5. Timeline
| Phase | Dates | Exit gate |
|---|---|---|
| Design | Oct 26, 2026 | Architecture, agent prompts and test plan approved |
| Build MVP | Oct 27 | Pipeline runs end to end on T1; all 12 tests executable |
| Evaluate and harden | Oct 28 | Trace review, prompt fixes, before/after documented; UI with checkpoints |
| Capstone submission | Oct 29 | Repo, writeup, deck and demo delivered |
| Pilot (proposed) | Nov to Dec 2026 | 3 PMs, 20 real meetings, metrics above met |
| Rollout (proposed) | Q1 2027 | Product org-wide |

## 6. Risks
| Risk | Impact | Mitigation |
|---|---|---|
| LLM invents requirements | Wrong scope is built | Mandatory quotes, code-level Grounding Verifier, PM approval gate, hallucination tests |
| Contradictions silently resolved | Stakeholder trust lost | Conflicts kept with both sides; blocking open questions |
| PMs over-trust the draft | Errors pass review | "Draft" status, edit log, edit rate tracked, PM sign-off required |
| Confidential meeting data sent to an LLM provider | Compliance exposure | Approved enterprise API terms, no training on inputs, PII redaction in v1.1 |
| Translation drift (Tamil/Tanglish) | Meaning changed | Original lines shown next to the translation; vague words kept vague |
| Cost growth at scale | Budget overrun | Cheap model for extraction and checks, strong model only for writing; per-run cost in traces |

## 7. Stakeholders
| Stakeholder | Interest | Role |
|---|---|---|
| PMs/TPMs | Faster, consistent PRDs | Primary users; approve at both checkpoints |
| Engineering leads | Estimable, unambiguous stories | Consume stories and sizes; give feedback on quality |
| Design | Personas and UX needs captured | Review personas and acceptance criteria |
| Head of Product (sponsor) | Time-to-market, consistency | Funding, success sign-off |
| Security / Legal | Data handling | Approve data-flow and vendor terms |
| Enterprise customers (indirect) | Their asks not lost | Benefit from traceable requirements |

## 8. Rollout plan
1. **Pilot:** 3 volunteer PMs run every planning meeting through PRD Genie for 4 weeks. Weekly review of traces, edit rate and the eval suite.
2. **Harden:** fix the top failure patterns, add PII redaction and version comparison, and connect the Confluence/Jira export.
3. **Expand:** all PMs, with a 30-minute training session and a PRD Genie playbook. The template stays owned by the PM council.
4. **Operate:** monthly eval re-runs on a growing test set, plus a cost and quality dashboard from Langfuse. Any prompt change ships only if the eval does not regress.
