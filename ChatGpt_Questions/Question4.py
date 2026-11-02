
# Vehicle System

class Vehicle:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed

# Child Classes
class Car(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model, speed)

    def display(self):
        print("="*20)
        print(f"Brand Name : {self.brand}")
        print(f"Model Name : {self.model}")
        print(f"Speed(kmph) : {self.speed}")

class Bike(Vehicle):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model, speed)

    def display(self):
        print("="*20)
        print(f"Brand Name : {self.brand}")
        print(f"Model Name : {self.model}")
        print(f"Speed(kmph) : {self.speed}")

# Object Creation 
car=Car("Toyota",2025,180)
car.display()

bike=Bike("Ninja",2023,220)
bike.display()