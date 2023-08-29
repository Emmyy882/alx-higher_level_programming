#!/usr/bin/python3
"""defines a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        Initializing a size for new square.

        Args:
            size (int): size for the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This function returns the current square area"""

        return self.__size ** 2
