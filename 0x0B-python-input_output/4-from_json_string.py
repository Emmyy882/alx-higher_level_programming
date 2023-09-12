#!/usr/bin/python3
"""a function that returnsan object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    a function that returns an object represented (python data structure)..
    ......represented by a JSON string.
    """
    return json.loads(my_str)
