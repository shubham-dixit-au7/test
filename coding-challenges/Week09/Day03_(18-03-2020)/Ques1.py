#Question- Describe how the O(n^2) approach given in the slides works.

#Answer-
def Matrix_chain_order(p,n):
	dp = [[0 for i in range (n)]for i in range (m)]
	for i in range (1, n):
		dp[i][i] = 0
	for l in range (1, n-1):
		for i in range (n-l):
			dp[i][i+l] = min(dp[i+1][i+l] + p[i-1] * p[i] * p[i+l], dp[i][i+l-1] + p[i-1] * p[i+l-1] * p[i+l])
	return dp[1][n-1]

	#here we have a nested loop which cause (n *n) times processing, there approach becomes as complexity of O[n^2]