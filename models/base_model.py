#!/usr/bin/python3
"""Defines the Basemodel class that all other classes will inherit from"""
import datetime
import uuid
import models


class BaseModel:
    """Defines all common attributes/methods for other classes
    attirbutes:
        id (str): unique id for each instance
        created_at (datetime): time instance was created
        updated_at (datetime): time instance was updated"""

    def __init__(self, *args, **kwargs):
        """Initiates a new BaseModel instance
        args: non-keyworded arguments
        kwargs: keyworded arguments"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """String representation of the instance"""
        return ("[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the attribute "updated_at" with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Create and return a dictionnary containing values of the instance"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy
