
# Student Marks

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.__marks=marks

    def get_marks(self):
        return self.__marks

    def set_marks(self,mark):
        if 0<=mark<=100:
            self.__marks=mark

# Create Object
std=Student("Aditya",95)
# get marks
print(std.get_marks())
# Set marks
std.set_marks(86)
# Get marks
print(std.get_marks())