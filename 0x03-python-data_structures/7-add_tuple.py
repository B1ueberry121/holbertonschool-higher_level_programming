#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    newtuple = [0, 0]

    for idx in range(2):
        try:
            newtuple[idx] += tuple_a[idx]
        except:
            newtuple[idx] += 0
        try:
            newtuple[idx] += tuple_b[idx]
        except:
            newtuple[idx] += 0

    return tuple(newtuple)
