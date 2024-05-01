# Challenge 7: Switch Statement
# Write a Python script that prompts the user to enter a day of the week (e.g., "Monday", "Tuesday", etc.). 
# Use the `match` statement to check the input and print out a message based on the day entered:

# - If the input matches "Monday" or "Tuesday", print "It's the start of the week."
# - If the input matches "Wednesday" or "Thursday", print "It's midweek."
# - If the input matches "Friday", print "It's almost the weekend."
# - If the input matches "Saturday" or "Sunday", print "It's the weekend."
# - If the input doesn't match any of the above, print "Invalid day entered."

day = input("Enter a day: ")
day = day.lower()

match day:

    case "monday" | "tuesday":
        print("It's the start of the week.")

    case "wednesday" | "thursday":
        print("It's midweek.")

    case "friday":
        print("It's almost the weekend.")

    case "saturday" | "sunday":
        print("It's the weekend.")

    case _:
        print("Invalid day entered.")
