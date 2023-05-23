"""
Use the Builder pattern when you want your code to be able to create different 
representations of some product (for example, stone and wooden houses).

The Builder pattern can be applied when construction of various representations 
of the product involves similar steps that differ only in the details.

The base builder interface defines all possible construction steps, 
and concrete builders implement these steps to construct particular representations 
of the product. Meanwhile, the director class guides the order of construction.
"""
from abc import ABC, abstractmethod

class Builder:

	@abstractmethod
	def step1(self):
		pass

	@abstractmethod
	def step2(self):
		pass

	@abstractmethod
	def step3(self):
		pass

	@abstractmethod
	def get_product(self):
		pass

class ConcreteBuilder1(Builder):

	def __init__(self):
		self._product = Prodcut()

	def step1(self):
		self._product.steps.append("step1 executed")
		return self

	def step2(self):
		self._product.steps.append("step2 executed")
		return self

	def step3(self):
		self._product.steps.append("step3 executed")
		return self

	def get_product(self):
		return self._product


class Prodcut:

	def __init__(self):
		self.steps = []
	def __str__(self):
		return "\n".join(self.steps)

class Director:

	def __init__(self, builder_obj):
		self._builder = builder_obj

	def construct(self):
		return self._builder.step1().step2().step3().get_product()


b1 = ConcreteBuilder1()
d1 = Director(b1)
product = d1.construct()
print(product)

#=================================================================#

class IHouseBuilder:

	@abstractmethod
	def set_building_type(self, building_type):
		pass

	@abstractmethod
	def set_num_of_doors(self, doors):
		pass

	@abstractmethod
	def set_windows(self, windows):
		pass

	@abstractmethod
	def set_num_of_garage(self, garage):
		pass

	@abstractmethod
	def get_result(self, garage):
		pass

class HouseBuilder(IHouseBuilder):

	def __init__(self):
		self._house = House()

	def set_building_type(self, building_type):
		self._house.building_type = building_type
		return self

	def set_num_of_doors(self, doors):
		self._house.doors = doors
		return self

	def set_windows(self, windows):
		self._house.windows = windows
		return self

	def set_num_of_garage(self, garage):
		self._house.garage = garage
		return self

	def get_result(self):
		return self._house

class House:

	def __init__(self):
		self.building_type = None
		self.doors = None
		self.windows = None
		self.garage = None

	def __str__(self):
		return "The {} has {} doors, {} windows & {} garage.".format(self.building_type, self.doors, self.windows, self.garage)

class Apartment_Director:

	def construct(self):
		return HouseBuilder().set_building_type("Apartment").set_num_of_doors(2).set_windows(4).set_num_of_garage(0).get_result()

class TownHouse_Director:

	def construct(self):
		return HouseBuilder().set_building_type("Town House").set_num_of_doors(4).set_windows(12).set_num_of_garage(1).get_result()


Apt_d = Apartment_Director()
apartment = Apt_d.construct()
print(apartment)

TW_d = TownHouse_Director()
tw = TW_d.construct()
print(tw)

#=================================================================#

class Director:
	#Director 
	def __init__(self, builder):
		self._builder = builder

	def construct_car(self):
		self._builder.create_new_car()
		self._builder.add_model()
		self._builder.add_tyre()
		self._builder.add_engine()

	def get_car(self):
		return self._builder.car


class Builder:
	#Abstract builder
	def __init__(self):
		self.car = None

	def create_new_car(self):
		self.car = Car()


class Mercedes_Builder(Builder):
	#concrete builder

	def add_model(self):
		self.car.model = "Mercedes CLA250"

	def add_tyre(self):
		self.car.tyres = "Regular Tires"

	def add_engine(self):
		self.car.engine = "Turbo"


class Car:
	#product

	def __init__(self):
		self.model = None
		self.tyres = None
		self.engine = None

	def __str__(self):
		return "Model: {}, Tyres: {}, Engine: {}".format(self.model, self.tyres, self.engine)

builder = Mercedes_Builder()
director = Director(builder)
director.construct_car()
car = director.get_car()
print(car)


