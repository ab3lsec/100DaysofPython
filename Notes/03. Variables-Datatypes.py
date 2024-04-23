# What are Variables?
# Variables are like containers that holds data in memory. In Python We can create a variable just by declaring the variable's name and its assign it a value using the assignmemnt operator(=)

name = "Bruce Wayne"
age = 35


# What are Data Types?
# A Datatype specifies the tyoe of data that a variable holds
# We can check the datatype of a variable using type() method.

# Built-in Datatypes:

# 1. Text Data: str
name = "Peter Parker"
print(type(name))     

# 2. Numeric Data: int, float, complex
age = 20
print(type(age))     

weight = 70.5 
print(type(weight)) 

# 3. Boolean Data (True/False)
isAdult = True
print(type(isAdult)) 

# 4. Sequenced Data: List (can be changed later), Tuple (cannot be changed later)

favMovies = [["Taxi driver", "Blade Runner"],["Avengers","DateNight"]]  # List
print(type(favMovies)) 

favFood = (('Biriyani', 'Burger'),('Pizza', 'Tacos'))  # Tuple
print(type(favFood)) 


# 5. Mapped data: Dictionary (like JSON Data)

student = {"name":"Jackson", "age":20, "isAdult":True}
print(type(student)) 