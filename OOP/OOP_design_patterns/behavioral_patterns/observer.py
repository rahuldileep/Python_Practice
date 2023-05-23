from abc import ABC, abstractmethod
from random import randrange

class Publisher:
	def __init__(self):
		self.subscribers = []
		self.state = 0

	def add(self, customer):
		# print("Subscribing customer - {}".format(customer))
		if customer not in self.subscribers:
			self.subscribers.append(customer)

	def remove(self, customer):
		self.subscribers.remove(customer)

	def business_logic(self):
		self.state = randrange(0,10)
		self.notify()

	def notify(self):
		print("Notifying customers...")
		for customer in self.subscribers:
			customer.update(self)

class Subscriber:

	@abstractmethod
	def update(self):
		pass

class ConcreteSubscriberA(Subscriber):

	def update(self, publisher_object):
		print("publisher state changed to", publisher_object.state)
		print("Subscriber A got the notification")

class ConcreteSubscriberB(Subscriber):

	def update(self, publisher_object):
		print("publisher state changed to", publisher_object.state)
		print("Subscriber B got the notification")

Pub = Publisher()
cust1 = ConcreteSubscriberA()
cust2 = ConcreteSubscriberB()
Pub.add(cust1)
Pub.add(cust2)
Pub.business_logic()
