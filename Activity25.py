from Activity25_1 import *

name = input("What is your name? : ")

print(f"Welcome, {name}, to my file compiler!")

t = True

while t == True:
    print("Please select a program to run:")
    print("A - Activity 1\nB - Activity 2\nC - Activity 3\nD - Activity 4\nE - Exit")

    new = input("Enter your choice: ").lower()

    if new == "a":
        activity1()
        continue
    elif new == "b":
        activity2()
        continue
    elif new == "c":
        activity3()
        continue
    elif new == "d":
        activity4()
        continue
    elif new == "e":
        print("Thank you for using my coding program!")
        break
    else:
        print("Invalid input. Please try again.")
