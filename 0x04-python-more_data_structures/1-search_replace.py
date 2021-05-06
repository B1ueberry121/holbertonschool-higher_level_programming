#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = my_list.copy()
    for idx in range(len(my_list)):
        if my_list[idx] == search:
            newlist[idx] = replace
    return newlist
