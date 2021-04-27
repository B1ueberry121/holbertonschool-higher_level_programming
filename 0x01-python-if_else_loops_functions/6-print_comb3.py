#!/usr/bin/python3
for dig1 in range(0, 10):
    for dig2 in range(dig1 + 1, 10):
        print("{:d}{:d}".format(dig1, dig2), end="")
        if dig1 * 10 + dig2 != 89:
            print(", ", end="")
print("")
