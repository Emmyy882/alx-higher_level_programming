#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    a function that replaces all occurences of
    an element in a new list
    """

    i = 0
    new_list = my_list[:]

    while i < len(new_list):
        if new_list[i] == search:
            new_list[i] = replace

        i += 1
    return new_list
