#!/usr/bin/python3
"""Module for testing the FileStorage class.
This module contains a suite of test cases for validating the functionalities
of the FileStorage class in the application. It covers tests for methods like
saving, reloading, deleting, and ensuring data integrity and consistency in the
FileStorage system.
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os
import json
from models.city import City


class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage class."""

    def setUp(self):
        """Prepare the test environment before each test."""
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Clean up the test environment after each test."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the 'all' method for retrieving all stored objects."""
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        """Test the 'new' method for adding new objects to storage."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        key = "User.{}".format(user.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """Test the 'save' method to ensure it correctly saves objects."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        self.assertTrue(os.path.isfile(self.file_path))
        with open(self.file_path, 'r') as f:
            content = json.load(f)
        key = "User.{}".format(user.id)
        self.assertIn(key, content)

    def test_reload(self):
        """Test the 'reload' method to reload objects from storage."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "User.{}".format(user.id)
        self.assertIn(key, new_storage.all())

    def test_new_multiple_objects(self):
        """Test adding multiple objects to storage."""
        storage = FileStorage()
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        key1 = "User.{}".format(user1.id)
        key2 = "User.{}".format(user2.id)
        self.assertIn(key1, storage.all())
        self.assertIn(key2, storage.all())

    def test_reload_no_file(self):
        """Test reloading storage when the file does not exist."""
        storage = FileStorage()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        storage.reload()

    def test_reload_empty_file(self):
        """Test reloading from an empty file."""
        storage = FileStorage()
        open(self.file_path, 'a').close()
        storage.reload()

    def test_reload_corrupted_file(self):
        """Test reloading from a corrupted JSON file."""
        with open(self.file_path, 'w') as f:
            f.write("This is not valid JSON")

    def test_save_existing_file(self):
        """Test saving objects when the file already exists."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        user2 = User()
        storage.new(user2)
        storage.save()
        with open(self.file_path, 'r') as f:
            content = json.load(f)
        key1 = "User.{}".format(user.id)
        key2 = "User.{}".format(user2.id)
        self.assertIn(key1, content)
        self.assertIn(key2, content)

    def test_all_after_reload(self):
        """Test the 'all' method after reloading storage."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertEqual(len(new_storage.all()), len(storage.all()))

    def test_new_different_objects(self):
        """Test adding different types of objects to storage."""
        storage = FileStorage()
        user = User()
        city = City()
        storage.new(user)
        storage.new(city)
        key_user = "User.{}".format(user.id)
        key_city = "City.{}".format(city.id)
        self.assertIn(key_user, storage.all())
        self.assertIn(key_city, storage.all())

    def test_delete_object(self):
        """Test deleting an object from storage."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        key = "User.{}".format(user.id)
        del storage._FileStorage__objects[key]
        self.assertNotIn(key, storage.all())

    def test_storage_consistency_after_save_and_reload(self):
        """Test for consistency in storage after save and reload."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        key = "User.{}".format(user.id)
        storage.save()
        storage.reload()
        self.assertIn(key, storage.all())

    def test_serialization_integrity(self):
        """Test the integrity of serialization in storage."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            key = "User.{}".format(user.id)
            self.assertIn(key, data)
            self.assertEqual(data[key]['id'], user.id)

    def test_reload_with_invalid_class(self):
        """Test reloading with an invalid class name in the JSON file."""
        storage = FileStorage()
        user = User()
        storage.new(user)
        storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        with open(self.file_path, 'w') as f:
            key = list(data.keys())[0]
            invalid_key = key.replace("User", "InvalidClass")
            data[invalid_key] = data.pop(key)
            json.dump(data, f)

    def test_FileStorage_reload(self):
        """Test the 'reload' method for FileStorage."""
        storage = FileStorage()
        user = User()
        user.name = "Test User"
        storage.new(user)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()

        key = "User.{}".format(user.id)
        self.assertIn(key, storage.all())
        self.assertEqual(storage.all()[key].name, "Test User")


if __name__ == "__main__":
    unittest.main()
