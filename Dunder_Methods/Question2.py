
#  Employee Representation

class Employee:
    def __init__(self,employee_name,employee_id,salary):
        self.employee_name=employee_name
        self.employee_id=employee_id
        self.salary=salary

    def __repr__(self):
        return (f"Employee Name : {self.employee_name}\nEmployee Id : {self.employee_id}\nEmployee Salary : {self.salary}")

# Object Creation...

emp=Employee("Aditya Shakya","STU2024097",98000)

print(emp)