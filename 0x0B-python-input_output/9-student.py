#!/usr/bin/python3
'''Class of a student'''


class Student:
    '''Class of a student'''
    def __init__(self, first_name, last_name, age):
        '''Initializer for student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieves a dictionary representation'''
        return self.__dict__
