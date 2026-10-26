"""Tests synthetic events against the public sample policy only."""
import unittest

from scripts.guard_mock import classify_event


class TestGuardMock(unittest.TestCase):
    def test_human_review_triggers_reconciliation(self):
        self.assertEqual(classify_event("review_submitted"), "reconcile")

    def test_bot_ready_event_is_ignored(self):
        self.assertEqual(classify_event("ready_for_review", "Bot"), "ignore")

    def test_irrelevant_event_is_ignored(self):
        self.assertEqual(classify_event("unrelated_event"), "ignore")

    def test_comment_triggers_reconciliation(self):
        self.assertEqual(classify_event("comment_created"), "reconcile")


if __name__ == "__main__":
    unittest.main()
