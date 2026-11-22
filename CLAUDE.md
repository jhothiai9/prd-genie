# PRD Genie

PRD Genie turns meeting transcripts, product briefs and stakeholder notes into a grounded PRD, epics and user stories.
It is an Interview Kickstart capstone ("Applied Agentic AI for PMs/TPMs"). The full problem statement is in `data/` and `docs/`.

## The one rule that matters
**Never invent requirements.** Every extracted item must carry an exact quote from the source and the source line number.
If the input does not say it, the output says UNKNOWN / TBD and adds an open question. Grading checks this on every test.

## Architecture (sequential pipeline)
A0 Intake -> gate (enough content?) -> A1 Extractor -> Grounding Verifier (code) -> HITL 1 (PM approves)
-> A2 PRD Generator -> A3 Story Breakdown -> [A4 Gap Analyzer || A5 Scope Estimator] -> HITL 2 (PM signs off) -> export.
`pipeline.json` is the source of truth for agent order, model and prompt file. Do not hard-code these in Python.

## Stack
- Python 3.12, `anthropic` SDK, `pydantic` v2 for every agent's output schema, `langfuse` for tracing, `streamlit` for the UI, `pytest`.
- Models: `claude-haiku-5-5` (A0, A1, A4, A5) and `claude-sonnet-5-5` (A2, A3). Model IDs come from `pipeline.json`.
- Use structured outputs (`output_config.format` / `client.messages.parse`) so every agent returns JSON that validates against its pydantic model. Do not use assistant prefill (it returns a 400 on current models). Do not send `temperature`.
- Secrets live only in `.env` (git-ignored): `ANTHROPIC_API_KEY`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST`.

## Layout
- `prompts/` one system prompt per agent (ROLE, INPUT, OUTPUT, RULES, VAGUE INPUT RULE). Edit prompts here, not in code.
- `prdgenie/` package: `schemas.py`, `llm.py` (one place that calls Claude + Langfuse), `agents/`, `verifier.py`, `pipeline.py`, `eval.py`.
- `app.py` Streamlit UI with the two HITL checkpoints.
- `data/` inputs; `data/test_cases.json` = T1-T12 with must_contain / must_not checks.
- `results/` eval outputs (never hand-edited); `docs/` writeup and assignment answers; `screenshots/`.

## How to work in this repo
- Use plan mode for anything touching more than one file. Show the plan before writing code.
- Build one agent at a time and run it on one input before wiring it into the pipeline.
- Write or update a pytest test before changing `verifier.py` or `schemas.py`. Run `pytest -q` before saying a task is done.
- After any prompt change, re-run the affected test cases with `python -m prdgenie.eval --ids T1,T3` and compare to the last results file.
- Keep functions small and typed. No print-debugging left in code; use `logging`.
- Commit after each working capability with a clear message.
