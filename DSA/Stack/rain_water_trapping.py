class Solution():
	def __init__(self,array):
		self.array = array
	def rain_water_trapping(self):
		_arr = self.array
		n = len(_arr)
		ngl = [0]*n
		ngr = [0]*n
		ngl[0] = _arr[0]
		ngr[n-1] = _arr[n-1]
		for i in range(1,n):
			ngl[i] = max(ngl[i-1],_arr[i])
		for i in range(n-2,-1,-1):
			ngr[i] = max(ngr[i+1],_arr[i])
		output = [0]*n
		for i in range(n):
			output[i] = min(ngl[i],ngr[i]) - _arr[i]
		print('Trapped Units:',sum(output))

input = [3,0,0,2,0,4]
obj = Solution(input)
obj.rain_water_trapping()