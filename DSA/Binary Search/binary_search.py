class Solution():
	def __init__(self, nums):
		self.nums = nums
	def binary_search(self,x):
		i,j = 0, len(self.nums)
		while i < j:
			mid = i + (j-i)/2
			if self.nums[mid] == x:
				print('Found %d at index %d'%(x,mid))
				break
			elif self.nums[mid] < x:
				i = mid+1
			else:
				j = mid-1
nums = [1,2,3,4,5,6,7,8,9,10]
obj = Solution(nums)
obj.binary_search(44)
