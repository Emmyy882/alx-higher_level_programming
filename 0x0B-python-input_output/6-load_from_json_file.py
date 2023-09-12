#!/usr/bin/python3
"""
Function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """
    # Write a function that creates an Object from a “JSON file”:
    # Prototype: def load_from_json_file(filename):
    # VARIABLE(" "):
    # Load From File(filename): Create object from a JSON file
    # Return: Always 0. (Success)
    """
    """
    The 'load_from_json_file' function is defined with one parameter:
    'filename'
    'which represents the name of the JSON file to load the object from
    """
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
