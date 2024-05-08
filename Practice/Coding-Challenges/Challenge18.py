# Challenge 18.1 : Even or Odd (Shorthand If-else Statements)
# Write a Python script that takes an integer input from the user and
# - prints "Even" if the number is even 
# - prints "Odd" if the number is odd, using shorthand if-else notation.

num = int(input("Enter a Random Number: "))

print("Even") if num % 2 == 0 else print("Odd")



# Challenge 18.2 : Find Greater Number (Shorthand if-else notation)
# Write a Python script that takes two integer inputs from the user 
# - prints "First is greater" if the first number is greater than the second, 
# - prints "Second is greater" if the second number is greater than the first,
# - prints "Both are equal" if both numbers are equal, using shorthand if-else notation.

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("First is greater!!") if a > b else print("Second is Greater!!") if a < b else print("Both are Equal!!")



# Challenge 18.3 : Find Type of triangle (using Shorthand if-else notation)
# Write a Python script that takes three numbers from user representing sides of a triangle.
# The script should determine whether the triangle is equilateral, isosceles, or scalene, 
# and print the result using shorthand if-else notation.

a = int(input("Enter First Side: "))
b = int(input("Enter Second Side: "))
c = int(input("Enter Third Side: "))

print("Equilateral") if a == b == c else print("Scalene") if a != b and b != c and a != c else print("Isoceles")

