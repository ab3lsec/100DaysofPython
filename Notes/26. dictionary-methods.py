# Dictionary Methods in Python
# Python contains builtin methiods to perform operations like update, dlete etc.. on a dictionary

stock = {
    "apple": 3,
    "banana": 6,
    "orange": 4,
    "grape": 8,
    "kiwi": 2,
}


# 1. update() : updates an existing key value, add new key value pairs.

newStock = { "apple": 10, "pear": 5, "watermelon": 10}   

stock.update(newStock)
print(stock)
 

# 2. clear() : clears all items in a dictionary and returns an Empty Dictionary {}

newStock.clear()
print(newStock)


# 3. pop() : removes the key-value pair corresponding to the specified key

stock.pop('kiwi')
print(stock)


# 4. popitem() : removes the dict item at the last index position.

stock.popitem()
print(stock)



