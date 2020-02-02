#Count sort

string= input("enter the list of integers separated by commas")
lst= list(map(int,string.split(",")))
n=len(lst)
nodupslist=list(set(lst))
nodupslist.sort()
print(nodupslist)
count=[0] * (max(lst)+1)
print(count)
for i in range(n):
  count[lst[i]]+=1
print(count)
sortedList= []
for i in nodupslist:
  for j in range(count[i]):
    sortedList.append(i)
    print("stepwise ->" ,sortedList)
print(sortedList)

