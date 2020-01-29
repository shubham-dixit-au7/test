#    Question- (when n=6)
#                *
#                **
#                ***
#                ****
#                *****
#                ******

value = int(input("Enter the value of lines to which this pattern works:"))
for number in range(0,value):
    print("*" * (number + 1) )