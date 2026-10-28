
# Create a parent class Employee 

class Employee:
    def __init__(self,name,basic_salary):
        self.name=name
        self.basic_salary=basic_salary

    def display(self):
        return f"Name : {self.name} \nBasic_Salary : {self.basic_salary}"

# Create a child class Manager

class Manager(Employee):
    def __init__(self, name, basic_salary,bonus):
        super().__init__(name, basic_salary)
        self.bonus=bonus

    # Create a method calculate salry() thst returns basic salary + bonus

    def calculate_salary(self):
        return (f"Bonus : {self.bonus}\nTotal Salary : {self.basic_salary+self.bonus}")


# Creates Objects

s1=Manager("Aditya",90000,20000)

print(s1.display())
print(s1.calculate_salary())