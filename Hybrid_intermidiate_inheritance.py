
# Intermediate Level Hybrid Inheritance....

class Person:
    # Define a Constructor
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("Name :",self.name)


class Student(Person):
    # Creates own Constructor
    def __init__(self, name,roll_no):
        Person.__init__(self,name)
        self.roll_no=roll_no

    def show_roll_no(self):
        print("Roll No :",self.roll_no)

class Employee(Person):
    def __init__(self, name,salary):
        Person.__init__(self,name)
        self.salary=salary

    def show_salary(self):
        print("Salary :",self.salary)

class TeachingAssistant(Student,Employee):
    def __init__(self, name, roll_no,salary):
        Student.__init__(self,name,roll_no)
        Employee.__init__(self,name,salary)

obj=TeachingAssistant("Aditya",27,1000)

obj.show_name()
obj.show_roll_no()
obj.show_salary()
        