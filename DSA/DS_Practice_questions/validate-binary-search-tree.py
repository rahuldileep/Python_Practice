"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
"""

class Node():
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class binary_tree():
	def __init__(self, node):
		self.head = node
	def display(self):
		current = self.head
		return self.preorder_traversal(current,[])
	def preorder_traversal(self, current, result):
		if not current:
			return
		result.append(current.value)
		self.preorder_traversal(current.left,result)
		self.preorder_traversal(current.right,result)
		return result

class Solution():
	def __init__(self, node):
		self.head = node
	def validate_binary_search_tree(self):
		root = self.head
		return self.helper(root,float('-Inf'),float('Inf'))
	def helper(self, node, lower_limit, upper_limit):
		if not node:
			return True
		if not lower_limit <= node.value <= upper_limit:
			return False
		if not self.helper(node.left, lower_limit, node.value):
			return False
		if not self.helper(node.right, node.value, upper_limit):
			return False
		return True
		
node1 = Node(2)
node1.left = Node(1)
node1.right = Node(3)
tree1 = binary_tree(node1)
print(tree1.display())
obj1 = Solution(node1)
print(obj1.validate_binary_search_tree())

node2 = Node(5)
node2.left = Node(1)
node2.right = Node(4)
node2.right.left = Node(3)
node2.right.right = Node(6)
tree2 = binary_tree(node2)
print(tree2.display())
obj2 = Solution(node2)
print(obj2.validate_binary_search_tree())


