#!/usr/bin/python3
"""Defines the FileStorage class. """

import os
import models
import unittest
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = storage
        self.file_path = self.storage._FileStorage__file_path

    def test_FileStorage_instanciation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_instanciation_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))
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
        self.assertTrue(isinstance(self.storage.all(), dict))
        self.assertEqual(
            self.storage.all(),
            self.storage._FileStorage__objects)

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

    def test_objects(self):
        """Test that objects is a dictionary."""
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))

    def test_file_path(self):
        """test that file_path is a string."""
        self.assertTrue(isinstance(self.storage._FileStorage__file_path, str))

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

if __name__ == "__main__":
    unittest.main()
