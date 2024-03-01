#!/usr/bin/python3
"""Unittests for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test the instantiation of the class Place"""

    def test_instantiation(self):
        place = Place()
        """test if Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel), True)
        """test if place is of class Place"""
        self.assertIsInstance(place, Place)

    def test_initialization(self):
        """tests if attributes are correct types"""
        place = Place()
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        self.assertIsInstance(place.amenity_ids, list)
        """It tests if the id, created_at and updated_at are of the type datetime"""


if __name__ == '__main__':
    unittest.main()
