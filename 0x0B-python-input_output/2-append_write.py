#!/usr/bin/python3
'''Appends a string to a text'''


def append_write(filename="", text=""):
    '''Appends a string to a text'''

    with open(filename, 'a') as x:
        return x.write(text)
