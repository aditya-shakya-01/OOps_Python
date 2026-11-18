
# Object Comparison

class Student:
    def __init__(self,marks):
        self.marks=marks

    def __eq__(self, value):
        return self.marks==value.marks

s1=Student(56)
s2=Student(56)

print(s1==s2)