#                   a
#                  abc
#                 abcde
#                abcdefg
#               abcdefghi

value = int(input("Enter the no. of rows -> ")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, (2 * line) + 1 ):
        print(chr(97 + star) , end ="")
    print()