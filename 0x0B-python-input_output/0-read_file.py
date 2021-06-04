#!/usr/bin/python3
'''Reads a text file'''


def read_file(filename=""):
    '''Reads a text file'''
    with open(filename, encoding='UTF8') as x:
        for y in x:
            print(y, end='')
