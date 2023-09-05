#!/usr/bin/python3
"""Defines a Rectangle"""


class Rectangle:
    """Represents a Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes rectangle.


        Args:
            width: width of rectangle
            height: height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """defining a getter method for the private attribute...
        width for the rectangle."""
        return self.__width

    @property
    def height(self):
        """defining a getter method for the private attribute...
        ...height for the Rectangle."""
        return self.__height
    

    @width.setter
    def width(self, value):
        """Get/Set the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


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
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """ '__str__()' method overrides the default string representation...
        ...of the object when using 'str(rectangle_instance)'....
        it creates a string representation of the triangle using the '#'..."""
        if self.width == 0 or self.height == 0:
            return ''
        else:
            res = list(map(
                lambda x: '#' * self.width + '\n' * (x != self.height - 1),
                range(self.height)))
            return ''.join(res)
            

    def __repr__(self):
        """This method returns a string representation of the object that can
        be used to recreate a new instance of the 'Rectangle' class
        """
        return 'Rectangle({:d}, {:d})'.format(self.width, self.height)

    def __del__(self):
        """prints a message for every deletion of a Rectangle"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
