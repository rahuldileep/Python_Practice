class Solution():
	def __init__(self,array):
		self.array = array
	def next_smaller_to_left(self):
		n = len(self.array)
		output = [-1]*n
		stack = []
		print('Input:',self.array)
		for i in range(n):
			if stack and stack[-1] < self.array[i]: 
				output[i] = stack[-1]
			else:
				while stack and stack[-1] >= self.array[i]:
					stack.pop()
				if stack and stack[-1] < self.array[i]: 
					output[i] = stack[-1]
			stack.append(self.array[i])
		print('Output:',output)
input =[6,2,5,4,5,1,6]
obj = Solution(input)
obj.next_smaller_to_left()