#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    a function that returns a set of all element
    s present in only one set
    """

    only_set1 = set_1 - set_2
    only_set2 = set_2 - set_1
    result_set = only_set1 | only_set2

    return result_set
