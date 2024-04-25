# What are Arguments?
# Arguments are the values passed inside a function when its called.
# These arguments supply the data to perform the operations in the function.
# There are four types of Arguments in Python:
# 1. Default Arguments
# 2. Keyword Arguments
# 3. Variable Length Arguments
# 4. Required Arguments



# Default Arguments:
# Default arguments are those for which we set default values during the function declaration.
# In this case, even if the value is not provided during fuction call, the program uses the default value
# If value is given during function call, then the program prefers it instead of defaults

def defaultParam(a, b=10):    # b is default
    print(a * b)

defaultParam(5)      


# Keyword Arguments:
# Using these arguments, we can use the argumnets in any order during the function call
# They use a key=value format during the function call.
# Basically the order in which arguments are passed during function declaration doesnt matter

def keywordParam(a, b, c):
    print((a + b) - c)

keywordParam(b=10, c=3, a=5)   


# Required Arguments:
# These arguments are mandatory, if failed to pass the values for these, then it will throw a "missing argument error"
# All the arguments for which values are not given during declartaion, are treated a Required Arguments

def reqParam(a, b):
    print(a * b)

reqParam(1, 10)



# return Statement
# return is used to return a value after executing the function via a function call.
# For Example, in a findSum() we can return the sum value
# this can be used when we want to store the value returned by the function
# If we use two or more return statements in a single function, the value of first return statement is returned.

def findSum(a, b):
    return a + b

sum = findSum(10, 20)

print(sum)

