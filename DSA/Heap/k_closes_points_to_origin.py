class Solution():
	def __init__(self,points,k):
		self.points = points
		self.k = k
	def k_closest_to_origin(self):
		import heapq
		dist = []
		for point in self.points:
			heapq.heappush(dist,(-1*(point[0]**2 + point[1]**2),point))
			if len(dist)>self.k:
				heapq.heappop(dist)
		print('%d closest points to origin %s'%(self.k, str(self.points)))
		for points in dist:
			print(points[1])
points = [(1,3),(-1,2),(5,8),(0,1),(-2,-2)]
obj = Solution(points,2)
obj.k_closest_to_origin()