import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    basemodel = BaseModel()

    def test_createBaseModel(self):
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_has_uuid(self):
        self.assertTrue(self.basemodel.id)

    def test_was_created_at(self):
        self.assertIsInstance(self.basemodel.created_at, datetime)

    def test_was_updated_at(self):
        self.assertIsInstance(self.basemodel.updated_at, datetime)

    def test_save_BaseModel(self):
        self.basemodel.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_BaseModel_to_dict(self):
        dictionnary = self.basemodel.to_dict()
        self.assertIsInstance(dictionnary, dict)

    def test_load_BaseModel(self):
        dictionnary = self.basemodel.to_dict()
        basemodel2 = BaseModel(**dictionnary)
        self.assertIsInstance(basemodel2, BaseModel)
        self.assertTrue(basemodel2.id, self.basemodel.id)
