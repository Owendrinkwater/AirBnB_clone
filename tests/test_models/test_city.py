#!/usr/bin/python3
"""Unittest for city."""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for the City class"""

    def setUp(self):
        """Set up a City instance for testing"""
        self.city = City()

    def test_instance(self):
        """Test that city is an instance of City and BaseModel"""
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test City attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_save_city(self):
        """Test save method on City instance"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict_city(self):
        """Test to_dict method for City"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["__class__"], "City")
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("id", city_dict)


if __name__ == '__main__':
    unittest.main()
