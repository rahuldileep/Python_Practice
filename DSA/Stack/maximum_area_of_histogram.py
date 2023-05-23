class Solution():
	def __init__(self,array):
		 self.array = array
	def max_area_histogram(self):
		_arr = self.array
		print('Input :',_arr)
		area = 0
		nsl = []
		nsr = []
		stack = []
		n = len(_arr)
		for i in range(n):
			if stack and stack[-1] < _arr[i]: 
				nsl.append(stack[-1][1])
			else:
				while stack and stack[-1][0] >= _arr[i]:
					stack.pop()
				if stack and stack[-1][0] < _arr[i]: 
					nsl.append(stack[-1][1])
				else:
					nsl.append(-1)
			stack.append((_arr[i],i))

		stack2 = []
		for i in range(n-1,-1,-1):
			while stack2 and stack2[-1][0] >= _arr[i]:
				stack2.pop()
			if stack2 and stack2[-1][0] < _arr[i]:
				nsr.insert(0,stack2[-1][1])
			else:
				nsr.append(n)
			stack2.append((_arr[i],i))
		for i in range(n):
			area = max((nsr[i]-nsl[i]-1)*_arr[i], area)
		print('Max area:',area)
obj = Solution([6,2,5,4,5,1,6])
obj.max_area_histogram()
