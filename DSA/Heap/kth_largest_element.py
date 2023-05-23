import heapq 

lst = [7,10,4,3,20,15]
k = 3
heap = []

for num in lst:
	heapq.heappush(heap,num)
	if len(heap)>k:
		heapq.heappop(heap)

print('%drd largest element:'%(k),heap[0])