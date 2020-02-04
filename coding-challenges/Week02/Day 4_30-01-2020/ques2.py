#Question- Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). 
#          Print average and product of all numbers.


#Answer-
count = 0 
sum = 0 
product = 1 
while(True):
    value = input("Enter a Integer -> ")
    if (value == 'q'): break
    value = int(value)
    sum = sum + value
    product = product * value
    count = count + 1
print("Average of all inputs are -> ",sum/count)
print("Product of all inputs are -> ",product)