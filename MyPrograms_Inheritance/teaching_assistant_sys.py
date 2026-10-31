
# Teaching Assistant System...

class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name

class Student(Person):
    def __init__(self, roll_number, **kwargs):
        super().__init__(**kwargs)
        self.roll_number=roll_number

class Employee(Person):
    def __init__(self,salary, **kwargs):
        super().__init__(**kwargs)
        self.salary=salary

class TeachingAssistant(Student,Employee):
    def __init__(self, name, roll_number, salary):
        super().__init__(name=name, roll_number=roll_number,salary=salary)
    def display(self):
        print(self.name)
        print(self.roll_number)
        print(self.salary)

print(TeachingAssistant.__mro__)
obj=TeachingAssistant("Aditya",1001,100000)

obj.display()