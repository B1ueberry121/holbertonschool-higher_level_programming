#!/usr/bin/pyhton3
'''Function that prints text divided into new lines'''


def text_indentation(text):
    '''Prints text in new lines'''
    if type(text) is not str:
        raise TypeError("text must be a string")
    counter = 0
    for x in text:
        if x == " " and counter == 1:
            continue
        print(x, end="")
        counter = 0
        if x in [".", "?", ":"]:
            print("\n")
            counter = 1
