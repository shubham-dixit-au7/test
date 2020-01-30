#    Question- (when n=4)
#                * * * *        (0 space  + * + 1 space + * + 1 space + * + 1 space + * )
#                 * * *         ( 1 space + * + 1 space + * + 1 space + *)
#                  * *          ( 2 space +  * + 1 space + *)
#                   *           ( 3space + * )

value = int(input("Enter the no. of rows ->")) 
for line in range(value):
    for star in range (0, line):
        print(" " , end ="")
    for space in range (0, value-line):
        print("* " ,end = "")
    print()