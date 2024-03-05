#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.base_model import BaseModel
import json


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class."""

    def setUp(self):
        """Create a new instance of FileStorage for each test."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up any resources allocated during the test."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)
        del self.storage

    def test_instanciates(self):
        """Tests that FileStorage correctly instantiates."""
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        """Test that the file path is a string."""
        self.assertTrue(isinstance(self.storage._FileStorage__file_path, str))

    def test_object(self):
        """Test that __objects is a dictionary."""
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))

    def test_all(self):
        """Test that the all method returns a dictionary."""
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))

    def test_file_creation(self):
        """Test that the file is created upon save."""
        base_model_instance = BaseModel()
        self.storage.new(base_model_instance)
        self.storage.save()
        self.assertTrue(os.path.isfile(self.storage._FileStorage__file_path))

    def test_overwrite_existing_object(self):
        """test that the save method overwrites an existing object."""
        my_obj = BaseModel()
        my_obj.my_number = 42
        self.storage.new(my_obj)
        self.storage.save()
        my_obj.my_number = 43
        self.storage.save()
        self.storage.reload()
        reloaded_obj = self.storage.all()["BaseModel.{}".format(my_obj.id)]
        self.assertEqual(
            reloaded_obj.my_number,
            43,
            "Object was not updated correctly in storage.")

    def test_custom_attribute_serialization_deserialization(self):
        """test that custom attributes are serialized and deserialized."""
        my_state = State(name="Hawaii")
        self.storage.new(my_state)
        self.storage.save()
        self.storage.reload()
        reloaded_state = self.storage.all()[f"State.{my_state.id}"]
        self.assertEqual(
            reloaded_state.name,
            "Hawaii",
            "State name attribute didn't match after reload.")

    def test_reload(self):
        """test that the reload method deserializes the JSON file."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("{}.{}".format(type(new_obj).__name__, new_obj.id),
                      all_objs)

    def test_reload_persistence(self):
        """test that the reload method is persistent."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), all_objs)

    def test_saving_and_reloading_multiple_objects(self):
        """test that the storage system can handle multiple objects."""
        base_model_instance = BaseModel()
        user_instance = User(email="user@example.com", password="password")
        self.storage.new(base_model_instance)
        self.storage.new(user_instance)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(base_model_instance.id),
                      self.storage.all())
        self.assertIn("User.{}".format(user_instance.id), self.storage.all())

    def test_objects_encapsulation(self):
        """test that __objects is encapsulated."""
        with self.assertRaises(AttributeError):
            print(self.storage.__objects)

    def test_serialization_integrity(self):
        """test that the serialization of an object is consistent."""
        user = User()
        user.name = "Test User"
        self.storage.new(user)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        key = "User.{}".format(user.id)
        self.assertIn(key, data)
        self.assertEqual(
            data[key]['name'],
            user.name,
            "User name did not match after serialization.")

    def test_storage_consistency_after_save_and_reload(self):
        """test that the storage system is consistent after save and reload."""
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = "User.{}".format(user.id)
        self.assertIn(
            key,
            self.storage.all(),
            "User object was not found after reload.")

    def test_new_different_objects(self):
        """test that the storage system can handle different objects."""
        user = User()
        state = State()
        self.storage.new(user)
        self.storage.new(state)
        key_user = "User.{}".format(user.id)
        key_state = "State.{}".format(state.id)
        self.assertIn(
            key_user,
            self.storage.all(),
            "User object was not found in storage.")
        self.assertIn(
            key_state,
            self.storage.all(),
            "State object was not found in storage.")


if __name__ == "__main__":
    unittest.main()
