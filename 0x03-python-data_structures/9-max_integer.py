#!/usr/bin/python3
def max_integer(my_list=[]):
    # if the list is empty return "None"
    if not my_list:
        return (None)
    else:
        my_list.sort()
    return (my_list[-1])
