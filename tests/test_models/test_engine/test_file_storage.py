#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.city import City


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class."""

    def setUp(self):
        self.file_path = FileStorage()
        

    def test_instanciates(self):
        """Tests that FileStorage correctly instantiates."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path(self):
        """Test that the file path is a string."""
        self.assertTrue(type(self.file_path), str)

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

if __name__ == '__main__':
    unittest.main()
