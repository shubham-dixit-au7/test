#                        *                   (4 spaces + *)
#                       ***                  (3 spaces + (2 *line_no.+1) * 1 star )
#                      *****                 (2 spaces + (2 *line_no.+1) * 1 star )
#                     *******                (1 space  +  (2 *line_no.+1) * 1 star )
#                    *********               (0 space  + (2 *line_no.+1) * 1 star )
#                     *******        (0 * space  + star * 7)
#                      *****         (1 * space  + star * 5)
#                       ***          (2 * space  + star * 3)
#                        *           (3 * space  + star * 1)

value = int(input("Enter the no. of rows -> ")) 
for line in range(1, value+1):
    for space in range (1, value-line+1):
        print(" " ,end = "")
    for star in range (0, (2 * line) - 1 ):
        print("*" , end ="")
    print()
for line in range(value-1):
    for space in range (0, line+1):
        print(" " , end ="")
    for star in range (0,  (2 *(value-line-1)-1)):
        print("*" ,end = "")
    print()