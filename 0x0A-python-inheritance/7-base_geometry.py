#!/usr/bin/python3
'''Class of BaseGeometry'''


class BaseGeometry():
    '''Class of BaseGeometry'''

    def area(self):
        '''Area not defined'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates the value'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
