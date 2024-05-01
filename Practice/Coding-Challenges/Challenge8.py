# Challenge 8: Checking Password Strength
# Imagine you're analyzing the security of a web application as part of a bug bounty program. 
# Write a function called `checkPasswStrength()` that takes a password as input and returns a message indicating its strength:

# - If the password length is less than 8 characters, return "Weak password: Password length should be at least 8 characters."
# - If the password contains only letters or only digits, return "Weak password: Password should contain a mix of letters and digits."
# - If the password contains both letters and digits and has a length of at least 8 characters, return "Strong password: Password is strong."

# Next, prompt the user to enter a password, call the `checkPasswStrength()` with the user-provided password. 
# Finally, print out the message indicating the password strength.

def checkPasswStrength(passw):
    if len(passw) < 8:
        return "Weak password: Password length should be at least 8 characters."
    
    elif passw.isalpha() or passw.isnumeric():
        return "Weak password: Password should contain a mix of letters and digits."
    
    else:
        return "Strong password: Password is strong."
    
    
password = input("Enter the Password: ")

result = checkPasswStrength(password)
print(result)
