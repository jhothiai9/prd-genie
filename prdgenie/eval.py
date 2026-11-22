"""Evaluation harness.

Usage: ``python -m prdgenie.eval --ids T1,T3``
Runs the selected cases from ``data/test_cases.json`` (inputs resolved from ``input_ref``),
checks ``must_contain`` / ``must_not`` / ``expect_stop``, and writes a timestamped file to ``results/``.
"""
