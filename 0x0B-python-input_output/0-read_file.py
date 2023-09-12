#!/usr/bin/python3
"""Function that reads a text file and prints its contents to stdout:
"""


def read_file(filename=""):
    """
    # Write a function that reads a text file (UTF8) and prints it to stdout:
    # Prototype: def read_file(filename=""):
    # You must use the with statement
    # VARIABLE(" "):
    # Read File(filename): 0. Read file
    """
    with open(filename, encoding='utf-8') as file:
        """'read_file' function is defined with an optional parameter
        'filename' represents the name of the file
        to be read"""
        file_contents = file.read()
        print(file_contents, end="")
