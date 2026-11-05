
# Car Speed Controller

class Car:
    def __init__(self,car_name,speed):
        self.car_name=car_name
        self.__speed=speed

    def acceleration(self,speed):
        if speed<self.__speed and speed>0:
            self.__speed+=speed
            return f"Car Speed : {self.__speed}"
        else:
            return "Speed not Increase..."

    def braking(self,speed):
        if speed<self.__speed:
            self.__speed-=speed
            return f"Car Speed : {self.__speed}"

# Object Creation
car=Car("BMW",100)
# Acceleration
print(car.acceleration(20))
# Breking
print(car.braking(40))
