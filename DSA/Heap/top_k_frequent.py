class Solution():
	def __init__(self, array, k):
		self.array = array
		self.k = k
	def top_k_freq_using_heap(self):
		import heapq
		heap = []
		hashmap = {}
		_arr =self.array
		for num in _arr:
			hashmap[num] = hashmap.get(num,0) + 1
		for k,v in hashmap.items():
			heapq.heappush(heap,(v,k))
			if len(heap) > self.k:
				heapq.heappop(heap)
		result = []
		for v,k in heap:
			result.append(k)
		print(result)

	def top_k_freq_using_dict(self):
		_arr = self.array
		hashmap = {}
		freq = {}
		result = []
		for num in _arr:
			hashmap[num] = hashmap.get(num,0) + 1
		print(hashmap)
		for k,v in hashmap.items():
			if v not in freq:
				freq[v] = [k]
			else:
				freq[v].append(k)
		for i in range(len(_arr),0,-1):
			if i in freq:
				result.extend(freq[i])
			if len(result)>=self.k:
				break
		print(result)

arr = [1,1,1,3,2,2,4]

obj = Solution(arr,2)
obj.top_k_freq_using_dict()
obj.top_k_freq_using_heap()