#    Question- (when n=4)
#                *******        (0 * space  + star * 7)
#                 *****         (1 * space  + star * 5)
#                  ***          (2 * space  + star * 3)
#                   *           (3 * space  + star * 1)

value = int(input("Enter the no. of rows ->")) 
for line in range(value):
    for star in range (0, line):
        print(" " , end ="")
    for space in range (0,  (2 *(value-line)-1)):
        print("*" ,end = "")
    print()