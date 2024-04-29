# Challenge 16: URL Sanitization

# One common task in bug bounty hunting is to perform URL sanitization 
# to prevent various types of attacks, such as Cross-Site Scripting (XSS) and SQL Injection.

# Write a Python function called sanitizeURL() that takes a URL as input and returns a sanitized version of the URL.
#  The function should perform the following sanitization steps:

# - Remove any trailing whitespace from the URL.
# - Convert the URL to lowercase.
# - Replace any occurrences of the string "javascript:" with an empty string.
# - Remove any leading or trailing slashes ("/") from the URL.


# Next, prompt the user to enter a URL. Call the sanitize_url function with the user-provided URL and print out the sanitized URL.

# This challenge will help you practice string manipulation techniques commonly used in bug bounty hunting to mitigate security vulnerabilities.


def sanitizeURL(url):

    print("Sanitizing Your URL.....")
    url = url.lower()
    url = url.strip()
    url = url.replace("javascript:", "")
    url = url.rstrip("/")
    url = url.lstrip("/")

    return url


# url = "/javascript:http://EXAMPLE.com/       "

url = input("Enter the URL: ")
print("Here is the Sanitized version of your URL:", sanitizeURL(url))