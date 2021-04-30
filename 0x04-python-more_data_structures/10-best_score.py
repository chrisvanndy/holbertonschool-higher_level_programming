#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    val = list(a_dictionary.values())
    key = list(a_dictionary.keys())
    return key[val.index(max(val))]
