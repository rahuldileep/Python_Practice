"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same 
color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

class Solution():
	def sort(self,nums):
		if len(nums)>1:
			mid = len(nums)//2
			left = nums[:mid]
			right = nums[mid:]
			self.sort(left)
			self.sort(right)
			i,j,k =0,0,0
			while i < len(left) and j < len(right):
				if left[i] < right[j]:
					nums[k] = left[i]
					i += 1
				else:
					nums[k] = right[j]
					j += 1
				k += 1
			while i < len(left):
				nums[k] = left[i]
				i += 1
				k += 1
			while j < len(right):
				nums[k] = right[j]
				j += 1
				k += 1
		return nums

obj = Solution()
print(obj.sort([2,0,2,1,1,0]))