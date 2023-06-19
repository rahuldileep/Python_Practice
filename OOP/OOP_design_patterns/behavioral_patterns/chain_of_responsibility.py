from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler:

	@abstractmethod
	def set_next(self, handler):
		pass

	@abstractmethod
	def handle(self, request):
		pass

class AbstractHandler(Handler):

	def __init__(self):
		self._next_handler = None

	def set_next(self, handler):
		self._next_handler = handler
		return handler

	def handle(self, request):
		print(f"Super handling {request} for {self}")
		if self._next_handler:
			return self._next_handler.handle(request)
		return None

class MonkeyHandler(AbstractHandler):

	def handle(self, request):

		if request == "banana":
			return "Monkey: I will eat {}".format(request)
		else:
			print(f"Monkey: I dont want {request}")
			return super().handle(request)

class SquirrelHandler(AbstractHandler):

	def handle(self, request):

		if request == "nut":
			return "Squirrel: I will eat {}".format(request)
		else:
			print(f"Squirrel: I dont want {request}")
			return super().handle(request)

class DogHandler(AbstractHandler):

	def handle(self, request):

		if request == "Bone":
			return "Dog: I will eat {}".format(request)
		else:
			print(f"Dog: I dont want {request}")
			return super().handle(request)

def client_code(handler):
	for food in ["nut", "banana", "Cup of coffee"]:
		print("Who wants a {}".format(food))
		result = handler.handle(food)
		if result:
			print(result)
		else:
			print("The {} was left untouched".format(food))


monkey = MonkeyHandler()
squirrel = SquirrelHandler()
dog = DogHandler()
monkey.set_next(squirrel).set_next(dog)
client_code(monkey)