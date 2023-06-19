from abc import ABC, abstractmethod

class Node():

	@abstractmethod
	def traverse(self):
		pass

	@abstractmethod
	def add(self):
		pass

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

class LeafNode(Node):

	def __init__(self, val):
		self.val = val

	def traverse(self):
		return f"LeafNode({str(self.val)})"

class ParentNode(Node):

	def __init__(self, val, is_root=False):
		self.val = val
		self.children = []
		self.is_root = is_root

	def add(self, child):
		self.children.append(child)
		child.parent = self

	def traverse(self):
		result = []
		for child in self.children:
			result.append(child.traverse())
# client_code(tree)
		return f"\tNode({self.val})->\t({','.join(result)})" if not self.is_root else f"root({self.val})->\t{','.join(result)}"


node1 = LeafNode(1)
node2 = LeafNode(2)
node3 = LeafNode(3)
node4 = LeafNode(4)
branch1 = ParentNode(10)
branch2 = ParentNode(20)
branch1.add(node1)
branch1.add(node2)
branch2.add(node3)
branch2.add(node4)
tree = ParentNode(100, True)
tree.add(branch1)
tree.add(branch2)
print(tree.traverse())