class Node(object):
	def __init__(self,key,value):
		self.key = key
		self.val = value

class HashMap(object):
	def __init__(self,size):
		self.size = size
		self.hash_list = [[] for _ in range(self.size)]

	def _get_hash_key(self,key):
		hash = 0
		for ch in key:
			hash += ord(ch)
		return hash%(self.size-1)

	def add(self,key,value):
		hash_key = self._get_hash_key(key)
		for item in self.hash_list[hash_key]:
			if item.key == key:
				item.val = value
				return
		self.hash_list[hash_key].append(Node(key,value))

	def print(self):
		print("############")
		for item in self.hash_list:
			if item is not None:
				for node in item:
					print(node.key,node.val)

	def remove(self,key):
		hash_key = self._get_hash_key(key)
		for index,item in enumerate(self.hash_list[hash_key]):
			if item.key == key:
				del self.hash_list[hash_key][index]
				return 

hm = HashMap(5)
hm.add("R","11")
hm.add("Ra","12")
hm.add("P","13")
hm.add("P","14")
hm.add("M","15")
hm.add("M","16")
hm.add("A","17")
hm.print()
hm.remove("R")
hm.print()
