#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# output= NUMBER and  a.) is positive b.) is zero c.) is negative
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
elif number < 0:
    print("{} is negative".format(number))
