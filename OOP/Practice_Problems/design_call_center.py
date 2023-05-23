from abc import ABCMeta, abstractmethod
from enum import Enum

class Employee(metaclass=ABCMeta):

	def __init__(self,employee_id, rank, call_center_id):
		self.employee_id = employee_id
		self.rank = rank
		self.call_center_id = call_center_id
		self.call = None

	def take_call(self,call):
		self.call = call
		self.call.employee = self
		self.call.state = CallState.IN_PROGRESS

	def end_call(self,call):
		self.call = call
		self.call.state = CallState.COMPLETE
		self.call_center.notify_call_completed(self.call)

	@abstractmethod
	def escalate_call(self):
		pass

	def _escalate_call(self):
		self.call.state = CallState.READY
        self.call_center.notify_call_escalated(self.call)
        self.call = None

class Operator(Employee):
	def __init__(self,employee_id):
		super(Operator,self).__init__(employee_id,Rank.OPERATOR)

	def escalate_call(self):
		self.call.level = Rank.SUPERVISOR
		self._escalate_call()

class Supervisor(Employee):
	def __init__(self.employee_id):
		super(Supervisor,self).__init__(employee_id,Rank.SUPERVISOR)

	def escalate_call(self):
		self.call.level = Rank.MANAGER
		self._escalate_call()

class Manger(Employee):
	def __init__(self,employee_id):
		super(Manager,self).__init__(employee_id,Rank.MANAGER)

	def escalate_call(self):
		raise NotImplemented('Managers must be able to handle any call')

class Call(object):

	def __init__(self,rank):
		self.rank = rank
		self.state = CallState.READY
		self.employee = None

class CallState(Enum):

	READY= 0
	IN_PROGRESS = 1
	COMPLETE = 2

class Rank(Enum):

	OPERATOR = 0
	SUPERVISOR = 1
	MANAGER = 2


class CallCenter(object):

	def __init__(self,operators, supervisors, managers):
		self.operators = operators
		self.supervisors = supervisors
		self.managers = managers
		self.queued_calls = deque()

	def dispatch_call(self,call):
		if call.rank not in ["operators", "supervisors", "managers"]:
			raise ValueError("Invalid Rank {}".format(call.rank))

		if call.rank == Rank.OPERATOR:
			employee = self._dispatch_call(call, self.operators)

		if call.rank == Rank.SUPERVISOR:
			employee = self._dispatch_call(call, self.supervisors)

		if call.rank == Rank.MANAGER:
			employee = self._dispatch_call(call, self.managers)

		if employee is None:
			self.queued_calls.append(call)

	def _dispatch_call(self,employees):
		for employee in employees:
			if employee.call is None:
				employee.take_call(call)
			    return employee
		return None





