"""
 Use the Abstract Factory when your code needs to work with various families of related products, 
 but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or 
 you simply want to allow for future extensibility.

The Abstract Factory provides you with an interface for creating objects from each class of the product family.
As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant 
of a product which doesn’t match the products already created by your app.
"""

from abc import ABC, abstractmethod

class Laptop(ABC):
	@abstractmethod
	def purchase(self):
		pass

class Tablet(ABC):
	@abstractmethod
	def purchase(self):
		pass

class DeviceFactory(ABC):
	@abstractmethod
	def create_laptop(self):
		pass

	@abstractmethod
	def create_tablet(self):
		pass

class AppleLaptop(Laptop):
	def purchase(self):
		print("Purchased a Apple laptop")

class MicrosoftLaptop(Laptop):
	def purchase(self):
		print("Purchased a Microsoft laptop")

class AppleTablet(Tablet):
	def purchase(self):
		print("Purchased a Apple tablet")

class MicrosoftTablet(Tablet):
	def purchase(self):
		print("Purchased a Microsoft tablet")


class ApppleFactory(DeviceFactory):
	def create_laptop(self):
		return AppleLaptop()
	def create_tablet(self):
		return AppleTablet()

class MicrosoftFactory(DeviceFactory):
	def create_laptop(self):
		return MicrosoftLaptop()
	def create_tablet(self):
		return MicrosoftTablet()

factory = ApppleFactory()
laptop = factory.create_laptop()
laptop.purchase()
tablet = factory.create_tablet()
tablet.purchase()

