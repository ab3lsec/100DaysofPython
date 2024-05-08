# Exercise: Convert a Message to Secret Code!!
# Write a Python Program to tarnsaltea message into secret code language.
# Use the rules below to translate 
# Encoding:
# 1. If the word contains alteast 3 chars, remiove the first letter and append it to the end.
# 2. Now append 3 random characters to the start and the end of string
# 3. Else (word < 3 characters) just reverse the string

# Decoding:
# 1. If the word contains less than 3 chars, reverse the string
# 2. Else, remove the three chars from beginning and the end
# 3. Then remove the last letter and append it to the beginning.


import random
import string

def encodeWord(word):
    strList = list(word)

    if len(word) >= 3:
        first = strList.pop(0)
        strList.append(first)

        rand1 = random.choices(string.ascii_uppercase, k=3)
        rand2 = random.choices(string.ascii_uppercase, k=3)
            
        strList.insert(0, rand1[0])
        strList.insert(1, rand1[1])
        strList.insert(2, rand1[2])

        strList = strList + rand2
            
        secretWord = ""
        for i in strList:
            secretWord += i
                    
        return secretWord

    else:
        secretWord = word.reverse()
        return secretWord


def decodeWord(word):
    strList = list(word)

    if len(word) < 3:
        decoded = word.reverse()
        return decoded

    else:
        for i in range(0,3):
            strList.pop(0)
            strList.pop(-1)

        last = strList.pop(-1)
        strList.insert(0, last)

        decoded = ""
        for i in strList:
            decoded += i

        return decoded


print("Select an Option:")
print("1. Encode   2. Decode")
choice = input("Enter You Choice: ")

match choice:
    case "1":
        word = input("Enter the Messsage to encode: ").upper()
        encoded = encodeWord(word)
        print(f"The Encoded Message: {encoded} ")

    case "2":
        word = input("Enter the Messsage to decode: ").upper()
        decoded = decodeWord(word)
        print(f"The Decoded Message: {decoded} ")

