# Break Statement
# break is be used inside a loop, if we want to stop executing the loop or break out of loop, if a condition satisfies.
# break statement terminates the execution of the loop it lies within.

# for i in range(1, 100):
#     print("5 x", i, "=", i * 5)

#     if (i == 10):
#         break


# In this example, Normally the Loop runs until "i = 99"
# But when i = 10, the break statemnt executes and terminates the rest of the loop execution.



# Continue Statement
# continue statement skips the iteration instead of terminating the entire loop execution
# If a condition is satisfied, then it skips that step and executes the rest of the loop

for i in range(1, 100):
    if (i == 10):
        print("Skipped")
        continue

    print("5 x", i, "=", i * 5)




# break breaks out of the Loop
# continue skips the iteration