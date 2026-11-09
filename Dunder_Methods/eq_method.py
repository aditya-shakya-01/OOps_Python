
# __eq__() method  --> Equal Method ....

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def __eq__(self, other):
        return self.name==other.name and self.marks==other.marks

s1=Student("Aditya",85)
s2=Student("Aditya",85)

print(s1==s2)
        

    