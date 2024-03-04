#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.base_model import BaseModel


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
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("{}.{}".format(type(new_obj).__name__, new_obj.id),
                      all_objs)

    def test_reload_persistence(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), all_objs)

    def test_saving_and_reloading_multiple_objects(self):
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

        with self.assertRaises(AttributeError):
            print(self.storage.__objects)


if __name__ == "__main__":
    unittest.main()
