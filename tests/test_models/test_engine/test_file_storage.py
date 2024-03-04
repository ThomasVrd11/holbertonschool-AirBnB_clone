#!/usr/bin/python3
"""Unittest for FileStorage class
We will use the unittest module to test the FileStorage class
instanciation and its methods.
file path
object
all"""

from pyexpat import model
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class
    we will use the unittest module to test the FileStorage class
    instanciation and its methods."""

    my_model = BaseModel()

    def test_instanciates(self):
        """Tests that FileStorage correctly instanciates
        It will be tested by verifying that the object is an instance
        """
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test __file path is exited
        It will be tested by verifying that the file path is a string
        If the file path is not a string, the test will fail"""
        path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(path))

    def test_object(self):
        """Test __object is type dict after deserialization object - dict
        By default, the __objects attribute should be an empty dictionary"""
        object_dict = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(object_dict))

    def test_all(self):
        """Test all method returns the __objects dictionary
        It will be tested by verifying that the __objects attribute is
        returned by the all method"""

        dict_return = {}
        FileStorage.all(None)
        self.assertEqual(os.path.isfile('file.json'), True)


if __name__ == "__main__":
    unittest.main()
