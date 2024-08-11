# Challenge 1: File Handling and Global Variables
# Create a program that maintains a log of user login attempts. Your program should:

# 1. Initialize a global variable to keep count of the number of login attempts.
# 2. Create a file named login_attempts.txt if it doesn't exist.
# 3. Write a function that:
#   - Prompts the user to enter a username.
#   - Writes the username and the current timestamp to login_attempts.txt.
#   - Increments the global variable tracking the number of login attempts.

# 4. Write another function that:
#   - Reads the contents of login_attempts.txt and prints each line.
#   - Displays the total number of login attempts using the global variable.


import time

loginCount = 0

def userLogin():
    username = input("Enter Your Username: ") 
    timestamp = time.strftime("%H:%M:%S")
    
    with open('loginattempts.txt', 'a') as f:
        entry = f"{username} - {timestamp}"
        f.write(entry + '\n')
        
        
        
userLogin()