def find_count_subset_sum(n,t):
	for i in range(1,n+1):
		for j in range(1,t+1):
			if nums[i-1] <= j:
				dp_table[i][j] = dp_table[i-1][j-nums[i-1]] + dp_table[i-1][j]
			else:
				dp_table[i][j] = dp_table[i-1][j]
	return dp_table[-1][-1]
nums = [1,1,2,3]
n = len(nums)
diff = 1

# s1-s2 = diff
# s1+s2 = sum(nums)
# ------------------
# 2s1 = sum(nums)+diff

target = (sum(nums)+diff)//2
dp_table = [[0 for x in range(target+1)] for y in range(n+1)]
for i in range(n+1):
	for j in range(target+1):
		if j == 0:
			dp_table[i][j] = 1

print(find_count_subset_sum(n,target))