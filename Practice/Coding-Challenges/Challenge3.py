# Challenge 3: Checking Age of a Person
# Write a Python script that prompts the user to enter their age. 
# Based on their age, print out the appropriate message:

# - If the age is less than 18, print "You are a minor."
# - If the age is between 18 and 65 (inclusive), print "You are an adult."
# - If the age is greater than 65, print "You are a senior citizen."

age = int(input("Enter Your Age: "))

if (age >= 0 and age < 18):
    print("You are a minor.")

elif (age >= 18 and age <= 65):
    print("You are an adult.")

else:
    print("You are a senior citizen.")

    