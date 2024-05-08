# Challenge 18: Analyzing HTTP Response Headers

# You are tasked with developing a script to analyze HTTP response headers of a given URL andidentify potential security vulnerabilities.
#  Write a Python program that does the following:

# Prompt the user to enter a URL.
# Send an HTTP request to the provided URL and retrieve the response headers.
# Analyze the response headers to check for common security vulnerabilities such as:
    # Missing security headers (e.g., Content-Security-Policy, X-Content-Type-Options, X-Frame-Options, etc.).
    # Insecure HTTP headers (e.g., Set-Cookie without the Secure flag).
    # Presence of server version information (e.g., Server header revealing server software and version).
# Print a report indicating any identified vulnerabilities along with recommendations for remediation.


import requests

req = requests.get("http://tryhackme.com/")

print(req.headers)

if "Content-Security-Policy" not in req.headers:
    print("vulnerable")