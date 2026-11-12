# ===============================
# # Student Management System
# ===============================

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def details(self):
        print("="*20)
        print(f"Student Name : {self.name}")
        print(f"Student Roll Number : {self.roll_no}")
        print(f"Student Marks : {self.marks}")
        print(f"Percentage : {self.percentage()}")

    def percentage(self):
        return f"Percentage : {self.marks/5} %"

std=[
    Student("Aditya",101,406),
    Student("Shiv",102,407),
    Student("Abhinav",103,378)
]      

for student in std:
    student.details()
