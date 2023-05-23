"""
The Bridge pattern lets you split the monolithic class into 
several class hierarchies. After this, you can change the classes 
in each hierarchy independently of the classes in the others. 
This approach simplifies code maintenance and minimizes the risk 
of breaking existing code.
Our purpose is to separate out implementation specific abstraction 
from implementation-independent abstraction
"""
from abc import ABC, abstractmethod

class Abstraction():

	def __init__(self, implementation):
		self.implementation = implementation

	def operation(self):
		return "Base abstraction called with: {}".format(self.implementation.implementation_operation())

class Extended_Abstraction(Abstraction):

	def operation(self):
		return "Extended abstraction called with: {}".format(self.implementation.implementation_operation())

class Implementation():

	@abstractmethod
	def implementation_operation(self):
		pass

class ConcreteImplementationA(Implementation):

	def implementation_operation(self):
		return "Concrete implementation of platform A"

class ConcreteImplementationB(Implementation):

	def implementation_operation(self):
		return "Concrete implementation of platform B"


def client_code(abstraction):
	print("Client calling operation: {}".format(abstraction.operation()))

implementation = ConcreteImplementationA()
abstraction = Abstraction(implementation)
client_code(abstraction)

implementation = ConcreteImplementationB()
abstraction = Extended_Abstraction(implementation)
client_code(abstraction)

####################################################################################################################


class ProducingAPI1:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API1 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class ProducingAPI2:

	"""Implementation specific Abstraction"""

	def produceCuboid(self, length, breadth, height):

		print(f'API2 is producing Cuboid with length = {length}, '
			f' Breadth = {breadth} and Height = {height}')

class Cuboid:

	def __init__(self, length, breadth, height, producingAPI):

		"""Initialize the necessary attributes
		Implementation independent Abstraction"""

		self._length = length
		self._breadth = breadth
		self._height = height

		self._producingAPI = producingAPI

	def produce(self):

		"""Implementation specific Abstraction"""

		self._producingAPI.produceCuboid(self._length, self._breadth, self._height)

	def expand(self, times):

		"""Implementation independent Abstraction"""

		self._length = self._length * times
		self._breadth = self._breadth * times
		self._height = self._height * times


"""Instantiate a cuboid and pass to it an
object of ProducingAPIone"""

cuboid1 = Cuboid(1, 2, 3, ProducingAPI1())
cuboid1.produce()

cuboid2 = Cuboid(19, 19, 19, ProducingAPI2())
cuboid2.produce()

####################################################################################################################

class Device:
	def is_enabled(self):
		pass
	def disbale(self):
		pass
	def enable(self):
		pass

class TV(Device):
	def __init__(self):
		self.power = False
	def is_enabled(self):
		return self.power
	def disbale(self):
		print("Powering off TV")
		self.power = False
	def enable(self):
		print("Powering on TV")
		self.power = True

class Radio(Device):
	def __init__(self):
		self.power = False
	def is_enabled(self):
		return self.power
	def disbale(self):
		print("Powering off Radio")
		self.power = False
	def enable(self):
		print("Powering on Radio")
		self.power = True
		
class Remote:
	def __init__(self, device):
		self.device = device
	def toggle_power(self):
		if self.device.is_enabled():
			self.device.disbale()
		else:
			self.device.enable()
tv = TV()
radio = Radio()
tv_remote = Remote(tv)
radio_remote = Remote(radio)
tv_remote.toggle_power()
radio_remote.toggle_power()

