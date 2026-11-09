class Student:
    school = "ABC College"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

s1 = Student("Aditya")
s2 = Student("Rahul")

Student.change_school("XYZ College")

print(s1.school)
print(s2.school)