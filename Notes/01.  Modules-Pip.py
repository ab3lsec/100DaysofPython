# What are Modules?
# Modules are basically a way in Python that allows us to borrow pre-written set of codes developed by others. In this way we can use the code written by other people in our program.

# There are 2 types of Modules:
# 1. Built-in Modules: these comes by default with Python. No need to install it seperately.
# 2. External Modules: these should be installed using Python package managers like pip.

# What is pip ?
# Pip is basically a package manager which is used for installing neccessary Modules onto our system. 
# For Example, If you want to use a module named "Pandas", its not installed in Python by defsult. So you need to install it externally to use that in our program.

# Syntax: pip3 install <MODULE-NAME>


# How to use a Module in a Python program?
# We can use a module using the Import command. Syntax: import <MODULE-NAME>

import requests
r = requests.get("www.example.com")
