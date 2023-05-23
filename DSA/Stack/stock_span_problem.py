class Solution():
	def __init__(self,array):
		self.array = array
	def stock_span_problem(self):
		_arr = self.array
		print('Stocks:', _arr)
		stack = []
		n = len(_arr)
		output = []
		for i in range(n):
			while stack and stack[-1][0] < _arr[i]:
				stack.pop()
			if stack and stack[-1][0] > _arr[i]:
				output.append(stack[-1][1])
			else:
				output.append(-1)
			stack.append((_arr[i],i))
		for i in range(n):
			output[i] = i - output[i]
		print(output)
input = [100,80,60,70,60,75,85]
obj = Solution(input)
obj.stock_span_problem()