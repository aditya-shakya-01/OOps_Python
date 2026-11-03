
# Hierarchical Inheritance

# Create a Parent Class 
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# Creates Three Child Class

class Circle(Shape):
    def area(self,radius):
        return (3.14*radius*radius)

class Rectangle(Shape):
    def area(self,length,width):
        return length*width

class Triangle(Shape):
    def area(self,base,height):
        return (1/2*base*height)

# Create Objects
cir=Circle()
print(cir.area(7))

tri=Triangle()
print(tri.area(2,3))
