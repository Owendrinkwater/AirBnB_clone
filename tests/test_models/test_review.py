#!/usr/bin/python3
"""Unittest for review."""

import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def test_attributes(self):
        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

if __name__ == '__main__':
    unittest.main()