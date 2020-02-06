#Question- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Answer-

n = int(input("Enter the size of list -> "))
arr=list(map(int,input().split()))
largest=max(arr)
for i in range(0,n):
    if(max(arr) == largest):
        arr.remove(max(arr))
arr.sort(reverse=True)
print(arr[0])