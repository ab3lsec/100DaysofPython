# Challenge 15 : Analyzing Hostnames for Subdomain Takeovers using Sets

# Subdomain takeover is a common security vulnerability 
# where an attacker can register a subdomain of a vulnerable domain that is not actively being used, and then gain control over it.

# Write a Python function called find_vulnerable_subdomains that takes a list of hostnames as input 
# and identifies potential subdomains that are vulnerable to takeover.

# The function should perform the following steps:

# Extract the subdomains from each hostname in the list.
# Convert the extracted subdomains into sets for efficient comparison.
# Check if any of the subdomains in the list are present in the list of active subdomains or DNS records.
# If a subdomain is not found in the list of active subdomains, add it to a set of vulnerable subdomains.
# After analyzing all hostnames, return the set containing the vulnerable subdomains.


activeSubdomains = {"subdomain1", "subdomain3"}

vulnSubdomains = set()

def findVulnSubdomains(hostnames):

    extractedSet = set()
    
    for i in hostnames:

        i = i.split(".")[0]
        extractedSet.add(i)
        
    vulnSubdomains = extractedSet.difference(activeSubdomains)

    return vulnSubdomains
    

hostnames = [
    "subdomain1.example.com",
    "subdomain2.example.com",
    "vulnerable-subdomain.example.com",
    "subdomain3.example.com",
]

print("Vulnerable Subdomains Found!! : ", findVulnSubdomains(hostnames))