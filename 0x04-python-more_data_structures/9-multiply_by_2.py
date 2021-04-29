#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    copy.update((x, y * 2) for x, y in copy.items())
    return copy
