#using for loop, ask user to input 10 numbers
#after input, get the summation of all numbers

num = 0
for kahit_ano in range(1,11):
    number = eval(input("Enter a number ->"))
    num += number
    print('bilang ng nagbayad na estudyante' ,num)
print('Total ng nagbayad na estudyante' ,num)
