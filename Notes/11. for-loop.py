# Loops in Python
# Loops are used in Python in order to execute a block of code repeatedly until a given condition is satisfied.
# There are 2 types of Loops in Python:
# 1. For Loop
# 2. While loop

# For Loops in Python:
# For loops can be used to iterate through a sequence of Iterable objects.
# Iterable objects can be a String, Dictionaries, tuples, lists, sets etc..

# For Looping through a String

name = "PYTHON"

for i in name:
    print(i)

# For Looping through a List

items = ["EGG", "BREAD", "BISCUITS", "CHOCOLATE", "ICECREAM"]

for item in items:
    print(item)


# Using range() Function:
# range() is used to return a sequence of numbers
# By deafult, it start from 0 and increments by 1 until the number specified as argument

# Syntax: range(start, end, step)
# If start is 1 and end is 10, then it returns numbers from "start to end-1"
# step indicates the increment value.

for num in range(0, 100, 10):
    print(num)