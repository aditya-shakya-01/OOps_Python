
# Multiple Inheritance in OOPs

class Father:
    def farmering(self):
        print("Farmer is the backbone of this country...")

class Mother:
    def cooking(self):
        print("Mother teaches Cooking...")

class Child(Father,Mother):  # Child class inherits both of properties
    def coding(self):
        print("Currently, I improved my coding Skill day by day...")

# Create object

coder=Child()

# Access Parents class properties

coder.farmering()
coder.cooking()
coder.coding()

# Understanding Attributes in multiple Inheritance...

class Father:
    def __init__(self):
        self.car="BMW"

    def show_car(self):
        print("Father's Car :",self.car)

class Mother:
    def __init__(self):
        self.house="Big House"

    def show_house(self):
        print("Mother's House :",self.house)

class Child(Father,Mother):
    def __init__(self):
        super().__init__()

obj=Child()

# Access Parent class properties...

obj.show_car()
obj.show_house()