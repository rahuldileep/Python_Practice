"""
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

class Solution():
	def __init__(self,nums,target):
		self.nums = nums
		self.target = target
	def find_idxs(self):
		start = 0
		end = len(self.nums)-1
		indices = []
		while start <= end:
			mid = (start+end)//2
			if self.nums[mid]==self.target:
				indices = self.middleout(mid)
				if indices:
					return indices
					break
			elif self.nums[mid] < self.target:
				start = mid+1
			else:
				end = mid-1
		return [-1,-1]
	def middleout(self, idx):
		left,right = idx, idx
		while self.nums[left] == self.nums[left-1] and left-1 >= 0:
			left = left-1
		while self.nums[right] == self.nums[right+1] and right+1 < len(self.nums):
			right = right+1
		return [left,right]
obj1 = Solution([5,7,7,8,8,10], 8)
print(obj1.find_idxs())
obj2 = Solution([5,7,7,8,8,10], 6)
print(obj2.find_idxs())