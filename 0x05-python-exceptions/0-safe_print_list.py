#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numprint = 0
    for element in range(0, x):
        try:
            print(my_list[element], end="")
        except:
            break
        numprint = (numprint + 1)
    print()
    return numprint
