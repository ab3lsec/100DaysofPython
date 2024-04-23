import time

timestamp = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))


if (hour > 5 and hour < 12):
    print("Good Morning!!, its", timestamp)
elif (hour >= 12  and hour < 16):
    print("Good AfterNoon!!, its", timestamp)
elif (hour > 16 and hour < 19):
    print("Good Evening!!, its", timestamp)
else:
    print("Good Night!!, its", timestamp)