#!/usr/bin/python3
'''Creates an object from JSON file'''


def load_from_json_file(filename):
    '''Creates an object from JSON file'''
    import json
    with open(filename) as x:
        return json.load(x)
