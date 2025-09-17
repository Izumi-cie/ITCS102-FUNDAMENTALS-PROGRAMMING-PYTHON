# code_challenge8.py
# Multiplication Table Maker

print("MULTIPLICATION TABLE MAKER")
num = eval(input("Enter a number: "))

print("\nMultiplication table for", num, ":")
for product in range(1, 11):
    print(num, "x", product, "=", num * product)