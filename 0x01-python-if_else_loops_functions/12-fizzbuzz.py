#!/usr/bin/python3
def fizzbuzz():
    x = 1
    while x < 101:
        if x % 3 != 0 and x % 5 != 0:
            print("{:d}".format(x), end="")
        else:
            if x % 3 == 0:
                print("Fizz", end="")
            if x % 5 == 0:
                print("Buzz", end="")
        if x != 100:
            print(" ", end="")
        x += 1
    print(" ", end="")
