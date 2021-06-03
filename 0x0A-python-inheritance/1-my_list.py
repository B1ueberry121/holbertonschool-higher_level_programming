#!/usr/bin/python3
'''Class of a list'''


class MyList(list):
    '''class from a list'''
    def print_sorted(self):
        '''prints a sorted list'''

        print(sorted(self))
