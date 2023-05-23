#Abstraction means to hide implementation using interface and abstract classes.
#It focuses only on revealing the necessary details of a system and hiding irrelevant information to minimize its complexity. 
#In simpler words, we can say that it means to show what an object does and how it hides.

from abc import abstractmethod

class Shape:

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

class Circle(Shape):
  def __init__(self, r = 0):
    self.radius = r
    self.pi = 3.142 

  #define methods
  def area(self):
    return self.pi * self.radius * self.radius

  def perimeter(self):
    return 2 * self.pi * self.radius

def main():
  circle = Circle(5)
  print("Area: {:.2f}".format(circle.area()))
  print("Perimeter: {:.2f}".format(circle.perimeter()))

if __name__ == "__main__":
    main()