# Foundation Of Object Relationship...

class Student :
    def __init__(self,name,laptop):
        self.name=name
        self.laptop=laptop

class Laptop:
    def __init__(self,brand):
        self.brand=brand

laptop1=Laptop("DELL")
student=Student("Aditya",laptop1)

print(student.laptop.brand)