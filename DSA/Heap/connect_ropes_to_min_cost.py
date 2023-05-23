class Solution():
	def __init__(self,array):
		self.array = array
	def min_cost(self):
		_arr = self.array
		import heapq
		heap = []
		for num in _arr:
			heapq.heappush(heap,num)
		while len(heap)>=2:
			m1 = heapq.heappop(heap)
			m2 = heapq.heappop(heap)
			m1 += m2
			heapq.heappush(heap,m1)
		print(heap.pop())
inp = [1,2,3,4,5]
obj = Solution(inp)
obj.min_cost()