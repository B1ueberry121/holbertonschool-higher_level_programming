#!/usr/bin/python3
'''Function that prints text divided into new lines'''


def text_indentation(text):
    '''Prints text in new lines'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    checker = 0
    for x in text:
        if x == " " and checker == 1:
            continue
        print(x, end="")
        checker = 0
        if x in [".", "?", ":"]:
            print("\n")
            checker = 1
