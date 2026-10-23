

class Car:
    # class variable
    car_type="seden"
    def __init__(self,carname,km):
        # instance variable
        self.carname=carname
        self.km=km

# create objects
car1=Car("Thar",500)
car2=Car("Honda City",800)

# Access class and instance variable 

print(Car.car_type)
print(car1.carname)
print(car1.km)

print(car2.carname)
print(car2.km)

# Modify instance variable

car1.carname="Toyota"

print(car1.carname) # Update instance variable

# Modify class variable 

Car.car_type="Farari"

print(Car.car_type)
