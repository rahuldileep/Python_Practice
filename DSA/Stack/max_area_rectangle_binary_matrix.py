class Solution():
	def __init__(self,matrix):
		self.matrix = matrix
	def max_area(self):
		def _MAH(array):
			n = len(array)
			nsl = [-1]*n
			nsr = [n]*n
			stack1 = []
			stack2 = []
			output = []
			temp = 0
			for i in range(n):
				if stack1 and stack1[-1][0] < array[i]:
					nsl[i] = stack1[-1][1]
				else:
					while stack1 and stack1[-1][0] >= array[i]:
						stack1.pop()
					if stack1 and stack1[-1][0] < array[i]:
						nsl[i] = stack1[-1][1]
				stack1.append((array[i],i))
			for i in range(n-1,-1,-1):
				if stack2 and stack2[-1][0] < array[i]:
					nsr[i] = stack2[-1][1]
				else:
					while stack2 and stack2[-1][0] >= array[i]:
						stack2.pop()
					if stack2 and stack2[-1][0] < array[i]:
						nsr[i] = stack2[-1][1]
 				stack2.append((array[i],i))
 			for i in range(n):
 				temp = max((nsr[i]-nsl[i]-1)*array[i],temp)
			return temp
		_matrix = self.matrix
		rows = len(_matrix)
		cols = len(_matrix[0])
		area = 0
		sum = [0]*rows
		for i in range(rows):
			for j in range(cols):
				if _matrix[i][j] == 0:
					sum[j] = 0
				else:
					sum[j] += _matrix[i][j]
			area = max(area,_MAH(sum))
		print('Max Area:',area)
input = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
obj = Solution(input)
obj.max_area()