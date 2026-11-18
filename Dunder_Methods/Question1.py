
# Student Information

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def __str__(self):
        return (f"Student Name : {self.name}\nStudent Age : {self.age}\nStudent Marks : {self.marks}")

s1=Student("Aditya Shakya",18,78)
print(s1)
