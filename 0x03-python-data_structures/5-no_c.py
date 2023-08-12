#!/usr/bin/python3

def no_c(my_string):
    """
    removes all characters c and C from a string
    """

    new_string = " "
    for char in my_string:
        if char != 'C' and char != 'c':
            new_string += char
    return new_string
