#!/usr/bin/python3
"""Defines the tests for the BaseModel class."""

import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import time


class TestBaseModel(unittest.TestCase):
    basemodel = BaseModel()

    def test_createBaseModel(self):
        """test that an instance of BaseModel is properly created."""
        self.assertIsInstance(self.basemodel, BaseModel)

    def test_has_uuid(self):
        """test that the id of the BaseModel is a valid uuid."""
        self.assertTrue(self.basemodel.id)
        self.assertIsInstance(self.basemodel.id, str)

    def test_was_created_at(self):
        """test that the BaseModel was created at a valid time."""
        self.assertIsInstance(self.basemodel.created_at, datetime)

    def test_was_updated_at(self):
        """test that the BaseModel was updated at a valid time."""
        self.assertIsInstance(self.basemodel.updated_at, datetime)

    def test_save_BaseModel(self):
        """test that the BaseModel is saved to the JSON file."""
        self.basemodel.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_BaseModel_to_dict(self):
        """test that the BaseModel can be converted to a dictionnary."""
        dictionnary = self.basemodel.to_dict()
        self.assertIsInstance(dictionnary, dict)

    def test_load_BaseModel(self):
        """test that the BaseModel can be loaded from a dictionnary."""
        dictionnary = self.basemodel.to_dict()
        basemodel2 = BaseModel(**dictionnary)
        self.assertIsInstance(basemodel2, BaseModel)
        self.assertTrue(basemodel2.id, self.basemodel.id)

    def test_BaseModel_str(self):
        """test that the BaseModel can be converted to a string."""
        actual_str = self.basemodel.__str__()
        expected_start = "[BaseModel] ({})".format(self.basemodel.id)
        self.assertTrue(actual_str.startswith(expected_start))
        self.assertIn('id', actual_str)
        self.assertIn('created_at', actual_str)
        self.assertIn('updated_at', actual_str)
        basemodel2 = BaseModel()
        expected_format = "[BaseModel] ({}) {}".format(basemodel2.id,
                                                       basemodel2.__dict__)
        self.assertEqual(basemodel2.__str__(), expected_format)

    def test_BaseModel_init_with_kwargs(self):
        """test that the BaseModel is properly created with kwargs."""
        time = datetime.now()
        basemodel = BaseModel(id="1234", created_at=time.isoformat(),
                              updated_at=time.isoformat())
        self.assertEqual(basemodel.id, "1234")
        self.assertEqual(basemodel.created_at, time)
        self.assertEqual(basemodel.updated_at, time)

    def test_BaseModel_init_with_args(self):
        """test that the BaseModel is properly created with args."""
        basemodel = BaseModel("1234", "other_value")
        self.assertNotIn("1234", basemodel.__dict__.values())
        self.assertNotIn("other_value", basemodel.__dict__.values())

    def test_BaseModel_update_attributes(self):
        """test that the BaseModel is properly updated."""
        self.basemodel.name = "Test"
        self.basemodel.number = 42
        self.basemodel.save()
        basemodel_dict = self.basemodel.to_dict()
        self.assertIn('name', basemodel_dict)
        self.assertEqual(basemodel_dict['name'], "Test")
        self.assertIn('number', basemodel_dict)
        self.assertEqual(basemodel_dict['number'], 42)

    def test_BaseModel_dict_contains_all_keys(self):
        """test that the BaseModel dict contains all keys."""
        basemodel_dict = self.basemodel.to_dict()
        self.assertIn('id', basemodel_dict)
        self.assertIn('created_at', basemodel_dict)
        self.assertIn('updated_at', basemodel_dict)
        self.assertIn('__class__', basemodel_dict)

    def test_BaseModel_custom_attribute_in_dict(self):
        """tets that the BaseModel custom attribute is in the dict."""
        basemodel = BaseModel()
        basemodel.color = "red"
        basemodel_dict = basemodel.to_dict()
        self.assertIn('color', basemodel_dict)
        self.assertEqual(basemodel_dict['color'], "red")
        del basemodel.color
        self.assertFalse(hasattr(basemodel, 'color'))

    def test_BaseModel_json_serialization_deserialization(self):
        """test that the BaseModel can be serialized and deserialized."""
        self.basemodel.save()
        with open("file.json", "r") as f:
            objs = json.load(f)
        self.assertIn(self.basemodel.__class__.__name__ + "." +
                      self.basemodel.id, objs)
        obj_data = objs[self.basemodel.__class__.__name__ + "." +
                        self.basemodel.id]
        new_instance = BaseModel(**obj_data)
        self.assertEqual(self.basemodel.to_dict(), new_instance.to_dict())

    def test_updated_at_on_save(self):
        """test that the BaseModel updated_at attribute is updated on save."""
        original_updated_at = self.basemodel.updated_at
        time.sleep(1)
        self.basemodel.save()
        self.assertNotEqual(original_updated_at, self.basemodel.updated_at)

    def test_str_representation(self):
        """test that the BaseModel has a valid string representation."""
        base_model_instance = BaseModel()
        expected_str_format = "[{}] ({}) {}".format(
            base_model_instance.__class__.__name__,
            base_model_instance.id,
            base_model_instance.__dict__
        )
        actual_str_representation = base_model_instance.__str__()
        self.assertTrue(actual_str_representation.startswith(
            f"[BaseModel] ({base_model_instance.id})"))
        for key in base_model_instance.__dict__.keys():
            self.assertIn(key, actual_str_representation)
        self.assertEqual(actual_str_representation, expected_str_format)


if __name__ == "__main__":
    unittest.main()
