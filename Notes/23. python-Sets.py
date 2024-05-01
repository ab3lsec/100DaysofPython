# Sets in Python
# Sets are basically collection of unordered data items.
# Sets items are eclosed in curly braces { } and seperated by commas.
# Sets are Immutable, means it cannot be changed after creation


# Sets do not contain duplicates!!
# Sets contains oonly uniques items, Duplicate values cannot be stored in a set.
# For Example, if you add the string "Jackson" 10 times, when it is printed it only prints it "Jackson" one time.
 
stud = {"Jackson", 19, 19, 19, True, "NY", 89.6}
print(type(stud))

print(stud)    # prints 19 only once


# How to create an Empty Set?
# If we use empty curly braces set = {}, python interprets it as a Dictionary datatype
# To create an empty set, we need to use the set() function
# Syntax: setName = set()

empty = set()
print(type(empty))


# Accessing Set items using For Loop

for item in stud:
    print(item)


# Checking an item is Present in the Set:
# We can check whether an item is present or not by using "in" Keyword in a Conditional Statement
# Syntax: if "item" in "setName"

if 19 in stud:
    print("19 Found!!")



# How to delete an entire set?
# to delete an entire set, we use "del" keyword

vuln = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}

del vuln

print(vuln)   # throws a "Set not Defined" Error!


# How to Clear items on a set?
# we can use clear() method to remove all items and return an empty set.

vuln = {"IDOR", "XSS", "SQLI", "CSRF", "SSRF"}

vuln.clear()

print(vuln) 