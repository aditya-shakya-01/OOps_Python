

# Employee Roles

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def calculate_annual_salary(self):
        print(self.salary+self.bonus)

class Manager(Employee):
    def __init__(self, name, salary,bonus):
        super().__init__(name, salary)
        self.bonus=bonus

    def show_details(self):
        print("="*20)
        print(f"Manager Name : {self.name}\nSalary : {self.salary}\nBonus : {self.bonus}")

class Developer(Employee):
    def __init__(self, name, salary,programming_language):
        super().__init__(name, salary)
        self.programming_language=programming_language

    def show_details(self):
            print("="*20)
            print(f"Developer Name : {self.name}\nSalary : {self.salary}\nProgramming Language : {self.programming_language}")

# Create Object For Manager and Developer
manager=Manager("Aditya",10000000,100000)

manager.show_details()

developer=Developer("Adi",100000,"Python")

developer.show_details()
