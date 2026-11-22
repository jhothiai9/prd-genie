# PRD Genie

> Work in progress — Interview Kickstart capstone (Applied Agentic AI for PMs/TPMs).

PRD Genie turns meeting transcripts, product briefs and stakeholder notes into a grounded PRD, epics and user stories.

**Core rule: never invent requirements.** Every extracted item carries an exact quote and source line id. Anything the input doesn't say is marked UNKNOWN / TBD and raised as an open question.

## Pipeline

```
A0 Intake -> gate -> A1 Extractor -> Grounding Verifier -> HITL 1 (PM approves)
-> A2 PRD -> A3 Stories -> [A4 Gaps || A5 Scope] -> HITL 2 (PM signs off) -> export
```

Stage order, models and prompts are defined in `pipeline.json`; prompts live in `prompts/`.

## Setup (Windows)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # then fill in the Anthropic and Langfuse keys
```

## Run

```powershell
streamlit run app.py                     # UI with the two HITL checkpoints
python -m prdgenie.eval --ids T1,T3      # eval selected test cases -> results/
pytest -q                                # tests
```

See `CLAUDE.md` for project layout and working conventions.
