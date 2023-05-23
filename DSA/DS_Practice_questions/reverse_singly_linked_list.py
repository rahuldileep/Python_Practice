"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

class Node():
	def __init__(self,val):
		self.val = val
		self.next = None
class Linked_list():
	def __init__(self):
		self.head = None
	def add(self,val):
		new_node = Node(val)
		if not self.head:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			current.next = new_node
	def display(self):
		result = []
		current = self.head
		while current:
			result.append(str(current.val))
			current = current.next
		return '->'.join(result)
	def reverse(self):
		current = self.head
		prev = None
		while current:
			next_node = current.next
			current.next = prev
			prev = current
			current = next_node
		self.head = prev
	def reverse_recursive(self,head):
		if not head or not head.next:
			return head
		p = self.reverse_recursive(head.next)
		head.next.next = head
		head.next = None
		self.head = p
		return p
	def sort_linked_list(self,head):
		if head is None or head.next is None:
			return head
		mid = self.get_mid(head)
		mid_next = mid.next
		mid.next = None
		left = self.sort_linked_list(head)
		right = self.sort_linked_list(mid_next)
		sorted_list = self.mergelist(left,right)
		return sorted_list
	def get_mid(self,head):
		if head == None:
			return head
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next
		return slow
	def mergelist(self,left,right):
		result = None
		if left is None:
			return right
		if right is None:
			return left
		if left.val < right.val:
			result = left
			result.next = self.mergelist(left.next,right)
		else:
			result = right
			result.next = self.mergelist(left,right.next)
		return result

obj=Linked_list()
obj.add(1)
obj.add(4)
obj.add(5)
obj.add(2)
obj.add(3)

# obj2=Linked_list()
# obj2.add(0)
# obj2.add(3)
# obj2.add(2)

# print(obj.display())
# obj.reverse_recursive(obj.head)
# print(obj.display())
# obj.reverse()
print(obj.display())
obj.sort_linked_list(obj.head)
print(obj.display())
# print(obj2.display())


