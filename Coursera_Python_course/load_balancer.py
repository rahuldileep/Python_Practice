"""In this exercise, we'll create a few classes to simulate a server
   that's taking connections from the outside and then a load balancer
   that ensures that there are enough servers to serve those connections.
   To represent the servers that are taking care of the connections, 
   we'll use a Server class. Each connection is represented by an id, 
   that could, for example, be the IP address of the computer connecting 
   to the server. For our simulation, each connection creates a random 
   amount of load in the server, between 1 and 10.
"""
import random

class Server():
	def __init__(self):
		self.connections = {}

	def add_connection(self, connection_id):
		load = random.random()*10
		self.connections[connection_id] = load

	def close_connection(self,connection_id):
		for key in self.connections.keys():
			if key == connection_id:
				del self.connections[connection_id]

	def get_load(self):
		total = 0
		for val in self.connections.values():
			total += val
		return total

	def __str__(self):
		return "{:.2f}".format(self.get_load())

class LoadBalancing():
	def __init__(self):
		self.connections = {}
		self.servers = [Server()]

	def add_connection(self,connection_id):
		server = random.choice(self.servers)
		self.connections[connection_id] = server
		server.add_connection(connection_id)
		self.ensure_availability()

	def close_connection(self,connection_id):
		for con_id, server in self.connections.items():
			if con_id == connection_id:
				server.close_connection(connection_id)
				del self.connections[connection_id]

	def avg_load(self):
		total = 0
		for server in self.servers:
			total += server.get_load()
		return total/len(self.servers)

	def ensure_availability(self):

		while self.avg_load() > 5:
			self.servers.append(Server())
		pass

	def __str__(self):
		loads = [str(server) for server in self.servers]
		return "[{}]".format(",".join(loads))

lb = LoadBalancing()
for connection in range(10):
	lb.add_connection(connection)
print(lb.avg_load())