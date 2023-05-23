"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution():
	def __init__(self,nums,target):
		self.nums = nums
		self.target = target
	def two_sum(self):
		seen = dict()
		for idx, val in enumerate(self.nums):
			complement = self.target-val
			if complement in seen:
				return [seen[complement], idx]
			seen[val] = idx
obj = Solution([2, 7, 11, 15], 9)
print(obj.two_sum())