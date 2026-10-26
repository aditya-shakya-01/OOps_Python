

# super() with __init__() and **kwargs

class Person:
    def __init__(self,name,**kwargs):
        super().__init__(**kwargs)
        self.name=name

class Student(Person):
    def __init__(self,roll_no,**kwargs):
        super().__init__(**kwargs)
        self.roll_no=roll_no

class Employee(Person):
    def __init__(self,salary,**kwargs):
        super().__init__(**kwargs)
        self.salary=salary

class TeachingAssistant(Student,Employee):
    def __init__(self, name, roll_no,salary):
        super().__init__(name=name,roll_no=roll_no,salary=salary)
       

obj=TeachingAssistant("Aditya",101,1000000)

print(obj.name)
print(obj.roll_no)
print(obj.salary)
        
