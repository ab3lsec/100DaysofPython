# Challenge 8: 
# Imagine you're conducting a security audit on a website's login system as part of a bug bounty program. 
# Write a Python script that simulates multiple login attempts. 
# Use a `for` loop to iterate through a list of usernames and passwords, and check if each combination is valid.

# Assume the following:

# - You have a list of usernames and passwords stored in separate lists.
# - The length of both lists is the same, and each username corresponds to the password at the same index.
# - You'll use the `range()` function to loop through the indices of the lists.

# Inside the loop:

# - Check if the current username and password combination is valid.
# - If valid, print a message indicating successful login.
# - If not valid, print a message indicating failed login.

# You can use `break` to exit the loop once a valid login is found.

userList = ["user123", "johndoe", "admin", "coolguy", "superuser", "testuser", "user1", "user2"]
passList = ["password123", "123456", "admin123", "letmein", "password", "abc123", "qwerty", "userpassword"]

validUser = "admin"
validPass = "admin123"

for i in range(8):
    print("Trying", userList[i],":",passList[i], "....")

    if ((validUser == userList[i]) and (validPass == passList[i])):
        print("Valid Credentials Found! SUCCESSFULLY LOGGED IN!!")
        break

    else:
        print("False credentials! LOGIN FAILED!!")
