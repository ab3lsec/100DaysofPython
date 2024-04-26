# What is List Comprehension?
# List comprehension is a method used to create new lists by peroforming operations on an iterable object.
# Iterable objects can be other lists, strings, tuples, sets or dictionaries

# Syntax:  newList = ["Expression" for "iterator" in "iterable" if "Condition"] 

# Expression: It is the iterator of the new list
# Iterator: It is the iterator of the Iterable
# Iterable: can be other lists, strings, tuples, sets or dictionaries
# Condition: this is optional if we want to perform a condition and only the items passed the condition are stored in the new list


tableOf20 = [item for item in range(21) if item % 2 == 0]
print(tableOf20)



keywords = [10, "admin", 77, "password", "secret", True, "vulnerable"]

alphaList = [key for key in keywords if isinstance(key, str)]
print(alphaList)

