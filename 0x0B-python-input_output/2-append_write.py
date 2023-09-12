#!/usr/bin/python3
"""a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file and..
    ...returns the number of characters added.
    # if the file doesn't exist, it should be created.
    # you must use the with statement.
    """

    with open(filename, mode='a', encoding="utf-8") as file:
        """file open function....
        'filename' is the file to write string and ...
        'text' represents the string to be appended to the file..
        """
        chars_added = file.write(text)
        return chars_added
