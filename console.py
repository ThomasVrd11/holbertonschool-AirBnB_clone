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
    class_listing = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        exit()

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.class_listing:
            print("** class doesn't exist **")
            return
        
        new_instance = eval(arg)()
        
