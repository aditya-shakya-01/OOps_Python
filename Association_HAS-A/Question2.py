
# Employee And Department 

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_details(self,department):
        print(f"Employee Name : {self.name}")
        print(f"Employee Salary : {self.salary}")
        print(f"Department : {department.department_name}")

class Department:
    def __init__(self,department_name):
        self.department_name=department_name

emp=Employee("Aditya Shakya",98000)
department=Department("Ai Engineer")

emp.show_details(department)