
# Student Management System 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Student(Person):
    def __init__(self, name, age,roll_no,course):
        super().__init__(name, age)
        self.roll_no=roll_no
        self.course=course

    def display(self):
        print(f"Student Name : {self.name}")
        print(f"Student Age : {self.age}")
        print(f"Student Roll No : {self.roll_no}")
        print(f"Student Course: {self.course}")

std=Student("Aditya",18,1001,"B.Sc Voc. Computer Application")

std.display()