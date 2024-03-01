import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_createBaseModel(self):
        basemodel = BaseModel()
        self.assertIsInstance(basemodel, BaseModel)
