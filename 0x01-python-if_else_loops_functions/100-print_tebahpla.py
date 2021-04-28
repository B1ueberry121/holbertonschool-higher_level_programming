#!/usr/bin/python3
counter = 0
swp = ord('A') - ord('a')
for alpha in range(ord('z'), ord('a') - 1, -1):
    if counter % 2 == 1:
        print("{}".format(chr(alpha + swp)), end="")
    else:
        print("{}".format(chr(alpha)), end="")
    counter += 1
