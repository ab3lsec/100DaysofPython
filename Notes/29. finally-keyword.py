
# Finally Block
# finally keyword is used to specify lines of code that must execute no matter what happens.
# finally block is used along with try and excxept blocks

def addNumbers():
    try: 
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print(f"{a} / {b} = {a / b}")
        return 1                           # returns 1 if try block succeefully executes                          
        
    except Exception as e:
        print("Invalid Input!!", e)
        return 0                           # returns 0 if there is an error
    
    finally:
        print("Thank You!!")

res = addNumbers()
print(res)


# The string "thank You" in finally block will execute in every situation, error or no error.