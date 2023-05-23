class Solution():
	def __init__(self,array):
		self.array = array
	def find_element(self,x):
		min_elem_idx = self.find_min()
		start1, end1 = 0, min_elem_idx-1
		start2, end2 = min_elem_idx, len(self.array) - 1
		while start1 <= end1:
			mid = start1 + (end1-start1)/2
			if self.array[mid] == x:
				print('Found element at index:')
				return mid
			elif self.array[mid] < x:
				start1 = mid+1
			else:
				end1 = mid - 1

		while start2 <= end2:
			mid = start2 + (end2-start2)/2
			if self.array[mid] == x:
				print('Found element at index:')
				return mid
			elif self.array[mid] < x:
				start2 = mid+1
			else:
				end2 = mid - 1		

	def find_min(self):
		N = len(self.array)
		start,end= 0, N-1
		while start <= end:
			if self.array[start] < self.array[end]:
				return start
			mid = start + (end - start)/2
			prev = (mid + N -1)%N
			nxt = (mid + 1)%N
			if self.array[mid]<=self.array[prev] and self.array[mid]<=self.array[nxt]:
				return mid
			if self.array[start]<=self.array[mid]:
				start = mid + 1
			elif self.array[mid]<=self.array[end]:
				end = mid -	1
nums = [11,12,15,18,2,5,6,8]
obj = Solution(nums)
print(obj.find_element(12))