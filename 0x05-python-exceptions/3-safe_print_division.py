#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        result = None
    finally:
        if result != None:
            print("Inside result: {:.1f}".format(result))
        else:
            return result
