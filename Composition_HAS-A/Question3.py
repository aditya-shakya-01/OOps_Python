
# Computer and Processor

class Processor:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed

class Computer:
    def __init__(self):
        self.processor=Processor("Dell","5600 mts")

    def display(self):
        print(f"Computer Brand Name : {self.processor.brand} and Speed is {self.processor.speed}.")

# Object Creation

computer=Computer()
computer.display()