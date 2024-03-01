#!/usr/bin/python3
"""Unittests for Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test the instantiation of the class Amenity"""

    def test_instantiation(self):
        amenity = Amenity()
        """test if Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel), True)
        """test if amenity is of class Amenity"""
        self.assertIsInstance(amenity, Amenity)

    def test_initialization(self):
        """tests if attributes are correct types"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)


if __name__ == '__main__':
    unittest.main()
