
# Q1. Animal Sounds 🐶

# Create Parent Class Animal
class Animal:
    def sound(self):
        print("Animal makes sound...")

# Create Three Child

class Dog(Animal):
    def sound(self):
        print("Dogs are barking...")

class Cat(Animal):
    def sound(self):
        print("Cat Meow...")

class Cow(Animal):
    def sound(self):
       
        print("Cow mooo...")
        super().sound()

# Object Creation
cat=Cat()
dog=Dog()
cow=Cow()

cat.sound()
dog.sound()
cow.sound()
