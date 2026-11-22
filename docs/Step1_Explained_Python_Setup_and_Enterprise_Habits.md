# Step 1 Explained: Python Setup and Enterprise Habits

2026-11-22

Step 1 builds a clean, isolated project skeleton and writes no agent logic yet. This page explains each phrase of the prompt, why each file in your folder exists, and the habits that make Python work look professional.

## What the prompt tells Claude to do

| Phrase in the prompt | What it means | Why it matters in a company |
| --- | --- | --- |
| Read @CLAUDE.md, @pipeline.json and the files in prompts/ and data/ | The @ attaches those files, so Claude works from our design and does not guess | Context first: a new developer reads the design before touching code |
| create a .venv | A virtual environment: a private folder holding this project's Python packages | Projects never share or clash over package versions, and the setup can be repeated on any machine |
| install requirements.txt | Installs the libraries listed in that file into the .venv | One file defines the dependencies, so a teammate or a server gets the same setup |
| create the package skeleton described in CLAUDE.md | A package is a folder (`prdgenie/`) of Python files called modules, each with one job | Small modules with one responsibility are easier to test, review and change |
| empty modules with docstrings | A docstring is a short description at the top of a file saying what it is for | Readers learn the intent without reading the code |
| Add a README stub | A starter README.md, the front page of the repository | The TA and any future reader see this first |
| Don't write agent logic yet | Stop after the skeleton | Build one thing at a time, so when something breaks you know which step caused it |
| Show me the plan first | Plan mode: Claude proposes, you approve | You review the change before any file is touched |

## Why each file in your folder matters

| File or folder | Purpose | Habit it teaches |
| --- | --- | --- |
| `CLAUDE.md` | Standing instructions that Claude Code re-reads every session, like an onboarding doc for a new developer | Write the project rules down once instead of repeating them |
| `pipeline.json` | Agent order, models and prompt files | Keep configuration separate from code, so you change a model without editing Python |
| `prompts/` | One prompt file per agent | Treat prompts like code: versioned, reviewable, and easy to compare in git |
| `data/` | Inputs and `test_cases.json` | Keep test data apart from code so tests are repeatable |
| `requirements.txt` | The list of libraries | One place to define dependencies |
| `.env.example` | The names of the secret settings, with fake values | Documents what a new person must provide without exposing real keys |
| `.env` (you create it) | Your real keys | Secrets live only here and are never committed |
| `.gitignore` | Tells git what to never upload: `.env`, `.venv`, caches, outputs | Prevents leaking keys and bloating the repo |
| `docs/` | Q1, Q2, writeup | Documentation lives with the code |

## Python habits we will use throughout

- **One virtual environment per project.** Never install into your global Python. When it is active, the terminal prompt shows `(.venv)`. In PowerShell the command is `.venv\Scripts\Activate.ps1`. If Windows blocks it, run once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.
- **Secrets in environment variables, never in code.** The code reads keys from `.env`. Before any push we run a check that no key is in the repo.
- **Validate data at the edges.** `pydantic` models check that each agent's JSON has the right fields and types, so bad output fails loudly instead of silently.
- **Type hints.** Writing `def load(path: str) -> dict:` tells readers and tools what goes in and out.
- **Small modules, one job each.** That is why we have separate `schemas`, `llm`, `verifier`, `pipeline` and `eval` files.
- **Tests before trust.** `pytest` runs automatically checkable examples. Rule: run `pytest -q` before every commit.
- **Logging, not print.** Logs have levels and timestamps and can be switched off or sent to a tool. Prints are debugging leftovers.
- **Pin versions.** After everything works we run `pip freeze` and record exact versions, so the project behaves the same next month.
- **Small commits with clear messages.** One working capability per commit, for example "Add grounding verifier with tests". The history becomes your build story.
- **Review before merge.** In a company, someone else reads the change first. In this project, that is the advisor reviewing what Claude Code wrote.

## What to check in Claude's plan before you approve

- The `.venv` is created inside the prd-genie folder, not somewhere else.
- It installs from `requirements.txt` and nothing extra.
- The new files are only the skeleton: empty modules with docstrings, a README stub, and `__init__.py` files.
- It does not edit your prompts, data or `pipeline.json`, and does not read or print `.env`.
- It does not write agent logic or call the API.

If the plan does anything else, send a screenshot to the advisor before approving.
