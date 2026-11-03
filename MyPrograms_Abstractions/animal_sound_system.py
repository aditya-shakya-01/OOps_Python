
# Animal Sound System

from abc import ABC,abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Create Two Child Class 

class Dog(Animal):
    def sound(self):
        print("Dogs are Barking...")

class Cat(Animal):
    def sound(self):
        print("Cats Meow...")

cat=Cat()
cat.sound()

dog=Dog()
dog.sound()


