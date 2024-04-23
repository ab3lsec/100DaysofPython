# Conditional Statements in Python
# Whenever we need to make a decision or execute a specific block of code only if a condition satisfies, then we use conditional statements
# If the condition evaluates to True, then it executes the code, else execute another block.
# These Statements uses conditional operators (<, >, >=, <=, ==, != )

# Types of Conditional Statements in Python:
# 1. if
# 2. if-else
# 3. if-else-elif  
# 4. nested if-else-elif

# 1. if-else Statement
# If the condiotion is True: Execute the block of code inside the If Statement
# If the condition is False: Executes the block of code on the else statement.
# Syntax: if (Condition): 

age = int(input("Enter Your Age: "))

if (age >= 18):
    print("You are Legal!!")

else:
    print("You ain't Legal!!")


# 2. if-elif-else Statements:
# Elif statements are used when we want to check multiple conditions, before executing the else block
# Normally when the if block fails, the program executes the else block
# But in elif statement, if the condition fails, the program checks the next condition in the elif block and finally executes else block.
# If the condition in if statement is True, then the program stops execution and ignores the other elif blocks.

age = int(input("Enter Your Age: "))

if (age <= 10):
    print("You are a child!!")

elif (age > 10 and age < 20):
    print("You are a Teen!!")

else:
    print("You are an Adult!!")


# 3. Nested-if Statements:
# Nested if Statements are If statements within an If Statement
# Basically we use this if we want to check a condition and execute a block inside an if statement


age = int(input("Enter Your Age: "))

if (age <= 10):
    print("You are a child!!")

elif (age > 10 and age < 20):
    if (age >= 18):              # Nested If 
        print("You are Legal!!")
    else:
        print("You ain't Legal!!")

    print("You are a Teen!!")
    
else:
    print("You are an Adult!!")