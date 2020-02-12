def insertIntoList(lst, n, element):
  if element < lst[0]:
    lst.insert(0,element)
  elif element > lst[n-1]:
    lst.append(element)
  else:
    for i in range(n-1):
      if lst[i] <= element <= lst[i+1]:
        lst.insert(i+1,element)
        break
  return lst

def insertionSort(lst):
  n = len(lst)
  newLst = []
  for i in range (n):
    val = lst.pop(0)
    if newLst == []:
      newLst = [val]
    else:
      newLst = insertIntoList(newLst,len(newLst), val)
  return newLst


lst = [5, 3, 4, 1, 8]
print("Original List: ", lst)
result = insertionSort(lst)
print("Sorted List In String form: ", end="")
print(" ".join([str(i) for i in result]))