#!/usr/bin/python3
import sys

i = 1
result = 0
num_args = len(sys.argv)

if num_args == 1:
    print(f"{result}")
else:
    while i > 0 and i < num_args:
        result = result + int(sys.argv[i])
        i = i + 1
    print(f"{result}")
