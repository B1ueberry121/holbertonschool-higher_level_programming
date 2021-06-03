#!/usr/bin/python3
'''Returns True if the object is instance of a class'''


def is_kind_of_class(obj, a_class):
    '''Returns True if object is instances of a class'''

    if isinstance(obj, a_class):
        return True
    return False
