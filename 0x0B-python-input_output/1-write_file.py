#!/usr/bin/python3
'''Writes a string to text file'''


def write_file(filename="", text=""):
    '''Writes a string to text file'''

    with open(filename, 'w') as x:
        return x.write(text)
