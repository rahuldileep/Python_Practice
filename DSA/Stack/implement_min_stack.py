# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

class Stack():
	def __init__(self):
		self.stack = []
		self.min_val = float("inf")
	def push(self,num):
		self.min_val = min(self.min_val,num)
		self.stack.append((num,self.min_val))
	def getMin(self):
		print(self.min_val)
	def pop(self):
		tmp,tmp_min = self.stack.pop() 
		self.min_val = self.stack[-1][1]
	def top(self):
		print(self.stack[-1][0])

minStack = Stack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()