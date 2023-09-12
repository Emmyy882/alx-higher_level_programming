#!/usr/bin/python3
"""
implementation of the 'class_to_json' function that returns a dictionary
representing the JSON serialization of an object:
"""


class Student:
    """
    # Write a class Student that defines a student by:
    # VARIABLE(" "):
    # To JSON(self): Student to JSON
    # Return: Always 0. (Success)
    """
    """
    The class_to_json function takes an object obj as input and returns a
    JSON serializable dictionary representation of the object.
    """

    """
    The function first checks if the object is of type str, int, or bool.
    If so, it directly returns the object since these types are already
    JSON serializable.
    """

    def to_json(self, attrs=None):
        if '__dict__' in dir(obj):
            return obj.__dict__
