def bubbleSort(lst, n):
	for i in range(1, n+1):
		swapped = False
		for j in range(n-i):	                   # to loop over right side values of lst[i] to check values
			if lst[j] > lst[j+1]:  				   #  checking adjacent values
				lst[j],lst[j+1] = lst[j+1], lst[j] # swapping values
				swapped = True
		if not swapped: 				   #just to stop unintended steps when array is sorted
			break
	return lst

lst = [29, 10, 14, 37, 14]
n = len(lst)
result = bubbleSort(lst ,n)
print(" ".join([str(i) for i in result]))
