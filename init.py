
# Define a Class
class Employee:
    # Class Variable
    Company_name="Google"
    def __init__(self,id,name):
        # instance variable
        self.id=id
        self.name=name

    def display(self):
        print(self.id)
        print(self.name)

# Object Creating

emp1=Employee("Aditya",101)
emp2=Employee("Krapansh",102)

# Access class and instance variable

print(Employee.Company_name)
emp1.display()

print()
emp2.display()

        