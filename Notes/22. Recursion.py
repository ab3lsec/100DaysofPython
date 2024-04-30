# What is Recursion?
# Recursion is used in the concepts of function.
# recursion is method by which a function can make a call to itself.
# the functions which follows recursion are known as Recursive Functions.

# Example: factorial fo a Number

def findFactorial(num):
    if (num == 1 or num == 0):
        return 1
    
    else:
        return num * findFactorial(num - 1)       # factorial(7) = 7 * factorial(6) i.e 6*5*4*3*2*1
        

num = int(input("Enter a number: "))

print("The factorial is", findFactorial(num))  


# Logic: to print factorial(5)

#  5 * factorial(4)
#  5 * 4 * factorial(3)
#  5 * 4 * 3 * factorial(2)
#  5 * 4 * 3 * 2 * factorial(1)

