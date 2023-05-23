"""
Use the Adapter class when you want to use some existing class, 
but its interface isn’t compatible with the rest of your code.

The Adapter pattern lets you create a middle-layer class that 
serves as a translator between your code and a legacy class, 
a 3rd-party class or any other class with a weird interface.
"""
class Target:
	def request(self):
		return "I am the target request"

class Adaptee:

	def service_request(self):
		return "I have the incompatible data"

class Adapter(Target):

	def __init__(self, adaptee):
		self._adaptee = adaptee

	def request(self):
		print("Converting the data:", self._adaptee.service_request())
		print("Adapted successfully")


def client_code(object):
	object.request()

t = Target()
adp = Adaptee()
adapter = Adapter(adp)
client_code(adapter)


print("*"*100)

class Hindi:

	def speak_Hindi(self):
		print("Namaste !!!")

class English:

	def speak_English(self):
		print("Hello !!!")

class Adapter2:
	def __init__(self, **language_args):
		self.__dict__.update(language_args)

hindi = Hindi()
english = English()
adp1 = Adapter2(speak = hindi.speak_Hindi)
adp2 = Adapter2(speak = english.speak_English)


def client(obj):
	obj.speak()

client(adp1)
client(adp2)

