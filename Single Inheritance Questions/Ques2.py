

# Create `Father` with a `car` attribute. Create `Son` that inherits from `Father`. Display the car using a `Son` object.

class Father:
    def __init__(self,car_name):
        self.car_name=car_name

    def show_car(self):
        print("Car Name :",self.car_name)


class Son(Father):
    def __init__(self, car_name,price,color):
        super().__init__(car_name)
        self.price=price
        self.color=color


    def start(self):
        print(f"Car {self.car_name} Color {self.color} Price {self.price} has been Started")


car=Son("BMW",3000000,"Black")

car.show_car()
car.start()