
#MultiLevel Inheritance...

class Grandfather:
    def house(self):
        print("Grandfather own a house")

class Father(Grandfather):
    def car(self):
        print("Father own a car")

class Child(Father):
    def bike(self):
        print("Childs Own a bike")

obj=Child()
obj.house()
obj.car()
obj.bike()