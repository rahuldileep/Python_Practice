from abc import ABC, abstractmethod

class Component:

	def __init__(self):
		self._parent = None

	@abstractmethod
	def operation(self):
		pass

	@property
	def parent(self):
		return self._parent

	@parent.setter
	def parent(self, parent):
		self._parent = parent

	def add(self, component):
		pass

	def remove(component):
		pass

	def is_composite(self):
		return False

class Leaf(Component):

	def operation(self):

		return "Leaf Node"

class Composite(Component):

	def __init__(self):
		self._children = []

	def add(self, component):
		self._children.append(component)
		component.parent = self

	def remove(self, component):
		self._children.remove(component)
		component.parent = None

	def is_composite(self):
		return True

	def operation(self):
		results = []
		for child in self._children:
			results.append(child.operation())
		print(results)
		return "Branch({})".format('+'.join(results))

def client_code(component):
	print("RESULT: {}".format(component.operation()), end="\n")

leaf1 = Leaf()
leaf2 = Leaf()
leaf3 = Leaf()
leaf4 = Leaf()
tree = Composite()
branch1 = Composite()
branch1.add(leaf1)
branch1.add(leaf2)
branch2 = Composite()
branch2.add(leaf3)
branch2.add(leaf4)
tree.add(branch1)
tree.add(branch2)
client_code(tree)
