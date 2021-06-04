#!/usr/bin/python3
'''Class of a student'''


class Student:
    '''Class of a student'''
    def __init__(self, first_name, last_name, age):
        '''Initializer for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Retrieves a dictionary representation'''
        clas = self.__dict__
        tmp = dict()
        if attrs is not None:
            for x in attrs:
                if x in clas:
                    tmp[x] = clas[x]
            return tmp
        return clas

    def reload_from_json(self, json):
        '''Replaces all attributes of student'''
        for x, y in json.items():
            self.__dict__[x] = y
