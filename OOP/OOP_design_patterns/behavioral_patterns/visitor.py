from abc import ABC, abstractmethod

class Component(ABC):

	@abstractmethod
	def accept(self, visitor):
		pass

class Visitor(ABC):

	@abstractmethod
	def visit_concrete_component_a(self, component):
		pass

	@abstractmethod
	def visit_concrete_component_b(self, component):
		pass

class ConcreteComponentA(Component):

	def accept(self, visitor):
		visitor.visit_concrete_component_a(self)

	def exclusive_method_concrete_component_a(self):
		return "A"

class ConcreteComponentB(Component):

	def accept(self, visitor):
		visitor.visit_concrete_component_b(self)

	def exclusive_method_concrete_component_b(self):
		return "B"

class ConcreteVisitor1(Visitor):

	def visit_concrete_component_a(self, component):
		print("{} + ConcreteVisitor1".format(component.exclusive_method_concrete_component_a()))

	def visit_concrete_component_b(self, component):
		print("{} + ConcreteVisitor1".format(component.exclusive_method_concrete_component_b()))

class ConcreteVisitor2(Visitor):

	def visit_concrete_component_a(self, component):
		print("{} + ConcreteVisitor2".format(component.exclusive_method_concrete_component_a()))

	def visit_concrete_component_b(self, component):
		print("{} + ConcreteVisitor2".format(component.exclusive_method_concrete_component_b()))

def client_code(components, visitor):
	for component in components:
		component.accept(visitor)

visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()
components = [ConcreteComponentA(), ConcreteComponentB()]
client_code(components, visitor1)
client_code(components, visitor2)

