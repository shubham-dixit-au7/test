# Question- Using range and for loop, print all multiples of 5, 7, 11 from 1 to 1001.


#Answer-
value = int(input("Enter the number for checking multiples between 1 to 1001( 5,7,11 are valid ).=")) 
count=0
for number in range(1,1002):
    if( value == 5):
        if(number % 5 == 0 ):
            count += 1
            print(number) 
    elif( value == 7 ):
        if(number % 7 == 0 ):
            count += 1
            print(number)
    elif( value == 11 ):
        if(number % 11 == 0):
            count += 1
            print(number)
    else:
        print("Invalid Input=",value)
print("Total number of Multiples of ", number , " are = " , count)