#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortorder = sorted(a_dictionary.keys())
    for idx in sortorder:
        print("{}: {}".format(idx, a_dictionary[idx]))
