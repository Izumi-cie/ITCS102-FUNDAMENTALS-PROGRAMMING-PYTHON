amount = eval(input("Enter amount to Deposit - ->"))

print("\nHere is a breakdown, using PH denomination:")

n1 = 1000
n2 = 500
n3 = 200
n4 = 100
n5 = 50
n6 = 20
n7 = 10
n8 = 5
n9 = 1

denominations = [n1, n2, n3, n4, n5, n6, n7, n8, n9]

for denom in denominations:
    count = amount // denom
    amount %= denom
    print(f"{count} = {denom}")