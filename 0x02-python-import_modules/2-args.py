#!/usr/bin/python3
import sys

num_args = len(sys.argv)
i = 1

if num_args == 1:
    print(f"0 arguments.")

elif num_args == 2:
    num_args = num_args - 1
    print(f"{num_args} argument:\n1: {sys.argv[1]}")

elif num_args > 2:
    print(f"{num_args - 1} arguments:")

    while i > 0 and i < num_args:
        print(f"{i}: {sys.argv[i]}")
        i = i + 1
