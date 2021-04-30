#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    # multiply the members of each touple 
    products = []
    for i in my_list:
        products.append(i[0] * i[1])
    # add the individual result of tuple multiplation
    sum1 = sum(products)
    # sum the second member of the touples
    weight = sum(i[1] for i in my_list)
    # divide the (sum of multiplication) by (sum of second member)
    average = sum1 / weight
    return average
