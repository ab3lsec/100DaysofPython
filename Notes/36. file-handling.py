# File Handling in Python
# Python supports file handlking which means we can read , write and append the coontents of a file inside the python prgram.

# Opening a File:
# to open a file we need to use the open() method.
# open() takes the name/path of the file and the file mode (read/write/append) as arguments

f = open('sample.txt', 'r')

# File Mode in Python:
# 1. read(r): this mode is used to read the contents and throws an errorif file doesnt exist.
# 2. write(w): this mode is for writing. the new content will overwrite the existng content. create the file if it doesnt exist.
# 3. append(a): similar to write but doesnt replace the existing content but append the new content to the end.
# 4. create(x): creates a new file and throws error if it already exist.
# 5. text(t): specifies the file must be handled as a text file.
# 6. binary(b): specifies the file must be handled as binary file (image,pdf etc..)


# Reading a File:
# to read the text content of a file we use the read() method on the opened file.
# After reading the file, we nee to close it using close() method.

f = open('sample.txt', 'r')
text = f.read()
print(text)
f.close()


# Writing a File:

f = open('sample.txt', 'w')
f.write('Hello Abel!')
f.close()


# The 'with' Statement:
# Alternatively we can use with statement which automaticalley closes the file.

with open('sample.txt', 'r') as f:
    text = f.read()

print(text)

