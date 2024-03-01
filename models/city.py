#!/usr/bin/python3
"""Defines the City class that inherits from BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """It is the city class that inherits from BaseModel.
    It has the following attributes:
    state_id: string - empty string: it will be the State.id
    name: string - empty string
    """

    state_id = ""
    name = ""
