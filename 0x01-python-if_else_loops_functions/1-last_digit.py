#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10

if digit > 5:
    string = "and is greater than 5"
elif digit == 0:
    string = "and is 0"
elif digit < 6 and digit != 0:
    string = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d} {:s}".format(number, digit, string))
