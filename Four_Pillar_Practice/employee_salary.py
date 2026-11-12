# ==============================
#     Employee Salary
# ==============================

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self._id=id
        self.__salary=salary

    def salary_increment(self):
        # Increment rate per year 5%
        rate=int(input("Enter your increment rate :"))
        return (self.__salary+self.__salary*rate/100)

    def display(self):
        print(f"Employee Name : {self.name}")
        print(f"Employee Id : {self._id}")
        print(f"Salary : {self.salary_increment()}")

emp=Employee("Aditya Shakya",101,98000)
emp.display()