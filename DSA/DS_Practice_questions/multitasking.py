class Solution():
	def multitasking(self, tasks, cooldown):
		counter = 0
		task_dict = {}
		for task in tasks:
			if task not in task_dict:
				counter += cooldown
				task_dict[task] = counter
			counter += 1
			print(task,counter,task_dict)
		return counter-1
print(Solution().multitasking([1,1,2,1],3))