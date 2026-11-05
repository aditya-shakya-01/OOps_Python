
# shape Calculator
from abc import ABC,abstractmethod
class Shape(ABC):
    @ abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2

class Retangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

# Object Creation 
cir=Circle(7)
print(cir.area())

retangle=Retangle(15,12)
print(retangle.area())