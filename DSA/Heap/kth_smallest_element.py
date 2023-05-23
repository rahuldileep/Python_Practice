import heapq 

lst = [7,10,4,3,20,15]
k = 3
heap = []

for num in lst:
	heapq.heappush(heap,-1*num)
	if len(heap)>k:
		heapq.heappop(heap)

print('%drd smallest element:'%(k),-1*heap[0])