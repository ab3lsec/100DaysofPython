# Challenge 19.1 : Calculate Area of Cirlcle importing math module

# import math

# def calcArea(radius):
#     area = math.pi * math.pow(radius, 2)
#     print(f"Area of Circle: {area}")

# if __name__ == "__main__":
#     calcArea(2) 



# Challenge 19.2 : Palindrome Checker

def isPalindrome(word):
    word = ''.join(letter for letter in word if letter.isalnum())

    rev = word[::-1]

    if rev == word:
        return True
    
    else:
        return False


if __name__ == "__main__":
    
    word = input("Enter a String: ")
    print("Is Palindrome!!") if isPalindrome(word) else print("Not Palindrome!!")


