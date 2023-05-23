### Dynamic Polymorphism - Method Overriding
### Static Polymorphism - Method Overloading & Operator Overloading 

# Method Overriding - if a subclass provides a specific implementation of a method that had already been defined 
# in one of its parent classes, it is known as method overriding.
class Parent:
	def __init__(self):
		pass
	def method_1(self):
		print("Method 1 from Parent class")
	def method_2(self):
		print("Method 2 from Parent class")

class Child(Parent):
	def __init__(self):
		super();
	def method_1(self):
		print("Method 1 from Child class")

c = Child()
c.method_1()
c.method_2()

# Method overloading - Methods are said to be overloaded if a class has more than one method with the same name,
# but either the number of arguments is different, or the type of arguments is different.
#Python does not support method ovrloading, multiple methods with same name cannot me defined. Instead we define
# parameters with a default value
class Area:
    def calculateArea(self, length, breadth=-1):
        if breadth != -1:
            return length * breadth
        else:
            return length * length

area = Area()
print("Area of rectangle = " + str(area.calculateArea(3, 4)))
print("Area of square = " + str(area.calculateArea(6)))

# Operator overloading - Operators can be overloaded to operate in a certain user-defined way. Its corresponding 
# method is invoked to perform its predefined function whenever an operator is used. For example, 
# when the + operator is called, it invokes the special function, add, but this operator acts differently
# for different data types.

class ComplexNumber:
	def __init__(self):
		self.real = 0
		self.imaginary = 0

	def set_values(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def display(self):
		print( "(",self.real, "+", self.imaginary, "i)") 

	def __add__(self, other):
		result = ComplexNumber()
		result.real = self.real + other.real
		result.imaginary = self.imaginary + other.imaginary
		return result

c1 = ComplexNumber()
c1.set_values(10,20)
c2 = ComplexNumber()
c2.set_values(30,40)
c_sum = c1+c2
c_sum.display()


