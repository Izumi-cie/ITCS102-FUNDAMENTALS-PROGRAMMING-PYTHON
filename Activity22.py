import random

num = random.randint(1,10)

tries = 0
math = True

while math == True:
    game = int(input("What number u guess(1-10): "))
    tries += 1

    if game == num:
        print("Congrats, you're right!!")
        print(f"the number is {num}")
        print(f"You online took {tries} tries")
        break

    else:
        print("WRONGGGG")
        continue