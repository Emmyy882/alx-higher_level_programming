#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    """ 
        getting the length of passed arguments 
        in command line 
    """
    num_args = len(sys.argv)

    if num_args - 1 != 3:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        exit(1)

    else:
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])

        if operator == '+':
            result = add(a, b)
            print(f"{a} {operator} {b} = {result}")

        elif operator == '-':
            result = sub(a, b)
            print(f"{a} {operator} {b} = {result}")

        elif operator == '*':
            result = mul(a, b)
            print(f"{a} {operator} {b} = {result}")

        elif operator == '/':
            result = div(a, b)
            print(f"{a} {operator} {b} = {result}")

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
