#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    a function that prints x elements of a list
    """

    try:
        count = 0
        for element in my_list:
            if count < x:
                print("{}".format(element), end="")
                count += 1
        print()
        return count
    except:
        return count
