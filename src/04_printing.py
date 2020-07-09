"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""
import math

x = 10
y = 2.24552
z = "I like turtles!"

# need to adjust to return properly rounded float


def round_up(num, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(num * multiplier) / multiplier

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"


print("x is %d, y is %f, z is %s" % (x, round_up(y), z))

# Use the 'format' string method to print the same thing
print('x is {}, y is {}, z is {}'.format(x, round_up(y), z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {round_up(y)}, z is {z}")
