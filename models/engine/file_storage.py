#!/usr/bin/python3
"""Module for FileStorage class definition.

This module defines the FileStorage class, which is responsible for
serializing instances to a JSON file and deserializing JSON file to instances.
It includes methods to add new objects to storage, save the current state to
a file, and reload objects from the file.
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """Class for serializing instances to and deserializing instances from
    a JSON file.

    Attributes:
        __file_path (str): Path to the JSON file used for serialization and
                        deserialization.
        __objects (dict): Dictionary to store all objects by '<class name>.id'.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary `__objects`.

        Returns:
            dict: The dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Add a new object to the storage dictionary.

        Args:
            obj: The object to be added to storage.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize the `__objects` dictionary to the JSON file."""
        with open(self.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in self.__objects.items()}, f
            )

    def reload(self):
        """Deserialize the JSON file to `__objects` if `__file_path` exists."""
        try:
            with open(self.__file_path, 'r') as f:
                object_dict = json.load(f)
                for key, value in object_dict.items():
                    cls_name = key.split('.')[0]
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
