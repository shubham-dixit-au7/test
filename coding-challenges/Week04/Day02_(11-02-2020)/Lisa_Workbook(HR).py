# Question-  https://www.hackerrank.com/challenges/lisa-workbook/problem

# Answer-

def workbook(n, k, arr):
    page, result = 0,0
    for i in range (n):
        ques = 0
        page += 1
        for j in range(arr[i]):
            if ques == k:
                ques = 0
                page += 1
            ques += 1
            if j+1 == page:
                result += 1 
    return result


nk = input().split()
n = int(nk[0])
k = int(nk[1])

arr = list(map(int, input().rstrip().split()))
result = workbook(n, k, arr)
print (result)