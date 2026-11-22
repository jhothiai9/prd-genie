"""Grounding Verifier (stage VER, code only).

Drops and logs any extracted item whose ``quote`` is not an exact substring of the source lines
it cites. Returns the cleaned extraction plus a list of rejected items for the HITL 1 view.
"""
