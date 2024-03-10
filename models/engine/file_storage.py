#!/usr/bin/python3
""" This module initializes the models package.
    It creates a FileStorage object called storage and calls reload() method
    on it to deserialize the JSON file to __objects.
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
    """Handles storage of all models in JSON format"""

    def __init__(self):
        """Initialize the storage system"""
        self.__file_path = "file.json"
        self.__objects = {}

        self.__class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
        }

    def all(self):
        """returns all objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionnary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj
                    in self.__objects.items()}
        with open(self.__file_path, "w") as newfile:
            json.dump(obj_dict, newfile)

    def reload(self):
        """Deserialize the JSON file to __objects"""
        if os.path.exists(self.__file_path) is True:
            try:
                with open(self.__file_path, "r") as file:
                    obj_dicts = json.load(file)
                for obj_id, obj in obj_dicts.items():
                    class_name = obj["__class__"]
                    if class_name in self.__class_map:
                        cls = self.__class_map[class_name]
                        self.new(cls(**obj))
            except Exception as excep:
                print("Error loading JSON file: {}".format(excep))
