# Challenge 14 : Common Letters in Strings

# Write a Python function called common_letters that takes two strings as input 
# and returns a set containing the common letters (characters) between the two strings.

# For example:

# For strings "hello" and "world", the common letters are "l" and "o", so the function should return the set {'l', 'o'}.
# For strings "python" and "java", there are no common letters, so the function should return an empty set {}.


def checkCommonLetters(first, second):

    firstSet = {item for item in first}
    secondSet = {item for item in second}

    common = firstSet.intersection(secondSet)

    if common:
        return common

    else:
        return set()
    
first = input("Enter First String: ")
second = input("Enter Second String: ")

result = checkCommonLetters(first, second)
print("Common Letters are: ", result)