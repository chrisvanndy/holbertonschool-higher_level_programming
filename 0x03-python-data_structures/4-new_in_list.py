#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx > 0:
        list_copy = my_list
        return (list_copy)
    if idx > (len(my_list)):
        list_copy2 = my_list
        return(list_copy2)
    if idx <= (len(my_list)) - 1:
        list_copy3 = my_list
        list_copy3[idx] = element
        return (list_copy3)
