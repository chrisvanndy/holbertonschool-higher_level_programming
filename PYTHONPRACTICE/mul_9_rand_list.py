#!/usr/bin/python3
import random
# define the list
# populate the list with random values 0-1000
rand100 = list(random.randint(1,1001) for i in range (100))
# filter list list for multiples of 9
print(list(filter((lambda x: x % 9 == 0), rand100)))
