# Why Custom Errors?
# In some situations, the user input seems well for a Python Interpreter but we expect an certain input.
# For Example, 
# if the program expects a number between 10 and 20
# and the user inputs 30, Python interpreter doesnt spot any error because 30 is still an integer.
# In this case we want to throw a "custom error" if user inputs numbers not b/w 10 and 20


# How to raise Custom errors in Python?
# We can use the 'raise' keyword to throw custom errors in python.


iphone = 1000
budget = int(input("Enter Your Maximum budget: "))

if budget < iphone:
    raise ValueError("Sorry, You can't Afford an Iphone!!")

else:
    print("You have Enough Money!!")

