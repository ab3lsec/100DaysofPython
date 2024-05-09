# Enumerate Function in Python
# enumerate() is a Python built-in method that is used when we iterate through an iterable like list, tuple string etc..
# enumerate() will provide the index value of the items each time the loop iterates.

# Why we use enumerate()
# Noramlly for finding an index we need to declare a variable and then increment it at each iteration. 
# Using enumerate() function we can declare an iterator and the enumerate() will handle the increment part

fruits = ["apple", "banana", "orange", "grape"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# Changing the Start Index Value:
# We can change the starting value of index using the "start=" parameter in enumerate()

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

for index, name in enumerate(names, start=1):  
    print(f"Index {index}: Name: {name}, Length {len(name)}")

 