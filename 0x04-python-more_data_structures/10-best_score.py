#!/usr/bin/python3
def best_score(a_dictionary):
    top = None
    score = 0
    if a_dictionary is None:
        return None
    if len(a_dictionary) > 0:
        for y, x in a_dictionary.items():
            if x > score:
                score = x
                top = y
    return top
