#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    a function that adds all unique integers in
    a list.
    """

    unique_num = set()
    total_sum = 0

    for num in my_list:
        unique_num.add(num)

    for num in unique_num:
        total_sum += num
    return total_sum
