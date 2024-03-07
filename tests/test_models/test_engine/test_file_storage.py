#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()
        self.storage_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        try:
            os.remove(self.storage_path)
        except FileNotFoundError:
            pass

    def test_instanciates(self):
        """Tests that FileStorage correctly instantiates."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test that the file path is a string."""
        self.assertTrue(type(self.storage_path), str)

    def test_object(self):
        storage = FileStorage()
        """Test that __objects is a dictionary."""
        self.assertEqual(type(storage.all()), dict)

    def test_all(self):
        """Test that the all method returns a dictionary."""
        storage = FileStorage()
        self.obj_dict = {}
        storage.all()
        self.assertEqual(os.path.isfile('file.json'), True)

    def test_new(self):
        """Test that a new object is correctly added to the storage."""
        new_obj = User()
        self.storage.new(new_obj)
        key = "User.{}".format(new_obj.id)
        self.assertIn(
            key,
            self.storage.all(),
            "New object not found in storage.")

    def test_reload_persistence(self):
        """test that the reload method is persistent."""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn("BaseModel.{}".format(new_obj.id), all_objs)

    def test_objects_encapsulation(self):
        """test that __objects is encapsulated."""
        with self.assertRaises(AttributeError):
            print(self.storage.__objects)

    def test_serialization_integrity(self):
        """test that the serialization of an object is consistent."""
        neo_storage = FileStorage()
        user = User()
        user.name = "Test User"
        user.save()
        neo_storage.new(user)
        neo_storage.save()
        with open(neo_storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
        key = "User.{}".format(user.id)
        self.assertIn(key, data)
        self.assertEqual(
            data[key]['name'],
            user.name)

    def test_FileStorage__file_path(self):
        # storage = FileStorage()
        expected_path = "file.json"
        self.assertEqual(str, type(self.storage_path))
        self.assertEqual(expected_path, self.storage_path)

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


'''

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




    def test_saving_and_reloading_multiple_objects(self):
        self.storage.save()
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
            '''

if __name__ == '__main__':
    unittest.main()
