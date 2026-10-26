"""Standalone illustrative guard policy; NOT production guard code.

No API requests, credentials, private repositories or live PR modification.
"""


def classify_event(event_type: str, author_type: str = "User") -> str:
    """Return a sample action, without invoking GitHub APIs."""
    if event_type == "ready_for_review" and author_type == "Bot":
        return "ignore"
    if event_type in {"review_submitted", "review_edited", "review_dismissed"}:
        return "reconcile"
    if event_type == "comment_created":
        return "reconcile"
    return "ignore"
