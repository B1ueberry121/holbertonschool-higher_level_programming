#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    agv = sys.argv
    agc = len(agv)
    if agc == 1:
        print("0 arguments.")
    elif agc == 2:
        print("{:d} argument:".format(agc - 1))
    else:
        print("{:d} arguments:".format(agc -1))
    for ind in range(1, agc):
        print("{:d}: {:s}".format(ind, agv[ind]))
