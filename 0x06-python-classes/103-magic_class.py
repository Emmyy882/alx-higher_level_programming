#!/usr/bin/python3
'''Python class definition of a bytecode.(Module)'''
import math


class MagicClass:
    '''
    # Write the Python class MagicClass that does exactly...
    # ....the same as the following Python bytecode:
    # VARIABLE(" "):
    # magic(int): ByteCode -> Python #5
    # Return: Always 0. (Success).
    '''
    '''The MagicClass' class has an '__init__' method that initializes the...
    ...the 'radius' arguments passed to the constructor is either an ...
    ... an integer or a float.'''

    def __init__(self, radius=0):
        '''If it is not, a TypeError is raised with an appropriate error...
        message, otherwise, the '__radius' attribute is set...
        ...to the value of 'radius'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''The 'area' method calculates the area of a circle using..'''
        '''..the formula '2 ** radius * pi...'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''The 'circumference' method calculates the circumference of....'''
        '''....a circle using the formula '2 * pi * radius...'''
        return 2 * math.pi * self.__radius
