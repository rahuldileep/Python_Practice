from abc import ABC, abstractmethod

class IChannel(ABC):
	@abstractmethod
	def broadcast(self):
		raise NotImplementedError()

class Customer():
	def __init__(self,age):
		self.age = age
	def get_age(self):
		return self.age

class Channel(IChannel):
	def broadcast(self):
		print("Broadcasting")

class Proxy(IChannel):
	def __init__(self, customer):
		self._customer = customer
		self.channel = Channel()
	def broadcast(self):
		cust_age = self._customer.get_age() 
		if cust_age < 18:
			print("18+ content only")
		else:
			self.channel.broadcast()

john = Customer(17)

channel = Proxy(john)

channel.broadcast()

print("Example #2:")

class Subject:
	@abstractmethod
	def operation(self):
		pass

class RealSubject(Subject):

	def request(self):
		print("Requesting...")

class Proxy(Subject):
	def __init__(self, real_object):
		self._real_obj = real_object
	def request(self):
		if self.access_check():
			self._real_obj.request()
			self.log_access()

	def access_check(self):
		print("Proxy: Checking access...")
		return True

	def log_access(self):
		print("Proxy: Logging the time of request")

def client_code(obj):

	obj.request()

real_obj = RealSubject()
print("Direct access")
client_code(real_obj)
print("###")
proxy_obj = Proxy(real_obj)
client_code(proxy_obj)

