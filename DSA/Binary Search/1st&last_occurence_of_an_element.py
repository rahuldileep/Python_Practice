class Solution():
	def __init__(self, nums):
		self.nums = nums
	def first_and_last_occ(self,x):
		self.x = x
		i,j = 0, len(self.nums)-1
		while i<=j:
			mid = i + (j-i)/2
			if self.nums[mid] == x:
				x1,x2 = self.expand(mid)
				print(x1,x2)
				break
			elif self.nums[mid] < x:
				i = mid + 1
			else:
				j = mid - 1
	def expand(self,mid):
		i,j = mid, mid
		while self.nums[i] == self.x:
			i -=1
			if i<0:
				break
		while self.nums[j] == self.x :
			j += 1
			if j>len(self.nums)-1:
				break
		return i+1,j-1

nums = [2,4,10,10,10,18,20]
obj = Solution(nums)
obj.first_and_last_occ(20)
