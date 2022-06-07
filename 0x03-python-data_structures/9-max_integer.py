#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        start_num = my_list[0]
        for i in my_list:
            if start_num < i:
                start_num = i
        return start_num
