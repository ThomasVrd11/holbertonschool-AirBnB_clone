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

    def setUp(self):
        self.city = City()

    def test_state_id_default(self):
        self.assertEqual(self.city.state_id, "")

    def test_name_assignment(self):
        self.city.name = "Paris"
        self.assertEqual(self.city.name, "Paris")

    def test_to_dict_contains_correct_keys(self):
        city = City()
        city.name = "Sartrouville"
        city.postal_code = "78500"
        self.assertIn("postal_code", city.to_dict())
        self.assertIn("name", city.to_dict())

    def test_to_dict_contains_correct_values_for_attributes(self):
        city = City()
        city.name = "Sartrouville"
        city.postal_code = "78500"
        self.assertEqual(city.to_dict()["name"], "Sartrouville")
        self.assertEqual(city.to_dict()["postal_code"], "78500")

if __name__ == '__main__':
    unittest.main()
