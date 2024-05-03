# Dictionaries in Python
# Dictionaries are ordered collection of data items.
# Dictionaries are used to store items in a "key:value" pair like JSON format.
# Dictionary items are enclosed between curly braces { } and seperated byt commas.

# Syntax: dictName = {key1:value1 , key2:value2 , key3:value3.....}

employees = {
    'EMP001':'John', 
    'EMP002':'Elsie', 
    'EMP003':'Heath', 
    'EMP004':'John'
    }

print(type(employees))


# How to access Dictionary Items?
# We can target a specific dictionary item using its key 
# the key must be specified between Square brackets[].
# Syntax: dictname['key']

print(employees["EMP004"])
print(employees["EMP002"])


# Accessing values using get() methood
# get() does the same thing but when given an invalid key, get() returns "None"
# whereas using Square brackets returns an error!!  

print(employees.get("EMP005"))  # returns None


# Accessing all Dict Keys
# We can access all dict keys using keys() method

print(employees.keys())


# Accessing all Dict Values
# We can access all dict values using values() method

print(employees.values())


# Accessing all Dict Items (key:value pairs)
# we can access all dict items using items() method.
# items() will convert each key value pairs as individual tuples.

print(employees.items())


# using For loop in Dictionaries

for key, value in employees.items():
    print(f"{key} : {value}")


# Updating an individual Key Value in Dictionary:

employees["EMP004"] = "Jhonny"
print(employees)


# Deleting an entire Dictionary (del)
# we can delete an entire diictionary using "del" keyword

del employees

del employees["EMP004"]    # deleting a single Key:value

