
# Fly Car System
class Vehicle:
    def __init__(self,brand,**kwargs):
        super().__init__(**kwargs)
        self.brand=brand

class Car(Vehicle):
    def __init__(self,number_of_doors,**kwargs):
        super().__init__(**kwargs)
        self.number_of_doors=number_of_doors

class Aircraft(Vehicle):
    def __init__(self,max_altitude,**kwargs):
        super().__init__(**kwargs)
        self.max_altitude=max_altitude

class FlyingCar(Car,Aircraft):
    def __init__(self, brand, number_of_doors,max_altitude):
        super().__init__(brand=brand,number_of_doors= number_of_doors,max_altitude=max_altitude)

    def show_details(self):
        print(f"Vehicle Brand : {self.brand}\nNumber Of Doors : {self.number_of_doors}\nMaximum Altitude : {self.max_altitude}")

car=FlyingCar("Toyota",4,"5000 Feet")
car.show_details()