#!/usr/bin/python3
'''Class of a Square'''
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''Class of a Square inherited from Rectangle'''

    def __init__(self, size):
        '''Initialize size'''
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''String representation'''

        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
