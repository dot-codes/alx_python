# #!/usr/bin/python3
# import random
# number = random.randint(-10000, 10000)
# # YOUR CODE HERE

# # print(number) 

# number1 = str(number)

# digit = (number1[-1])

# digitint = int(digit)

# if digitint > 5:
#     result = "and is greater than 5"
# if digitint == 0:
#     result = "and is 0"
# elif digitint < 6 and digitint > 0:
#     result = "and is less than 6 and not 0"



# print(f"Last digit of {number} is {digit} {result}")


import random

number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(number_str[-1])

if number < 0:
    last_digit = -last_digit  # Make the last digit negative for negative numbers

if last_digit > 5:
    result = "and is greater than 5"
elif last_digit == 0:
    result = "and is 0"
else:
    result = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {result}")
