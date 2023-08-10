#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num_args = len(sys.argv) - 1
    i = 1

    if num_args == 0:
        print("0 arguments.")

    elif num_args == 1:
        print("{} argument:\n1: {}".format(num_args, sys.argv[1]))

    else:
        print("{} arguments:".format(num_args))

        while i > 0 and i <= num_args:
            print("{}: {}".format(i, sys.argv[i]))
            i = i + 1
