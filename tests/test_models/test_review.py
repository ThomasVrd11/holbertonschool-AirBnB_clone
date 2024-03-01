#!/usr/bin/python3
"""Unittests for User class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test the instantiation of the class Review"""

    def test_instantiation(self):
        review = Review()
        """test if Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel), True)
        """test if review is of class Review"""
        self.assertIsInstance(review, Review)

    def test_initialization(self):
        """tests if attributes are correct types
        It tests if the id, created_at and updated_at are of the type string"""
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)
        """It tests if the id, created_at and updated_at are of the type datetime"""


if __name__ == '__main__':
    unittest.main()
