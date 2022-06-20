#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.lf}".format(result))
    except ZeroDivisionError, ValueError:
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result
