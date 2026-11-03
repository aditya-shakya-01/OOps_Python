
# Vehicle Start System

from abc import ABC,abstractmethod

class Vehicle:
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car Start with a Key"

class Bike(Vehicle):
    def start(self):
        return "Bike starts with a self-start Button"

bike=Bike()
bike.start()

car=Car()
car.start()