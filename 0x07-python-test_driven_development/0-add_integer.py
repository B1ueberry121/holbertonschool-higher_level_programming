#!/usr/bin/python3
'''function that adds two integers'''


def add_integer(a, b=98):
    '''adds integers if not integers return error'''
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)