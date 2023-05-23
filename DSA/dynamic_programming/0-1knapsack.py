def max_profit(i,C):
	if i == len(wt) or C <= 0:
		return 0
	elif wt[i] <= C:
		return max(val[i]+max_profit(i+1,C-wt[i]), max_profit(i+1,C))
	else:
		return max_profit(i+1,C)

def max_profit_mem(i,C):
	if i == len(wt) or C <= 0:
		return 0
	if mem_table[i][C] != -1:
		return mem_table[i][C]
	elif wt[i] <= C:
		mem_table[i][C] = max(val[i]+max_profit(i+1,C-wt[i]), max_profit(i+1,C))
		return mem_table[i][C]
	else:
		mem_table[i][C] = max_profit(i+1,C)
		return mem_table[i][C]

def max_profit_dp(n,C):
	for i in range(1,n+1):
		for j in range(1,C+1):
			if wt[i-1] <= j:
				dp_table[i][j] = max(val[i-1]+dp_table[i-1][j-wt[i-1]], dp_table[i-1][j])
			else:
				dp_table[i][j] = dp_table[i-1][j]
	return dp_table[-1][-1]

wt = [1,3,4]
val = [1,2,5]
C = 5
n = len(wt)
mem_table = [[-1 for x in range(C+1)] for y in range(n)]
dp_table = [[0 for x in range(C+1)] for y in range(n+1)]
print(max_profit(0,C))
print(max_profit_mem(0,C))
print(max_profit_dp(n,C))