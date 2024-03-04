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
    """TestFileStorage class
    Test the FileStorage class and its methods"""
    model = BaseModel()

    def test_instanciates(self):
        """Test the instanciation of the FileStorage class
        By default, the file path should be file.json
        and the object should be an empty dictionary"""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test the file path
        We will check if the file path is a string"""
        correct_path = FileStorage._FileStorage__file_path
        self.assertEqual(str, type(correct_path))

    def test_object(self):
        """Test if the object is a dictionary
        Here we will check if the object is a dictionary
        By default, it should be empty."""
        dict_obj = FileStorage._FileStorage__objects
        self.assertEqual(dict, type(dict_obj))

    def test_all(self):
        """Test the all method
        By default, the all method should return an empty dictionary
        """
        dictionary = {}
        FileStorage.all(None)
        self.assertEqual(dictionary, FileStorage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
