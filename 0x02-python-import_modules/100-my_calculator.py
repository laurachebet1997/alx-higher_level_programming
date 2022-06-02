#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def my_calc(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator_sign = argv[2]
    b = int(argv[3])
    if operator_sign == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, operator_sign, b, add(a, b)))
    elif operator_sign == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, operator_sign, b, sub(a, b)))
    elif operator_sign == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, operator_sign, b, mul(a, b)))
    elif operator_sign == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, operator_sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    my_calc(sys.argv)
