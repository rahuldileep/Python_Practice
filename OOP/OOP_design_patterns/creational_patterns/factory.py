"""
Use the Factory Method when you don’t know beforehand the exact types and dependencies of the objects your code should work with.
The Factory Method separates product construction code from the code that actually uses the product. 
Therefore it’s easier to extend the product construction code independently from the rest of the code.

For example, to add a new product type to the app, you’ll only need to create a new creator subclass and 
override the factory method in it.

"""
import abc
from pprint import pprint

class Person(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def person_method(self):
		pass

class Teacher(Person):

	def __init__(self):
		self.name = "Teacher"

	def person_method(self):
		print("I am a Teacher")


class Student(Person):

	def __init__(self):
		self.name = "Student"

	def person_method(self):
		print("I am Student")

class factoryclass:

	def factorymethod(self, val):
		if val == "teacher":
			return Teacher()
		if val == "student":
			return Student()

obj = factoryclass()
fact_obj = obj.factorymethod("student")
fact_obj.person_method()

fact_obj = obj.factorymethod("teacher")
fact_obj.person_method()
print("*"*100)


#====================================================================================================================================================================================#

class Creator:

	@abc.abstractmethod
	def factory_method(self):
		pass

	def logic_operation(self):
		product = self.factorymethod()
		product.operation()

class ConcreteCreator1(Creator):

	def factorymethod(self):
		print("Inside factory method of creator 1")
		return ConcreteProduct1()

class ConcreteCreator2(Creator):

	def factorymethod(self):
		print("Inside factory method of creator 2")
		return ConcreteProduct2()


class Product:

	@abc.abstractmethod
	def operation(self):
		pass

class ConcreteProduct1(Product):

	def operation(self):
		print("Operation called in product 1")

class ConcreteProduct2(Product):

	def operation(self):
		print("Operation called in product 2")


def client_code(creator_object):
	creator_object.logic_operation()

if __name__ == '__main__':
	client_code(ConcreteCreator1())
	print("*"*100)


#====================================================================================================================================================================================#



class Logistic:

	@abc.abstractmethod
	def create_transport(self):
		pass

	def transport(self):
		trn = self.create_transport()
		trn.delivery()


class RoadLogistic(Logistic):

	def create_transport(self):
		print('Inside create transport method of Road logostic')
		return Truck()

class SeaLogistic(Logistic):

	def create_transport(self):
		return Ship()

class Transport:

	@abc.abstractmethod
	def delivery(self):
		pass

class Truck(Transport):

	def delivery(self):
		print("Delivery by Truck")

class Ship(Transport):

	def delivery(self):
		print("Delivery by Ship")

def client_code(logisitic_object):

	logisitic_object.transport()


if __name__ == '__main__':
	client_code(RoadLogistic())
	print("*"*100)

#====================================================================================================================================================================================#
