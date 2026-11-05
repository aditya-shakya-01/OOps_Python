
# Vehicle Start System

from abc import ABC,abstractmethod
class Vehicle(ABC):
    @ abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return f"Car is Starting..."

class Bike(Vehicle):
    def start(self):
        return f"Bike is Starting..." 

class Bus(Vehicle):
    def start(self):
        return f"Bus is starting..." 

# Object Creation
car=Car()
print(car.start())

bike=Bike()
print(bike.start())

bus=Bus()
print(bus.start())