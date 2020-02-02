#selection sort-

string= input("enter the list of integers separated by commas")
lst= list(map(int,string.split(",")))
n=len(lst)
for i in range(n-1):
  minIndex=i
  minimum=lst[i]
  for j in range(i+1,n):
    if lst[j]<minimum:
      minimum = lst[j]
      minIndex= j
      lst[i],lst[minIndex]=lst[minIndex],lst[i]
  print("Step ",i+1," ( i = ",i+1 ," )-> ", lst)
print("Sorted List -> ",lst)