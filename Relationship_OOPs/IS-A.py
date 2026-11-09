
# IS-A in OOPs

class Student:
    def __init__(self,name):
        self.name=name

class Teacher(Student):
    pass

s1=Student("Aditya")
print(s1.name)