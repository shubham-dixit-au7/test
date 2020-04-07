# Question- Using the recursive fibonacci number function, print first n fibonacci numbers. (Any Answer containing loops will not be checked)

# Answer-
def fab(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fab(n - 1) + fab(n - 2)

n = int(input())
for i in range(n + 1):
  if i < n:
    print(fab(i), end = ", ")
  else:
    print(fab(i))



	
