
# Vehicle Movement
# Create a Parent Class

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Car is running on the Road.")

class Bike(Vehicle):
    def move(self):
        print("Bike is starting in the race track.")

class Airoplane(Vehicle):
    def move(self):
        print("Airoplane is running on the ranway.")

# Object Creation

car=Car()
airoplane=Airoplane()
bike=Bike()

car.move()
airoplane.move()
bike.move()