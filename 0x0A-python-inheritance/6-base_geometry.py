#!/usr/bin/python3
"""Implementation of the 'BaseGeometry' class with the 'area' method:"""


class BaseGeometry:
    """
    # Write a class BaseGeometry (based on 5-base_geometry.py).
    # Exception with the message area() is not implemented.....
    # VARIABLE(" "):
    # Base Geometry(area): Improve Geometry
    # Return: Always 0. (Success)
    """
    """
    The 'BaseGeometry' class now includes the 'area' method, which raises...
    an exception with the message 'area() is not implemented'"""
    def area(self):
        raise Exception("area() is not implemented")
