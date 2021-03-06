#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This class defines the attributes of a Square'''

    def __init__(self, size=0):
        '''This method creates a new instance of Square'''
        self.__size = size

    def area(self):
        '''This method calculates the area of a square'''
        return self.__size ** 2

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        try:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")

    def my_print(self):
        '''Prints the square'''
        size = self.__size

        if size == 0:
            print()
        else:
            for x in range(size):
                for y in range(size):
                    print("#", end="")
                print()
