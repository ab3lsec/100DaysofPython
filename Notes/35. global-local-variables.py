# What is Local variable?
# When a variable is decalred inside a function, then it can be only accessed within the Function
# If we call the same variable somewhere in the program outside the func, then it thrwos an error.

# What is Global Variable?
# Variables that are declarted outside the function can be accessed anywhere in the program.
# These variables are called as Global variables.


name = "Jhon"   # Global Variable

def hello():
    name = "Abel"    # Local Variable
    print(f"Local Name: {name}")

hello()

print(f"Global Name: {name}")     # prints Jhon coz its global 



# How to change the value of Global variibale inside the function?
# Normally if we reinitialize the valuie of a global var inside the func, it treates its as a local var
# to avoid this we need to use "global" keyword beform redeclaring the variable value.

color = "Red"

def showcolor():
    global color
    color = "Green"
    print(color)

showcolor()
print(color)
