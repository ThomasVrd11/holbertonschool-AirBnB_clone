#!/usr/bin/python3
"""
The entry point of the command interpreter.
Very simple console for the AirBnB project.
what can be done with this console:
    - Create a new object (ex: a new User or a new Place)
    - Retrieve an object from a file, a database etc
    - Do operations on objects (count, compute stats, etc)
    - Update attributes of an object
    - Destroy an object
    - Show all objects, or show all instances of a class
    - Show an object
    - Update an object
    - Destroy an object
    - Quit the console
    - EOF (End Of File) to exit the program
Usage:
    - Run the console and type help to see the commands
    - Run the console and type <class name>.<command>(<parameters>)
    - Run the console and type <class name>.<command>(<id>, <attribute>, <value>)
    - Run the console and type <class name>.<command>(<id>)
    - Run the console and type <class name>.<command>()
    - Run the console and type <command>()
    - Run the console and type <command>(<id>)
    - Run the console and type <command>(<id>, <attribute>, <value>)
    - Run the console and type <command>(<class name>)
    - Run the console and type <command>(<class name>, <id>)
    - Run the console and type <command>(<class name>, <id>, <attribute>, <value>)
    - Run the console and type <command>(<class name>, <id>, <attribute>)
"""

from models import storage
import cmd
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    Class for the line-oriented command interpreters.
    It is used to create line-oriented command interpreters.
    We can use this class to create a simple command line interpreter.
    """
    promptdefou = '(hbnb) '
    class_listing = ["BaseModel", "User", "City",
                     "Amenity", "Place", "State", "Review"]

    funct_listing = ['create', 'show', 'update', 'all', 'destroy']

    def precmd(self, arg):
        """parses command input
        apparently forced to call it precmd by cmd module
        it is called before the command is executed"""
        if '.' in arg and '(' in arg and ')' in arg:
            my_class = arg.split('.')
            my_func = my_class[1].split('(')
            param = my_func[1].split(')')
            if my_class[0] in HBNBCommand.class_listing and \
               my_func[0] in HBNBCommand.funct_listing:
                arg = my_func[0] + ' ' + my_class[0] + ' ' + param[0]
        return arg

    def do_quit(self, arg):
        """Quit command to exit the program cleanly
        """
        quit()

    def do_EOF(self, arg):
        """Exits the program with <Ctrl+D and prints nothing for clean exit >
        """
        print()
        quit()

    def emptyline(self):
        """Handles the emptyline scenario and does nothing"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        """
        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in HBNBCommand.class_listing:
            print("** class doesn't exist **")

        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id.
        """
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif list_arg[0] not in HBNBCommand.class_listing:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                print(dict_all_obj[string])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id and save
        into the JSON file)
        """
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")
            return

        elif list_arg[0] not in HBNBCommand.class_listing:
            print("** class doesn't exist **")
            return

        elif len(list_arg) < 2:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            else:
                del (dict_all_obj[string])
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        it can be used to print all instances of a class
        """
        dict_all_obj = storage.all()
        list_obj = []

        if len(arg) == 0:
            for key, vals in dict_all_obj.items():
                list_obj.append(str(vals))
            print(list_obj)

        elif arg in HBNBCommand.class_listing:
            for keys, vals in dict_all_obj.items():
                if vals.__class__.__name__ == arg:
                    list_obj.append(str(vals))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        It can be used to update an instance of a class
        """
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")

        elif list_arg[0] not in HBNBCommand.class_listing:
            print("** class doesn't exist **")
            return

        elif len(list_arg) == 1:
            print("** instance id missing **")
            return

        else:
            dict_all_obj = storage.all()
            string = f'{list_arg[0]}.{list_arg[1]}'

            if string not in dict_all_obj.keys():
                print("** no instance found **")

            elif len(list_arg) == 2:
                print("** attribute name missing **")
                return

            elif len(list_arg) == 3:
                print("** value missing **")
                return

            else:
                setattr(dict_all_obj[string], list_arg[2], list_arg[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
