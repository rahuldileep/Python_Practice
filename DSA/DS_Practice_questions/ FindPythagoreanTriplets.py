"""
print(findPythagoreanTriplets2([3, 5, 12, 5, 13]))
# True
"""
class Solution():
	def findPythagoreanTriplets(self,input):
		squares = [n*n for n in input]
		for a in input:
			for b in input:
				if a*a + b*b in squares:
					return True
		return False
obj = Solution()
print(obj.findPythagoreanTriplets([3, 5, 12, 5, 13]))