# Challenge 16: URL Path Analysis

# In bug bounty hunting, understanding the structure and potential vulnerabilities of URL paths is crucial. 
# Write a Python function called analyze_url_paths that takes a list of URLs as input and analyzes the paths of those URLs for common security vulnerabilities.

# The function should perform the following analysis:

# Identify and count the occurrences of any directory traversal attempts (e.g., "../" or "%2e%2e%2f") in the URL paths.
# Identify and count the occurrences of any potential sensitive paths (e.g., "admin", "config", "password") in the URL paths.


# Next, prompt the user to enter URLs. Ask the user to enter the URLs separated by commas (e.g., "https://example.com/,https://example.com/admin"). 
# Split the input string by commas and convert each part into a list of URLs. 
# Finally, call the analyze_url_paths function with the user-provided list of URLs and print out the analysis result.

# This challenge will help you practice analyzing URLs for potential security vulnerabilities, which is a critical skill in bug bounty hunting.


# Using the split function to take the input. 
urls = input("Enter the URLs: ").split(",")

print(urls)

