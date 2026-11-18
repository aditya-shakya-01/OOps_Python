
# Weak HAS-A Relationship (Aggregation)

class Teacher:
    def __init__(self,name):
        self.name=name

class Department:
    def __init__(self,department_name,teacher):
        self.department_name=department_name
        self.teacher=teacher

    def display(self):
        print(f"Department Name : {self.department_name}\nStudent Name : {self.teacher.name}")

t1=Teacher("Rakesh Bhaiya")

d1=Department("Development Master Program",t1)

d1.display()