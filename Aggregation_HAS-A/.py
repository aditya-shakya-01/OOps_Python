
class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def show_student(self):
        print(self.roll_no,self.roll_no)

class College:
    def __init__(self,college_name):
        self.college_name=college_name
        
    def show_student(self):
        print("College :",self.college_name)

std=[
    Student("Aditya",101),
    Student("Adi",102)
]

college=College("K.A.P.G. College")

college.show_student()