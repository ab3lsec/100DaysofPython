# List Methos in Python
# Python provides built-in Functions to perform operations of a given List
# There are list methods for performing operations like sorting given list into acsending/desc, appending new items, finding length etc..

superheroes = ["batman", "superman", "flash", "spiderman", "hulk", 'aquaman', "flash"]

# 1. sort() : Sorts the list in ascending/descending order and Updates the original List.

superheroes.sort()   # use "reverse=True" as argument to sort in descending order
print(superheroes)


# 2. reverse() : reverse the order of the list, i.e first item will go to last and last item will come to first

superheroes.reverse()
print(superheroes)


# 3. index() : returns the index value of the specified item in the list. 
# If there is same item twice, then it returns the index of first occurence

print(superheroes.index("flash"))


# 4. count() : return the count of number of times the specifed item is present in the list

print(superheroes.count("flash"))


# 5. copy() ; copies the contents of an existing list to create a new list.

heroes = superheroes.copy()
print(heroes)


# 6. append() : inserts a new items to the end of the list.
superheroes.append("thor")
print(superheroes)


# 7. insert() : inserts a new item at the specified index. 

superheroes.insert(5, "cyborg")
print(superheroes)

# 8. remove() : removes the first occurence of a specified value

superheroes.remove("flash")

# 9. extend() : adds the items of one list to a second list.
# i.e the second list will have all the items of first list,but the first list remain unchanged.

marvel = ["ironman", "vision", "hawkeye"]

superheroes.extend(marvel)
print(superheroes)
print(marvel)     # remains the same


# Concatenating two lists:
# We can concatenate two lists using the plus (+) operator

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

numbers = odd + even
print(numbers)

