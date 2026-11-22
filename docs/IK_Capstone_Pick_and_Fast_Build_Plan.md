# IK Capstone: Pick and Fast Build Plan

2026-10-26

## Recommendation: PRD Genie

Pick PRD Genie. It is the fastest of the four projects to finish well, and it matches what you already do every week.

The guide's rule is that you must pick one of the four given projects (CalendarMate, SalesGenie, PRD Genie, Mira), build its 3 core capabilities plus at least 1 extended one, and you may then add your own twist. Your niche goes in as the twist, not as a new project.

- **Your daily pattern is already this pipeline.** Your Tamil audio, OCR and video-summary work is: raw transcript in, cleaned structured document out, with unclear spots flagged instead of guessed. PRD Genie is exactly that, with "requirements" in place of sermon text.
- **Claude is the named best model for it.** The playbook lists Claude for PRD generation, which lines up with your Claude Certified Architect prep.
- **Fastest setup.** File upload only, no OAuth, no live APIs. The sequential pipeline (extract, then PRD, then stories) is the pattern the playbook calls most reliable.
- **Richest grading data.** It ships transcripts including contradictory and empty ones, so hallucination fixes are easy to show in traces.

**Signature twist:** a multilingual intake step that accepts a Tamil or Tanglish meeting transcript (or audio via speech-to-text), produces an English requirements list, and keeps every requirement tied to the source line it came from.

## Alternatives

| Project | Fit for you | Why it ranks lower |
| --- | --- | --- |
| Mira (2nd) | Strong. Multi-CSV grounding is close to your Excel trackers; shows a router pattern. | 4 data files and a router with 4 branches mean more agents to debug, roughly one extra day. |
| SalesGenie (3rd) | Medium. Simplest data, sequential pipeline. | Sales is not your niche, so the writeup and twist would feel generic. |
| CalendarMate | Low. | Google OAuth2 setup and live APIs cost time you do not have. |

## Architecture and tools

A sequential pipeline of agents. Every transcript follows the same path, which is when the playbook says sequential beats router.

1. **Intake and Language Normalizer** (your twist): detects Tamil, Tanglish or English, translates to English, numbers every source line. Never turns a vague phrase into a firm one.
2. **Requirement Extractor** (core 1): stated, ambiguous and contradicted requirements, each with its source line. Returns insufficient input rather than inventing.
3. **PRD Generator** (core 2): fills prd_template.md only from approved items; unknowns stay TBD with an open question.
4. **Epic and Story Breakdown** (core 3): epics and stories with acceptance criteria, traced to requirement IDs.
5. **Gap Analyzer** (extended): lists missing items as questions for the PM, never as answers.

| Category | Choice and why |
| --- | --- |
| Workflow platform | Python app built with Claude Code; the pipeline.json file is the exported workflow definition. |
| LLM | Claude: a small fast model for intake and extraction, a stronger one for PRD writing. |
| Inputs | File upload only: the transcripts, stakeholder notes, prd_template.md. |
| Observability | Langfuse; traces per agent with tokens, cost and latency. |

## Submission checklist

| Required item | What it will be |
| --- | --- |
| Workflow JSON + README in a GitHub repo | pipeline.json, prompts folder, README |
| Architecture diagram | Pipeline diagram |
| Baseline test results | T1 to T12 table: input, output, keywords present, hallucination, pass/fail |
| Screenshots | Workflow canvas or pipeline, a live run, observability traces |
| Writeup (1 to 2 pages) | All sections from playbook step 7.1 |
| Q1 to Q4 answers | From the problem statement document |
| Cost analysis | Real token counts x model price x daily runs |
| Slide deck | 8 to 10 slides |
| Public repo link | Submitted on the IK portal |

The rubric rewards honesty about failures. We record at least one real hallucination and its fix.
