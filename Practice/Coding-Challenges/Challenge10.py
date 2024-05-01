# Challenge 10: URL Path Analysis using Lists
# Imagine you're analyzing the security of a web application as part of a bug bounty program. 
# Write a Python function called check_vulnerable_endpoints that takes a list of URLs as input 
# and checks each URL for potential vulnerabilities in the endpoint paths.

# Assume that vulnerable endpoints contain any of the following keywords:
# "admin", "password", "config", "backup".

# The function should return a list containing tuples of (URL, vulnerability) for each URL that contains a vulnerable endpoint. 
# If no vulnerabilities are found in any URL, the function should return an empty list.

# Next, prompt the user to enter a list of URLs, call the check_vulnerable_endpoints function with the user-provided list, 
# and print out the list of vulnerable endpoints found.

urls = [
    "http://example.com",
    "https://example.com/admin",
    "http://example.com/login",
    "https://example.com/backup",
    "http://example.com/dashboard",
    "https://example.com/vulnerable"
]

keywords = ["admin", "password", "config", "backup"]

def checkVulnEndpoints(urls):
        
    VulnList = []

    for url in urls:
        for keyword in keywords:
                if keyword in url:
                    VulnList.append((url, keyword))

    return VulnList

print(checkVulnEndpoints(urls))