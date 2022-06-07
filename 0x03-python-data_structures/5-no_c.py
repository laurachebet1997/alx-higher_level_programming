#!/usr/bin/python3
def no_c(my_string):
    separatestring = ""
    for i in my_string:
        if i is not 'c' and i is not 'C':
            separatestring += i
    return(separatestring)
