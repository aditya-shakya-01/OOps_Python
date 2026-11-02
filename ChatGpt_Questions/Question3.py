
# Employee Salary

class Employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary

class Manager(Employee):
    def __init__(self, name, basic_salary,bonus):
        super().__init__(name, basic_salary)
        self.bonus=bonus

    def final_salary(self):
        return f"Total Salary : {(self.basic_salary*10/100)+self.basic_salary}"
    
# Object Creations

manager=Manager("Aditya",98000,10)

print(manager.final_salary())
        