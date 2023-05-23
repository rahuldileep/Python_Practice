"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution():
	def find_non_duplicate(self,input):
		seen = set()
		for item in input:
			if item in seen:
				seen.remove(item)
			else:
				seen.add(item)
		return seen.pop()
obj = Solution()
print(obj.find_non_duplicate([4,1,2,1,2]))