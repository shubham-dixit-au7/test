# Question 1) Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the 						entire range of values in your array to sort. 
# 			Each time a value occurs in the original array, you increment the counter at that index. 
# 			At the end, run through your counting array, printing the value of each non-zero valued index that number of times. 
# 			For example, consider an array . All of the values are in the range , so create an array of zeroes, . 
# 			The results of each iteration follow:
			
# 			i    arr[i]    result
			
# 			0    1    [0, 1, 0, 0]              
# 			1    1    [0, 2, 0, 0]
# 			2    3    [0, 2, 0, 1]
# 			3    2    [0, 2, 1, 1]
# 			4    1    [0, 3, 1, 1]

# 			Now we can print the list of occurrences,0 3 1 1  or determine the sorted array: sorted = [1,1,1,2,3]

# Answer-

lst = [1, 1, 3, 2, 1]
print("Original Array ->", lst)
n =len(lst)
lstCount = [0]* (max(lst)+1)
nodupList = list(set(lst))
nodupList.sort()
for i in range(n):
  lstCount[lst[i]]+=1
print(lstCount)
sortedList = []
for i in nodupList:
  for j in range(lstCount[i]):
    sortedList.append(i)
    print(sortedList)