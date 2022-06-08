#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list1 = set(my_list)
    return(list(reduce(lambda x,y: x+y, my_list1)))
