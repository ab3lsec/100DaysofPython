# Tuple Methods in Python
# Python provides built-in Functions to perform operations of a given tuple
# There are tuple methods for performing operations like counting an element, finding index, finding length etc..

superheroes = ("batman", "superman", "flash", "spiderman", "hulk", 'aquaman', "flash")

# 1. count() : returns the number of times the specified element present in the tuple

print(superheroes.count("flash"))

#  2. index() : returns the first occurence index of the given element 

print(superheroes.index("flash"))

print(superheroes.index("flash", 3, 7))      # Searching on a range. Syntax: index(element, startIndex, stopIndex)

# 3. len() : returns the length of tuple

print(len(superheroes))


# Manipulating tuples:
# If tuples are immutable, then how we can alter it?
# In this case, we need to first convert the tuple into a LIST!!
# then use the list methods to make the changes abd the convert it back to a Tuple!

science = ("physics", "chemistry", "maths", "biology")

tempList = list(science)

tempList.pop(2)
tempList.append("zoology")

science = tuple(tempList)
print(science)


# Concatenating two tuple
# We can concatenate two tuple using the plus (+) operator

commerce = ("accounts", "economics", "business")

subs = science + commerce
print(subs)