#!/usr/bin/python3
"""
The entry point of the command interpreter.
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
    Args:
        Cmd : built in class
    """
    prompt = '(hbnb) '
    list_class = ["BaseModel", "User", "City",
                  "Amenity", "Place", "State", "Review"]

    list_function = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            my_class = arg.split('.')
            my_func = my_class[1].split('(')
            param = my_func[1].split(')')
            if my_class[0] in HBNBCommand.list_class and \
               my_func[0] in HBNBCommand.list_function:
                arg = my_func[0] + ' ' + my_class[0] + ' ' + param[0]
        return arg

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, arg):
        """Exits the program with <Ctrl+D>
        """
        print()
        quit()

    def emptyline(self):
        """Handles the emptyline"""
        pass

    def do_create(self, arg):
        """Creates a new instance
        """
        if len(arg) == 0:
            print("** class name missing **")

        elif arg not in HBNBCommand.list_class:
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

        elif list_arg[0] not in HBNBCommand.list_class:
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

        elif list_arg[0] not in HBNBCommand.list_class:
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

    def do_all(self, arg):  # sourcery skip: for-append-to-extend
        """Prints all string representation of all instances
        based or not on the class name
        """
        dict_all_obj = storage.all()
        list_obj = []

        if len(arg) == 0:
            for key, vals in dict_all_obj.items():
                list_obj.append(str(vals))
            print(list_obj)

        elif arg in HBNBCommand.list_class:
            for keys, vals in dict_all_obj.items():
                if vals.__class__.__name__ == arg:
                    list_obj.append(str(vals))
            print(list_obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute
        """
        list_arg = arg.split(" ")

        if len(arg) == 0:
            print("** class name missing **")

        elif list_arg[0] not in HBNBCommand.list_class:
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

    def do_count(self, arg):
        """Count the number of instances of a class"""
        count = 0
        list_arg = arg.split(" ")
        dict_all_obj = storage.all()
        for v in dict_all_obj.values():
            if v.__class__.__name__ == list_arg[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
