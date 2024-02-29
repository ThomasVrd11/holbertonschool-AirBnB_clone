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
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        token = arg.split()
        dict_objs = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif token[0] not in self.class_listing:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(token[0], token[1])
            if instance_key not in dict_objs.keys():
                print("** no instance found **")
            else:
                print(dict_objs[instance_key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
        token = arg.split()
        dict_objs = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        elif token[0] not in self.class_listing:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(token[0], token[1])
            if instance_key not in dict_objs.keys():
                print("** no instance found **")
            else:
                del dict_objs[instance_key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name
        it can be used with or without class name"""
        dict_objs = storage.all()
        list_objs = []
        
        if len(arg) == 0:
            for keys, values in dict_objs.items():
                list_objs.append(str(values))
            print(list_objs)
            
        elif arg in self.class_listing:
            for keys, values in dict_objs.items():
                if values.__class__.__name__ == arg:
                    list_objs.append(str(values))
            print(list_objs)

        else:
            print("** class doesn't exist **")
            
    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        token = arg.split(" ")
        dict_objs = storage.all()
        
        if len(arg) == 0:
            print("** class name missing **")

        elif token[0] not in self.class_list:
            print("** class doesn't exist **")

        elif len(token) < 2:
            print("** instance id missing **")

        else:
            instance_key = "{}.{}".format(token[0], token[1])

            if instance_key not in dict_objs.keys():
                print("** no instance found **")

            elif len(token) < 3:
                print("** attribute name missing **")

            elif len(token) < 4:
                print("** value missing **")

            else:
                setattr(dict_objs[instance_key], token[2], token[3])
                storage.save()
                
if __name__ == "__main__":
    HBNBCommand().cmdloop()
