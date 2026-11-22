"""Pipeline runner driven by ``pipeline.json``.

A0 Intake -> GATE (stop with missing_info if not enough content) -> A1 Extractor -> VER
-> HITL1 (approve / edit / send back to A1 with note) -> A2 PRD -> A3 Stories
-> [A4 Gap || A5 Scope] -> HITL2 (approve / reject with note) -> EXPORT (markdown, docx, json).
HITL steps are pause points; the UI (``app.py``) or eval harness supplies the decision.
"""
