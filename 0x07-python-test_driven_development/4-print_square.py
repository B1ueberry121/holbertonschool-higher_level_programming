#!/usr/bin/python3
'''Function that prints a square with #'''


def print_square(size):
    '''Prints a square of size'''

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size musr be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
