#!/usr/bin/python3
"""Defines the FileStorage class."""

import unittest
from models.base_model import BaseModel
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
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        with open(self.file_path, "r") as f:
            objs = json.load(f)
        self.assertIn("{}.{}".format(type(new_obj).__name__, new_obj.id), objs)

    def test_reload(self):
        new_obj = BaseModel()
        self.storage.new(new_obj)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIn(f"{type(new_obj).__name__}.{new_obj.id}", all_objs)


if __name__ == "__main__":
    unittest.main()
