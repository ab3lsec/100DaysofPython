# String Methods in Python
# Python provides built-in Functions to perform operations of a give String
# There are string methods for performing operations oike converting given string into lower/uppercase, cuttong, finding length etc...

# STRINGS ARE IMMUTABLE!!!
# Strings in python are immutable datatype
# Which means whenever we apply an operation on string using string methods, it doesn't affect the original string
# But instead it creates a new string
# For Example, We declared str = "Hello" and then later inthe program we used str.upper(), this converts the string and form a new string instead of changing the original

hello = "Hello"
print(hello.upper())  # Prints HELLO
print(hello)        # Prints Hello



# 1. len() : Finding Length of the string

name = "Edward Snowden"
print(len(name))

# 2. upper() : Converts the string to uppercase
# 3. lower() : Converts the string to lowercase

print(name.upper())
print(name.lower())

# 4. strip() : Removes all whitespaces before and after string

stripString = "    hello World      "
print(stripString)
print(stripString.strip())

# 5. rstrip() : Removes the specified trailing characters in the string

rstripStr = "Hello!!!!!!!!!!"
print(rstripStr)
print(rstripStr.rstrip("!"))

# 6. replace() : replaces one string with another string 

batman = "Bruce Banner"
print(batman.replace("Banner", "Wayne"))


# 7. split() : Splits the string in differents parts and stores each part as a item in List

dlg = "I am Vengeance!!"
print(dlg.split(" "))    # uses "space" as a delimeter


# 8. count() : counts the number of occurnences of a specific word or letter in  an entire string

print(dlg.count("e"))
print(dlg.count("am"))


# 9. endswith() : returns a boolean vaklue stating whether the string ends with the given character or word

print(dlg.endswith("!"))
print(dlg.endswith("Vengeance!!"))

print(dlg.endswith("am"))
print(dlg.endswith("am", 2, 4))  # checks "am" is the word endind at the index 2-4  


# 10. find() : finds the first occurence of the given word and returns its index value. returns "-1" if nothing is found

msg = "His name is Woody, He is a good man!!"
print(msg.find("is"))

