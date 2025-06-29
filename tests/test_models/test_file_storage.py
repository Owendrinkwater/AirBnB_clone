#!/usr/bin/python3
"""Unittest for FileStorage class"""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Reset storage before each test"""
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """Cleanup after each test"""
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_private_class_attributes_exists(self):
        """Test if __file_path and __objects exist"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all_method_returns_dict(self):
        """Test that all() returns __objects"""
        self.assertEqual(self.storage.all(), {})

    def test_new_method_adds_object(self):
        """Test that new() adds an object correctly"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], obj)

    def test_save_creates_file_with_correct_data(self):
        """Test that save() writes __objects to file.json"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        with open("file.json", "r") as f:
            data = json.load(f)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)

    def test_reload_loads_objects_correctly(self):
        """Test that reload() loads objects from file.json"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()

        # Simulate fresh reload
        FileStorage._FileStorage__objects = {}
        self.storage.reload()

        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].id, obj.id)

if __name__ == '__main__':
    unittest.main()

