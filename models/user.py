#!/usr/bin/python3
"""Defines the User class that inherits from BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """It is the user class that inherits from BaseModel.
    It has the following attributes:
    email: string - empty string
    password: string - empty string
    first_name: string - empty string
    last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    