#!/usr/bin/python3
'''Write a class rectangle'''


class Rectangle:
    '''Defines a basic rectangle with height and width'''
    def __init__(self, width=0, height=0):
        '''Initializes values for height and width'''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Getter method for the value of width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Setter method for the value of width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Getter method for the value of height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter method for the value of height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
