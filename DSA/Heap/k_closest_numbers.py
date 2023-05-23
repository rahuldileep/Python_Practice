import heapq

class Solution():
	def __init__(self,array,k,x):
		self.array = array
		self.k = k
		self.x = x
	def k_closest(self):
		_arr = self.array
		n = len(_arr)
		heap = []
		for i in range(n):
			heapq.heappush(heap,(-1*abs(self.x - _arr[i]),_arr[i]))
			if len(heap) > k:
				heapq.heappop(heap)
		for i,v in heap:
			print(v)

arr = [5,6,7,8,9]
k = 3
x = 7
obj = Solution(arr,k,x)
obj.k_closest()