def min_subset_sum_diff(n,c):
	for i in range(1,n+1):
		for j in range(1,c+1):
			if nums[i-1] <= j:
				dp_table[i][j] = dp_table[i-1][j-nums[i-1]] or dp_table[i-1][j]
			else:
				dp_table[i][j] = dp_table[i-1][j] 
	return dp_table[-1][-1]

nums = [1,2,7]
n = len(nums)
c = sum(nums)
dp_table = [[False for x in range(c+1)] for y in range(n+1)]

for i in range(n+1):
	for j in range(c+1):
		if j == 0:
			dp_table[i][j] = True

print(min_subset_sum_diff(n,c))
min_diff = float("+inf")
vector = dp_table[n][:(c//2)+1]
for i in range(len(vector)):
	if vector[i] == True:
		min_diff = min(min_diff, c-2*i)
print("min_subset_sum_diff:",min_diff)