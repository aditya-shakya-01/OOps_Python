
# Employee Salary System

from abc import ABC,abstractmethod

class Employee:
    salary=60000.0
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return f"Full Time Employee Salary : {self.salary}"

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return f"Part Time Employee Salary : {self.salary/2}"

emp=FullTimeEmployee()
emp1=PartTimeEmployee()

print(emp.calculate_salary())
print(emp1.calculate_salary())