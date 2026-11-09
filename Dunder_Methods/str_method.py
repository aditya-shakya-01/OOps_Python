
# __str__() Method  ---> String Method

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    # Now i created a __str__() method
    def __str__(self):
        return f"Student Name : {self.name}, Marks : {self.marks}"

s1=Student("Aditya Shakya",85)
print(s1)