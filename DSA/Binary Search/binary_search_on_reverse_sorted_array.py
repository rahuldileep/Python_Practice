class Solution():
	def __init__(self, nums):
		self.nums = nums
	def binary_search_on_reverse(self,x):
		i,j = 0, len(self.nums)
		while i < j:
			mid = i + (j-i)/2
			if self.nums[mid] == x:
				print('Found %d at index %d'%(x,mid))
				break
			elif self.nums[mid] > x:
				i = mid+1
			else:
				j = mid-1
nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
obj = Solution(nums)
obj.binary_search_on_reverse(7)
