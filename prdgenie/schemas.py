"""Pydantic v2 output models for every LLM agent.

Models (names match ``output_schema`` in pipeline.json):
- ``IntakeResult``   (A0) input_type, source_language, lines, original_lines, enough_content, missing_info
- ``Extraction``     (A1) stated_requirements, ambiguous_items, conflicts, stakeholders, personas,
                          deadlines, dependencies, extraction_status
- ``StoryBreakdown`` (A3) epics -> features -> stories
- ``GapReport``      (A4) gaps, risks, readiness
- ``ScopeReport``    (A5) estimates, summary
A2 returns Markdown and has no model.
"""
