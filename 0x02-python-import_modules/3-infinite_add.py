#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    i = 1
    result = 0
    num_args = len(sys.argv)

    if num_args == 1:
        print("{}".format(result))
    else:
        while i > 0 and i < num_args:
            result = result + int(sys.argv[i])
            i = i + 1
        print("{}".format(result))
