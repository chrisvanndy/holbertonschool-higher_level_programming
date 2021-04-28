#!/usr/bin/python
def add_tuple(tuple_a=(), tuple_b=()):
    # if a touple is smaller than two values = 0
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    # newtuple = tuple1 + tuple2
    num1 = tuple_a[0] + tuple_b[0]
    num2 = tuple_a[1] + tuple_b[1]
    return (num1, num2)
