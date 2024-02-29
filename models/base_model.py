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