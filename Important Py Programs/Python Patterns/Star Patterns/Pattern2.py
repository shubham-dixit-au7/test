#    Question- (when n=6)

#                ******
#                *****
#                ****
#                ***
#                **
#                *


value = int(input("Enter the value of lines to which this pattern works:"))
for number in range( value , 0, -1 ):
    print( "*" * number )