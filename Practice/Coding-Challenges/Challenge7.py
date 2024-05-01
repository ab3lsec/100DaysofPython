# Challenge 7: Calculating Area using Functions
# Write a Python function called `calcRectArea` that takes two arguments: `length` and `width`.
# The function should calculate and return the area of the rectangle.

# Next, prompt the user to enter the length and width of a rectangle, and call the `calcRectArea` function with the user-provided values. 
# Finally, print out the calculated area.

def calcRectArea(length, width):
    return length * width

len = int(input("Enter the Length: "))
wid = int(input("Enter the Width: "))

area = calcRectArea(len, wid)

print("The Area of Rectangle is: ", area)