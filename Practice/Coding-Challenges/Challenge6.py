# Challenge 6:
# Imagine you're analyzing a web application as part of a bug bounty program. 
# Write a Python script that simulates scanning a list of URLs for potential vulnerabilities.

# Assume you have a list of URLs stored in a list. For each URL, 
# your task is to check if it contains any of the following sensitive keywords: "admin", "password", "secret", "vulnerable".

# - If a URL contains any of these keywords, print a message indicating a potential vulnerability found. 
# - Otherwise, print a message indicating that the URL is safe.

# You can use a for loop to iterate through the list of URLs and perform the checks for each URL

urls = [
    "http://example.com",
    "https://example.com/admin",
    "http://example.com/login",
    "https://example.com/secret-page",
    "http://example.com/dashboard",
    "https://example.com/vulnerable"
]

keywords = ["admin", "password", "secret", "vulnerable"]

for url in urls:

    if any(keyword in url for keyword in keywords):   # using list-Comprehension
        print("Potential vulnerability found in: ", url)

    else:
        print("URL is Safe: ", url)


