#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# output="Last digit of {number} is [-1] and is a.) >5 b.)<6 c.) =0
str1 = "Last digit of "
if number >= 0:
    lastnum = number % 10
elif number < 0:
    lastnum = (number % 10) * -1
if lastnum > 5:
    print("{}{} is {} and is is greater than 5".format(str1, number, lastnum))
elif lastnum == 0:
    print("{}{} is {} and is 0".format(str1, number, lastnum))
else:
    print("{}{} is {} and is less than 6 and not 0"
          .format(str1, number, lastnum))
