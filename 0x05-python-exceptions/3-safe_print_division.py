#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {:.lf}".format(result))
    except:
        result = None
        print("Inside result: {:}".format(result))
    finally:
        #print("Inside result: {:.lf}".format(result))
        return result
