"""Smoke tests: the package imports and pipeline.json points at real prompt files."""

import importlib
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    "prdgenie",
    "prdgenie.schemas",
    "prdgenie.llm",
    "prdgenie.verifier",
    "prdgenie.pipeline",
    "prdgenie.eval",
    "prdgenie.agents",
    "prdgenie.agents.a0_intake",
    "prdgenie.agents.a1_extractor",
    "prdgenie.agents.a2_prd",
    "prdgenie.agents.a3_stories",
    "prdgenie.agents.a4_gap",
    "prdgenie.agents.a5_scope",
]


@pytest.mark.parametrize("name", MODULES)
def test_module_imports(name: str) -> None:
    assert importlib.import_module(name).__doc__


def test_pipeline_prompts_exist() -> None:
    stages = json.loads((ROOT / "pipeline.json").read_text(encoding="utf-8"))["stages"]
    prompts = [s["prompt"] for s in stages if s["kind"] == "llm"]
    assert len(prompts) == 6
    for prompt in prompts:
        assert (ROOT / prompt).is_file(), prompt
