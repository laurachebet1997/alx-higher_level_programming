#!/usr/bin/python3
def no_c(my_string):
    separatestring = ""
    for i in my_string:
        if i != 'c' or i != 'C':
            separatestring += i
    return(separatestring)
