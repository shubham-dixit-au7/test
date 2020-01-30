#                           A
#                           BB
#                           CCC
#                           DDDD
#                           EEEEE
#                           FFFFFF

value = int(input("Enter the value of lines to which this pattern works:"))
for line in range(0,value):
    for char in range (0, line + 1):
        print(chr(65 + line), end ="")
    print()