# Set Methods in Python
# There are three major operations on sets:
# 1. Union: Take two sets A,B. Combine these two sets into a new set C with all the items in set A and B.
# 2. Intersection : Takes two sets A,B. Forms a new Set C by taking the items that are common in both Set A and B.
# 3. Symmetric Difference: does the opposite of intersection, combines everything except common values.

# 1. union() : combines value of two set into a new set. the Two sets remains Unchanged.

s1 = {1, 3, 5, 7}
s2 = {2, 4, 6, 8}

s3 = s1.union(s2)

print(s3)
print(s1)   # remain unchanged
print(s2)


# 2. update() : combines values of two sets and updates the existing set

s1 = {1, 3, 5, 7}
s2 = {2, 4, 6, 8}

s1.update(s2)

print(s1)    # updated s1


# 3. intersection() : combines common values of two sets into a new set. the Two sets remains Unchanged.

s1 = {1, 3, 5, 7, 6}
s2 = {3, 2, 4, 7, 1}

s3 = s1.intersection(s2)

print(s3)
print(s1)   # remain unchanged
print(s2)


# 4. intersection_update() : combines common values of two sets and updates the existing set

s1 = {1, 3, 5, 7, 6}
s2 = {3, 2, 4, 7, 1}

s1.intersection_update(s2)

print(s1)    # updated s1


# 5. isdisjoint() : returns True, if no items in Set A is present in Set B. If there are common items, returns False.

vuln1 = {"IDOR", "XSS", "SQLI"}
vuln2 = {"CSRF", "SSRF"}

print(vuln1.isdisjoint(vuln2))


# 6. issuperset() : returns True, If all values in set B is present in Set A. Operataion is performed on Set A.

vuln1 = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}
vuln2 = {"IDOR", "XSS"}

print(vuln1.issuperset(vuln2))


# 7. issubset() : returns True, If returns True, If all values in set B is present in Set A. Operataion is performed on Set B.

vuln1 = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}
vuln2 = {"IDOR", "XSS"}

print(vuln2.issubset(vuln1))


# 8. add() : used to add a new item to the set. we use update() to add multiple items at once.

vuln1 = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}
vuln2 = {"IDOR", "XSS"}

vuln2.add("SSTI")
print(vuln2)


# 9. remove() : removes the specified item from the set. If the item not present, throws an ERROR!!
# 10. discard() : removes the specified item from the set. NO ERROR!, If item not present.


vuln2.remove("SSTI")
print(vuln2)


# 11. pop() : pops a random item on the list, becuase sets are unordered, each time it executes the items are in new order.

poppedItem  = vuln2.pop()
print(poppedItem)


# 12. clear() : remove all items and return an empty set.

vuln = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}

vuln.clear()

print(vuln) 