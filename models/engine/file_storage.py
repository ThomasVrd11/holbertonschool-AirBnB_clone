#!/usr/bin/python3
import json
import os


class FileStorage:
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        with open(self.__filename, "w") as newfile:
            file = json.dumps(self.__objects)
            newfile.write(file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                self.__objects = json.load(file)
