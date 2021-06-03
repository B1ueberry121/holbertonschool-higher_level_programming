#!/usr/bin/python3
'''Square class'''
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    '''Class of a square inherited from Rectangle'''

    def __init__(self, size):
        '''Initialize size'''
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)
        self.__size = size
