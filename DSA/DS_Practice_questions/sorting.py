import random
class sorting_algo():
	def __init__(self,nums):
		self.nums = nums

class selection_sorting_algo(sorting_algo):
	def selection_sort(self):
		A = self.nums
		for i in range(len(A)):
			min_idx = i
			for j in range(i+1,len(A)):
				if A[j] < A[min_idx]:
					min_idx = j
			A[min_idx], A[i] = A[i], A[min_idx]

class bubble_sort_algo(sorting_algo):
	def bubble_sort(self):
		A = self.nums
		for i in range(len(A)):
			for j in range(len(A)-1,i,-1):
				if A[j] < A[j-1]:
					A[j], A[j-1] = A[j-1], A[j]

class insertion_sort_algo(sorting_algo):
	def insertion_sort(self):
		A = self.nums
		self.recursive(A,len(A))
		self.iterative(A)

	def recursive(self,A,n):
		if n<=1:
			return
		self.recursive(A,n-1)
		self.iterative(A)
		i = n-1
		nth = A[i]
		j = i-1
		while j>=0 and A[j]>nth:
			A[j+1] = A[j]
			j -= 1
		A[j+1] = nth
		return

	def iterative(self,A):
	 	for i in range(1,len(A)):
	 		nth = A[i]
	 		j = i-1
	 		while j>=0 and A[j]>nth:
	 			A[j+1] = A[j]
	 			j -= 1
	 		A[j+1] = nth
	 	return


class merge_sort_algo(sorting_algo):
	def merge_sort(self):
		self.mergesort_helper(0,len(self.nums)-1)
	def mergesort_helper(self,start,end):
		if start>=end:
			return 
		mid = (start+end)//2
		self.mergesort_helper(start, mid)
		self.mergesort_helper(mid+1, end)
		i = start
		j = mid+1
		aux = []
		while i <= mid and j <= end:
			if self.nums[i] <= self.nums[j]:
				aux.append(self.nums[i])
				i += 1
			else:
				aux.append(self.nums[j])
				j += 1
		while i<= mid:
			aux.append(self.nums[i])
			i += 1
		while j<=end:
			aux.append(self.nums[j])
			j += 1
		self.nums[start:end+1] = aux	


class heap_sort_algo(sorting_algo):
	def heap_sort(self):
		aux = []
		import heapq
		heapq.heapify(self.nums)
		while self.nums:
			aux.append(heapq.heappop(self.nums))
		self.nums[:] = aux[:]

class quick_sort_algo(sorting_algo):
	def quick_sort(self):
		self.quick_sort_helper(0,len(self.nums)-1)
	def quick_sort_helper(self, start, end):
		if start >= end:
			return 
		rand_idx = random.randint(start, end)
		self.nums[rand_idx], self.nums[start] = self.nums[start], self.nums[rand_idx]
		pivot = self.nums[start]
		left = start
		right = start
		for right in range(start+1,end+1):
			if self.nums[right] < pivot:
				left += 1
				self.nums[left], self.nums[right] = self.nums[right], self.nums[left]
		self.nums[start], self.nums[left] = self.nums[left], self.nums[start]
		self.quick_sort_helper(start,left-1)
		self.quick_sort_helper(left+1,end)


input_array1 = [4,1,3,5,2]
print('Input1:', input_array1)
merge_sort_object = selection_sorting_algo(input_array1)
merge_sort_object.selection_sort()
print('Output1:',input_array1)

input_array1 = [4,1,3,5,2]
print('Input2:', input_array1)
merge_sort_object = bubble_sort_algo(input_array1)
merge_sort_object.bubble_sort()
print('Output2:',input_array1)

input_array1 = [4,1,3,5,2]
print('Input3:', input_array1)
merge_sort_object = insertion_sort_algo(input_array1)
merge_sort_object.insertion_sort()
print('Output3:',input_array1)

input_array1 = [4,1,3,5,2]
print('Input4:', input_array1)
merge_sort_object = merge_sort_algo(input_array1)
merge_sort_object.merge_sort()
print('Output4:',input_array1)

input_array1 = [4,1,3,5,2]
print('Input5:', input_array1)
heap_sort_object = heap_sort_algo(input_array1)
heap_sort_object.heap_sort()
print('Output5:',input_array1)

input_array1 = [4,1,3,5,2]
print('Input6:', input_array1)
heap_sort_object = quick_sort_algo(input_array1)
heap_sort_object.quick_sort()
print('Output6:',input_array1)