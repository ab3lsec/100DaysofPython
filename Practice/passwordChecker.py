password = input("Enter the Password: ")

while (password != "rockyou"):
    print("Wrong Password!!")
    password = input("Enter the Password: ")
    continue

else:
    print("Login Successfull!!")