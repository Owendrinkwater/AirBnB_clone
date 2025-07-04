#!/usr/bin/python3
"""Unittest for BaseModel."""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
from models import storage
import uuid


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_id_is_string(self):
        """Test that id is a string and unique."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertIsInstance(model1.id, str)
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_type(self):
        """Test that created_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_type(self):
        """Test that updated_at is a datetime object."""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ representation of the model."""
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_save_method(self):
        """Test that save() updates updated_at."""
        model = BaseModel()
        old_time = model.updated_at
        model.save()
        self.assertGreater(model.updated_at, old_time)

    def test_to_dict_returns_dict(self):
        """Test that to_dict() returns a dictionary."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_keys(self):
        """Test that to_dict() contains expected keys."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)

    def test_to_dict_datetime_format(self):
        """Test datetime fields in ISO format."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())


class TestBaseModelSave(unittest.TestCase):
    """Tests the save method of BaseModel"""

    def setUp(self):
        """Clean up the file.json before test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        self.model = BaseModel()

    def tearDown(self):
        """Remove file.json after test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_updates_updated_at(self):
        """Test that save updates updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_creates_file(self):
        """Test that save creates file.json"""
        self.model.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_stores_instance(self):
        """Test that instance is in storage after save"""
        self.model.save()
        all_objs = storage.all()
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, all_objs)

        
if __name__ == '__main__':
    unittest.main()

