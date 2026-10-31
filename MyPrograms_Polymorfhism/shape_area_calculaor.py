
# Shape Area Calculator

class Shape:
    def area(self):
        pass

class Retangle(Shape):
    def area(self,length,width):
        return f"Ratangle Area : {length*width}"

class Square(Shape):
    def area(self,side):
        return f"Square Area : {side*side}"

class Circle(Shape):
    def area(self,radius):
        return f"Circle Area : {3.14*radius*radius}"

# Object Creations

retangle=Retangle()
square=Square()
circle=Circle()

print(retangle.area(10,5))
print(square.area(5))
print(circle.area(7))