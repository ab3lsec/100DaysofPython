# Challenge 11: Reversing a Tuple
# Write a Python function called reverseTuple() that takes a tuple as input 
# and returns a new tuple with its elements reversed.

# Next, prompt the user to enter values for a tuple. Ask the user to enter the values separated by commas (e.g., 1,2,3) 
# and then convert these values into a tuple. Finally, call the reverse_tuple function with the user-provided tuple and print out the reversed tuple.

# This challenge will allow you to practice defining functions, working with tuples, 
# and performing tuple manipulation operations without directly inputting tuples.

nums = (1, 2, 3, 4, 5)

def reverseTuple(nums):
    
    temp = list(nums)      # converting tuple into list
    temp.reverse()
    nums = tuple(temp)
    return nums
    
print(reverseTuple(nums))