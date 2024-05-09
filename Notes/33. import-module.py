# How import works in Python?
# Importing a module means process of loading an external module containing code into the current program.
# For Example: If we want to do math operation, we dont have to write seperate methods for each operation, we can just import the math module and use the prewritten methods.
# also we can import "requests", if we want to deal with HTTP Requests and responses.

# "import" keyword  following the module name is used to import an external modue into the program.
# Syntax: import <module_Name>
 
import math

print(math.sqrt(3))



# from keyword:
# We can use from keyword if we want to import a specific method from the module
# By doing this, we can import required methods instead of importing everything in that module.

from math import sqrt, pi

print(sqrt(3))   # Dont have to specify the module name for using the method

print(pi)



# as keyword
# as keyword is used to import a module or a method in a specific custom name   
# by doing this we can use the custom name to call the module.
# For Ex, if we import math as "m" we can use m.sqrt() instead of math.sqrt()

import math as m

print(m.sqrt(3))

 

# dir() Method:
# dir() can be used to learn about an unknown module
# dir(module) return a list of the methods containing in that specified module.
# They are like man pages in Linux

print(dir(math))

 