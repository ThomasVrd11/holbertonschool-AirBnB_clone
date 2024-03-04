#!/usr/bin/python3
"""Unit test for the state module"""
import unittest
from models.state import State
from models.base_model import BaseModel
import models


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
        self.assertTrue(isinstance(state, State))
        self.assertTrue(isinstance(state, BaseModel))

    def test_state_attributes(self):
        my_state = State(name="California")
        self.assertEqual(my_state.name, "California")
        self.assertTrue(hasattr(my_state, "id"))
        self.assertTrue(hasattr(my_state, "created_at"))
        self.assertTrue(hasattr(my_state, "updated_at"))

    def test_to_dict_method(self):
        my_state = State(name="California")
        state_dict = my_state.to_dict()
        self.assertEqual(state_dict["name"], "California")
        self.assertEqual(state_dict["__class__"], "State")
        self.assertTrue("created_at" in state_dict)
        self.assertTrue("updated_at" in state_dict)
        self.assertTrue("id" in state_dict)

    def test_save_and_reload_state(self):
        my_state = State(name="Nevada")
        my_state.save()
        del my_state
        models.storage.reload()
        reloaded_state = models.storage.all()["State.{}".format(my_state.id)]
        self.assertEqual(reloaded_state.name, "Nevada")




if __name__ == '__main__':
    unittest.main()
    # * It will run the test if the module is run directly
    # * It will not run if the module is imported
