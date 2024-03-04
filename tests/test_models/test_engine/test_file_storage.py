#!/usr/bin/python3
"""Unittest for FileStorage class."""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Unit tests suite for FileStorage class."""

    def setUp(self):
        """Create a new instance of FileStorage for each test."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up any resources allocated during the test."""
        del self.storage
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

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


if __name__ == "__main__":
    unittest.main()
