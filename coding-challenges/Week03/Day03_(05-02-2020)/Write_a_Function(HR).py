def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and year % 100 !=0:
        leap = True
    elif year % 400 == 0:
        leap =True
    return leap

year = int(input("Enter the year to be checked -> "))
print(is_leap(year))