#!/usr/bin/python3
"""Defines the FileStorage class. """

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = storage
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        try:
            os.remove(self.file_path)
        except Exception:
            pass

    def test_init(self):
        self.assertTrue(isinstance(self.storage, type(storage)))

    def test_all(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn(
            "{}.{}".format(
                new_obj.__class__.__name__,
                new_obj.id),
            all_objs)

    def test_new(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        all_objs = self.storage.all()
        self.assertIn(
            "{}.{}".format(
                new_obj.__class__.__name__,
                new_obj.id),
            all_objs)

    def test_save(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        with open(self.file_path, "r") as f:
            file_contents = f.read()
            self.assertIn("BaseModel.{}".format(new_obj.id), file_contents)

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
            print(storage.__objects)

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

    def test_instanciates(self):
        """Test that FileStorage instanciates correctly."""
        storage_instance = FileStorage()
        self.assertTrue(isinstance(storage_instance, FileStorage))
        
        
    def test_file_path(self):
        """test that file_path is a string."""
        self.assertTrue(isinstance(self.storage._FileStorage__file_path, str))

    def test_objects(self):
        """Test that objects is a dictionary."""
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))
    def test_all_bis(self):
        """Test that all returns the FileStorage objects."""
        self.assertEqual(
            self.storage.all(),
            self.storage._FileStorage__objects)

    def test_new_bis(self):
        """Test that new adds an object to the FileStorage objects."""
        bm = BaseModel()
        self.storage.new(bm)
        self.assertIn(bm, self.storage._FileStorage__objects.values())

    def test_save_bis(self):
        """Test that save writes the FileStorage objects to the file path."""
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            self.assertIn(bm.to_dict(), json.load(f).values())

    def test_all_ter(self):
        """Test that all returns the dictionary of objects."""
        self.assertTrue(isinstance(self.storage.all(), dict))

if __name__ == "__main__":
    unittest.main()
