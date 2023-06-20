# Strategy is a behavioral design pattern that turns a set of behaviors into objects and 

# The original object, called context, holds a reference to a strategy object. The context delegates executing the behavior to the linked strategy object. 
# In order to change the way the context performs its work, other objects may replace the currently linked strategy object with another one.

from abc import ABC, abstractmethod
class Context:

	def __init__(self, strategy):
		self._strategy = strategy

	@property
	def strategy(self):
		return self._strategy

	@strategy.setter
	def strategy(self, strategy):
		self._strategy = strategy

	def business_logic(self):
		r = self._strategy.do_algorithm([3,5,8,1,2])
		print(r)

class Strategy:

	@abstractmethod
	def do_algorithm(self):
		pass

class ConcreteStrategyA(Strategy):

	def do_algorithm(self, data):
		return sorted(data)

class ConcreteStrategyB(Strategy):

	def do_algorithm(self, data):
		return sorted(data)[::-1]


context = Context(ConcreteStrategyA())
context.business_logic()
context.strategy = ConcreteStrategyB()
context.business_logic()
