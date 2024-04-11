# Taking User Inputs in Python:
# In Python, we can use the input() function to take user input.

name = input("Enter Your Name: ")
print("Hello", name)

# input() function takes in user inpt value as "String" datatype by default.
# So if we want to convert int to number we need to perform an Implicit Typecasting.

first = int(input("Enter First Number: "))
second = int(input("Enter Second Number: "))
print(type(first)) 

sum = first + second
print(sum)

