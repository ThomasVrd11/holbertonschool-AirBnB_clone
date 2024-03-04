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

    def test_name_default(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

    def test_to_dict_contains_correct_keys(self):
        amenity = Amenity()
        amenity.name = "Chong"
        self.assertIn("name", amenity.to_dict())
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())

    def test_to_dict_contains_correct_values_for_name(self):
        amenity = Amenity()
        amenity.name = "Tony"
        self.assertEqual(amenity.to_dict()["name"], "Tony")


if __name__ == '__main__':
    unittest.main()
