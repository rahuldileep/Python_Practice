# State is a behavioral design pattern that allows an object to change the behavior when its internal state changes.

from abc import abstractmethod
from enum import Enum

print("\n*******************************EXAMPLE 1********************************\n")

class Context:

	_state = None

	def __init__(self, state):
		self.state_transition(state)

	def state_transition(self, new_state):
		print(f"setting state: {new_state}")
		self._state = new_state
		self._state.context = self
		print(f"new state context: {self._state.context}")

	def request1(self):
		self._state.handle1()

	def request2(self):
		self._state.handle2()

class State:

	@property
	def context(self):
		return self._context

	@context.setter
	def context(self, context):
		self._context = context

	@abstractmethod
	def handle1(self):
		pass
	@abstractmethod
	def handle2(self):
		pass


class ConcreteStateA(State):

	def handle1(self):
		print("ConcreteStateA handled request1")
		print("Switching State to B")
		self.context.state_transition(ConcreteStateB())

	def handle2(self):
		print("ConcreteStateA handled request2")

class ConcreteStateB(State):

	def handle1(self):
		print("ConcreteStateB handled request1")

	def handle2(self):
		print("ConcreteStateB handled request2")
		print("Switching State to A")
		self.context.state_transition(ConcreteStateA())


context = Context(ConcreteStateA())
context.request1()
context.request2()
context.request2()

print("\n*******************************EXAMPLE 2********************************\n")

class ATM:
	_currentATMState = None

	def __init__(self, currentATMState):
	    self.changestate(currentATMState)

	def changestate(self,new_state):
		print(f"State changing from {self._currentATMState} to {new_state}")
		self._currentATMState = new_state
		new_state.atm_context = self
		new_state.handle()


class ATMCard:
	def __init__(self, cardNumber, customerName):
		self.__cardNumber = cardNumber
		self.__customerName = customerName

class ATMState:

	@property
	def atm_context(self):
		return self._atm_context
	@atm_context.setter
	def atm_context(self, atm_context):
		self._atm_context = atm_context
	@abstractmethod
	def insertCard(self, card):
		pass
	@abstractmethod	
	def authenticatePin(self):
		pass 
	@abstractmethod
	def handle(self):
		pass

class IdleState(ATMState):
	def insertCard(self):
		print("Card Inserted")
		self._atm_context.changestate(HasCardState())
	def handle(self):
		self.insertCard()

class HasCardState(ATMState):
	def authenticatePin(self):
		print("PIN Authenticated")
		self._atm_context.changestate(SelectOperationState())
	def handle(self):
		self.authenticatePin()

class SelectOperationState(ATMState):
	def selectOperation(self):
		pass
	def handle(self):
		pass

atm = ATM(IdleState())



