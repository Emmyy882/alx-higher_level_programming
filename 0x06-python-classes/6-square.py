#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """
        Initializing size for a new square.

        Args:
            size (int): size for the new square.
            position (int, int): The position of the new square.
        """

        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(num, int) and num >= 0 for num in value):
            """If the size is less than '0', it raises a 'ValueError'
            Exception with the message, 'size must be >= 0'"""
            """Otherwise, it assigns the provided 'size' value to the Private
            ...Instance attribute '__size'"""
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """This function returns the cuurent square area"""

        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""

        if self._size == 0:
            """if the size is 0, print an empty line"""
            print("")
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * sellf.position[0] + "#" * self.size)
