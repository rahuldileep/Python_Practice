"""
Use the Prototype pattern when your code shouldn’t depend on the concrete classes 
of objects that you need to copy.

This happens a lot when your code works with objects passed to you from 3rd-party code 
via some interface. The concrete classes of these objects are unknown, 
and you couldn’t depend on them even if you wanted to.
"""

import copy
class Prototype:

	def __init__(self):
		self.objects = {}

	def register_object(self, name, obj):
		self.objects[name] = obj

	def unregister_object(self, name):
		del self.objects[name]

	def clone(self, name, **attr):
		obj = copy.deepcopy(self.objects.get(name))
		obj.__dict__.update(attr)
		return obj

class Car:
	def __init__(self):
		self.model = None
		self.color = None
		self.options = None

	def __str__(self):
		return "Model: {} | Color: {} | option: {}".format(self.model, self.color, self.options)

c = Car()
prototype = Prototype()
prototype.register_object("car",c)
cla = prototype.clone("car", model="CLA", color = "Black")
s_class = prototype.clone("car", model="S", color = "Black", options="Sunroof")

print(cla)
print(s_class)