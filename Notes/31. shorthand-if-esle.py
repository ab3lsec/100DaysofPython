# Shorthand If-else Notation
# The way of writing conditional statements and code in a single line is called Shorthand Notation
# This can be a convenient way if we want to assign the output of an If-else statement to a variable.

# Syntax (If-Else) : <Statements> if <condition> else <Statements>
# Syntax (If-Elif-Else) : <Statements> if <condition> else <Statements> if <condition> else <Statements>

# Shorthand If-Else COndition:

num = int(input("Enter a Random Number: "))

print("Even") if num % 2 == 0 else print("Odd")


# Shorthand If-Elif-ELse Condition:

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("First is greater!!") if a > b else print("Second is Greater!!") if a < b else print("Both are Equal!!")

