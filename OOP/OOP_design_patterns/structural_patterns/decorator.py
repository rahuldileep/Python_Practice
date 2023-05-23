from functools import wraps
from abc import ABC, abstractmethod

def decorator(fn):
	"""
	This is a decorated function
	"""
	@wraps(fn)
	def wrapper(*args, **kwargs):
		"""
		Inside wrapper function
		"""
		print("Inside wrapper function")
		ret = fn(*args, **kwargs)
		return "Wrapped the original output >>>>\n" + ret + "<<<<<"

	return wrapper

@decorator
def func():
	"""
	 This is test function
	"""
	return "Inside original function"

print(func())

help(func)




class Component:
	@abstractmethod
	def operation(self):
		pass

class ConcreteComponent(Component):

	def operation(self):
		print("Inside ConcreteComponent operation")

def client_code(component_obj):
	print("Client Calling component operation")
	component_obj.operation()


class Decorator(Component):

	def __init__(self, component):
		self._component = component

	@property
	def component(self):
		return self._component

	def operation(self):
		self._component.operation()

class ConcreteDecorator1(Decorator):

	def operation(self):
		print("Inside ConcreteDecorator1 operation")
		self.component.operation()

class ConcreteDecorator2(Decorator):

	def operation(self):
		print("Inside ConcreteDecorator2 operation")
		self.component.operation()


simple = ConcreteComponent()
d1 = ConcreteDecorator1(simple)
d2 = ConcreteDecorator2(d1)
client_code(d2)