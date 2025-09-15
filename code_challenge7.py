# CODE CHALLENGE 7
# Odd number summation

total = 0

for this in range(10):
    num = int(input("Enter a number: "))
    if num % 2 != 0:
        total += num

print("The sum of all the ODD numbers is", total)
