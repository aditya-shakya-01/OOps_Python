
# School Management System

# Create a parent class Person()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show_person(self):
        print("="*30)
        print("Name :",self.name)
        print("Age :",self.age)

# Create two Child Classes

class Student(Person):
    def __init__(self, name, age,roll_number):
        super().__init__(name, age)
        self.roll_number=roll_number

    def student_details(self):
        print("="*30)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Roll Number :",self.roll_number)

class Teacher(Person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        self.subject=subject

    def teacher_details(self):
        print("="*30)
        print("Name :",self.name)
        print("Age :",self.age)
        print("Course :",self.subject)
obj=Person("Krapansh",20)
obj_tech=Teacher("Aditya",18,"BSc")
objstd=Student("Rakesh Bhaiya",22,1001)

obj.show_person()
obj_tech.teacher_details()
objstd.student_details()
