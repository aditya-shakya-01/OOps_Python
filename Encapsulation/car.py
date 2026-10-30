
class Car:
    def __init__(self,car_name,owner_name):
        self.car_name=car_name
        self._owner_name=owner_name

    def show_Info(self):
        print(f"Car name is {self.car_name} and owner's Name is : {self._owner_name}")

car=Car("Totota","Aditya")

car.show_Info()