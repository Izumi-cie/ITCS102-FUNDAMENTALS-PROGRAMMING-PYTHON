#Odd Number Summation
#input 10 odd numbers

odd_sum = 0
for i in range(1,11,1):
    num = eval(input("Enter a number -->"))
    if num % 2 == 1:
        odd_sum += num
print(f"The sum of all odd number is: {odd_sum}")