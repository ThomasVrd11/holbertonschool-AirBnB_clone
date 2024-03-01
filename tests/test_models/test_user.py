#!/usr/bin/python3
"""Unittest for User class module"""
import unittest
from models.user import User
from models.base_model import BaseModel

class Test_user(unittest.TestCase):
    """Test the instantation of the User class
    It will also test the class attributes"""
    
    def test_instattion(self):
        user = User()
        """test if inheritance is right coming from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel), True)
        """test if class User is used by user"""
        self.assertIsInstance(user, User)
        
    def test_initialization(self):
        """tests if attributes"""
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        # * test if the attributes are empty strings
        
        if __name__ == '__main__':
            unittest.main()
            # * It will run the test if the module is run directly
            # * It will not run if the module is imported
        