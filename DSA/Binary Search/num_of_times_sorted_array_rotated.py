class Solution():
	def __init__(self,array):
		self.array = array
	def count_rotation(self):
		N = len(self.array)
		start, end = 0, N-1
		while start<=end:
			if self.array[start] <= self.array[end]:
				return start
			mid = start + (end-start)/2
			prev = (mid + N - 1)%N
			nxt = (mid+1)%N
			if self.array[mid] <= self.array[prev] and self.array[mid] < self.array[nxt]:
				return mid
			elif self.array[start]<=self.array[mid]:
				start = mid+1
			elif self.array[mid]<=self.array[end]:
				end = mid-1


nums = [9,10,11,12,15,18,2,5,6,8]
obj = Solution(nums)
print('# of rotations:',obj.count_rotation())