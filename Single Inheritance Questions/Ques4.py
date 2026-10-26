
# Create a parent class with an `__init__()` method that accepts `name`. Inherit it into a child class and initialize the object.

class Parent:
    def __init__(self,name):
        self.name=name

class Child(Parent):
    def __init__(self, name):
        super().__init__(name)

    def show(self):
        print(self.name)

name=Child("Aditya Shakya")

name.show()