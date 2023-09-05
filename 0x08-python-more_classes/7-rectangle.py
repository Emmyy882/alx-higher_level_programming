#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle.


        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Get/Set the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get/Set height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ '__str__()' method overrides the default string representation...
        ...of the object when using 'str(rectangle_instance)'....
        it creates a string representation of the triangle using the '#'..."""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        rectangle_str = ""
        for i in range(self.height):
            string += str(self.print_symbol) * self.width
            if i < self.height - 1:
                string += "\n"
        return string
            

    def __repr__(self):
        """This method returns a string representation of the object that can
        be used to recreate a new instance of the 'Rectangle' class
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every deletion of a Rectangle"""
        print("Bye rectangle...")     
