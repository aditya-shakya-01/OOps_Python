
# Create `Person` and `Student` classes. Use `super()` in the child's constructor to initialize the parent's attributes.

class Person:
    def __init__(self,name):
        self.name=name

    def display(self):
        print("Name :",self.name)

class Child(Person):
    def __init__(self, name,mob):
        super().__init__(name)
        self.mob=mob
        super().display()

    def display(self):
        print("Mob :",self.mob)

s1=Child("Aditya Shakya",9627209265)

s1.display()
