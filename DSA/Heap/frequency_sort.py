class Solution():
	def __init__(self,array):
		self.array = array
	def frequency_sort(self):
		_arr = self.array
		from collections import Counter
		import heapq
		hashtable = Counter(_arr)
		heap = []
		result = []
		print(hashtable)
		for k,v in hashtable.items():
			heapq.heappush(heap,(v,k))
		for v,k in heap:
			for i in range(v):
				result.append(k)
		print(result)
array = [1,1,1,1,3,3,3,2,2,4]
obj = Solution(array)
obj.frequency_sort()