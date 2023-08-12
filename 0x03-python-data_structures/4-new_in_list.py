#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    a function that replaces an element in a list at a specific position without modifying the original list.
    """

    new_list = list.copy(my_list)
    if idx < 0:
        return new_list
    elif idx > (len(new_list) - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list
