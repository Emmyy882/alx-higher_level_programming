#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    pronts all integers of a list in reverse order
    """
    
    if my_list is None:
        return

    my_list.reverse()
    while i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
