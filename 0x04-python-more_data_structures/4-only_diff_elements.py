#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    a function that returns a set of all element
    s present in only one set
    """

    new_set = set()
    new_set = set_1 | set_2

    return new_set
