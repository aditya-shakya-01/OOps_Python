
# Create a `Parent` class with a `show()` method. Create a `Child` class that inherits from `Parent`. Call the method using a child object.


class Parent:
    def __init__(self,name):
        self.name=name

    def display(self):
        return f"{self.name} is a good Coder."

class Child(Parent):
    def __init__(self, name,roll_no):
        self.roll_no=roll_no
        super().__init__(name)

    def show(self):
        return f"Name : {self.name}\nRoll_no : {self.roll_no}"

obj=Child("Aditya",101)

print(obj.display())
print(obj.show())