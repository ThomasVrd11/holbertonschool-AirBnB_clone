#!/usr/bin/python3
"""This is the console module.
This module contains the HBNBCommand class that is the entry point of the command interpreter.
"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that is the entry point of the command interpreter."""
    prompt = '(hbnb)'
    class_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True
    
    