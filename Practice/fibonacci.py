# def findFibonacci(num):
#     if num == 0:
#         return 0
    
#     elif num == 1:
#         return 1
    
#     else:
#         return findFibonacci(num-1) + findFibonacci(num-2)
    

# print(findFibonacci(9))



def analyzeURL(url):

    if "../" in url:
        url = url.replace("../", "")
        return analyzeURL(url)

    elif "%2e%2e%2f" in url:
        url = url.replace("%2e%2e%2f", "")
        return analyzeURL(url)
    
    else:
        return url


url = "/path/to/../%2e%2e%2fetc/passwd"

print("Sanitized: ", analyzeURL(url))