#!/usr/bin/python3
"""Unittest for state."""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        s = State()
        self.assertEqual(s.name, "")

if __name__ == '__main__':
    unittest.main()