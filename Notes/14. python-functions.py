# Functions in Python
# When we want to execute certain logic repeatedly in multiple places in the program, we can use a function.
# A function can be declared with the set of statements that has to be executed repeatedly and the function be called whenever needed.
# There are two types of functions:
# 1. Built-in Functions : they are already written in Python which serves specific purposes. Example: range(), print(), input(), len()
# 2. User-defined Functions


# User-defined Functions:
# These are created by the user in the program to perform a desired task or purpose.
# "def" keyword is used to declare a function in Python.
# We can perform a function call wherever in the program when we want to execute the statements.

# Function Declaration Syntax: def functionName(parameter1, parameter2...):
# Function Call Syntax: functionName(value1, value2 ... )


def rectArea(l, b):    # Function Declaration
    area = l * b 
    print(area)

rectArea(10, 20)   # Function Call


# Pass Keyword 
# Pass is used in a function when we have not defined the function body.
# For Example, we define a function and not write the body, Normally this throws an indendation error
# But if we use "pass", it skips that function declaration and execute the remaining code


def passExample(a, b):
    pass

