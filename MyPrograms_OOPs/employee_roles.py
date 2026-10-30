

# Employee Roles

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_annual_salary(self):
        print(self.salary+self.)

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language=programming_language

# Create Object For Manager and Developer
manager=Manager("Aditya",10000000,100000)
