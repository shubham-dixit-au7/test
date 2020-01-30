#Question (n=5)
#                        *                   (4 spaces + *)
#                       ***                  (3 spaces + (2 *line_no.+1) * 1 star )
#                      *****                 (2 spaces + (2 *line_no.+1) * 1 star )
#                     *******                (1 space  +  (2 *line_no.+1) * 1 star )
#                    *********               (0 space  + (2 *line_no.+1) * 1 star )

value = int(input("Enter the no. of rows -> ")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, (2 * line) + 1 ):
        print("*" , end ="")
    print()
