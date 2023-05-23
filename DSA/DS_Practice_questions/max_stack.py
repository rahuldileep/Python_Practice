"""
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
"""
class MaxStack():
	def __init__(self):
		self.data = []
		self.max = 0
	def push(self,val):
		self.data.append(val)
		self.max = max(self.max,max(self.data))
	def pop(self):
		val = self.data.pop()
		self.max = max(self.max,max(self.data))
		return val
	def popMax(self):
		for i in range(len(self.data)-1,-1,-1):
			if self.data[i] == self.max:
				return self.data.pop(i)
	def top(self):
		return self.data[-1]
	def peekMax(self):
		return self.max

stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
print(stack.top())
print(stack.popMax())
print(stack.top())
print(stack.peekMax())
print(stack.pop())
print(stack.top())