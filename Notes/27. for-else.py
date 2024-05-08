# Using Else Statement with For loop:
# We can use an else statement with a for loop 
# the else block will execute in two situations:
# 1. If for loop fails to execute
# 2. When for loop SUccessfully finishes the execution


for i in []:      # For loop doesnt execute (no index in empty list)
    print(i)

else:
    print("Executing Else block!")


for i in range(5):     # Successfully executes for loop till the end
    print(i)

else:
    print("Executing Else block!")


# When Else block doesn't execute?
# Else block will not execute if there is a conditional satement or a break statement and the loop breaks.
# When loop break, the loop will not execute to the end and the else block will not execute.

for i in range(7):
    print(i)
    if i == 5:
        break                 # breaks the loop

else:
    print("Executng else block!!")    # else block doesn't execute