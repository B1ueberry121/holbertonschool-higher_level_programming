#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    newlist = a_dictionary.copy()
    for idx, x in newlist.items():
        newlist[idx] = x * 2
    return newlist
