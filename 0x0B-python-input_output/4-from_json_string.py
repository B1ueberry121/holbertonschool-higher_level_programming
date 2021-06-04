#!/usr/bin/python3
'''Returns an object'''


def from_json_string(my_str):
    '''Returns an object'''
    import json
    return json.loads(my_str)
