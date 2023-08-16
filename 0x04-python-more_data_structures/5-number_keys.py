#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    a function that returns the number of keys
    in a dictionary
    """
    
    num = 0
    for k in a_dictionary.items():
        num += 1
    return num
