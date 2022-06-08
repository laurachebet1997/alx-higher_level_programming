#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return(0)
    else:
        num1, num2 = 0, 0
        for x, y in my_list:
            num1 += x*y
            num2 += y
        return(num1/num2)
