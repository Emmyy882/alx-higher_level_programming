#!/usr/bin/python3
"""
script that adds command-line arguments to a Python list and
saves them to a file:
"""
import sys
from os import path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"
"""
# Write a class Student that defines a student by:
# VARIABLE(" "):
# To JSON(self): Student to JSON
# Return: Always 0. (Success)
"""
"""
The script starts by importing the sys module for accessing command-line
arguments and the path module from the os package for working with file paths.
"""
"""
The save_to_json_file function from the 5-save_to_json_file.py module and the
load_from_json_file function from the 6-load_from_json_file.py module
are imported.
"""
# Check if the file exists
if path.exists(filename):
    # Load the existing list from the file
    my_list = load_from_json_file(filename)
else:
    # Create an empty list if the file doesn't exist
    my_list = []

# Add the command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
