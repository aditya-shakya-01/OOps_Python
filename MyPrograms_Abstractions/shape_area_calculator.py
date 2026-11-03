
# Shape Area Calculator

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Retangle(Shape):
    def area(self,length,width):
        return f"Retangle Area : {length*width}"


class Circle(Shape):
    def area(self,radius):
        return f"Circle Area : {3.14*radius*radius}"


retangle=Retangle()
print(retangle.area(10,5))

circle=Circle()
print(circle.area(7))

