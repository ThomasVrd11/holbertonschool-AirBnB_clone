#!/usr/bin/python3
"""Unittests for City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test the instantiation of the class City"""

    def test_instantiation(self):
        city = City()
        """test if City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel), True)
        """test if city is of class City"""
        self.assertIsInstance(city, City)

    def test_initialization(self):
        """tests if attributes are correct types"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)


if __name__ == '__main__':
    unittest.main()
