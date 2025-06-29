#!/usr/bin/python3
"""Unit tests for FileStorage functionality related to BaseModel."""

import unittest
import os
import json
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
     """Test suite for FileStorage methods related to BaseModel."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()
        self.model.name = "Test Model"
        self.model.my_number = 42
        self.file_path = "file.json"
        storage.save()

    def tearDown(self):
        """Clean up test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        FileStorage__objects = storage.all()
        FileStorage__objects.clear()

    def test_save_creates_json_file(self):
        """Test that save() creates file.json."""
        self.asserTrue(os.path.exists(self.file_path))

    def test_reload_loads_objects(self):
        """Test that reload() restores objects from file.json."""
        model_id = self.model.id
        storage.save()
        storage._FileStorage__objects.clear()  # clear objects manually
        self.assertEqual(len(storage.all()), 0)
        storage.reload()
        reloaded_keys = storage.all().keys()
        found = any(model_id in key for key in reloaded_keys)
        self.assertTrue(found)

    def test_save_and_reload_data_integrity(self):
        """Test object data is preserved across save and reload."""
        storage.save()
        model_dict_before = self.model.to_dict()
        storage._FileStorage__objects.clear()
        storage.reload()
        key = f"BaseModel.{self.model.id}"
        reloaded = storage.all()[key]
        model_dict_after = reloaded.to_dict()
        self.assertEqual(model_dict_before, model_dict_after)


    if __name__ == '__main__':
        unittest.main()
