"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
class Node():
	def __init__(self,value):
		self.value = value
		self.next = None
class LinkedList():
	def __init__(self,node):
		self.head = node
	def display(self):
		current = self.head
		result = []
		while current:
			result.append(str(current.value))
			current = current.next
		print( '->'.join(result))

class Solution():
	def __init__(self,list1,list2):
		self.list1 = list1
		self.list2 = list2
	def add_two_numbers(self):
		dummy = Node(0)
		self.head = dummy
		current = self.head
		self.helper(current, self.list1, self.list2, 0)
		self.head = self.head.next
	def helper(self, current_head, list1, list2, carry):
		while list1 or list2:
			v1 = list1.value if list1 else 0
			v2 = list2.value if list2 else 0
			sum_val = v1 + v2 + carry
			carry = sum_val//10
			current_head.next = Node(sum_val%10)
			current_head = current_head.next
			if list1:
				list1 = list1.next
			if list2:
				list2 = list2.next
			self.helper(current_head, list1, list2,carry)
		if carry > 0:
			current_head.next = Node(carry)
	def display(self):
		current = self.head
		result = []
		while current:
			result.append(str(current.value))
			current = current.next
		print('->'.join(result))

node1 = Node(2)
node1.next = Node(4)
node1.next.next = Node(3)
node2 = Node(5)
node2.next = Node(6)
node2.next.next = Node(4)
list1 = LinkedList(node1)
list2 = LinkedList(node2)
list1.display()
list2.display()
print('-------')
obj = Solution(list1.head,list2.head)
obj.add_two_numbers()
obj.display()
