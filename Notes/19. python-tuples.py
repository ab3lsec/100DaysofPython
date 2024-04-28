# Tuples in Python
# Tuples are similar to lists. 
# They are basically a collection of data items stored in a single variable.
# The only diffrenece b/w lsts and tuples are that TUPLES ARE IMMUTABLE!!
# which means we alter the tuple once after its creation.

# the values inside the tuple are known as "tuple Items"
# Items in a tuple are enclosed between parantheses ( ) and sperated using commas.
# items in a tuple can be of any datatype

backend = ("python", "php", "ruby", "nodejs", "javascript", "c#")
print(type(backend))

# If there is only a single item like a number, python will treat it as integer instead of tuple
# To avoid this add a comma, after the first item

num = (1,)
print(type(num))



# How to Target each Items in a List!!
# We can target individual lists items the same way like strings using the "index value"
# Syntax: listName[indexValue]

print(backend[2])
print(backend[3])

print(backend[-1])      # Negetive Indexing (Logic: len(list) - 3) i.e names[2]
print(backend[-4])  



# Checking an item is Present in the Tuple:
# We can check whether an item is present in the tuple or not by using "in" Keyword in a Conditional Statement
# Syntax: if "itemName" in "ListName"


if "php" in backend:
    print("PHP Found!!")

else:
    print("PHP not found!")



# Slicing in Tuple:
# We can slice a tuple to form a new tuple.
# But we cannot slice the existing tuple, it remains constant.
# If we want to slice we need to make a new tuple and store the sliced items in it.

# Syntax: tupleName[startIndex: endIndex: StepValue]

newBackend = backend[1:4]       # doesnt print the value at 4th index
print(newBackend)

