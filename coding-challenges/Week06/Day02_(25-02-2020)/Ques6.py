#Question- https://www.geeksforgeeks.org/given-level-order-traversal-binary-tree-check-tree-min-heap/

#Answer-

def Is_Minheap(arr,length):
    n_par = int(length/2 - 1)
    for i in range(n_par):
        if arr[i] > arr[2 * i + 1]:  
            return 0
        if ((2 * i + 2) < length) and (arr[i] > arr[2* i + 2]): 
                return 0
    return 1


level_order = [2, 4, 7, 8, 16, 9, 13, 11]  
n = len(level_order) 
if Is_Minheap(level_order, n):
    print('Tree is min-heap')
else:
    print('Tree is not min-heap')

