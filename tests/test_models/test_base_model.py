#!/usr/bin/python3
"""Defines the tests for the BaseModel class."""

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

    def test_BaseModel_str(self):
        actual_str = self.basemodel.__str__()
        expected_start = "[BaseModel] ({})".format(self.basemodel.id)
        # check if str has expected start
        self.assertTrue(actual_str.startswith(expected_start))
        # check if str include the key attributes
        self.assertIn('id', actual_str)
        self.assertIn('created_at', actual_str)
        self.assertIn('updated_at', actual_str)
        basemodel2 = BaseModel()
        expected_format = "[BaseModel] ({}) {}".format(basemodel2.id,
                                                       basemodel2.__dict__)
        self.assertEqual(basemodel2.__str__(), expected_format)

    def test_BaseModel_init_with_kwargs(self):
        time = datetime.now()
        basemodel = BaseModel(id="1234", created_at=time.isoformat(),
                              updated_at=time.isoformat())
        self.assertEqual(basemodel.id, "1234")
        self.assertEqual(basemodel.created_at, time)
        self.assertEqual(basemodel.updated_at, time)

    def test_BaseModel_init_with_args(self):
        basemodel = BaseModel("1234", "other_value")
        self.assertNotIn("1234", basemodel.__dict__.values())
        self.assertNotIn("other_value", basemodel.__dict__.values())

    def test_BaseModel_update_attributes(self):
        self.basemodel.name = "Test"
        self.basemodel.number = 42
        self.basemodel.save()
        basemodel_dict = self.basemodel.to_dict()
        self.assertIn('name', basemodel_dict)
        self.assertEqual(basemodel_dict['name'], "Test")
        self.assertIn('number', basemodel_dict)
        self.assertEqual(basemodel_dict['number'], 42)

    def test_BaseModel_dict_contains_all_keys(self):
        basemodel_dict = self.basemodel.to_dict()
        self.assertIn('id', basemodel_dict)
        self.assertIn('created_at', basemodel_dict)
        self.assertIn('updated_at', basemodel_dict)
        self.assertIn('__class__', basemodel_dict)

    def test_BaseModel_custom_attribute_in_dict(self):
        basemodel = BaseModel()
        basemodel.color = "red"
        basemodel_dict = basemodel.to_dict()
        self.assertIn('color', basemodel_dict)
        self.assertEqual(basemodel_dict['color'], "red")


if __name__ == "__main__":
    unittest.main()
