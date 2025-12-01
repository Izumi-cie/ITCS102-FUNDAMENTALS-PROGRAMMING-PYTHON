from Activity1 import Activity1
from Activity2 import Activity2
from Activity3 import Activity3
from Activity4 import Activity4
from Activity5 import Activity5
from Activity6 import Activity6
from Activity7 import Activity7
from Activity8 import Activity8
from Activity9 import Activity9
from Activity10 import Activity10
from Activity11 import Activity11
from Activity12 import Activity12
from Activity13 import Activity13
from Activity14 import Activity14
from Activity15 import Activity15
from Activity16 import Activity16
from Activity17 import Activity17
from Activity18 import Activity18
from Activity19 import Activity19
from Activity20 import Activity20
from Activity21 import Activity21
from Activity22 import Activity22
from Activity23 import Activity23
from Activity24_1 import Activity241
from Activity24 import Activity24
from Activity25 import activity25
from Activity25_1 import Activity251

from code_challenge1 import kodc1
from code_challenge2 import kodc2
from code_challenge3 import kodc3
from code_challenge4 import kodc4
from code_challenge5 import kodc5
from code_challenge6 import kodc6
from code_challenge7 import kodc7
from code_challenge8 import kodc8
from code_challenge9 import kodc9
from code_challenge10 import kodc10
from code_challenge11 import kodc11
from code_challenge12 import kodc12
from code_challenge13 import kodc13
from code_challenge14 import kodc14
from code_challenge15 import kodc15
from code_challenge16 import kodc16


print("Welcome to my coding program!")
name = input("Welcome! What is your name? : ")
print(f"Hello, {name}!")

tr = True
while tr:
    print("Please choose an option below:")
    print("1 - Activities\n2 - Code Challenges\nP - Exit Program")
    n = input("Enter your choice: ")

    # ACTIVITIES
    if n == "1":
        print("You selected: Activities")
        print("1 = Activities 1–5\n2 = Activities 6–10\n3 = Activities 11–15\n4 = Activities 16–20\n5 = Activities 21–25\nM = Back to Menu")
        act1 = eval(input("Choose a category: "))

        if act1 == 1:
            print("Activities 1–5")
            print("1 = Activity 1\n2 = Activity 2\n3 = Activity 3\n4 = Activity 4\n5 = Activity 5\nM = Back to Menu")
            ac1 = input("Choose an activity: ").lower()
            if ac1 == "1":
                print("You selected Activity 1")
                Activity1()
                continue
            elif ac1 == "2":
                print("You selected Activity 2")
                Activity2()
                continue
            elif ac1 == "3":
                print("You selected Activity 3")
                Activity3()
                continue
            elif ac1 == "4":
                print("You selected Activity 4")
                Activity4()
                continue
            elif ac1 == "5":
                print("You selected Activity 5")
                Activity5()
                continue
            elif ac1 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif act1 == 2:
            print("Activities 6–10")
            print("6 = Activity 6\n7 = Activity 7\n8 = Activity 8\n9 = Activity 9\n10 = Activity 10\nM = Back to Menu")
            ac2 = input("Choose an activity: ").lower()
            if ac2 == "6":
                print("You selected Activity 6")
                Activity6()
                continue
            elif ac2 == "7":
                print("You selected Activity 7")
                Activity7()
                continue
            elif ac2 == "8":
                print("You selected Activity 8")
                Activity8()
                continue
            elif ac2 == "9":
                print("You selected Activity 9")
                Activity9()
                continue
            elif ac2 == "10":
                print("You selected Activity 10")
                Activity10()
                continue
            elif ac2 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif act1 == 3:
            print("Activities 11–15")
            print("11 = Activity 11\n12 = Activity 12\n13 = Activity 13\n14 = Activity 14\n15 = Activity 15\nM = Back to Menu")
            ac3 = input("Choose an activity: ").lower()
            if ac3 == "11":
                print("You selected Activity 11")
                Activity11()
                continue
            elif ac3 == "12":
                print("You selected Activity 12")
                Activity12()
                continue
            elif ac3 == "13":
                print("You selected Activity 13")
                Activity13()
                continue
            elif ac3 == "14":
                print("You selected Activity 14")
                Activity14()
                continue
            elif ac3 == "15":
                print("You selected Activity 15")
                Activity15()
                continue
            elif ac3 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif act1 == 4:
            print("Activities 16–20")
            print("16 = Activity 16\n17 = Activity 17\n18 = Activity 18\n19 = Activity 19\n20 = Activity 20\nM = Back to Menu")
            ac4 = input("Choose an activity: ").lower()
            if ac4 == "16":
                print("You selected Activity 16")
                Activity16()
                continue
            elif ac4 == "17":
                print("You selected Activity 17")
                Activity17()
                continue
            elif ac4 == "18":
                print("You selected Activity 18")
                Activity18()
                continue
            elif ac4 == "19":
                print("You selected Activity 19")
                Activity19()
                continue
            elif ac4 == "20":
                print("You selected Activity 20")
                Activity20()
                continue
            elif ac4 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif act1 == 5:
            print("Activities 21–25")
            print("21 = Activity 21\n22 = Activity 22\n23 = Activity 23\n24 = Activity 24\n24.1 = Activity 24.1\n25 = Activity 25\n25.1 = Activity 25.1\nM = Back to Menu")
            ac5 = input("Choose an activity: ").lower()
            if ac5 == "21":
                print("You selected Activity 21")
                Activity21()
                continue
            elif ac5 == "22":
                print("You selected Activity 22")
                Activity22()
                continue
            elif ac5 == "23":
                print("You selected Activity 23")
                Activity23()
                continue
            elif ac5 == "24":
                print("You selected Activity 24")
                Activity24()
                continue
            elif ac5 == "24.1":
                print("You selected Activity 24.1")
                Activity241()
                continue
            elif ac5 == "25":
                print("You selected Activity 25")
                activity25()
                continue
            elif ac5 == "25.1":
                print("You selected Activity 25.1")
                Activity251()
                continue
            elif ac5 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        continue

    # CODE CHALLENGES
    elif n == "2":
        print("You selected: Code Challenges")
        print("1 = Challenges 1–5\n2 = Challenges 6–10\n3 = Challenges 11–15\nM = Back to Menu")
        np = input("Choose a category: ")

        if np == "1":
            print("Code Challenges 1–5")
            print("1 = Challenge 1\n2 = Challenge 2\n3 = Challenge 3\n4 = Challenge 4\n5 = Challenge 5\nM = Back to Menu")
            cc1 = input("Choose a challenge: ").lower()
            if cc1 == "1":
                print("You selected Challenge 1")
                kodc1()
                continue
            elif cc1 == "2":
                print("You selected Challenge 2")
                kodc2()
                continue
            elif cc1 == "3":
                print("You selected Challenge 3")
                kodc3()
                continue
            elif cc1 == "4":
                print("You selected Challenge 4")
                kodc4()
                continue
            elif cc1 == "5":
                print("You selected Challenge 5")
                kodc5()
                continue
            elif cc1 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif np == "2":
            print("Code Challenges 6–10")
            print("6 = Challenge 6\n7 = Challenge 7\n8 = Challenge 8\n9 = Challenge 9\n10 = Challenge 10\nM = Back to Menu")
            cc2 = input("Choose a challenge: ").lower()
            if cc2 == "6":
                print("You selected Challenge 6")
                kodc6()
                continue
            elif cc2 == "7":
                print("You selected Challenge 7")
                kodc7()
                continue
            elif cc2 == "8":
                print("You selected Challenge 8")
                kodc8()
                continue
            elif cc2 == "9":
                print("You selected Challenge 9")
                kodc9()
                continue
            elif cc2 == "10":
                print("You selected Challenge 10")
                kodc10()
                continue
            elif cc2 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        elif np == "3":
            print("Code Challenges 11–15")
            print("11 = Challenge 11\n12 = Challenge 12\n13 = Challenge 13\n14 = Challenge 14\n15 = Challenge 15\nM = Back to Menu")
            cc3 = input("Choose a challenge: ").lower()
            if cc3 == "11":
                print("You selected Challenge 11")
                kodc11()
                continue
            elif cc3 == "12":
                print("You selected Challenge 12")
                kodc12()
                continue
            elif cc3 == "13":
                print("You selected Challenge 13")
                kodc13()
                continue
            elif cc3 == "14":
                print("You selected Challenge 14")
                kodc14()
                continue
            elif cc3 == "15":
                print("You selected Challenge 15")
                kodc15()
                continue
            elif cc3 == "m":
                print("Returning to Menu...")
            else:
                print("Invalid choice. Please try again.")
                continue

        continue

    # EXIT PROGRAM
    elif n == "p".lower():
        print("Are you sure you want to exit?")
        ex = input("Type 'Exit' to quit or 'Continue' to go back: ").lower()
        if ex == "continue":
            print("Returning to Menu...")
            continue
        elif ex == "exit":
            print("Thank you for using my coding program!!")
            print("Goodbye!")
            break

    else:
        print("Invalid choice. Please select one of the available options.")
        continue