
# Mobile and Battery 

class Battery:
    def __init__(self,capicity):
        self.capicity=capicity

class Mobile:
    def __init__(self):
        self.battery=Battery("6 Hours +")

    def display(self):
        print(f"Mobile Capicity : {self.battery.capicity}.")

# Object Creation

mob=Mobile()
mob.display()