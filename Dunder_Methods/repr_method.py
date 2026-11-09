
# __repr__() method --> Representation Method

class Student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __repr__(self):
        return f"Student Name : {self.name!r} , Marks :{self.marks!r}"

s1=Student("Aditya Shakya",85)
print(s1)