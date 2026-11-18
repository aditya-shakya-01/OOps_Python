
# Department And Teacher

class Teacher:
    def __init__(self,name):
        self.name=name

class Department:
    def __init__(self,department_name,teacher):
        self.department_name=department_name
        self.teacher=teacher

    def display(self):
        print(f"Teacher Name : {self.teacher.name}\nDepartment Name : {self.department_name}")

t1=Teacher("Raju Sir")
t2=Teacher("Rakesh Bhaiya")

d1=Department("B.Sc Computer Science",t2)

d1.display()