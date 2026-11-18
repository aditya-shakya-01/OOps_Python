
# Strong HAS-A Relationship (Composition)

class Room:
    def __init__(self,name):
        self.name=name


class House:
    def __init__(self):
        self.room1=Room("Kichen")  # The room is created inside the House consructor... 
        self.room2=Room("Bathroom")

    def display(self):
        print(f"Room 1 : {self.room1.name}\nRoom 2 : {self.room2.name}")

h=House()
h.display()