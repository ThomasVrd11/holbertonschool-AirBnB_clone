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
        self.file_path = self.storage._FileStorage__file_path

    def tearDown(self):
        """Clean up any resources allocated during the test."""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
        del self.storage

    def test_instanciates(self):
        """Tests that FileStorage correctly instantiates."""
        self.assertIsInstance(self.storage, FileStorage)

    def test_file_path(self):
        """Test that the file path is a string."""
        self.assertEqual(type(self.file_path), str)

    def test_object(self):
        """Test that __objects is a dictionary."""
        self.assertEqual(type(self.storage.all()), dict)

    def test_all(self):
        """Test that the all method returns a dictionary."""
        all_objects = self.storage.all()
        self.assertEqual(type(all_objects), dict)
