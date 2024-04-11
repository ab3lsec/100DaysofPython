# What is Typecasting?
# Typecasting allows us to convert on datatype to other datyatype.
# For Example, if we want to convert a numerical value to string, we use Typecasting in Python

# Need for Typecasting: 
# In this example, the value of num1 is "1" and num2 is "2", and we have done an Addition operation "a+b"
# But the problem is num1 and num2 has string datatype, when two strings are added, it concatenates into a single string.
# To make this string value to numbers we need to do Typecasting!

num1 = "1"
num2 = "2"
print(num1 + num2)     # Output: 12

# Python Methods for Typecasting
# int(), float(), str(), ord(), hex(), oct(), tuple(), list(), dict(), set()

print(int(num1) + int(num2))  # Output: 3 


# Types of Typecating:
# 1. Explicit Conversion: this is done manually by the developer as per the requirement.

string = "87"
number = 13
print("THE SUM IS: ", int(string) + number)


# 2. Implicit Conversion: this is done by Python durning the runtime. 

integer = 7
float = 3.5
print(integer + float)   # Python converts the interger value "7" to float "7.0"