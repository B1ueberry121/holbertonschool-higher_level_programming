#!/usr/bin/python3
'''Returns True if the object is an instance of a class'''


def inherits_from(obj, a_class):
    '''Returns True if object is inherited'''

    if issubclass(type(obj), a_class):
        return True
    return False
