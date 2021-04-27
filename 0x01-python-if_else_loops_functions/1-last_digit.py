#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    num = number * (-1)
    last = num % 10
else:
    last = number % 10
six = "is less than 6 and not 0"
if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(number, last))
else:
    print("Last digit of {} is {} and is {}".format(number, last, six))
