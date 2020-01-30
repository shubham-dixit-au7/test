string = input("Enter a String -> ")
upper, lower= 0, 0
for i in string:
    if(i.isupper()):
        upper=upper+1
    elif(i.islower()):
        lower=lower+1
print("Total no. of uppercase characters present in string are " , upper)
print("Total no. of lowercase characters present in string are " , lower)