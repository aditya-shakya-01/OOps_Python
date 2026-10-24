
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