
# Mobile Phone 

class Mobile:
    def __init__(self,brand,battery):
        self.brand=brand
        self.__battery=battery

    def charge(self,battery):
        if 0<=battery<=100:
            self.__battery=battery

    def use_battery(self):
        print(f"Mobile Brand Name : {self.brand}")
        print(f"Use the Battery : {self.__battery}")

# Object Creation
phn=Mobile("Apple",89)
# Show Battery
phn.use_battery()
# Charge Battery
phn.charge(99)
# Show Battery
phn.use_battery()
        