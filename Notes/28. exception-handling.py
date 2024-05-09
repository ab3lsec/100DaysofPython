# Exception Handling in Python:
# Exception handling is used to handle unexpected errors that occurs during execution which results program termition.
# If an error occur and the porogram crashes. it fails to execute important lines of code after that.
# So to avoid, the termination due to these unexpected errors we use this technique.


# Try....Except Block
# try and except blocks are used to handle exceptions and errors in Python
# "try" block is executed when there is no error!!
# "except" block is executred when an error occur in "try" block and program fails to complete.


# Sample Scenario:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"{a} + {b} = {a+b}")

print("Important Code!!")

# This program expects the user to input two values to perform the operation and sucessfully execute the program
# When the user fails to input any of those or input invalid datatypes like strings, then the program crashes and throws a system error.
# this fails to execute the important lines of code below

            
# Using Exception Handling technique:

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a} / {b} = {a / b}")
    
except Exception as e:
    print("Invalid Input!!", e)

print("Important Code!!")


# In this code, if any error occur in Try block, the mnessage in except block prints
# But the program wont terminate, it executes the remaining code below.


