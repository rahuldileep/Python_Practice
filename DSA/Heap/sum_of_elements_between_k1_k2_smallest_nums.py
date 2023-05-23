class Solution():
	def __init__(self,array, k1, k2):
		self.nums = array
		self.k1 = k1
		self.k2 = k2
	def func(self):
		num1 = self.kth_smallest(self.k1)
		num2 = self.kth_smallest(self.k2)
		_sum = 0
		for num in self.nums:
			if num>num1 and num<num2:
				_sum += num
		print(_sum)
	def kth_smallest(self,k):
		import heapq
		heap = []
		for num in self.nums:
			heapq.heappush(heap,-1*num)
			if len(heap)>k:
				heapq.heappop(heap)
		return -1*heap[0]

nums = [1,3,12,5,15,11]
obj = Solution(nums,3,6)
obj.func()