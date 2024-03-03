#!/usr/bin/python3
"""Unit test for the state module"""
import unittest
from models.state import State
from models.base_model import BaseModel


class Test_state(unittest.TestCase):
    """Test the instantation of the State class
    It will also test the class attributes"""

    def test_instantation(self):
        state = State()
        """Tests if inheritance is right coming from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel), True)
        """Tests if class State is used by state"""
        self.assertIsInstance(state, State)

        def test_initialisation(self):
            """Tests if attributes are strings"""
            state = State()
            self.assertIsInstance(state.name, str)
            # * test if the attributes are empty strings

if __name__ == '__main__':
    unittest.main()
    # * It will run the test if the module is run directly
    # * It will not run if the module is imported
