#                   a
#                  a b
#                 a b c
#                a b c d
#               a b c d e

value = int(input("Enter the no. of rows ->")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, line+1):
        print(chr(97 + star )+" " , end ="")
    print()