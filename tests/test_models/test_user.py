#!/usr/bin/python3
"""Unittest for User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os
import json
from models import storage


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.user.email = "john@example.com"
        self.user.password = "1234"

    def tearDown(self):
        """Clean up after tests"""
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_inheritance(self):
        """Test User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes_exist(self):
        """Test if User attributes exist"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_default(self):
        """Test default attribute values"""
        u = User()
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")

    def test_save_and_reload(self):
        """Test saving and reloading user from storage"""
        self.user.save()
        user_id = f"User.{self.user.id}"

        # Reload storage
        storage.reload()
        objs = storage.all()
        self.assertIn(user_id, objs)
        reloaded_user = objs[user_id]
        self.assertEqual(reloaded_user.email, "john@example.com")
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")
        self.assertEqual(reloaded_user.password, "1234")

    def test_to_dict_contains_attributes(self):
        """Test if to_dict includes all attributes"""
        d = self.user.to_dict()
        self.assertIn("email", d)
        self.assertIn("first_name", d)
        self.assertIn("last_name", d)
        self.assertIn("password", d)
        self.assertEqual(d["__class__"], "User")


if __name__ == '__main__':
    unittest.main()
