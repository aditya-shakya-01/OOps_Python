
# Single Inheritance (Inheritance Attributes and Methods)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def indroduction(self):
        print(self.name)
        print(self.age)

class Student(Person):
    def studing(self):
        print(self.name,"is studying ")


s1=Student("Adi",18)

s1.indroduction()
s1.studing()