
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

# What happens when the parent has a constructor


class Animal:
    def __init__(self,dog_name):
        self.dog_name=dog_name

class Dog(Animal):
    def bark(self):
        print(self.dog_name,"is barking")

# Now creates objects
dog1=Dog("Jenufier")

dog1.bark()


# Method overriding in single inheritance

class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

# Create object

d1=Dog()
d1.sound()