# Tuesday: build PRD Genie with Claude Code

Copy each prompt into Claude Code in order. Wait for each step to finish and pass before starting the next one.
Plan time: about 6 hours. Commit after every step.

## 0. Claude Code basics (5 minutes)

- Start it: open PowerShell in the project folder, type `claude`.
- **Shift+Tab** cycles modes: normal (asks before each edit), auto-accept edits, and **plan mode** (it only plans, no edits). Use plan mode for every new step, read the plan, then say "go".
- `/init` creates a CLAUDE.md. We already have one, so skip it.
- `/clear` starts a fresh conversation (do this between big steps; CLAUDE.md is re-read automatically).
- `/cost` shows usage. `Esc` interrupts. `Esc Esc` lets you rewind to an earlier message.
- `@path/to/file` in a prompt points Claude at a file.
- `!command` runs a shell command directly (for example `!pytest -q`).

## 1. Project setup (20 minutes)

Unzip the starter kit into `E:\claudeCowork\IK Capstone project\prd-genie`, then in PowerShell:

```
cd "E:\claudeCowork\IK Capstone project\prd-genie"
git init
copy .env.example .env      # then open .env and paste your keys
claude
```

Prompt 1 (plan mode):
> Read @CLAUDE.md, @pipeline.json and the files in prompts/ and data/. Set up the Python project: create a .venv, install requirements.txt, and create the package skeleton described in CLAUDE.md (empty modules with docstrings). Add a README stub. Don't write agent logic yet. Show me the plan first.

Then: `git add -A`, `git commit -m "skeleton"`, add the GitHub remote and push.

## 2. Schemas and the one LLM wrapper (40 minutes)

Prompt 2 (plan mode):
> In prdgenie/schemas.py create pydantic v2 models for every agent output, exactly matching the OUTPUT sections in prompts/a0_intake.md, a1_extractor.md, a3_stories.md, a4_gap.md and a5_scope.md (A2 returns Markdown). Then write prdgenie/llm.py with one function `call_agent(stage_id, user_content, schema=None)` that reads model and prompt file from pipeline.json, calls Claude with the system prompt, uses structured outputs when a schema is given, and is traced with Langfuse `@observe` (one span per agent, named by stage id, with tokens and cost). Load keys from .env. Write pytest tests for the schemas first. Use the claude-api skill for the SDK details.

Check it: `!pytest -q`, then ask Claude to run A0 on T1 only and show the JSON. Open Langfuse and confirm a trace appears. **Take a screenshot of that first trace.**

## 3. Extractor + Grounding Verifier (60 minutes)

Prompt 3 (plan mode):
> Write tests first for prdgenie/verifier.py: given the A0 lines and an Extraction, every item whose `quote` is not an exact substring of the referenced lines (normalise whitespace and quotes only) is removed and recorded in a `rejected` list with the reason; return a groundedness score = kept/total. Then implement it. Then implement agents A0 and A1 and a small CLI: `python -m prdgenie.pipeline --input data/... --until A1` that prints the verified extraction.

Run it on T1, T3, T7 and T9 from data/eval_prdgenie_inputs.txt. Check by eye:
- T7 keeps "10,000", "< 200ms at p95" and "v52" exactly.
- T3 shows a conflict with both sides.
- T9 stops at the gate.

Commit.

## 4. PRD + Stories, end to end on T1 (60 minutes)

Prompt 4 (plan mode):
> Implement A2 (PRD generator, input = data/prd_template.md + verified extraction) and A3 (story breakdown). Add a command-line HITL 1 step: show the extracted requirements as a numbered table and let me approve, delete an item, or send back with a note (which re-runs A1 with the note). Save every run to outputs/<timestamp>/ as JSON + prd.md + stories.md. Run the full pipeline on T1.

T1's PRD is T11, and its stories are T12. Check that all 10 template sections are present and there is no requirement that T1 didn't state. Commit.

## 5. Gap Analyzer + Scope Estimator in parallel (40 minutes)

Prompt 5:
> Implement A4 and A5 and run them in parallel after A3 (concurrent.futures is fine). Add HITL 2 as a final approve/reject step, then export prd.md, stories.md, gaps.md, estimates.md and a .docx of the PRD.

## 6. Eval harness (60 minutes)

Prompt 6 (plan mode):
> Write prdgenie/eval.py: for each case in data/test_cases.json, build the input (eval:Tn = that line of data/eval_prdgenie_inputs.txt; pipeline:T1:A2 = the T1 run's PRD), run the pipeline with HITL auto-approved, check must_contain case-insensitively against the combined output, check expect_stop, and use a cheap LLM judge (claude-haiku-5-5) for each must_not rule with a yes/no + reason. Tag each Langfuse trace with the test id. Write results/baseline_results_<timestamp>.md with one table per test in the playbook format (Test ID, Input, Output, Expected keywords present, Hallucination detected, Pass/Fail), plus a summary table and total cost. Support `--ids T1,T3`.

Run all 12 tests. Commit and push. **This is the "before" run. Keep its results file and don't edit it.**

## 7. Optional: make your own slash command (10 minutes)

Ask Claude:
> Create a project slash command /run-evals in .claude/commands/run-evals.md that runs the eval for given ids, then compares the newest results file with the previous one and summarises what changed.

Then tell me in the thread how many tests passed. I'll help read the failures on Wednesday.
