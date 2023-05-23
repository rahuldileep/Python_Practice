class Solution():

	def __init__(self,events):
		self.events = events

	def get_event_date(self,event):
		return event.date

	def current_users(self):
		self.events.sort(key=self.get_event_date)
		machines = {}
		for event in self.events:
			if event.machine not in machines:
				machines[event.machine] = set()
			if event.event_type == 'login':
				machines[event.machine].add(event.user)
			elif event.event_type == 'logout':
				if event.user in machines[event.machine]:
					machines[event.machine].remove(event.user)
		return machines

	def generate_report(self):
		machines = self.current_users()
		for machine, users in machines.items():
			if len(users) > 0:
				user_list = ','.join(users)
				print('{}: {}'.format(machine, user_list))

class Event():
	def __init__(self, date, event_type, machine, user):
		self.date = date
		self.event_type = event_type
		self.machine = machine
		self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

obj_users = Solution(events)
obj_users.generate_report()
