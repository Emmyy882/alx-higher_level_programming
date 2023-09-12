#!/usr/bin/python3
"""a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an object to a text file, using JSON...
    .....representation.
    # my_obj contains the text that should be written. while
    # filename is the name of the file to contain the written text.
    # you must use the width statement.
    """

    with open(filename, mode='w', encoding="utf-8") as file:
        """open function open the file 'filename' and writes to it"""
        file = write(json.dump(my_obj, filename))
