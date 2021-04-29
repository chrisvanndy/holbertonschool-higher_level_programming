#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    for numbers in my_list:
        if numbers not in new_list:
            new_list.append(numbers)
    return sum(new_list)
