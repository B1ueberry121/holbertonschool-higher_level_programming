#!/usr/bin/python3
'''This module contains the Square class'''


class Square:
    '''This class defines the attribute of a Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''This method creates a new instance of Square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Getter method for size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Setter method for size'''
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        '''Getter for position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Setter for position'''
        if type(value) is tuple and len(value) == 2 and\
           type(value[0]) is int and type(value[1]) is int and\
           value[0] >= 0 and value[1] >= 0:
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        '''This method calculates the are of a square'''
        return self.size ** 2

    def my_print(self):
        '''Print the square'''
        size = self.size
        x, y = self.position

        if size == 0:
            print("")
        else:
            for l in range(y):
                print("")
            for w in range(size):
                for z in range(x):
                    print(" ", end="")
                for k in range(size):
                    print("#", end="")
                print("")
