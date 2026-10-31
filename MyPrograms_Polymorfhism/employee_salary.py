
# Employee Salary

class Employee:
    salary=60000.0 # Full month working 8 hours in a day full time
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return f"Full time Employee Salary : {self.salary}"

class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return f"Part Time Employee Salary : {self.salary/2}"

# Object Creation

full=FullTimeEmployee()
part=PartTimeEmployee()

print(full.calculate_salary())
print(part.calculate_salary())