# OS module in Python
# OS mdule contains builtin methods that can be used to interact with the operating syatem and peroform operations
# We can do Operations like,
# - Create files and directories
# - Manipulate contents of files
# - Manage Processes
# - Run System commands etc..


# Important methods:
# 1. os.mkdir() : creates a New Directory
# 2. os.path.exists() : check whether a file/ directory exists or not
# 3. os.rename() : Renames a file/ directory
# 4. os.listdir() : lists the contents of the specified directory
# 5. os.rmdir() : removes an empty directory
# 6. os.remove() : removes a file
# 7. os.getcwd() : Gets current Working directory
# 8. os.chdir() : Changes the CWD to the specified directory

import os

# Interacting with File System:

# 1. Creating a file/directory

os.mkdir("data")  


# 2. Checking if a file/directory exists

if (not os.path.exists("test")):
    os.mkdir("test")  


# 3. Creating Multiple Files in a directory.

for i in range(0, 10):
    os.mkdir(f"test/File{i+1}")


# 4. Renaming a file/directory:

os.rename("test", "sample")   


# Listing files under a directory:

folders = os.listdir("test")
print(folders)                # returns a list of folders


for folder in folders:
    print(os.listdir(folder))
 
 