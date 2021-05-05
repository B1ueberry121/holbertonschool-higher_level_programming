#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    bignum = my_list[0]

    for idx in range(len(my_list)):
        if my_list[idx] > bignum:
            bignum = my_list[idx]

    return (bignum)
