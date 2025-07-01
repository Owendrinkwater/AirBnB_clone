#!/usr/bin/python3
"""Unittest for Ammenity."""

import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        a = Amenity()
        self.assertEqual(a.name, "")

if __name__ == '__main__':
    unittest.main()