#Question- Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of given two numbers.


#Answer-

first = int(input ("Enter First Number -> "))
second = int(input ("Enter Second Number -> "))

  
    if first > second: 
        small = second 
    else: 
        small = second 
    for iterable in range(1, small+1): 
        if((first % iterable == 0) and (second % iterable == 0)): 
            gcd = iterable 
print ("The gcd of 60 and 48 is : ",gcd) 
 