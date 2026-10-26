"""Synthetic tests only; none interact with production Guard."""
import unittest

from scripts.guard_mock import classify_event


class TestGuardMock(unittest.TestCase):
    def test_human_review_submitted(self):
        self.assertEqual(classify_event("review_submitted"), "reconcile")

    def test_review_edited(self):
        self.assertEqual(classify_event("review_edited"), "reconcile")

    def test_review_dismissed(self):
        self.assertEqual(classify_event("review_dismissed"), "reconcile")

    def test_bot_ready_ignored(self):
        self.assertEqual(classify_event("ready_for_review", "Bot"), "ignore")

    def test_human_ready_not_modeled(self):
        self.assertEqual(classify_event("ready_for_review", "User"), "ignore")

    def test_comment_created(self):
        self.assertEqual(classify_event("comment_created"), "reconcile")

    def test_unknown_event_ignored(self):
        self.assertEqual(classify_event("unknown"), "ignore")

    def test_empty_event_ignored(self):
        self.assertEqual(classify_event(""), "ignore")


if __name__ == "__main__":
    unittest.main()
