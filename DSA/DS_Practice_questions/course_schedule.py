"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""
from collections import defaultdict

class Solution():
	def course_schedule(self, numCourses, prerequisites):
		visited = set()
		graph = defaultdict(list)
		for course, prerequisite in prerequisites:
			graph[course].append(prerequisite)
		for course in graph:
			visited.add(course)
			for prerequisite in graph[course]:
				if prerequisite in graph:
					for prerequisite_2 in graph[prerequisite]:
						if prerequisite_2 in visited:
							return False
			visited.remove(course)
		return True
	def recursive_solution(self,numCourses, prerequisites):
		visited = set()
		graph = defaultdict(list)
		for course, prerequisite in prerequisites:
			graph[course].append(prerequisite)
		def visit(course):
			visited.add(course)
			for prereq in graph[course]:
				if prereq in visited or visit(prereq):
					return True
			visited.remove(course)
			return False
		for cn in range(numCourses):
			if visit(cn):
				return False
		return True

obj = Solution()
print(obj.course_schedule(numCourses = 2, prerequisites = [[1,0]]))
print(obj.recursive_solution(numCourses = 2, prerequisites = [[1,0],[0,1]]))