
# Shape Calculator

# Parent Class
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius*self.radius

retangle=Retangle(10,5)
print(retangle.area())

circle=Circle(7)
print(circle.area())