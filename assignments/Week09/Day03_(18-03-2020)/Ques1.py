#Question- Write a Python program to iterate over dictionaries using for loops.

#Answer-

import sys 


def matrixMultiplication(a, i, j): 

    if (i == j): 
        return 0
    minimumVal = sys.maxsize 
    for k in range(i, j):   
        counter = (matrixMultiplication(a, i, k) 
            + matrixMultiplication(a, k+1, j) 
                + a[i-1] * a[k] * a[j]) 
        if counter < minimumVal: 
            minimumVal = counter; 
    return minimumVal; 
 
user_input = [1, 2, 4, 3, 4] 
n = len(user_input)
print("Minimum value -> ", 
                matrixMultiplication(user_input, 1, n-1))