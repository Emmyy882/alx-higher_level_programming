#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        Initializing size for a new square.

        Args:
            size (int): size for the new square.
        """

        self.size = size

    @property
    def size(self):
        """retrieve the value set."""

        return self.__size

    @size.setter
    def size(self, value):
        """set the value passed to it"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This function returns the cuurent square area"""

        return self.__size ** 2
