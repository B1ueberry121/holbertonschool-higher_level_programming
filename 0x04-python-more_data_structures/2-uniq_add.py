#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    newlist = set(my_list)
    for x in newlist:
        result += x
    return result
