"""The single place that calls Claude.

Responsibilities:
- Load ``.env`` secrets (ANTHROPIC_API_KEY, LANGFUSE_*).
- Read model id and prompt file for a stage from ``pipeline.json`` (never hard-coded).
- Call ``client.messages.parse`` with the stage's pydantic model as structured output
  (no assistant prefill, no ``temperature``), or plain text for Markdown stages.
- Wrap each call in a Langfuse trace/span.
"""
