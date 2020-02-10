# Question- Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given integer B in array 
            # A.
            # Your algorithm runtime complexity must be in the order of O(log n). Return an array of size 2, such that first element = starting position of B in A and second element = ending position of B in A, if B is not found in A return [-1, -1].

            # Input 1:
            # A = [5, 7, 7, 8, 8, 10]
            # B = 8
            # Output 1:
            # [3, 4]
            # Explanation 1:
            # First occurence of 8 in A is at index 3
            # Second occurence of 8 in A is at index 4
            # ans = [3, 4]

            # Input 2:
            # A = [5, 17, 100, 111]
            # B = 3
            # Output 2:
            # [-1, -1]


# Answer-
def findIndexOfTarget(lst, size, target) : 
    first = -1
    last = -1
    indexLst = []
    for i in range(0,size) : 
        if (target != lst[i]) : 
            continue
        if (first == -1) : 
            first = i 
        last = i 
      
    if (first != -1) : 
        indexLst.extend([first, last])
        return indexLst
    else : 
        return [-1, -1] 

lst =[]
size= int(input("Enter the  size of the list -> "))
for i in range (0,size):
    elem=int(input())
    lst.append(elem)
target = int(input("Enter the target value -> "))
print(findIndexOfTarget(lst, size, target)) 