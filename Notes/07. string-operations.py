# Finding Length of a String - len()
# Length of a specified string can be printed using the len() function

name = "BRUCE-WAYNE"
print(len(name))

# String as an Array
# A string can be treated as an Array where each characters can be each elements of an Array
# Each character in a string can be targeted using its corresponding index value

print(name[0:5])    # Starts form 0 index to index 5 
print(name[:5])    # Pythons adds a 0 by default

print(name[6:])  # Python adds len(name) value by default after colon

# Negetive Slicing

print(name[0:-5]) 
# Logic: print(name[0:len(name)-5])  

print(name[-5:-1])
# Logic: print(name[len(name)-4:len(name)-3])


# Finding a Pattern in a String:
# We can check whether a pattern is present in the string or not by using "in" Keyword in a Conditional Statement
# Syntax: if "pattern" in "String"

str = "Michael Jackson"

if "son" in str:
    print("Pattern Found!!")

else:
    print("No Matches!!")