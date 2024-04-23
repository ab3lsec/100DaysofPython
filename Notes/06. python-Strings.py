# What are Strings?

# String is a Built-in datatype that holds a sequence of Textual data.
# Anything enclosed between "double quotes" is considered as a String in Python

favMovie = "Fight Club"
print(favMovie)

# If we want to use "double quotes" inside the string, then we need to enclose the string with 'single quotes'
# If we want to use "single quotes" inside the string, then we need to enclose the string with 'double quotes'

quote = '"Believe you can and you\'re halfway there." - Theodore Roosevelt'

# If we want to use both double and single qoute, then we need to use the escape sequence (\)

# Multi-Line Strings: to print a multi-line string, we enclose the string between """three Double Qutes"""

longString = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut 
labore et dolore magna aliqua"""
print(longString)


# Accessing a Specific Character in a String

# In a String, each character has its corresponding index value which start from 0.
# So the first character will be at index 0, the second at index 1 and so on..
# To access a specific character we can traget it using the index value:  string[indexValue]

name = "Jackson"
print(name[2])   # prints "c"
print(name[6])   # prints "n"


# Using For Loop in Strings

for char in name:
    print(char)