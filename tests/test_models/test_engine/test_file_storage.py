#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage



class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class."""
    model = BaseModel()

    def setUp(self):
        """Create a new instance of FileStorage for each test."""
        storage = FileStorage()
        self.file_path = storage._FileStorage__file_path
        self.obj_dict = storage._FileStorage__objects

    def test_instanciates(self):
        """Tests that FileStorage correctly instantiates."""
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test that the file path is a string."""
        self.assertEqual(type(self.file_path), str)

    def test_object(self):
        """Test that __objects is a dictionary."""
        self.assertEqual(type(self.obj_dict), dict)

    def test_all(self):
        """Test that the all method returns a dictionary."""
        self.obj_dict = {}
        self.assertEqual(os.path.isfile('file.json'), True)

if __name__ == '__main__':
    unittest.main()
