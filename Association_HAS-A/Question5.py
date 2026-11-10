
# Car And Driver 

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model


class Driver:
    def __init__(self,name,licence_num):
        self.name=name
        self.licence_num=licence_num

    def information(self,car):
        print(f"Driver Name : {self.name}")
        print(f"Licence Number : {self.licence_num}")
        print(f"Brand Name : {car.brand}")
        print(f"Model : {car.model}")

car=Car("BMW","M5")
driver=Driver("Shyam","DP83G326")

driver.information(car)