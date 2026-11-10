
# Association in OOPs Programming

class Student:
    def __init__(self,student_name):
        self.student_name=student_name
        # self.laptop=laptop

    def study(self,laptop):
        print(f"{self.student_name} is working on {laptop.laptop_name} Laptop and laptop price {laptop.price}")
        laptop.code()

class Laptop:
    def __init__(self,laptop_name,price):
        self.laptop_name=laptop_name
        self.price=price

    def code(self):
        print(f"{self.laptop_name} in coding Mode")

laptop1=Laptop("DELL",25000)
std=Student("Aditya Shakya")
std.study(laptop1)

