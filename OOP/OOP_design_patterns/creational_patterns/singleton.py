class Singleton:
	_shared_dict = {}
	instance = None

	def __new__(cls,**kwargs):
		if not hasattr(cls,'instance') or not cls.instance:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self, **kwargs):
		Singleton._shared_dict.update(kwargs)

	def __str__(self):
		return str(self._shared_dict)

s1 = Singleton(IND="India")
s2 = Singleton(US="United States")
print(s1)
print(s2)

################################################################

class Singleton:
	instance = None
	def __new__(cls,*args):
		if not hasattr(cls,'instance') or not cls.instance:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self,language):
		self.language = language

	def get_language(self):
		return self.language

obj1 = Singleton("English")
obj2 = Singleton("German")

print(obj1)
print(obj2)
print(obj1.get_language())
print(obj2.get_language())


class Database:
	instance = None
	_shared_dict = {}

	def __new__(cls,**kwargs):
		if not cls.instance:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self, **kwargs):
		Database._shared_dict.update(kwargs)

	def __str__(self):
		return str(self._shared_dict)

s1 = Database(CA="California")
s2 = Database(NY="New York")
print(s1)
