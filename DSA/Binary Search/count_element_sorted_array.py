class Solution():
	def __init__(self, array):
		self.nums = array
	def count_k(self,k):
		self.k = k
		i,j = 0, len(self.nums)-1
		while i <= j:
			mid = i + (j-i)/2
			if self.nums[mid] < k:
				i = mid + 1
			elif self.nums[mid] > k:
				j = mid -1
			else:
				count = self.middleout(mid)
				print('# of %d: %d'%(k,count))
				break
	def middleout(self,idx):
		i,j = idx,idx
		count = 0
		while self.nums[i] == self.k:
			i -= 1
			count += 1
			if i<0:
				break
		while self.nums[j] == self.k:
			j += 1
			count += 1
			if j > len(self.nums)-1:
				break
		return count-1
nums = [2,4,10,10,10,18,20]
obj = Solution(nums)
obj.count_k(22)
