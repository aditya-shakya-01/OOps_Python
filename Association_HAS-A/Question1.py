
# Student And Address

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

class Address:
    def __init__(self,city,state):
        self.city=city
        self.state=state

    def details(self,std):
        print(f"Student Name : {std.name}")
        print(f"Roll No : {std.roll_no}")
        print(f"City : {self.city}")
        print(f"State : {self.state}")

std=Student("Aditya Shakya","STU2024097")
add=Address("Kasganj","Uttar Pradesh")

add.details(std)