#!/usr/bin/python3
"""Unittest for city."""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_attributes(self):
        c = City()
        self.assertEqual(c.name, "")
        self.assertEqual(c.state_id, "")

if __name__ == '__main__':
    unittest.main()