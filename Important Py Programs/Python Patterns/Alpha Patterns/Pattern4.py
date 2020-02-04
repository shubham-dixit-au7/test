#                   e
#                  e d
#                 e d c
#                e d c b 
#               e d c b a

value = int(input("Enter the no. of rows ->")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, line+1):
        print(chr(101- star ) , end =" ")
    print()