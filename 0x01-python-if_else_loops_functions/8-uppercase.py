#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            convertion = ord('A') - ord('a')
            x = chr(ord(x) + convertion)
        print("{}".format(x), end="")
    print("")
