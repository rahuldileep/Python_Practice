#find all the subsets of the given array

def subsets(slate,idx):
	result.append(slate)
	for i in range(idx,len(nums)):
		if i>idx and nums[i]==nums[i-1]:
			continue
		subsets(slate+[nums[i]],i+1)


nums = [1,2,2]
result = []
subsets([],0)
print(result)

