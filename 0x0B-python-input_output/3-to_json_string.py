#!/usr/bin/python3
'''Returns the JSON representation'''


def to_json_string(my_obj):
    '''Returns the JSON representation'''
    import json
    return json.dumps(my_obj)
