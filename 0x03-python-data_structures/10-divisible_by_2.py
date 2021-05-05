#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:

        newlist = my_list.copy()

        for idx in range(len(my_list)):
            if my_list[idx] % 2 == 0:
                newlist[idx] = True
            else:
                newlist[idx] = False

        return (newlist)
