#!/usr/bin/python3
"""Defines the FileStorage class. """

import os
import json
from tkinter import N
import models
import unittest
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def test_FileStorage_instanciation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_instanciation_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        basemodel = BaseModel()
        models.storage.new(basemodel)
        self.assertIn("BaseModel." + basemodel.id, models.storage.all().keys())
        self.assertIn(basemodel, models.storage.all().values())
        user = User()
        models.storage.new(user)
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        state = State()
        models.storage.new(state)
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        place = Place()
        models.storage.new(place)
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        city = City()
        models.storage.new(city)
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        amenity = Amenity()
        models.storage.new(amenity)
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())
        review = Review()
        models.storage.new(review)
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_with_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        save_text = ""
        basemodel = BaseModel()
        models.storage.new(basemodel)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + basemodel.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)


    def test_reload(self):
        basemodel = BaseModel()
        models.storage.new(basemodel)
        user = User()
        models.storage.new(user)
        state = State()
        models.storage.new(state)
        place = Place()
        models.storage.new(place)
        city = City()
        models.storage.new(city)
        amenity = Amenity()
        models.storage.new(amenity)
        review = Review()
        models.storage.new(review)

        models.storage.save()
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + basemodel.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_no_file(self):
        if os.path.exists(models.storage._FileStorage__file_path):
                os.remove(models.storage._FileStorage__file_path)
        try:
            models.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised an exception {e} when no file exists.")

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

if __name__ == "__main__":
    unittest.main()
