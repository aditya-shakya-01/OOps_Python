
# University Management system 

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self, name, age,roll_number):
        super().__init__(name, age)
        self.roll_number=roll_number

class UniversityStudent(Student):
    def __init__(self, name, age, roll_number,university_name,course):
        super().__init__(name, age, roll_number)
        self.university_name=university_name
        self.course=course

    def displayInfo(self):
        print("="*30)
        print("University Name :",self.university_name)
        print("Course Name :",self.course)
        print("Name :",self.name)
        print("Roll Number :",self.roll_number)
        print("Age :",self.age)
Students=[
    UniversityStudent("Aditya Shakya",18,1001,"RMPSU","B.S.c (Computer Application)"),
    UniversityStudent("Krapansh",19,1002,"RMPSU","B.Sc(Biotechnology)"),
    UniversityStudent("AVbhinav",20,1003,"RMPSU","B>Sc(Computer Application)")

]

for user in Students:
    user.displayInfo()

        