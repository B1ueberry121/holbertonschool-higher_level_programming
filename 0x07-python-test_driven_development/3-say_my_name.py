#!/usr/bin/pyhton3
'''Function that prints a name'''


def say_my_name(first_name, last_name=""):
    '''Prints a name is <fist_name> <last_name>'''

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))