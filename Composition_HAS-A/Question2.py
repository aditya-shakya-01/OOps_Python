
# Car And Engine

class Engine:
    def __init__(self,engine_type,horsepower):
        self.engine_name=engine_type
        self.horsepower=horsepower


class Car:
    def __init__(self,engine):
        self.engine=engine
        self.engine1=Engine("Modify","2000 HP")

    def start(self):
        print(f"Car has been started {self.engine}.")
        print(f"Car Engine Type {self.engine1.engine_name} and engine housepower is {self.engine1.horsepower}.")

# Object Creation

car=Car("BMW")
car.start()
