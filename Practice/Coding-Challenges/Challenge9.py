# Challenge 9: Remove Duplicate Numbers
# Write a Python function called removeDupes() that takes a list of numbers as input 
# and removes any duplicate numbers from the list, keeping only the first occurrence of each number. 
# The function should return the modified list without duplicates.

# For example:

# numbers = [1, 2, 3, 4, 2, 5, 6, 3, 7]
# result = remove_duplicates(numbers)
# print(result)  # Output should be: [1, 2, 3, 4, 5, 6, 7]

# Next, prompt the user to enter a list of numbers, 
# call the removeDupes() function with the user-provided list, and print out the modified list without duplicates.

numbers = [7, 1, 2, 7, 3, 4, 2, 5, 6, 3, 7, 4 ]

def removeDupes(numbers):

    numbers.sort()

    uniqNums = [num for num in numbers if numbers.count(num) == 1]
    repeatNums = [num for num in numbers if numbers.count(num) > 1]

    for i in repeatNums:
        repeatNums.remove(i)

    numbers = uniqNums + repeatNums
    numbers.sort()

    return numbers


result = removeDupes(numbers)
print(result)


    

