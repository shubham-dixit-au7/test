#    Question- (when n=6)
#                *        (star * line_no.)
#                **       (star * line_no.)
#                ***      (star * line_no.)
#                ****     (star * line_no.)
#                *****    (star * line_no.)
#                ******   (star * line_no.)
#                *****    line 7 star 5
#                ****     line 8 star 4
#                ***      line 9 star 3
#                **       line10 star 2
#                *        line11 star 1



value = int(input("Enter the number of rows ->"))
value= value//2 + 1
for line in range( value+1 ):
    print( "*" * (line + 1) )
for line1 in range ( value, 0 ,-1 ):
    print ( "*" * line1 )
