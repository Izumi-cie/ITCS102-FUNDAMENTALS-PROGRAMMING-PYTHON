num = eval(input("Enter a number: "))

factorial = 1
for this in range(num, 0, -1):
    factorial *= this

print("The factorial of", num, "is", factorial)
