
# House And Room

class Room:
    def __init__(self,room_name,area):
        self.room_name=room_name
        self.area=area

class House:
    def __init__(self):
        self.room1=Room("Bedroom","West Direction")
        self.room2=Room("Kitchen","East Direction")
        self.room3=Room("Temple","North Direction")
        self.room4=Room("Washroom","South Direction")


    def display(self):
        print(f"Room 1: {self.room1.room_name} and Direction {self.room1.area}")
        print(f"Room 2 :{self.room2.room_name} and direction {self.room2.area}")
        print(f"Room 3: {self.room3.room_name} and Direction {self.room3.area}")
        print(f"Room 4 :{self.room4.room_name} and direction {self.room4.area}")

h1=House()
h1.display()