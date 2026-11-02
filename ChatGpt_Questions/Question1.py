
# Animal Hierarchy

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# Creates Child Classes

class Dog(Animal):
    def display(self):
        print("Dog name :",self.name)
        print("Age :",self.age)

class Cat(Animal):
    def display(self):
        print("Cat name :",self.name)
        print("Age :",self.age)

# Object Creation

dog=Dog("Max",3)
dog.display()

cat=Cat("Mrs. Krapanshii",4)
cat.display()