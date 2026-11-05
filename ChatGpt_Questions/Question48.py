
# Employee Salary

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def details(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Salary : {self.__salary}")

    def set_salary(self,amount):
        if amount<0:
            raise Exception("Please Enter a Valid Amount...")
        self.__salary=amount
            


# Object Creation
emp=Employee("Aditya Shakya",98000)
# Get Salary
emp.details()
# Set Salary
emp.set_salary(8000)
# Get Salary
emp.details()