# What is __name__ == "__main__" in Python?
# __name__ == __main__ is a pattern used to check whether the program is run directly 
# or it is imported as a module in another program.
# When the program is ran directly, the __name__ variable will have the value "__main__"
# When its imported and used in another program, the __name__ variable will have the value of its module name.

# For Example:

def main():
    print("Ran Directly!!")

main()

# if we write this code in a file named "main.py"
# and we imported this in another program named "sample.py"
# Just by importing the module, the function call main() in main.py will execute in sample.py

# Why this is Important?
# Imagine the method was sensitive and deleted file on the local machine,
# in this case, the method executes just by importing it and not by calling it like main.main()


# So to avoid this we need to write a conditional statement

def main():
    print("Ran Directly!!")

if __name__ == "__main__":
    main()


# In this case the function call will only execute when __name__ variable has __main__ as its value.
# which means when used in another program __name__ variale value changes and this function call main() doesnt execute.
