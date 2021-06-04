#!/usr/bin/python3
'''Writes an object to a text file'''


def save_to_json_file(my_obt, filename):
    '''Writes an object to a text file'''
    import json
    with open(filename, 'w') as x:
        json.dump(my_obt, x)
