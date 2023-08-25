#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# print(number)

number1 = str(number)

digit = (number1[-1])

digitint = int(digit)

if digitint > 5:
    result = "and is greater than 5"
if digitint == 0:
    result = "and is 0"
elif digitint < 6 and digitint > 0:
    result = "and is less than 6 and not 0"


print(f"Last digit of {number} is {digit} {result}")