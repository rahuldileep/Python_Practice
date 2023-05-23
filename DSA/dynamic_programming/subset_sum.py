def subset_sum(i,target):
	if target == 0:
		return True
	if i == len(nums):
		return False
	elif nums[i] <= target:
		return subset_sum(i+1,target-nums[i]) or subset_sum(i+1,target)
	else:
		return subset_sum(i+1,target)

def subset_sum_mem(i,target):
	if target == 0:
		return True
	if i == len(nums):
		return False
	elif mem_table[i][target] != -1:
		return mem_table[i][target]
	elif nums[i] <= target:
		mem_table[i][target] = subset_sum(i+1,target-nums[i]) or subset_sum(i+1,target)
		return mem_table[i][target]
	else:
		mem_table[i][target] = subset_sum(i+1,target)
		return mem_table[i][target]

def subset_sum_dp(n,target):
	for i in range(1,n+1):
		for j in range(1,target+1):
			if nums[i-1] <= j:
				dp_table[i][j] = dp_table[i-1][j-nums[i-1]] or dp_table[i-1][j]
			else:
				dp_table[i][j] = dp_table[i-1][j]
	return dp_table[-1][-1]

nums = [2,3,7,8,10]
target = 11
n = len(nums)
mem_table = [[-1 for x in range(target+1)] for y in range(n)]
dp_table = [[False for x in range(target+1)] for y in range(n+1)]
for i in range(n+1):
	for j in range(target+1):
		if j == 0:
			dp_table[i][j] = True

print(subset_sum(0,target))
print(subset_sum_mem(0,target))
print(subset_sum_dp(n,target))