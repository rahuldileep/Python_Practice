def subset_sum_counter(i, target):
	if target == 0:
		return 1
	if i == len(nums):
		return 0
	if nums[i] <= target:
		return subset_sum_counter(i+1,target-nums[i]) + subset_sum_counter(i+1,target)
	else:
		return subset_sum_counter(i+1,target)

def subset_sum_counter_mem(i,target):
	if target == 0:
		return 1
	if i == len(nums):
		return 0
	elif mem_table[i][target] != -1:
		return mem_table[i][target]
	if nums[i] <= target:
		mem_table[i][target] = subset_sum_counter(i+1,target-nums[i]) + subset_sum_counter(i+1,target)
		return mem_table[i][target]
	else:
		mem_table[i][target] =  subset_sum_counter(i+1,target)
		return mem_table[i][target]

def subset_sum_counter_dp(n,target):
	for i in range(1,n+1):
		for j in range(1,target+1):
			if nums[i-1] <= j:
				dp_table[i][j] = dp_table[i-1][j-nums[i-1]] + dp_table[i-1][j]
			else:
				dp_table[i][j] = dp_table[i-1][j]
	return dp_table[-1][-1]

# nums = [2,3,5,6,8,10]
nums = [1,1,2,3]
target = 4
n = len(nums)
mem_table = [[-1 for x in range(target+1)] for y in range(n)]
dp_table = [[0 for x in range(target+1)] for y in range(n+1)]
for i in range(n+1):
	for j in range(target+1):
		if j == 0:
			dp_table[i][j] = 1

print(subset_sum_counter(0,target))
print(subset_sum_counter_mem(0,target))
print(subset_sum_counter_dp(n,target))
