
vulnReports = {}

def getUserInput():
    url = input("Enter target URL: ")
    vulnType = input("Enter vulnerability type: ")
    vulnDesc = input("Enter description: ")
    severity = input("Enter severity level: ")

    content = {
        'Target URL': url,
        'Vulnerability Type': vulnType,
        'Description': vulnDesc,
        'Severity': severity
    }
    
    return content

def createKey():
    index = 1

    while True:
        key =  f"VR-0{index}"
        if key not in vulnReports:
            return key
        index += 1
    

def addNewReport():
    newVuln = getUserInput()
    key = createKey()

    if key:
        vulnReports[key] = newVuln
        print(f"New vulnerability report added with ID: {key}")


def viewReports():

    if vulnReports:
        for id, vuln in vulnReports.items():
            print(f"ID: {id}")
            for key, value in vuln.items():
                print(f"{key} : {value}")

    else:
        print("No vulnerability reports found.")


def searchReport(id):

    if id in vulnReports:
        print(f"Vulnerability report with ID {id}:")
        for key, value in vulnReports[id].items():
            print(f"{key} : {value}")

    else:
        print(f"Report {id} not found!")


def updateReport(id):

    if id in vulnReports:
        update = getUserInput()
        vulnReports[id] = update
        print(f"Report {id} updated successfully!")
    
    else:
        print(f"Report {id} not found!")


def deleteReport(id):

    if id in vulnReports:
        del vulnReports[id]
        print(f"Report {id} deleted successfully!")

    else:
        print(f"Report {id} not found!")


while True:
    print("\n1. Add a new vulnerability report")
    print("2. View all vulnerability reports")
    print("3. Search for a vulnerability report")
    print("4. Update details of a vulnerability report")
    print("5. Delete a vulnerability report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addNewReport()

    elif choice == "2":
        viewReports()

    elif choice == "3":
        id = input("Enter ID to search: ").upper()
        searchReport(id)

    elif choice == "4":
        id = input("Enter ID to update: ").upper()
        updateReport(id)

    elif choice == "5":
        id = input("Enter ID to delete: ").upper()
        deleteReport(id)

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

