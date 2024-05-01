# Challenge 2: String Operations
# Write a Python script that takes a user input string and performs the following operations:

# 1. Convert the string to uppercase.
# 2. Reverse the string.
# 3. Replace all vowels in the string with the character 'X'.

# After performing these operations, print the modified string.

word = "Python is a programming language"

# Changing to UpperCase
word  = word.upper()

# Reversing String
word = word[::-1]

# Replacing vowels with X
vowels = ["A", "E", "I", "O", "U"]

for i in vowels:
    word = word.replace(i, "X")


print(word)
