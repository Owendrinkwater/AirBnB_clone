#!/usr/bin/python3
"""Unittest for state."""

import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime


class TestState(unittest.TestCase):
    """Unittest for State class"""

    def test_inheritance(self):
        self.assertIsInstance(State(), BaseModel)

    def test_attributes_exist(self):
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

    def test_attribute_assignment(self):
        s = State()
        s.name = "Nairobi"
        self.assertEqual(s.name, "Nairobi")

    def test_save_updates_updated_at(self):
        s = State()
        old_updated_at = s.updated_at
        s.save()
        self.assertNotEqual(s.updated_at, old_updated_at)

    def test_to_dict_contains_class_name(self):
        s = State()
        s_dict = s.to_dict()
        self.assertEqual(s_dict["__class__"], "State")

    def test_to_dict_contains_all_keys(self):
        s = State()
        s.name = "Nakuru"
        s_dict = s.to_dict()
        self.assertIn("id", s_dict)
        self.assertIn("created_at", s_dict)
        self.assertIn("updated_at", s_dict)
        self.assertIn("name", s_dict)


if __name__ == '__main__':
    unittest.main()
