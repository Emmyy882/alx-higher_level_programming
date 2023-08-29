#!/usr/bin/python3
"""Defines a square"""


class Square:
    """represents a square"""
    __size

    def __init__(self, size):
        """
        Initializes a square with the given size

        Args:
            size (int): The size of the square.
        """
        self.__size = size
