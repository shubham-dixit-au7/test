# Question- Alice is in a shopping mall to buy books, shirts 
# 		and shoes. The mall has exactly N different shops and each shop contains all these three items at different prices. Alice has a plan which she will be following. As per her plan, she won't buy the same item from the current shop if she had already bought that item from the shop adjacent to the current shop.
# 		Alice wants to follow her strategy strictly but at the same time she wants to minimize the total money she spends on shopping. You are provided description about all N shops i.e costs of all three items in each shop. You need to help Alice find minimum money that she needs to spend such that she buys exactly one item from every shop.
# 		First line contain number of test cases T. Each test case in its first line contain N denoting the number of shops in shopping mall.
# 		Then each of next N lines contains three space separated integers denoting cost of books, shirts and shoes in that particular shop.
# 		Constraints
# 		1 ≤ T ≤ 10 1 ≤ N ≤ 100000 Cost of each item (book/shirt/shoe) does not exceed 10000
		 
# 		Sample Input 0
# 		1
# 		3
# 		1 50 50
# 		50 50 50
# 		1 50 50
# 		Sample Output 0
# 		52


#Answer-
T = input()
for x in range(T):
  N = input()
  cost = []
  for i in range(N):
    cost.append(map(int, input().strip().split()))
  
  DP = [ [0, 0, 0] for _ in range(N) ]
  DP[0][0] = cost[0][0]
  DP[0][1] = cost[0][1]
  DP[0][2] = cost[0][2]
  
  for i in range(1, N):
    DP[i][0] = min( DP[i - 1][1], DP[i - 1][2] ) + cost[i][0]
    DP[i][1] = min( DP[i - 1][0], DP[i - 1][2] ) + cost[i][1]
    DP[i][2] = min( DP[i - 1][0], DP[i - 1][1] ) + cost[i][2]
  
  print (min( DP[N - 1][0], DP[N - 1][1], DP[N - 1][2] ))