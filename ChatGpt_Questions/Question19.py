
# Employee Work System 

from abc import ABC,abstractmethod
class Employee(ABC):
    salary=60000.0
    @ abstractmethod
    def calculate_salary(self):
        pass

class PartTimeEmployee(Employee):
    
    def calculate_salary(self):
        return f"Fart Time Employee Salary : {self.salary/2}"

class FullTimeEmployee(Employee):
    
    def calculate_salary(self):
        return f"Full Time Employee Salary : {self.salary}"

# Object Creation

part=PartTimeEmployee()
print(part.calculate_salary())
full=FullTimeEmployee()
print(full.calculate_salary())