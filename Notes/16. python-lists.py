# Lists in Python
# List is an important datatype in Python.
# Lists can be used when we want to store mutiple different values/ data items in a single entity.
# For Example: Storing a list of names in a single "names" entity

# the values inside the list are known as "List Items"
# List Items are enclosed between square brackets [ ] and sperated using commas.

names = ["John", "Jackson", "Amelie", "Frank", "Ben"]
print(names)
print(type(names))


# LISTS ARE MUTABLE!!
# which means they can be changed or modified after creation.


# How to Target each Items in a List!!
# We can target individual lists items the same way like strings using the "index value"
# Syntax: listName[indexValue]

print(names[2])
print(names[4])

print(names[-3])      # Negetive Indexing (Logic: len(list) - 3) i.e names[2]
print(names[-5])      # 5-5 = 0 i.e names[0]



# Using list items of Multiple datatypes
# Lists allows list items of any datatype.
# For Example, we can use a list of numbers with string and Boolean values in it.

sample = [1, 2, 3, "One", "Two", True]
print(sample)



# Checking an item is Present in the List:
# We can check whether an item is present in the or not by using "in" Keyword in a COnditional Statement
# Syntax: if "itemName" in "ListName"

names = ["John", "Jackson", "Amelie", "Frank", "Ben"]

if "Amelie" in names:
    print("Amelie is Present!!")

else:
    print("Couldn't Find Amelie!")

    

