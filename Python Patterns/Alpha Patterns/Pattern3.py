#                   e
#                  edc
#                 edcba
#                gfedcba
#               ihgfedcba

value = int(input("Enter the no. of rows -> ")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, (2 * line) + 1 ):
        print(chr( (97+(2 * (value-1))) - star) , end ="")
    print()
