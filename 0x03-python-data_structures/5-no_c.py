#!/usr/bin/python3
def no_c(my_string):
    newstring = ""

    for idx in range(len(my_string)):
        if my_string[idx] != "C" and my_string[idx] != "c":
            newstring += my_string[idx]

    return (newstring)
