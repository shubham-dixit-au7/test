#Question- https://www.geeksforgeeks.org/find-number-pairs-xy-yx/

#Answer-
import bisect 

def count(x, Y, n, arr): 
    if x == 0: 
        return 0
    if x == 1: 
        return arr[0] 
    index = bisect.bisect_right(Y, x) 
    answer = n - index 
    answer += arr[0] + arr[1] 
    if x == 2: 
        answer -= arr[3] + arr[4] 
    if x == 3: 
        answer += arr[2] 
    return answer 
def countPair(X, Y, m, n): 
    arr = [0] * 5
    for i in range(n): 
        if Y[i] < 5: 
            arr[Y[i]] += 1
    Y.sort() 
    totalPairs = 0 
    for x in X: 
        totalPairs += count(x, Y, n, arr) 
  
    return totalPairs 
  


  
X = [2, 1, 6] 
Y = [1, 5] 
print("Total no. of pairs are = ",  
       countPair(X, Y, len(X), len(Y)))