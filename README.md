# AirBnB Clone - The Console

## Overview
Welcome to the AirBnB clone project! This project is the first step towards building a full web application: the AirBnB clone. This initial phase involves creating a command interpreter for managing AirBnB objects, laying the foundation for the subsequent web static, MySQL, API, and web dynamic projects.

## Objectives
- Learn how to create a Python package
- Explore how to create a command interpreter in Python using the `cmd` module
- Understand unit testing and implement tests in a large project
- Practice serializing and deserializing Class instances
- Handle JSON file reading and writing
- Manage datetime and UUID
- Understand the usage of `*args` and `**kwargs`
- Practice handling named arguments in functions

## Features
- A parent class `BaseModel` to manage initialization, serialization, and deserialization of instances
- Serialization and deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
- Classes for AirBnB (`User`, `State`, `City`, `Place`, etc.) that inherit from `BaseModel`
- A file storage engine to persist objects to a file (JSON file)
- A console (command interpreter) to manage the objects of the project

## Command Interpreter
The console is a command-line interpreter that allows management of the application's objects. It supports commands like:
- `create`: Create a new instance
- `show`: Show an instance based on its ID
- `destroy`: Destroy an instance based on its ID
- `all`: Show all instances of a class or all classes
- `update`: Update an instance based on its ID
- `quit` or `EOF`: Exit the program

## Requirements
- Python scripts are executable and follow the PEP 8 style guide
- All files end with a new line
- Unit tests are included
- Projects include a `README.md` and `AUTHORS` file

## Setup
To start the console, run:
```bash
./console.py
```

The console works in both interactive and non-interactive modes, allowing for flexibility in how commands are executed.

## Usage Examples
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create BaseModel
(hbnb) show BaseModel 1234-5678
(hbnb) destroy BaseModel 1234-5678
(hbnb) all
(hbnb) quit
$
```

In non-interactive mode:
```bash
echo "help" | ./console.py
```

## File Storage
The project implements a simple file storage system using JSON serialization and deserialization. It involves converting class instances to dictionaries for easy JSON storage and retrieval.

## Project Structure
- `models/` directory contains all class definitions
- `models/engine/` directory contains the file storage class
- `tests/` directory contains all unit tests
- `console.py` is the entry point of the command interpreter

## Testing
Unit tests can be run with the following command:
```bash
python3 -m unittest discover tests
```

## Collaboration
This project is developed by Thomas Viard and Nicolas Taillepierre.

*Project developed as part of the curriculum at Holberton School.*
