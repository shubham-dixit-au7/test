#Question (n=5)
#                        *                   (4 spaces + *)
#                       * *                  (3 spaces + * + 1 space + *)
#                      * * *                 (2 spaces + * + 1 space + * + 1 space + *)
#                     * * * *                (1 space  + * + 1 space + * + 1 space + * + 1 space + *)
#                    * * * * *               (0 space  + * + 1 space + * + 1 space + * + 1 space + * + 1 space + *)

value = int(input("Enter the no. of rows ->")) 
for line in range(value):
    for space in range (0, value-line-1):
        print(" " ,end = "")
    for star in range (0, line+1):
        print("* " , end ="")
    print()
