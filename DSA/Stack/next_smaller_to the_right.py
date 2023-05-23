class Solution():
	def __init__(self, array):
		self.array = array
	def next_smaller_element_to_right(self):
		n = len(self.array)
		print('Input:',self.array)
		output = [-1]*(n)
		stack = []
		for i in range(n-1,-1,-1):
			if stack and stack[-1] < self.array[i]:
				output[i] = stack[-1]
			else:
				while stack and stack[-1] >= self.array[i]:
					stack.pop()
				if stack and stack[-1] < self.array[i]:
					output[i] = stack[-1]
			stack.append(self.array[i])
		print(output)

input = [1,3,0,0,1,2,4]
obj = Solution(input)
obj.next_smaller_element_to_right()